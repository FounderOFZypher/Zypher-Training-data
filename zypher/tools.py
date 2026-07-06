from __future__ import annotations

import json
from typing import Any, Callable


ToolFn = Callable[[dict[str, Any]], str]


class ToolRegistry:
    """Lightweight tool-calling registry for the Zypher backend."""

    def __init__(self) -> None:
        self._tools: dict[str, tuple[str, ToolFn]] = {}

    def register(self, name: str, description: str, fn: ToolFn) -> None:
        self._tools[name] = (description, fn)

    def list_tools(self) -> list[dict[str, str]]:
        return [{"name": n, "description": d} for n, (d, _) in self._tools.items()]

    def run(self, name: str, arguments: dict[str, Any]) -> str:
        if name not in self._tools:
            return json.dumps({"error": f"Unknown tool: {name}"})
        _, fn = self._tools[name]
        return fn(arguments)

    @staticmethod
    def default() -> "ToolRegistry":
        reg = ToolRegistry()

        def search_docs(args: dict[str, Any]) -> str:
            return json.dumps({"status": "delegated_to_rag", "query": args.get("query", "")})

        reg.register("search_knowledge_base", "Search the Zypher enterprise knowledge base", search_docs)
        return reg
