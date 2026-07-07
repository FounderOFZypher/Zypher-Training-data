---
id: SYNAPSE-00320
title: "Synapse: coltex_living_brain ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, coltex_living_brain, incident_command]
related: [HUB-COLTEX_LIVING_BRAIN, HUB-INCIDENT_COMMAND]
see_also: [HUB-COLTEX_LIVING_BRAIN, HUB-INCIDENT_COMMAND]
depends_on: [HUB-COLTEX_LIVING_BRAIN]
---

# Neural Synapse: coltex_living_brain → incident_command

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**documents** — documents in `coltex_living_brain` documents `incident_command`.

## Source hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
