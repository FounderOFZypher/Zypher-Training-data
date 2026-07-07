---
id: SYNAPSE-00141
title: "Synapse: agent_orchestrator ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, agent_orchestrator, ml_training_pipeline]
related: [HUB-AGENT_ORCHESTRATOR, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Neural Synapse: agent_orchestrator → ml_training_pipeline

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**calls** — documents in `agent_orchestrator` calls into `ml_training_pipeline`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
