---
id: SYNAPSE-00251
title: "Synapse: knowledge_graph_store ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, knowledge_graph_store, coltex_living_brain]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Neural Synapse: knowledge_graph_store → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**calls** — documents in `knowledge_graph_store` calls into `coltex_living_brain`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
