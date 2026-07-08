# Coltex

**A Self-Hosted AI Knowledge Platform**

Turn scattered business knowledge into AI-ready intelligence — deploy on your own infrastructure with complete data ownership.

## Quick start (self-hosted)

```bash
git clone https://github.com/FounderOfColtex/Coltex-Knowledge-Platform.git
cd Coltex-Knowledge-Platform
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate.bat
pip install -e .
coltex serve
```

Knowledge Studio is available to devices on your network at **http://\<your-server-ip\>:8080** (default `lan` profile).

### Deployment profiles

| Profile | Bind | Port | Use case |
|---------|------|------|----------|
| `local` | 127.0.0.1 | 8787 | Single-machine development |
| `lan` | 0.0.0.0 | 8080 | **Default** — LAN, home server, NAS, VPS |
| `production` | 0.0.0.0 | 443 | Domain + HTTPS |

```bash
coltex serve --profile local          # loopback only
coltex serve --profile lan            # network access (default)
coltex serve --profile production     # HTTPS on port 443
coltex serve --host 0.0.0.0 --port 8080
coltex deploy                         # show deployment config & access URLs
```

Configure in **`config/deployment.yaml`** — host, port, protocol, domain, SSL certificates, and networking.

Full guide: [docs/deployment/self-hosted.md](docs/deployment/self-hosted.md)

---

## Access examples

| Environment | URL |
|-------------|-----|
| Local development | `http://127.0.0.1:8787` |
| Office LAN | `http://192.168.x.x:8080` |
| Custom domain | `https://knowledge.company.com` |
| Docker / VPS | `http://your-server-ip:8080` |

---

## Docker

```bash
docker compose up -d
```

See [docs/deployment/self-hosted.md](docs/deployment/self-hosted.md) for Docker, Windows Server, Linux, and TLS setup.

---

## Knowledge Studio

| Page | Purpose |
|------|---------|
| **Dashboard** | Documents, embeddings, health, build workspace |
| **Workspace** | Create or open a `.ctex` workspace |
| **Knowledge** | Browse knowledge objects |
| **Sources** | Upload PDF, DOCX, MD, TXT, HTML, JSON |
| **Search** | Universal search |
| **Ask Knowledge** | Q&A with sources |
| **Settings** | Embedding model, chunk size, etc. |

---

## Workspace (.ctex)

Coltex projects are `.ctex` workspace files — like `.uproject` or `.blend`. Create from Knowledge Studio or:

```bash
coltex new MyWorkspace
coltex build
```

---

## Environment variables

| Variable | Purpose |
|----------|---------|
| `COLTEX_HOST` | Bind host (`0.0.0.0` for network) |
| `COLTEX_PORT` | Bind port |
| `COLTEX_PROTOCOL` | `http` or `https` |
| `COLTEX_DOMAIN` | Public domain |
| `COLTEX_PUBLIC_URL` | Full public URL override |
| `COLTEX_SSL_CERT` | TLS certificate path |
| `COLTEX_SSL_KEY` | TLS private key path |
| `COLTEX_DEPLOYMENT_PROFILE` | `local`, `lan`, or `production` |

---

## License

MIT — see [LICENSE](LICENSE).
