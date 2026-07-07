---
id: PATHWAY-0900
title: "Neural Pathway: amygdala → frontal (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: amygdala
lobe_target: frontal
pathway_type: commissural
tags: [pathway, commissural, amygdala, frontal]
related: [LOBE-AMYGDALA, LOBE-FRONTAL]
see_also: [LOBE-AMYGDALA, LOBE-FRONTAL]
synthesizes: [LOBE-AMYGDALA]
---

# Neural Pathway: amygdala → frontal

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `amygdala` connect to lobe `frontal` via this commissural pathway.

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
- Target: `LOBE-FRONTAL` (frontal)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
