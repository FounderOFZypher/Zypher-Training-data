---
id: PATHWAY-0806
title: "Neural Pathway: thalamus → brainstem (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: thalamus
lobe_target: brainstem
pathway_type: commissural
tags: [pathway, commissural, thalamus, brainstem]
related: [LOBE-THALAMUS, LOBE-BRAINSTEM]
see_also: [LOBE-THALAMUS, LOBE-BRAINSTEM]
synthesizes: [LOBE-THALAMUS]
---

# Neural Pathway: thalamus → brainstem

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `thalamus` connect to lobe `brainstem` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-THALAMUS` (thalamus)
- Target: `LOBE-BRAINSTEM` (brainstem)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
