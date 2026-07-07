# Coltex — Setup Guide

Build, grow, and query the Coltex Living Brain.

## Install

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Bootstrap the living brain

```bash
make living-brain                 # 300 domain docs + synapses + neural map
make living-brain-grow COUNT=500  # grow further
make living-brain-mega            # 10,000 documents
```

## Index and query

```bash
make index
python3 -m brain retrieve "How does GraphRAG work?" --context
python3 -m brain pulse
make living-brain-pulse
```

## Build dataset for distribution

```bash
# Premium smoke (25,000 documents)
make product-premium-smoke

# Full hyper tier (cluster deployment)
make product-hyper

# Compliance audit
make audit-distribution
```

## Output artifacts

| Artifact | Path |
|----------|------|
| Chunks | `data/product/chunks/chunks.jsonl` |
| Catalog | `data/product/catalog.jsonl` |
| Embeddings | `data/product/embeddings/embeddings.jsonl` |
| Graph | `data/product/graph/edges.jsonl` |
| Manifest | `data/product/manifest.json` |
| Neural map | `data/brain/neural-map.json` |

## Query examples

```bash
make index
python3 -m brain retrieve "How does GraphRAG work?" --context
python3 examples/rag_query.py "chunking strategies"
```

## Corpus generation tiers

| Command | Approximate output |
|---------|-------------------|
| `make living-brain` | 300+ domain-organized docs |
| `make generate-smoke` | 2,000 documents |
| `make generate-mega` | 100,000 documents |
| `make generate-ultra` | 1,000,000 documents |
| `make generate-hyper` | Uncapped streaming |

See [README](../README.md) for full living brain architecture.
