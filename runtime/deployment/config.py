"""Self-hosted deployment configuration loader."""

from __future__ import annotations

import os
import socket
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_CONFIG = ROOT / "config/deployment.yaml"


@dataclass
class DeploymentConfig:
    mode: str = "self-hosted"
    tagline: str = "A Self-Hosted AI Knowledge Platform"
    profile: str = "lan"
    host: str = "0.0.0.0"
    port: int = 8080
    protocol: str = "http"
    domain: str = ""
    public_url: str = ""
    ssl_enabled: bool = False
    ssl_cert: Path | None = None
    ssl_key: Path | None = None
    open_browser: bool = False
    allow_remote: bool = True
    cors_origins: list[str] = field(default_factory=lambda: ["*"])
    studio_name: str = "Knowledge Studio"
    config_path: Path = DEFAULT_CONFIG

    @property
    def bind_address(self) -> tuple[str, int]:
        return self.host, self.port

    @property
    def base_url(self) -> str:
        if self.public_url:
            return self.public_url.rstrip("/")
        if self.domain:
            return f"{self.protocol}://{self.domain}".rstrip("/")
        host = self.host
        if host in ("0.0.0.0", "::"):
            host = get_lan_ip()
        if (self.protocol == "https" and self.port == 443) or (
            self.protocol == "http" and self.port == 80
        ):
            return f"{self.protocol}://{host}"
        return f"{self.protocol}://{host}:{self.port}"

    def access_urls(self) -> list[dict[str, str]]:
        urls: list[dict[str, str]] = []
        if self.public_url or self.domain:
            urls.append({"label": "Public URL", "url": self.base_url + "/"})
        if self.host in ("0.0.0.0", "::"):
            lan = get_lan_ip()
            port_suffix = "" if (
                (self.protocol == "https" and self.port == 443)
                or (self.protocol == "http" and self.port == 80)
            ) else f":{self.port}"
            urls.append({
                "label": "Network (LAN)",
                "url": f"{self.protocol}://{lan}{port_suffix}/",
            })
        if self.host in ("127.0.0.1", "localhost", "0.0.0.0", "::"):
            port_suffix = "" if (
                (self.protocol == "https" and self.port == 443)
                or (self.protocol == "http" and self.port == 80)
            ) else f":{self.port}"
            urls.append({
                "label": "Local",
                "url": f"{self.protocol}://127.0.0.1{port_suffix}/",
            })
        seen = set()
        unique = []
        for item in urls:
            if item["url"] not in seen:
                seen.add(item["url"])
                unique.append(item)
        return unique

    def to_dict(self) -> dict[str, Any]:
        return {
            "mode": self.mode,
            "tagline": self.tagline,
            "profile": self.profile,
            "host": self.host,
            "port": self.port,
            "protocol": self.protocol,
            "domain": self.domain or None,
            "public_url": self.public_url or None,
            "ssl": {
                "enabled": self.ssl_enabled,
                "cert_file": str(self.ssl_cert) if self.ssl_cert else None,
                "key_file": str(self.ssl_key) if self.ssl_key else None,
            },
            "networking": {
                "allow_remote": self.allow_remote,
                "cors_origins": self.cors_origins,
            },
            "studio": {"name": self.studio_name},
            "access_urls": self.access_urls(),
            "base_url": self.base_url + "/",
        }


def get_lan_ip() -> str:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"


def _resolve_path(value: str | None) -> Path | None:
    if not value:
        return None
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def load_deployment(
    config_path: str | Path | None = None,
    profile: str | None = None,
    host: str | None = None,
    port: int | None = None,
    protocol: str | None = None,
    domain: str | None = None,
    public_url: str | None = None,
    ssl_cert: str | None = None,
    ssl_key: str | None = None,
    open_browser: bool | None = None,
) -> DeploymentConfig:
    cfg_path = Path(config_path or os.environ.get("COLTEX_DEPLOYMENT_CONFIG", DEFAULT_CONFIG))
    if not cfg_path.is_absolute():
        cfg_path = ROOT / cfg_path

    raw: dict[str, Any] = {}
    if cfg_path.exists():
        raw = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
    dep = raw.get("deployment", {})

    active_profile = (
        profile
        or os.environ.get("COLTEX_DEPLOYMENT_PROFILE")
        or dep.get("profile", "lan")
    )
    profiles = dep.get("profiles", {})
    prof = profiles.get(active_profile, profiles.get("lan", {}))

    resolved_host = (
        host
        or os.environ.get("COLTEX_HOST")
        or dep.get("server", {}).get("host")
        or prof.get("host", "0.0.0.0")
    )
    resolved_port = port or _env_int("COLTEX_PORT") or dep.get("server", {}).get("port") or prof.get("port", 8080)
    resolved_protocol = (
        protocol
        or os.environ.get("COLTEX_PROTOCOL")
        or dep.get("protocol")
        or prof.get("protocol", "http")
    ).lower()

    ssl_cfg = dep.get("ssl", {})
    cert = ssl_cert or os.environ.get("COLTEX_SSL_CERT") or ssl_cfg.get("cert_file")
    key = ssl_key or os.environ.get("COLTEX_SSL_KEY") or ssl_cfg.get("key_file")
    cert_path = _resolve_path(cert)
    key_path = _resolve_path(key)

    ssl_enabled = bool(ssl_cfg.get("enabled", False))
    if cert_path and key_path and cert_path.exists() and key_path.exists():
        ssl_enabled = True
    elif resolved_protocol == "https" and not ssl_enabled:
        resolved_protocol = "http"
    if ssl_enabled:
        resolved_protocol = "https"

    net = dep.get("networking", {})
    browser = open_browser
    if browser is None:
        env_browser = os.environ.get("COLTEX_OPEN_BROWSER")
        if env_browser is not None:
            browser = env_browser.lower() in ("1", "true", "yes")
        else:
            browser = prof.get("open_browser", False)

    return DeploymentConfig(
        mode=dep.get("mode", "self-hosted"),
        tagline=dep.get("tagline", "A Self-Hosted AI Knowledge Platform"),
        profile=active_profile,
        host=resolved_host,
        port=int(resolved_port),
        protocol=resolved_protocol,
        domain=domain or os.environ.get("COLTEX_DOMAIN") or dep.get("domain", ""),
        public_url=public_url or os.environ.get("COLTEX_PUBLIC_URL") or dep.get("public_url", ""),
        ssl_enabled=ssl_enabled,
        ssl_cert=cert_path,
        ssl_key=key_path,
        open_browser=bool(browser),
        allow_remote=net.get("allow_remote", True),
        cors_origins=list(net.get("cors_origins", ["*"])),
        studio_name=dep.get("studio", {}).get("name", "Knowledge Studio"),
        config_path=cfg_path,
    )


def _env_int(name: str) -> int | None:
    value = os.environ.get(name)
    if value is None:
        return None
    try:
        return int(value)
    except ValueError:
        return None
