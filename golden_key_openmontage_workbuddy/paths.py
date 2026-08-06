from __future__ import annotations

import os
from pathlib import Path


PRODUCT_DIRECTORY = "GoldenKeyOpenMontageForWorkBuddy"


def default_repo_root() -> Path:
    configured = os.environ.get("OPENMONTAGE_WORKBUDDY_ROOT")
    if configured:
        return Path(configured).expanduser().resolve()
    return Path(__file__).resolve().parents[1]


def default_data_root() -> Path:
    configured = os.environ.get("OPENMONTAGE_WORKBUDDY_DATA_ROOT")
    if configured:
        return Path(configured).expanduser().resolve()

    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        return (
            Path(local_app_data) / PRODUCT_DIRECTORY / "Data"
        ).expanduser().resolve()

    xdg_data_home = os.environ.get("XDG_DATA_HOME")
    if xdg_data_home:
        return (Path(xdg_data_home) / PRODUCT_DIRECTORY / "Data").resolve()

    return (Path.home() / ".local" / "share" / PRODUCT_DIRECTORY / "Data").resolve()
