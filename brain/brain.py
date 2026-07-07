"""
Coltex RAG database engine.

Knowledge base · vector index · metadata · graph relationships · retrieval pipeline.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from brain.embeddings.encoder import EmbeddingEncoder
from brain.graph.relationships import GraphIndex
from brain.indexing.vector_index import VectorIndex
from brain.ingestion.loader import KnowledgeBase
from brain.metadata.index import MetadataIndex
from brain.reranking.reranker import Reranker
from brain.retrieval.pipeline import RetrievalPipeline
from brain.types import RetrievalResult


class Coltex:
    """
    Coltex RAG database engine:
    - Knowledge Base (documents)
    - Vector Database (embeddings)
    - Metadata Index
    - Graph Relationships
    - Retrieval Pipeline
    """

    def __init__(self, config: dict[str, Any] | None = None, config_path: str | Path = "config/brain.yaml"):
        self.config = config or self._load_config(config_path)
        self._init_components()

    @staticmethod
    def _load_config(path: str | Path) -> dict[str, Any]:
        with Path(path).open(encoding="utf-8") as f:
            return yaml.safe_load(f)

    def _init_components(self) -> None:
        kb_cfg = self.config["knowledge_base"]
        self.kb = KnowledgeBase(
            paths=kb_cfg["paths"],
            glob_pattern=kb_cfg.get("glob", "**/*.md"),
            exclude=kb_cfg.get("exclude"),
        )

        emb_cfg = self.config.get("embeddings", {})
        self.encoder = EmbeddingEncoder(emb_cfg.get("model", "sentence-transformers/all-MiniLM-L6-v2"))

        vs_cfg = self.config.get("vector_store", {})
        self.vector_index = VectorIndex(
            self.kb,
            self.encoder,
            persist_dir=vs_cfg.get("persist_dir", "data/brain/vector_store"),
            collection_name=vs_cfg.get("collection_name", "coltex"),
        )

        self.metadata_index = MetadataIndex(self.kb)

        gr_cfg = self.config.get("graph", {})
        self.graph_index = GraphIndex(
            self.kb,
            max_hops=int(gr_cfg.get("max_hops", 2)),
            max_extra=int(gr_cfg.get("max_extra_chunks", 8)),
        )

        ret_cfg = self.config.get("retrieval", {})
        self.retrieval = RetrievalPipeline(
            vector_index=self.vector_index,
            metadata_index=self.metadata_index,
            graph_index=self.graph_index,
            reranker=Reranker(ret_cfg.get("source_weights")),
            vector_top_k=int(ret_cfg.get("vector_top_k", 10)),
            metadata_top_k=int(ret_cfg.get("metadata_top_k", 8)),
            final_top_k=int(ret_cfg.get("final_top_k", 8)),
            max_context_chars=int(ret_cfg.get("max_context_chars", 14000)),
        )

    def index(self, force: bool = False) -> int:
        if force:
            import shutil
            if self.vector_index.persist_dir.exists():
                shutil.rmtree(self.vector_index.persist_dir)
            self.vector_index._collection = None
            self.vector_index._client = None
        if force or not self.vector_index.is_indexed:
            return self.vector_index.index()
        self.vector_index._connect()
        return self.vector_index._collection.count()

    def retrieve(self, query: str) -> RetrievalResult:
        return self.retrieval.retrieve(query)

    def index_document(self, doc) -> None:
        """Index a single document without full rebuild."""
        self.metadata_index.refresh()
        self.vector_index.index_document(doc)

    @property
    def document_count(self) -> int:
        return len(self.kb)

    def stats(self) -> dict[str, Any]:
        indexed = 0
        try:
            indexed = self.vector_index._collection.count() if self.vector_index._collection else 0
        except Exception:
            pass
        return {
            "documents": len(self.kb),
            "indexed_vectors": indexed,
            "vector_store": str(self.vector_index.persist_dir),
        }

    def pulse(self) -> dict[str, Any]:
        """Living brain vitals — document counts, graph density, neural map."""
        base = self.stats()
        domains: dict[str, int] = {}
        hubs: dict[str, int] = {}
        synapses = 0
        reflexes = 0
        edges = 0

        for doc in self.kb.documents:
            path = doc.path.replace("\\", "/")
            if "/domains/" in path:
                parts = path.split("/domains/")
                if len(parts) > 1:
                    cat = parts[1].split("/")[0]
                    domains[cat] = domains.get(cat, 0) + 1
            if "/synapses/" in path:
                synapses += 1
            if "/reflexes/" in path:
                reflexes += 1
            if doc.hub:
                hubs[doc.hub] = hubs.get(doc.hub, 0) + 1
            edges += len(doc.related) + sum(len(v) for v in doc.relationships.values())

        neural_map_path = Path("data/brain/neural-map.json")
        neural_map = {}
        if neural_map_path.exists():
            import json
            try:
                neural_map = json.loads(neural_map_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                pass

        return {
            **base,
            "living_brain": {
                "status": "alive" if base["documents"] > 0 else "dormant",
                "domains": domains,
                "domain_count": len(domains),
                "hubs": hubs,
                "hub_count": len(hubs),
                "synapses": synapses,
                "reflexes": reflexes,
                "graph_edges": edges,
                "neural_map": neural_map_path.exists(),
                "neural_map_summary": {
                    "total_documents": neural_map.get("total_documents"),
                    "domain_count": neural_map.get("domain_count"),
                } if neural_map else None,
            },
        }
