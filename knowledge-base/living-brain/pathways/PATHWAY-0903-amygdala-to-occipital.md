---
id: PATHWAY-0903
title: "Neural Pathway: amygdala → occipital (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: amygdala
lobe_target: occipital
pathway_type: modulatory
tags: [pathway, modulatory, amygdala, occipital]
related: [LOBE-AMYGDALA, LOBE-OCCIPITAL]
see_also: [LOBE-AMYGDALA, LOBE-OCCIPITAL]
synthesizes: [LOBE-AMYGDALA]
---

# Neural Pathway: amygdala → occipital

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `amygdala` connect to lobe `occipital` via this commissural pathway.

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
- Target: `LOBE-OCCIPITAL` (occipital)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
