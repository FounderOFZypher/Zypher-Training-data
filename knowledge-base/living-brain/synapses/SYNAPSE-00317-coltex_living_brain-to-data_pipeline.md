---
id: SYNAPSE-00317
title: "Synapse: coltex_living_brain ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, coltex_living_brain, data_pipeline]
related: [HUB-COLTEX_LIVING_BRAIN, HUB-DATA_PIPELINE]
see_also: [HUB-COLTEX_LIVING_BRAIN, HUB-DATA_PIPELINE]
depends_on: [HUB-COLTEX_LIVING_BRAIN]
---

# Neural Synapse: coltex_living_brain → data_pipeline

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**depends_on** — documents in `coltex_living_brain` depends on `data_pipeline`.

## Source hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
