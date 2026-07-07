---
id: PATHWAY-0502
title: "Neural Pathway: cerebellum → parietal (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: cerebellum
lobe_target: parietal
pathway_type: modulatory
tags: [pathway, modulatory, cerebellum, parietal]
related: [LOBE-CEREBELLUM, LOBE-PARIETAL]
see_also: [LOBE-CEREBELLUM, LOBE-PARIETAL]
synthesizes: [LOBE-CEREBELLUM]
---

# Neural Pathway: cerebellum → parietal

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `cerebellum` connect to lobe `parietal` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-CEREBELLUM` (cerebellum)
- Target: `LOBE-PARIETAL` (parietal)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
