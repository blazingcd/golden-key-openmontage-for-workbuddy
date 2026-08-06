---
name: golden-key-openmontage
description: Use Golden Key OpenMontage in WorkBuddy for brand/company, lead-conversion, product-marketing, and subject-IP video production through the locked pipeline, stage-skill, artifact, reviewer, and checkpoint contracts.
---

# Golden Key OpenMontage for WorkBuddy

Treat this package as Pre-Alpha. WorkBuddy is the only Agent; never start or emulate a nested model-driven Agent Host.

## Preflight

1. Locate the checked-out Golden Key OpenMontage for WorkBuddy repository.
2. Run `golden-key-workbuddy doctor` from that repository. If the command is not installed yet, run `python -m golden_key_openmontage_workbuddy doctor`.
3. Read `AGENT_GUIDE.md` before production and obey Rule Zero.
4. Report missing local runtimes and Provider configuration without silently changing the requested production path.

## Production contract

1. Select one of the four Golden Key manifests from the user's request and grounded evidence:
   - `golden-key-brand-company`
   - `golden-key-lead-conversion`
   - `golden-key-product-marketing`
   - `golden-key-subject-ip`
2. Read the selected manifest in `pipeline_defs/`.
3. Before each stage, read the manifest-declared Stage Skill under `skills/pipelines/`.
4. Discover tools through the Tool Registry and stay within the current manifest/stage allowance.
5. Validate every canonical Artifact against its schema.
6. Run the Reviewer and obey the native Checkpoint/human-approval rules.

## Safety boundaries

- Do not call a real or paid Provider without explicit user approval.
- Do not bypass Stage Skills, Artifact validation, Reviewer, or Checkpoint gates.
- Do not import, launch, or recreate `agent_host_authority`, `model_driven_agent_host`, or `openai_compatible_transport`.
- The MCP decision is pending a real WorkBuddy comparison Gate. Do not require or invent an MCP server in W1.
- Do not claim installation readiness, real WorkBuddy acceptance, or `OFFLINE ADAPTER READY`.
