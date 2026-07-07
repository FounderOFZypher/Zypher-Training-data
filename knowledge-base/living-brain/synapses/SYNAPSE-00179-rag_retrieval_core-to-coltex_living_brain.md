---
id: SYNAPSE-00179
title: "Synapse: rag_retrieval_core ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, rag_retrieval_core, coltex_living_brain]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Neural Synapse: rag_retrieval_core → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**calls** — documents in `rag_retrieval_core` calls into `coltex_living_brain`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
