from __future__ import annotations

from zypher.knowledge_base import Document


def format_context(documents: list[Document], max_chars: int = 12000) -> str:
    if not documents:
        return "No relevant documents found in the knowledge base."

    blocks: list[str] = []
    used = 0
    for i, doc in enumerate(documents, start=1):
        block = f"### Document {i}: {doc.title}\nSource: {doc.path}\n\n{doc.content[:2000]}"
        if used + len(block) > max_chars:
            break
        blocks.append(block)
        used += len(block)
    return "\n\n---\n\n".join(blocks)
