---
id: SYNAPSE-00017
title: "Synapse: auth_service ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, auth_service, coltex_living_brain]
related: [HUB-AUTH_SERVICE, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-AUTH_SERVICE, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-AUTH_SERVICE]
---

# Neural Synapse: auth_service → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**see_also** — documents in `auth_service` is related to `coltex_living_brain`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
