---
id: PATHWAY-0600
title: "Neural Pathway: brainstem → frontal (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: brainstem
lobe_target: frontal
pathway_type: inhibitory
tags: [pathway, inhibitory, brainstem, frontal]
related: [LOBE-BRAINSTEM, LOBE-FRONTAL]
see_also: [LOBE-BRAINSTEM, LOBE-FRONTAL]
synthesizes: [LOBE-BRAINSTEM]
---

# Neural Pathway: brainstem → frontal

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `brainstem` connect to lobe `frontal` via this commissural pathway.

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
- Target: `LOBE-FRONTAL` (frontal)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
