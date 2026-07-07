---
id: SYNAPSE-00287
title: "Synapse: ml_training_pipeline ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, ml_training_pipeline, coltex_living_brain]
related: [HUB-ML_TRAINING_PIPELINE, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Neural Synapse: ml_training_pipeline → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**depends_on** — documents in `ml_training_pipeline` depends on `coltex_living_brain`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
