---
id: SYNAPSE-00308
title: "Synapse: coltex_living_brain ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, coltex_living_brain, graphrag_engine]
related: [HUB-COLTEX_LIVING_BRAIN, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-COLTEX_LIVING_BRAIN, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-COLTEX_LIVING_BRAIN]
---

# Neural Synapse: coltex_living_brain → graphrag_engine

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**documents** — documents in `coltex_living_brain` documents `graphrag_engine`.

## Source hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
