---
id: SYNAPSE-00197
title: "Synapse: security_operations ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, security_operations, coltex_living_brain]
related: [HUB-SECURITY_OPERATIONS, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-SECURITY_OPERATIONS, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Neural Synapse: security_operations → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**documents** — documents in `security_operations` documents `coltex_living_brain`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
