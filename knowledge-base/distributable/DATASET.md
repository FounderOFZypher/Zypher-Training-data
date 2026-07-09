# Coltex Mega RAG — Distributable Dataset Package

Commercial package orientation for the **100,000,000+** Mega RAG corpus.

## Contents

| Path | Description |
|------|-------------|
| `_samples/` | Audit sample markdown (first N from Mega stream) |
| `DATASET.md` | This file |
| `../PROVENANCE.md` | Content origin & compliance |

## Quick load (Python)

```python
import json

with open("data/product/chunks/chunks.jsonl") as f:
    chunks = [json.loads(line) for line in f]

with open("data/product/catalog.jsonl") as f:
    catalog = [json.loads(line) for line in f]

with open("data/product/graph/edges.jsonl") as f:
    edges = [json.loads(line) for line in f]

print(f"{len(catalog)} docs, {len(chunks)} chunks, {len(edges)} edges")
```

## Build from source

```bash
pip install -r requirements.txt
make product-mega-smoke    # capped commercial validation
make product-mega          # full 100M+ Mega SKU (cluster)
make marketplace-packs
make audit-distribution
```

## Sellable artifacts

| Artifact | Path |
|----------|------|
| Catalog | `data/product/catalog.jsonl` |
| Chunks | `data/product/chunks/chunks.jsonl` |
| Graph | `data/product/graph/edges.jsonl` |
| Manifest | `data/product/manifest.json` |
| Marketplace packs | `data/product/marketplace/packs.json` |
| Generation stats | `data/product/generation_stats.json` |

## Compliance

- **Commercial license:** [EULA.md](../../EULA.md) · [PROFESSIONAL-LICENSE.md](../../PROFESSIONAL-LICENSE.md) · [ENTERPRISE-LICENSE.md](../../ENTERPRISE-LICENSE.md) · [MEGA-LICENSE.md](../../MEGA-LICENSE.md)
- **Personal (non-commercial):** [PERSONAL-LICENSE.md](../../PERSONAL-LICENSE.md)
- **Engine:** MIT — [LICENSE](../../LICENSE)
- **Provenance:** `knowledge-base/PROVENANCE.md`
- **Audit:** `benchmarks/distribution_audit.json` (after build)
- **SKU docs:** [docs/commercial/sku-matrix.md](../../docs/commercial/sku-matrix.md)
