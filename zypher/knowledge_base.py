from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


@dataclass
class Document:
    doc_id: str
    title: str
    path: str
    content: str
    category: str = ""
    tags: list[str] | None = None
    related: list[str] | None = None


def _parse_md(path: Path) -> Document:
    text = path.read_text(encoding="utf-8")
    meta: dict = {}
    body = text
    m = FRONTMATTER_RE.match(text)
    if m:
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            meta = {}
        body = text[m.end() :].strip()
    elif text.count("---") >= 2:
        parts = text.split("---")
        try:
            meta = yaml.safe_load(parts[1].strip()) or {}
        except yaml.YAMLError:
            meta = {}
        body = "---".join(parts[2:]).strip()

    title = meta.get("title") or path.stem
    return Document(
        doc_id=str(meta.get("id", path.stem)),
        title=str(title),
        path=str(path),
        content=body,
        category=str(meta.get("category", "")),
        tags=list(meta.get("tags") or []),
        related=[str(r) for r in (meta.get("related") or [])],
    )


class KnowledgeBase:
    """Load and index markdown knowledge-base documents."""

    def __init__(self, paths: list[str], glob_pattern: str = "**/*.md", exclude: list[str] | None = None):
        self.documents: list[Document] = []
        self.by_id: dict[str, Document] = {}
        exclude = exclude or []
        for base in paths:
            root = Path(base)
            if not root.exists():
                continue
            for path in sorted(root.glob(glob_pattern)):
                if any(path.match(pat) for pat in exclude):
                    continue
                if not path.is_file():
                    continue
                doc = _parse_md(path)
                self.documents.append(doc)
                self.by_id[doc.doc_id] = doc

    def __len__(self) -> int:
        return len(self.documents)

    def get_related(self, doc: Document, max_chunks: int = 4) -> list[Document]:
        found: list[Document] = []
        for rel_id in doc.related or []:
            if rel_id in self.by_id:
                found.append(self.by_id[rel_id])
            if len(found) >= max_chunks:
                break
        return found
