from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "workbuddy-skill" / "golden-key-openmontage" / "SKILL.md"
ONBOARDING_SKILL = (
    ROOT / "workbuddy-skill" / "golden-key-openmontage-onboarding" / "SKILL.md"
)


def _read_skill(path: Path = SKILL) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
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
    assert "MCP is optional, local, and deterministic" in body
    assert "direct CLI is the canonical fallback" in body
    assert "Do not call a real or paid Provider without explicit user approval" in body


def test_workbuddy_config_directory_defers_optional_mcp_to_w4_packaging() -> None:
    readme = (ROOT / ".workbuddy" / "README.md").read_text(encoding="utf-8")

    assert not (ROOT / ".workbuddy" / "mcp.json").exists()
    assert "Skill-first" in readme
    assert "MCP" in readme


def test_registered_skills_use_the_portable_runtime_locator_before_doctor() -> None:
    for skill_path in (SKILL, ONBOARDING_SKILL):
        _, body = _read_skill(skill_path)
        assert "WORKBUDDY-RUNTIME.json" in body
        assert "launcher" in body
        assert "doctor --json" in body
        assert "Do not guess or search the user's drives" in body

    _, production = _read_skill(SKILL)
    assert "Locate the checked-out" not in production


def test_production_skill_requires_user_consent_before_dependency_downloads() -> None:
    _, body = _read_skill(SKILL)

    assert "runtime plan --json" in body
    assert "runtime prepare --confirm-download --json" in body
    assert "explicitly agrees" in body
    assert "does not modify the system Python" in body
    assert "Node is optional" in body
    assert "FFmpeg is required for compose" in body


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


def test_workbuddy_onboarding_is_a_separate_consumer_skill() -> None:
    metadata, body = _read_skill(ONBOARDING_SKILL)

    assert metadata["name"] == "golden-key-openmontage-onboarding"
    description = metadata["description"]
    assert "new or uncertain WorkBuddy users" in description
    assert "Do not use once" in description

    for command in (
        "golden-key-workbuddy doctor",
        "golden-key-workbuddy context",
        "golden-key-workbuddy pipelines",
        "golden-key-workbuddy config inspect",
        "golden-key-workbuddy config guide",
    ):
        assert command in body

    assert "WorkBuddy consumer experience" in body
    assert "not a Golden Key Core stage" in body
    assert "stop onboarding" in body
    assert "`golden-key-openmontage` production Skill" in body
    assert "must not invent a parallel business-questionnaire contract" in body
    assert "配置API密钥.cmd" in body
    assert "Do not ask the user to paste" in body
    assert "present_unverified" in body


def test_workbuddy_onboarding_does_not_own_material_inventory_or_setup() -> None:
    _, body = _read_skill(ONBOARDING_SKILL)

    assert "Guide material handoff" in body
    assert "Existing source materials" in body
    assert "Reference material" in body
    assert "No material yet" in body
    assert "Ask at most one material-handoff question" in body
    assert "attach or drag in only the files relevant to this video" in body
    assert "Do not ask the user to inventory or list all available materials" in body
    assert "Do not hardcode a C-drive or D-drive location" in body
    assert "claim that WorkBuddy has imported, indexed, or understood a file" in body
    assert "Do not manage a Golden Key SaaS material library" in body
    assert "Do not put onboarding behavior into the managed Golden Key Core" in body
    assert "Do not call a real or paid Provider" in body
    assert "Do not present MCP, Python, CLI" in body


def test_production_skill_guides_missing_provider_keys_without_chat_secrets() -> None:
    _, body = _read_skill(SKILL)

    assert "config guide --json" in body
    assert "配置API密钥.cmd" in body
    assert "Do not ask the user to paste" in body
    assert "present_unverified" in body
    assert "does not authorize a Provider call" in body
