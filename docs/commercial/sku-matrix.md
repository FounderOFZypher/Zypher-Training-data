# Coltex SKU Matrix

License tiers and commercial packages for the Coltex RAG Vector Dataset.

---

## License tiers

| | **Personal** | **Commercial (EULA)** |
|---|--------------|------------------------|
| **SKU** | `coltex-personal-v1` | `coltex-enterprise-v3` / premium tiers |
| **Price** | **$79 USD** (one-time) | Contact / $1,000+ |
| **License** | [PERSONAL-LICENSE.md](../PERSONAL-LICENSE.md) | [EULA.md](../EULA.md) |
| **Use case** | Non-commercial, personal | Business & production |
| **Intended users** | Students, hobbyists, researchers | Teams, enterprises, vendors |
| **Build command** | `make product-personal` | `make product-enterprise` |

### Personal License — $79

- Install on personal devices or servers
- Personal learning, experimentation, research
- Private AI projects
- **Not** for commercial use, SaaS, resale, or redistribution

See [PERSONAL-LICENSE.md](../PERSONAL-LICENSE.md) for full terms.

---

## Commercial dataset tiers

| | **Enterprise Curated** | **Premium Standard** | **Premium Hyper** |
|---|------------------------|----------------------|-------------------|
| **SKU** | `coltex-enterprise-v3` | `coltex-premium-v2.1` | `coltex-premium-hyper-v2.1` |
| **Price** | Contact | $1,000+ | $1,000+ (volume) |
| **Documents** | 12,993 curated | 25,000 streamed | Uncapped |
| **Domains** | 63 | 27 categories | 27+ categories |
| **Graph architecture** | Full (hubs, links, routes) | Streamed edges | Streamed edges |
| **Embeddings** | Optional | Pre-computed (500k cap) | Cluster-scale |
| **Benchmarks** | 200+ pairs | 500+ pairs | 500+ pairs |
| **Audit report** | ✅ | ✅ | ✅ |
| **Build command** | `make product-enterprise` | `make product-premium-smoke` | `make product-hyper` |
| **Best for** | Production RAG | Buyer validation | Maximum scale |

---

## What's included (commercial tiers)

- Coltex EULA with full provenance documentation
- `manifest.json` with SHA-256 checksums
- `distribution_audit.json` compliance report
- Typed metadata on every document
- Quality gate validation
- Benchmark datasets

---

## Support & delivery

| Delivery method | Format |
|-----------------|--------|
| Git release tarball | `.tar.gz` with `data/product/` |
| Cloud storage | S3 / GCS signed URL |
| Hugging Face Dataset | Parquet or JSONL |

Contact: repository maintainer for licensing and delivery.
