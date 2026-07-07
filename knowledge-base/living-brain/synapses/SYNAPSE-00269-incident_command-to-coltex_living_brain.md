---
id: SYNAPSE-00269
title: "Synapse: incident_command ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, incident_command, coltex_living_brain]
related: [HUB-INCIDENT_COMMAND, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-INCIDENT_COMMAND, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Neural Synapse: incident_command → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**documents** — documents in `incident_command` documents `coltex_living_brain`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
