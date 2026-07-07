---
id: PATHWAY-0109
title: "Neural Pathway: temporal → amygdala (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: temporal
lobe_target: amygdala
pathway_type: excitatory
tags: [pathway, excitatory, temporal, amygdala]
related: [LOBE-TEMPORAL, LOBE-AMYGDALA]
see_also: [LOBE-TEMPORAL, LOBE-AMYGDALA]
synthesizes: [LOBE-TEMPORAL]
---

# Neural Pathway: temporal → amygdala

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `temporal` connect to lobe `amygdala` via this commissural pathway.

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
- Target: `LOBE-AMYGDALA` (amygdala)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
