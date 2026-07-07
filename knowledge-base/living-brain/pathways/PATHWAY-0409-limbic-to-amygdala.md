---
id: PATHWAY-0409
title: "Neural Pathway: limbic → amygdala (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: limbic
lobe_target: amygdala
pathway_type: associative
tags: [pathway, associative, limbic, amygdala]
related: [LOBE-LIMBIC, LOBE-AMYGDALA]
see_also: [LOBE-LIMBIC, LOBE-AMYGDALA]
synthesizes: [LOBE-LIMBIC]
---

# Neural Pathway: limbic → amygdala

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `limbic` connect to lobe `amygdala` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-LIMBIC` (limbic)
- Target: `LOBE-AMYGDALA` (amygdala)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
