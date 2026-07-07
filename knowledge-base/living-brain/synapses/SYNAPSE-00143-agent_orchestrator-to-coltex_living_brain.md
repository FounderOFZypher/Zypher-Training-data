---
id: SYNAPSE-00143
title: "Synapse: agent_orchestrator ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, agent_orchestrator, coltex_living_brain]
related: [HUB-AGENT_ORCHESTRATOR, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Neural Synapse: agent_orchestrator → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**depends_on** — documents in `agent_orchestrator` depends on `coltex_living_brain`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
