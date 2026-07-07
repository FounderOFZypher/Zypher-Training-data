# Coltex Living Brain

The largest connected RAG knowledge brain — domains, hubs, synapses, and graph-linked documents.

## Grow the brain
```bash
make living-brain              # scaffold folders + synapses + neural map
make living-brain-grow COUNT=500   # add 500 domain documents
make living-brain-mega         # 10,000 documents across all domains
```

## Query
```bash
make index
python3 -m brain retrieve "How does GraphRAG traverse synapses?" --context
python3 -m brain pulse
```

## Structure
```
living-brain/
├── domains/     # 30+ technology domains
├── hubs/        # Neural clusters (auth, GraphRAG, indexing…)
├── synapses/    # Cross-domain graph links
├── cortex/      # Brain meta-layer
├── memory/      # Episodic knowledge
└── reflexes/    # Fast-path operational docs
```
