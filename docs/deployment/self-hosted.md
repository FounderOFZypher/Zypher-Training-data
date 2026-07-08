# Self-Hosted Deployment

Coltex is **A Self-Hosted AI Knowledge Platform**. You install and run it on infrastructure you control — Windows servers, Linux, Docker, VPS, home servers, NAS, or cloud VMs. Your data never leaves your environment.

Localhost (`127.0.0.1`) is one deployment option, not the product itself.

---

## Deployment profiles

Configure in `config/deployment.yaml` or via environment variables.

### Local (development)

Loopback only — single machine.

```bash
coltex serve --profile local
# http://127.0.0.1:8787
```

### LAN (default)

Accessible to authorized devices on your network.

```bash
coltex serve --profile lan
# http://192.168.x.x:8080
# http://your-server-hostname:8080
```

### Production (domain + TLS)

```yaml
# config/deployment.yaml
deployment:
  profile: production
  domain: knowledge.company.com
  ssl:
    enabled: true
    cert_file: /etc/coltex/cert.pem
    key_file: /etc/coltex/key.pem
```

```bash
coltex serve --profile production
# https://knowledge.company.com
```

---

## Configuration reference

```yaml
deployment:
  mode: self-hosted
  profile: lan

  server:
    host: "0.0.0.0"    # bind all interfaces
    port: 8080

  protocol: http       # http | https
  domain: ""           # e.g. knowledge.company.com
  public_url: ""       # optional full URL override

  ssl:
    enabled: false
    cert_file: config/certs/cert.pem
    key_file: config/certs/key.pem

  networking:
    allow_remote: true
    cors_origins: ["*"]
```

### Environment overrides

```bash
export COLTEX_HOST=0.0.0.0
export COLTEX_PORT=8080
export COLTEX_DOMAIN=knowledge.company.com
export COLTEX_SSL_CERT=/etc/coltex/cert.pem
export COLTEX_SSL_KEY=/etc/coltex/key.pem
coltex serve
```

Inspect resolved config:

```bash
coltex deploy
```

---

## Windows Server

```cmd
cd C:\Coltex-Knowledge-Platform
python -m venv .venv
.venv\Scripts\activate.bat
pip install -e .
coltex serve --profile lan
```

Allow port **8080** in Windows Firewall for network access.

Access from other devices: `http://<server-ip>:8080`

---

## Linux / VPS

```bash
git clone https://github.com/FounderOfColtex/Coltex-Knowledge-Platform.git
cd Coltex-Knowledge-Platform
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
coltex serve --profile lan
```

Run as a systemd service:

```ini
[Unit]
Description=Coltex Self-Hosted Knowledge Platform
After=network.target

[Service]
Type=simple
User=coltex
WorkingDirectory=/opt/coltex
Environment=COLTEX_DEPLOYMENT_PROFILE=lan
ExecStart=/opt/coltex/.venv/bin/coltex serve --no-browser
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

---

## Docker

```bash
docker compose up -d
```

Default: binds `0.0.0.0:8080`, mounts `./workspaces` for persistent `.ctex` data.

```yaml
# docker-compose.yml overrides
environment:
  COLTEX_DOMAIN: knowledge.company.com
  COLTEX_SSL_CERT: /certs/cert.pem
  COLTEX_SSL_KEY: /certs/key.pem
  COLTEX_PROTOCOL: https
```

---

## Reverse proxy (HTTPS)

Place nginx or Caddy in front of Coltex:

```nginx
server {
    listen 443 ssl;
    server_name knowledge.company.com;
    ssl_certificate     /etc/ssl/certs/coltex.pem;
    ssl_certificate_key /etc/ssl/private/coltex.key;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Set in `config/deployment.yaml`:

```yaml
deployment:
  public_url: https://knowledge.company.com
```

---

## Kubernetes (planned)

Coltex is designed for container deployment. A Helm chart and Kubernetes manifests are on the roadmap. Until then, use Docker with your cluster's ingress controller.

---

## What stays the same

- `.ctex` workspaces
- Knowledge Studio UI
- AI processing pipeline
- Ask Knowledge, search, graph, embeddings
- MIT license — full source ownership

Only the **deployment model** changed: Coltex is infrastructure you host, not a localhost toy.
