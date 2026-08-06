from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_ci_runs_the_w1_gate_and_release_idempotency_check() -> None:
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(
        encoding="utf-8"
    )

    assert "Run WorkBuddy W1 gate" in workflow
    assert "python -m golden_key_openmontage_workbuddy gate" in workflow
    assert "sync_workbuddy_core.py sync-release" in workflow
    assert "GH_TOKEN: ${{ github.token }}" in workflow
    assert "git diff --exit-code" in workflow
