---
id: SYNAPSE-00316
title: "Synapse: coltex_living_brain ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, coltex_living_brain, security_operations]
related: [HUB-COLTEX_LIVING_BRAIN, HUB-SECURITY_OPERATIONS]
see_also: [HUB-COLTEX_LIVING_BRAIN, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-COLTEX_LIVING_BRAIN]
---

# Neural Synapse: coltex_living_brain → security_operations

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**documents** — documents in `coltex_living_brain` documents `security_operations`.

## Source hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
