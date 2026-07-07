---
id: PATHWAY-0102
title: "Neural Pathway: temporal → parietal (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: temporal
lobe_target: parietal
pathway_type: associative
tags: [pathway, associative, temporal, parietal]
related: [LOBE-TEMPORAL, LOBE-PARIETAL]
see_also: [LOBE-TEMPORAL, LOBE-PARIETAL]
synthesizes: [LOBE-TEMPORAL]
---

# Neural Pathway: temporal → parietal

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `temporal` connect to lobe `parietal` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-TEMPORAL` (temporal)
- Target: `LOBE-PARIETAL` (parietal)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
