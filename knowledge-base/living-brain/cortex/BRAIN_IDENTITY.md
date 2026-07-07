---
id: CORTEX-00001
title: Coltex Living Brain Identity
doc_type: deep_dive
category: rag
hub: coltex_living_brain
tags: [cortex, identity, living-brain]
---

# Coltex Living Brain

The cortex is the meta-layer of Coltex — it defines what this brain *is*.

## Purpose
Coltex is a **living knowledge brain**: documents, synapses, hubs, and domains
that grow procedurally and connect via typed graph edges.

## Anatomy
| Region | Path | Role |
|--------|------|------|
| Domains | `domains/` | Category-organized knowledge (RAG, K8s, Python…) |
| Hubs | `hubs/` | Service-level clusters (auth, indexing, GraphRAG…) |
| Synapses | `synapses/` | Cross-hub neural links |
| Cortex | `cortex/` | Meta-reasoning and brain identity |
| Memory | `memory/` | Long-horizon episodic knowledge |
| Reflexes | `reflexes/` | Fast-path FAQs and runbooks |

## Pulse
```bash
python3 -m brain pulse
make living-brain-pulse
```
