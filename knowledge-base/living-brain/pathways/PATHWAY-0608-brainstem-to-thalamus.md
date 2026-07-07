---
id: PATHWAY-0608
title: "Neural Pathway: brainstem → thalamus (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: brainstem
lobe_target: thalamus
pathway_type: commissural
tags: [pathway, commissural, brainstem, thalamus]
related: [LOBE-BRAINSTEM, LOBE-THALAMUS]
see_also: [LOBE-BRAINSTEM, LOBE-THALAMUS]
synthesizes: [LOBE-BRAINSTEM]
---

# Neural Pathway: brainstem → thalamus

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `brainstem` connect to lobe `thalamus` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-BRAINSTEM` (brainstem)
- Target: `LOBE-THALAMUS` (thalamus)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
