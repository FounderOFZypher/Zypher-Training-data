# Coltex Product Licensing

## License tiers

Coltex offers three license tiers depending on your use case:

| Tier | Price | License | Best for |
|------|-------|---------|----------|
| **Personal** | **$79 USD** (one-time) | [PERSONAL-LICENSE.md](../PERSONAL-LICENSE.md) | Students, hobbyists, researchers — non-commercial |
| **Professional** | **$399 USD** (one-time) | [PROFESSIONAL-LICENSE.md](../PROFESSIONAL-LICENSE.md) | Freelancers, startups, commercial developers — one entity |
| **Enterprise** | Contact / $1,000+ | [EULA.md](../EULA.md) | Large-scale dataset packages, enterprise deployment |

Choose the tier that matches your intended use.

---

## Personal License — $79 USD

**Intended users:** Students, hobbyists, researchers, and individuals using Coltex for non-commercial purposes.

**You may:** Install on personal devices, learn and experiment, create private AI projects, modify for personal use, receive updates (if offered).

**You may not:** Commercial use, sell services, offer SaaS/hosted Coltex, redistribute or resell, share license keys, remove copyright notices.

Full terms: [PERSONAL-LICENSE.md](../PERSONAL-LICENSE.md)

---

## Professional License — $399 USD

**Intended users:** Freelancers, consultants, startups, software companies, and commercial developers.

**Includes everything in the Personal License, plus:**

- Use Coltex in commercial products
- Build AI applications and generate revenue
- Deploy Coltex within your business
- Fine-tune AI models using Coltex-processed data (where applicable)
- Integrate Coltex into customer-facing software

**Restrictions:** No reselling original Coltex software, no competing hosted service without permission, no selling copies, no sharing across organizations, no removing notices.

**Scope:** One company or one legal entity (additional seats available). Priority email support may be included if offered.

Full terms: [PROFESSIONAL-LICENSE.md](../PROFESSIONAL-LICENSE.md) · Summary: [knowledge-base/PROFESSIONAL-LICENSE.md](../knowledge-base/PROFESSIONAL-LICENSE.md)

---

## Enterprise License (EULA)

The Coltex **Enterprise RAG Vector Dataset** for large-scale commercial deployment is licensed under the **Coltex End User License Agreement (EULA)**.

| Document | Purpose |
|----------|---------|
| [EULA.md](../EULA.md) | Full enterprise End User License Agreement |
| [knowledge-base/EULA.md](../knowledge-base/EULA.md) | Dataset scope summary |
| [PROVENANCE.md](../knowledge-base/PROVENANCE.md) | Content origin and compliance |
| [NOTICE](../NOTICE) | Third-party open-source dependencies (engine tooling only) |

See [EULA.md](../EULA.md) for complete terms. SKU details: [commercial/sku-matrix.md](commercial/sku-matrix.md).

---

## Build commands by tier

```bash
# Personal ($79 — non-commercial)
make product-personal

# Professional ($399 — commercial, one entity)
make product-professional

# Enterprise (commercial dataset packages)
make product-enterprise
make product-premium-smoke

# Compliance audit
make audit-distribution
```

---

## Disclaimer

This document summarizes the licensing approach. It is not legal advice. Consult qualified counsel before commercial use.

For enterprise agreements, additional seats, or tier upgrades: contact the repository maintainer.
