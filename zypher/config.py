from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass
class ZypherConfig:
    xs_config_path: Path
    rag_config_path: Path
    xs: dict[str, Any]
    rag: dict[str, Any]

    @property
    def base_model(self) -> str:
        return self.xs.get("base_model") or self.xs["model"]["name"]

    @property
    def adapter_path(self) -> Path:
        path = self.xs.get("inference", {}).get("adapter_path")
        if path:
            return Path(path)
        return Path(self.xs["training"]["output_dir"]) / "final"

    @property
    def system_prompt(self) -> str:
        return self.rag["zypher"]["system_prompt"].strip()


def load_config(
    xs_path: Path | str = "config/zypher_xs.yaml",
    rag_path: Path | str = "config/rag.yaml",
) -> ZypherConfig:
    with Path(xs_path).open(encoding="utf-8") as f:
        xs = yaml.safe_load(f)
    with Path(rag_path).open(encoding="utf-8") as f:
        rag = yaml.safe_load(f)
    return ZypherConfig(Path(xs_path), Path(rag_path), xs, rag)
