---
id: SYNAPSE-00315
title: "Synapse: coltex_living_brain ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, coltex_living_brain, rag_retrieval_core]
related: [HUB-COLTEX_LIVING_BRAIN, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-COLTEX_LIVING_BRAIN, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-COLTEX_LIVING_BRAIN]
---

# Neural Synapse: coltex_living_brain → rag_retrieval_core

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**calls** — documents in `coltex_living_brain` calls into `rag_retrieval_core`.

## Source hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
