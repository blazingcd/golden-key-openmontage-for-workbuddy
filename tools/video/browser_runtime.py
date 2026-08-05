"""Shared local-browser discovery for browser-backed video runtimes.

Remotion and HyperFrames both need a Chromium-family executable. Runtime
availability must not depend on an implicit first-run browser download: that
can hang in restricted/offline environments and makes preflight lie.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import Iterable, Optional


def resolve_browser_executable(
    explicit: str | None = None,
    *,
    env_keys: Iterable[str] = (),
) -> Optional[str]:
    """Return an existing Chrome/Chromium/Edge executable, if available."""

    requested = [explicit]
    requested.extend(os.environ.get(key) for key in env_keys)
    for raw in requested:
        if raw and Path(raw).expanduser().is_file():
            return str(Path(raw).expanduser().resolve())

    for command in (
        "chrome",
        "chrome.exe",
        "chromium",
        "chromium.exe",
        "msedge",
        "msedge.exe",
    ):
        found = shutil.which(command)
        if found:
            return str(Path(found).resolve())

    candidates: list[Path] = []
    if os.name == "nt":
        for root_name in ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA"):
            root = os.environ.get(root_name)
            if not root:
                continue
            base = Path(root)
            candidates.extend(
                [
                    base / "Google" / "Chrome" / "Application" / "chrome.exe",
                    base / "Microsoft" / "Edge" / "Application" / "msedge.exe",
                ]
            )
    elif os.name == "posix":
        candidates.extend(
            [
                Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
                Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
                Path("/usr/bin/google-chrome"),
                Path("/usr/bin/chromium"),
                Path("/usr/bin/chromium-browser"),
            ]
        )

    for candidate in candidates:
        if candidate.is_file():
            return str(candidate.resolve())
    return None


def resolve_remotion_root(
    explicit: str | None = None,
    *,
    repo_root: Path | None = None,
) -> Optional[Path]:
    """Resolve a prepared remotion-composer without installing dependencies."""

    candidates: list[Path] = []
    requested = explicit or os.environ.get("OPENMONTAGE_REMOTION_ROOT")
    if requested:
        candidates.append(Path(requested).expanduser())
    candidates.append(Path.cwd() / "remotion-composer")
    if repo_root is not None:
        candidates.append(repo_root / "remotion-composer")

    for candidate in candidates:
        if (
            candidate.is_dir()
            and (candidate / "package.json").is_file()
            and (candidate / "node_modules").is_dir()
        ):
            return candidate.resolve()
    return None
