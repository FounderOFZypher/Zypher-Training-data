---
id: SYNAPSE-00053
title: "Synapse: graphrag_engine ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, graphrag_engine, coltex_living_brain]
related: [HUB-GRAPHRAG_ENGINE, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Neural Synapse: graphrag_engine → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**documents** — documents in `graphrag_engine` documents `coltex_living_brain`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
