from __future__ import annotations

from zypher.config import ZypherConfig, load_config
from zypher.graphrag import GraphRAG
from zypher.knowledge_base import KnowledgeBase
from zypher.memory import ConversationMemory
from zypher.retrieval import format_context
from zypher.tools import ToolRegistry
from zypher.vector_store import VectorStore
from zypher.xs import ZypherXS


class ZypherBackend:
    """
    Enterprise RAG backend:

    User → memory + retrieval (vector + graph) → Zypher XS → answer
    """

    def __init__(self, config: ZypherConfig | None = None):
        self.config = config or load_config()
        rag = self.config.rag

        kb_cfg = rag["knowledge_base"]
        self.kb = KnowledgeBase(
            paths=kb_cfg["paths"],
            glob_pattern=kb_cfg.get("glob", "**/*.md"),
            exclude=kb_cfg.get("exclude"),
        )

        vs_cfg = rag["vector_store"]
        self.vector_store = VectorStore(
            self.kb,
            persist_dir=vs_cfg["persist_dir"],
            collection_name=vs_cfg["collection_name"],
            embedding_model=vs_cfg["embedding_model"],
        )

        gr_cfg = rag.get("graphrag", {})
        self.graphrag = GraphRAG(
            self.kb,
            max_hops=gr_cfg.get("max_hops", 2),
            max_extra_chunks=gr_cfg.get("max_extra_chunks", 4),
        ) if gr_cfg.get("enabled", True) else None

        self.memory = ConversationMemory(max_turns=rag.get("memory", {}).get("max_turns", 20))
        self.tools = ToolRegistry.default() if rag.get("tools", {}).get("enabled", True) else None
        self.xs = ZypherXS(self.config)

        if not self.memory.messages:
            self.memory.add("system", self.config.system_prompt)

    def index_knowledge_base(self) -> int:
        return self.vector_store.index()

    def retrieve(self, query: str) -> str:
        vs_cfg = self.config.rag["vector_store"]
        top_k = int(vs_cfg.get("top_k", 6))
        if self.graphrag:
            docs = self.graphrag.retrieve(self.vector_store, query, top_k=top_k)
        else:
            docs = self.vector_store.search(query, top_k=top_k)
        return format_context(docs)

    def chat(self, user_message: str) -> str:
        context = self.retrieve(user_message)
        rag_user_content = (
            f"<context>\n{context}\n</context>\n\n"
            f"User question: {user_message}\n\n"
            "Answer using the context above. If context is insufficient, say what is missing."
        )
        self.memory.add("user", rag_user_content)

        messages = self.memory.as_list()
        reply = self.xs.generate(messages)
        self.memory.add("assistant", reply)
        return reply
