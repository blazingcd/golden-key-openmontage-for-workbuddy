from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "workbuddy-skill" / "golden-key-openmontage" / "SKILL.md"


def _read_skill() -> tuple[dict, str]:
    text = SKILL.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    _, frontmatter, body = text.split("---", 2)
    return yaml.safe_load(frontmatter), body


def test_workbuddy_skill_exposes_the_direct_agent_contract() -> None:
    metadata, body = _read_skill()

    assert metadata == {
        "name": "golden-key-openmontage",
        "description": (
            "Use Golden Key OpenMontage in WorkBuddy for brand/company, lead-conversion, "
            "product-marketing, and subject-IP video production through the locked pipeline, "
            "stage-skill, artifact, reviewer, and checkpoint contracts."
        ),
    }
    assert "WorkBuddy is the only Agent" in body
    assert "Read `AGENT_GUIDE.md` before production" in body
    assert "golden-key-workbuddy doctor" in body
    assert "MCP decision is pending" in body
    assert "Do not call a real or paid Provider without explicit user approval" in body


def test_workbuddy_config_directory_does_not_enable_mcp_prematurely() -> None:
    readme = (ROOT / ".workbuddy" / "README.md").read_text(encoding="utf-8")

    assert not (ROOT / ".workbuddy" / "mcp.json").exists()
    assert "Skill-first" in readme
    assert "MCP decision Gate" in readme


def test_workbuddy_skill_uses_the_w2_deterministic_lifecycle() -> None:
    _, body = _read_skill()

    for command in (
        "golden-key-workbuddy context",
        "golden-key-workbuddy pipelines",
        "golden-key-workbuddy project create",
        "golden-key-workbuddy project status",
        "golden-key-workbuddy stage inspect",
        "golden-key-workbuddy tool list",
        "golden-key-workbuddy tool execute",
        "golden-key-workbuddy task submit",
        "golden-key-workbuddy task status",
        "golden-key-workbuddy task run",
        "golden-key-workbuddy task cancel",
        "golden-key-workbuddy task recover",
        "golden-key-workbuddy config inspect",
        "golden-key-workbuddy config template",
        "golden-key-workbuddy artifact validate",
        "golden-key-workbuddy checkpoint submit",
    ):
        assert command in body
    assert "Only WorkBuddy selects the Pipeline" in body
    assert "inside the project's `artifacts/` directory" in body
    assert "--ack-agent-skill" in body
    assert "API or Hybrid" in body
    assert "WorkBuddy conversation model" in body
    assert "production Provider" in body
    assert "Submit validates and queues" in body
    assert "not safely cancelable" in body
    assert "never retry automatically" in body
