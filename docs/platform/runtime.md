# Coltex Runtime

Local CLI for the Coltex Mega RAG runtime.

## Start here

```bash
python3 -m runtime status
python3 -m runtime dashboard
```

## Commands

| Command | Capability |
|---------|------------|
| `python3 -m runtime status` | Runtime and engine status |
| `python3 -m runtime dashboard` | Documents, sources, searches, health |
| `python3 -m runtime upload file.pdf` | Upload and process a source |
| `python3 -m runtime sources` | List uploaded sources |
| `python3 -m runtime knowledge` | Browse knowledge objects |
| `python3 -m runtime search "..."` | Universal search |
| `python3 -m runtime ask "..."` | Ask Knowledge |
| `python3 -m runtime health` | Knowledge Health scores |
| `python3 -m runtime settings` | Workspace settings |
| `python3 -m runtime curator` | Proactive knowledge alerts |
| `python3 -m runtime monitor` | Runtime monitoring |
| `python3 -m runtime explain "..."` | Retrieval explainability |
| `python3 -m runtime connector filesystem` | Filesystem connector sync |
| `python3 -m runtime ingest DOC` | Event pipeline |

---

## Runtime architecture

```
Coltex Runtime (CLI)
├── Intelligence Engine    — relationship discovery, quality analysis
├── Search Engine          — hybrid knowledge object search
├── Memory Engine          — working → archive memory tiers
├── Scheduler              — automated maintenance jobs
├── Event Bus              — ingest cascade
├── Connectors             — filesystem, GitHub
└── Console                — web UI (coltex serve)
```

---

## Related

- [Platform overview](overview.md)
- [Commercial product](../commercial/product-overview.md)
- [Deployment](../deployment/self-hosted.md)
