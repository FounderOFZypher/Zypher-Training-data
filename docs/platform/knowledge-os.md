# Coltex Knowledge Architecture

**Coltex Mega RAG is a commercial RAG corpus with an operational runtime.**

Organizations need more than a place to store documents. They need a system that
**understands** knowledge, **connects** it, **reasons** over it, **retrieves** the
right evidence, and **improves** the corpus over time.

---

## Mental model

| Commodity RAG | Coltex Mega RAG |
|---------------|-----------------|
| Buy a small dump | Operate a 100M+ commercial corpus |
| Store → Retrieve | Understand → Connect → Reason → Retrieve → Improve |
| Index documents | Intelligence engine improves the corpus |
| Search metrics | Knowledge Health operational scores |
| Static chunks | Lifecycle: Created → Verified → Published → Deprecated |
| Hardcoded integrations | Extensible plugin and event architecture |
| RAG pipeline | Reasoning layer with evidence assembly |

---

## What customers are buying

A **commercial Mega RAG corpus** plus a runtime that:

- Runs knowledge as a managed resource with lifecycle and governance
- Detects problems (duplicates, contradictions, staleness, broken links)
- Recommends fixes (merges, replacements, documentation gaps)
- Propagates changes through an event-driven pipeline
- Schedules maintenance automatically
- Extends through plugins, hooks, and custom connectors
- Separates retrieval from reasoning for trustworthy AI answers

---

## Intelligence loop

```
Ingest → Embed → Graph link → Retrieve → Evaluate → Curate → Improve → Re-index
```

Details: [intelligence-engine.md](intelligence-engine.md)

---

## Related documents

- [Commercial product overview](../commercial/product-overview.md)
- [Platform overview](overview.md)
- [Platform roadmap](roadmap.md)
- [Intelligence Engine](intelligence-engine.md)
