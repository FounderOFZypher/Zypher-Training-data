---
id: SYNAPSE-00319
title: "Synapse: coltex_living_brain ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, coltex_living_brain, knowledge_graph_store]
related: [HUB-COLTEX_LIVING_BRAIN, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-COLTEX_LIVING_BRAIN, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-COLTEX_LIVING_BRAIN]
---

# Neural Synapse: coltex_living_brain → knowledge_graph_store

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**calls** — documents in `coltex_living_brain` calls into `knowledge_graph_store`.

## Source hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
