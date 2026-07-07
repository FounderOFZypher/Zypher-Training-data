"""Region-aware neural graph routing for advanced GraphRAG traversal."""

from __future__ import annotations

from collections import deque

from brain.ingestion.loader import KnowledgeBase, RELATIONSHIP_FIELDS
from brain.types import Document, ScoredDocument

# Region path markers → boost factor during graph expansion
REGION_BOOST = {
    "/synapses/": 1.15,
    "/pathways/": 1.12,
    "/hippocampus/": 1.08,
    "/cortex/L4-reasoning/": 1.10,
    "/cortex/L5-executive/": 1.10,
    "/memory/semantic/": 1.05,
    "/memory/procedural/": 1.05,
    "/reflexes/": 1.03,
    "/amygdala/": 1.06,
}

# Advanced edge types get slight score boost
ADVANCED_EDGES = frozenset({
    "synthesizes", "validates", "extends", "derived_from", "triggers",
})


class NeuralRouter:
    """
    Advanced graph expander with region-aware scoring and multi-edge-type BFS.
    Used by GraphIndex when advanced routing is enabled.
    """

    def __init__(
        self,
        kb: KnowledgeBase,
        max_hops: int = 3,
        max_extra: int = 12,
        region_boost: dict[str, float] | None = None,
    ):
        self.kb = kb
        self.max_hops = max_hops
        self.max_extra = max_extra
        self.region_boost = region_boost or REGION_BOOST

    def _region_multiplier(self, doc: Document) -> float:
        path = doc.path.replace("\\", "/")
        mult = 1.0
        for marker, boost in self.region_boost.items():
            if marker in path:
                mult = max(mult, boost)
        return mult

    def _edge_bonus(self, doc: Document, parent: Document) -> float:
        bonus = 0.0
        for edge_type in ADVANCED_EDGES:
            targets = doc.relationships.get(edge_type, [])
            if parent.doc_id in targets or parent.doc_id in doc.related:
                bonus += 0.05
        return min(bonus, 0.15)

    def expand(self, seeds: list[Document]) -> list[ScoredDocument]:
        seen = {d.doc_id for d in seeds}
        results: list[ScoredDocument] = []
        queue: deque[tuple[Document, Document | None, int]] = deque(
            (doc, None, 0) for doc in seeds
        )

        while queue and len(results) < self.max_extra:
            current, parent, depth = queue.popleft()
            if depth >= self.max_hops:
                continue

            related_docs = self.kb.get_related(
                current,
                max_chunks=self.max_extra,
                edge_types=list(RELATIONSHIP_FIELDS),
            )
            for related in related_docs:
                if related.doc_id in seen:
                    continue
                seen.add(related.doc_id)

                hop_score = max(0.25, 0.85 - depth * 0.18)
                hop_score *= self._region_multiplier(related)
                if parent:
                    hop_score += self._edge_bonus(related, parent)
                hop_score = min(hop_score, 1.0)

                results.append(ScoredDocument(
                    document=related,
                    score=hop_score,
                    source="graph",
                ))
                queue.append((related, current, depth + 1))

        results.sort(key=lambda s: s.score, reverse=True)
        return results[: self.max_extra]

    def search_from_seeds(self, seeds: list[ScoredDocument]) -> list[ScoredDocument]:
        return self.expand([s.document for s in seeds])
