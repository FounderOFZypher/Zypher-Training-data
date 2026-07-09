# Distributable Corpus

Streaming-generated original synthetic documents for Coltex Mega RAG commercial builds.

| Path | Purpose |
|------|---------|
| `_samples/` | Audit sample markdown files |
| `DATASET.md` | Load instructions |
| `data/product/catalog.jsonl` | Document catalog metadata |
| `data/product/chunks/chunks.jsonl` | Vector-ready chunks |

## Generation

```bash
make corpus-mega
make product

# Capped commercial validation
make product-mega-smoke

# Full Mega SKU (uncapped — cluster build)
make product-mega
```

All content is **original synthetic**, covered by the commercial [EULA](../../EULA.md), and must pass distribution audit.

Runtime source remains MIT — see [LICENSE](../../LICENSE).
