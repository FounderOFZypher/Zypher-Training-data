---
id: SYNAPSE-00215
title: "Synapse: data_pipeline ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, data_pipeline, coltex_living_brain]
related: [HUB-DATA_PIPELINE, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-DATA_PIPELINE, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-DATA_PIPELINE]
---

# Neural Synapse: data_pipeline → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**depends_on** — documents in `data_pipeline` depends on `coltex_living_brain`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
