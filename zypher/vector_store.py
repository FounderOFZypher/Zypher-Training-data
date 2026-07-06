from __future__ import annotations

from pathlib import Path

from zypher.knowledge_base import Document, KnowledgeBase


class VectorStore:
    """Semantic search over the knowledge base."""

    def __init__(
        self,
        kb: KnowledgeBase,
        persist_dir: str = "data/vector_store",
        collection_name: str = "zypher_kb",
        embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
    ):
        self.kb = kb
        self.persist_dir = Path(persist_dir)
        self.collection_name = collection_name
        self.embedding_model_name = embedding_model
        self._client = None
        self._collection = None
        self._model = None

    def _ensure(self) -> None:
        if self._collection is not None:
            return
        import chromadb
        from sentence_transformers import SentenceTransformer

        self.persist_dir.mkdir(parents=True, exist_ok=True)
        self._client = chromadb.PersistentClient(path=str(self.persist_dir))
        self._collection = self._client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"},
        )
        self._model = SentenceTransformer(self.embedding_model_name)

        if self._collection.count() == 0 and self.kb.documents:
            self.index()

    def index(self) -> int:
        self._ensure()
        ids, texts, metas = [], [], []
        for doc in self.kb.documents:
            text = f"{doc.title}\n{doc.content}"[:8000]
            ids.append(doc.doc_id)
            texts.append(text)
            metas.append({"title": doc.title, "path": doc.path, "category": doc.category})
        embeddings = self._model.encode(texts, show_progress_bar=True).tolist()
        self._collection.add(ids=ids, documents=texts, embeddings=embeddings, metadatas=metas)
        return len(ids)

    def search(self, query: str, top_k: int = 6) -> list[Document]:
        self._ensure()
        if self._collection.count() == 0:
            return []
        q_emb = self._model.encode([query]).tolist()
        results = self._collection.query(query_embeddings=q_emb, n_results=min(top_k, self._collection.count()))
        docs: list[Document] = []
        for doc_id in results["ids"][0]:
            if doc_id in self.kb.by_id:
                docs.append(self.kb.by_id[doc_id])
        return docs
