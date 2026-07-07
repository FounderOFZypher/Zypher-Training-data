---
id: SYNAPSE-00277
title: "Synapse: ml_training_pipeline ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, ml_training_pipeline, agent_orchestrator]
related: [HUB-ML_TRAINING_PIPELINE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Neural Synapse: ml_training_pipeline → agent_orchestrator

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**calls** — documents in `ml_training_pipeline` calls into `agent_orchestrator`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
