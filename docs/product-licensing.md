# Coltex Product Licensing

## License tiers

Coltex offers two license tiers depending on your use case:

| Tier | Price | License | Best for |
|------|-------|---------|----------|
| **Personal** | **$79 USD** (one-time) | [PERSONAL-LICENSE.md](../PERSONAL-LICENSE.md) | Students, hobbyists, researchers — non-commercial use |
| **Commercial** | Contact / $1,000+ | [EULA.md](../EULA.md) | Businesses, production RAG, revenue-generating products |

Choose the tier that matches your intended use. Commercial activity requires the EULA, not the Personal License.

---

## Personal License — $79 USD

**Intended users:** Students, hobbyists, researchers, and individuals using Coltex for non-commercial purposes.

**You may:** Install on personal devices, learn and experiment, create private AI projects, modify for personal use, receive updates (if offered).

**You may not:** Commercial use, sell services, offer SaaS/hosted Coltex, redistribute or resell, share license keys, remove copyright notices, reverse engineer to compete commercially.

Full terms: [PERSONAL-LICENSE.md](../PERSONAL-LICENSE.md) · Summary: [knowledge-base/PERSONAL-LICENSE.md](../knowledge-base/PERSONAL-LICENSE.md)

---

## Commercial License (EULA)

The Coltex **Dataset** for commercial use (knowledge base, vector chunks, embeddings, graph edges, benchmarks, product artifacts) is licensed under the **Coltex End User License Agreement (EULA)**.

| Document | Purpose |
|----------|---------|
| [EULA.md](../EULA.md) | Full commercial End User License Agreement |
| [knowledge-base/EULA.md](../knowledge-base/EULA.md) | Dataset scope summary |
| [knowledge-base/LICENSE](../knowledge-base/LICENSE) | Purchaser rights summary |
| [PROVENANCE.md](../knowledge-base/PROVENANCE.md) | Content origin and compliance |
| [NOTICE](../NOTICE) | Third-party open-source dependencies (engine tooling only) |

### What the EULA covers

| Content | License | Included in product? |
|---------|---------|---------------------|
| Distributable `CHUNK-*.md` files | Coltex EULA | Yes (commercial tier) |
| Product artifacts (`data/product/`) | Coltex EULA | Yes |
| Benchmark datasets (`benchmarks/`) | Coltex EULA | Yes |
| `knowledge-base/_excluded_from_distribution/` | — | **No** |
| `knowledge-base/generated/` | — | **No** |

### Commercial permitted use (summary)

- Internal and production RAG / AI development
- Build and sell commercial software powered by the Dataset
- Load chunks and embeddings into your vector databases
- Create derivative products (no raw Dataset redistribution)

### Commercial restrictions (summary)

- No reselling raw Dataset as a standalone product
- No public redistribution to repos or model hubs
- No removing provenance or EULA notices

See [EULA.md](../EULA.md) for complete terms. SKU details: [commercial/sku-matrix.md](commercial/sku-matrix.md).

---

## Third-party dependencies (runtime)

The Coltex **engine** uses open-source libraries listed in [NOTICE](../NOTICE). Those components remain under their respective licenses (Apache-2.0, MIT, BSD, etc.).

Runtime dependencies are **not bundled** in the Dataset package. You are responsible for their license compliance when used.

---

## Build commands by tier

```bash
# Personal tier ($79 — non-commercial)
make product-personal

# Commercial tiers
make product-enterprise
make product-premium-smoke

# Compliance audit
make audit-distribution
```

---

## Disclaimer

This document summarizes the licensing approach. It is not legal advice. Consult qualified counsel before commercial use.

For enterprise agreements or tier upgrades: contact the repository maintainer.
