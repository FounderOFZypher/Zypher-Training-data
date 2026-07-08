# Coltex V1 — Self-Hosted Product

**Tagline:** A Self-Hosted AI Knowledge Platform

**Goal:** Turn scattered business knowledge into AI-ready intelligence in under 10 minutes — on infrastructure you control.

Deploy on Windows Server, Linux, Docker, VPS, home servers, NAS, or cloud VMs. Localhost is one profile, not the product.

---

## Start Knowledge Studio

```bash
pip install -e .
coltex serve                  # self-hosted on LAN (default profile)
coltex serve --profile local  # loopback only
coltex deploy                 # show access URLs
```

---

## Deployment

See [docs/deployment/self-hosted.md](../deployment/self-hosted.md)

Config: `config/deployment.yaml`

---

## License

MIT — see [LICENSE](../../LICENSE).
