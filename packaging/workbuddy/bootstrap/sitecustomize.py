from __future__ import annotations

import os
import sys
from pathlib import Path


data_root = os.environ.get("OPENMONTAGE_WORKBUDDY_DATA_ROOT", "").strip()
if data_root:
    managed_packages = Path(data_root) / "Runtime" / "Python" / "site-packages"
    if managed_packages.is_dir():
        managed_path = str(managed_packages.resolve())
        if managed_path not in sys.path:
            sys.path.insert(0, managed_path)
