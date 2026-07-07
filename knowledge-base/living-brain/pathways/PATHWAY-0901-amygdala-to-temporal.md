---
id: PATHWAY-0901
title: "Neural Pathway: amygdala → temporal (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: amygdala
lobe_target: temporal
pathway_type: excitatory
tags: [pathway, excitatory, amygdala, temporal]
related: [LOBE-AMYGDALA, LOBE-TEMPORAL]
see_also: [LOBE-AMYGDALA, LOBE-TEMPORAL]
synthesizes: [LOBE-AMYGDALA]
---

# Neural Pathway: amygdala → temporal

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `amygdala` connect to lobe `temporal` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-AMYGDALA` (amygdala)
- Target: `LOBE-TEMPORAL` (temporal)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
