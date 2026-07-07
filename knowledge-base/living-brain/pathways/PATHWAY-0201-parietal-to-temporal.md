---
id: PATHWAY-0201
title: "Neural Pathway: parietal → temporal (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: parietal
lobe_target: temporal
pathway_type: associative
tags: [pathway, associative, parietal, temporal]
related: [LOBE-PARIETAL, LOBE-TEMPORAL]
see_also: [LOBE-PARIETAL, LOBE-TEMPORAL]
synthesizes: [LOBE-PARIETAL]
---

# Neural Pathway: parietal → temporal

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `parietal` connect to lobe `temporal` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-PARIETAL` (parietal)
- Target: `LOBE-TEMPORAL` (temporal)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
