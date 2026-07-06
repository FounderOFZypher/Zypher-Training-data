from __future__ import annotations

from zypher.knowledge_base import Document, KnowledgeBase


class GraphRAG:
    """Expand vector hits with graph-linked related chunks."""

    def __init__(self, kb: KnowledgeBase, max_hops: int = 2, max_extra_chunks: int = 4):
        self.kb = kb
        self.max_hops = max_hops
        self.max_extra_chunks = max_extra_chunks

    def expand(self, seed_docs: list[Document]) -> list[Document]:
        seen = {d.doc_id for d in seed_docs}
        merged = list(seed_docs)
        for doc in seed_docs:
            for related in self.kb.get_related(doc, self.max_extra_chunks):
                if related.doc_id not in seen:
                    seen.add(related.doc_id)
                    merged.append(related)
        return merged

    def retrieve(self, vector_store, query: str, top_k: int = 6) -> list[Document]:
        seeds = vector_store.search(query, top_k=top_k)
        return self.expand(seeds)
