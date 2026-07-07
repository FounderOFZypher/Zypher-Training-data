# Coltex Hypercortex — Living Brain v2

The most advanced connected RAG knowledge architecture: **6 cortical layers**, **10 brain lobes**, **4 memory tiers**, **18 neural hubs**, and **millions of graph edges**.

## Architecture
```
living-brain/
├── cortex/L1-sensory … L6-meta    # 6 cortical layers
├── lobes/frontal, temporal, …     # 10 functional lobes
├── domains/                       # 62+ technology domains
├── hubs/                          # 18 neural clusters
├── synapses/                      # Hub-to-hub links
├── pathways/                      # Lobe-to-lobe routes
├── memory/working|episodic|…      # 4 memory tiers
├── hippocampus/                   # Long-term consolidation
├── cerebellum/                    # CI/CD motor coordination
├── brainstem/                     # Autonomic ops
├── thalamus/                      # Query relay
├── amygdala/                      # Priority routing
└── reflexes/                      # Instant-recall FAQs
```

## Grow
```bash
make living-brain-advanced         # Full Hypercortex bootstrap
make living-brain-grow COUNT=1000  # Add domain documents
make living-brain-mega             # 10,000 documents
```

## Query
```bash
make index
python3 -m brain pulse
python3 -m brain retrieve "Explain Hypercortex pathway routing" --context
```
