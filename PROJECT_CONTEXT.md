# WorkBuddy Shell V2 Project Context

This repository is the WorkBuddy Shell V2 product, not an embedded OpenMontage production repository.

## Architecture

```text
User <-> WorkBuddy conversation
        |
        v
WorkBuddy Shell V2 six modules
        |
        v
verified Golden Key OpenMontage Package -> WorkBuddy assumes OpenMontage production role
```

Tencent WorkBuddy is the only running Agent. Shell V2 owns installation/lifecycle, Package Registration/Locator, runtime preparation, Launcher, WorkBuddy entry, and status/result relay. It verifies and binds Package/runtime identity but does not select or execute Pipeline, Stage, Provider, model, media, or creative work. "OpenMontage Agent" denotes the production role WorkBuddy assumes after reading the verified Package Guide, not a separately launched Agent process.

## Current implementation and evidence boundary

- `golden_key_openmontage_workbuddy/package_registration.py`: Stage 2 Package Registration and Locator implementation.
- `golden_key_openmontage_workbuddy/runtime_prepare.py`: accepted Stage 3 bounded optional-capability preparation.
- `golden_key_openmontage_workbuddy/session_launcher.py`: accepted Stage 4 fixed Package-tool Launcher.
- `tests/workbuddy/test_package_registration.py`, `tests/workbuddy/test_runtime_prepare.py`, and `tests/workbuddy/test_session_launcher.py`: direct contract evidence.
- `docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`: accepted Stage 2 Registration/Locator contract and its non-Installer boundary.

Stage 2 has accepted the Registration/Locator implementation and one real temporary-Package validation containing the complete required private toolchain: a usable Python 3.10+ environment with locked core dependencies, FFmpeg/ffprobe, and Node/npm/npx at the highest current Package floor (currently Node 22+). The temporary Package was cleaned up. No retained final Release, installed production PackageRoot, or production Package Registration currently follows from that PASS; final Package materialization and production Registration remain a later final-delivery/Installer task due before Stage 5 production acceptance, not a Stage 3 or Stage 4 prerequisite.

Stage 3 planning and implementation are `PASS_ACCEPTED`. Its single public entry is `prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`, and its result set is exactly `DETECTION_REPORT / CONSENT_REQUIRED / INTEGRATED / SKIPPED / BLOCKED`. It performs bounded detection of optional Remotion and HyperFrames capabilities, returns a zero-download plan for missing or incompatible items, and integrates only a capability explicitly approved by the user. Stage 3 does not assemble the final Package, create production Registration, touch Python/FFmpeg/Node, select a renderer, scan drives, run video, or automatically replay a business request. Optional downloads use approved mainland-China mirrors with no automatic overseas fallback.

Stage 4 planning and implementation are also `PASS_ACCEPTED`. Its single public entry is `launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`. The Launcher accepts only a release-specific immutable `PackageToolDefinitionV1` supplied by the approved Package definition/final-delivery Installer owner, spawns exactly one fixed Package tool, and returns a recursively immutable `LauncherReceiptV1` limited to nine outcomes. It remains Provider- and runtime-opaque; it does not select or configure Remotion, HyperFrames, or any Provider.

The current accepted repository tree tracks exactly 37 files. Stage 5 WorkBuddy entry and Stage 6 status/result relay remain `NOT_GRANTED`, and final Package materialization/production Registration remain unproven. Stage 5 is the future end-user entry; it will invoke Stage 2 Locator, pass the literal user message separately from controls, and call Stage 4. Stage 6 will relay facts and should directly reuse `LauncherReceiptV1` when no real conversion gap exists. If future Stage 5 real-client evidence shows that WorkBuddy cannot continue the same task after consent, WorkBuddy asks the user to say `继续刚才的任务`; Shell never auto-replays.

The previous Stage 3 execution packet, `prepare_runtime_on_demand(...)` and `prepare_optional_capability(...)` signatures, Shell-owned all-component Runtime Lock, Package-bound capability model, and pre-implementation Stage 4 gates are `SUPERSEDED`. They may remain only as explicitly historical evidence and do not override the accepted Stage 3/4 contracts above.

## Authority order

1. `docs/workbuddy/v2/TASK-REGISTER.md` — live state, exact objects, authorization, next task.
2. `docs/workbuddy/v2/PROJECT-CHARTER.md` — product roles and six-module responsibilities.
3. `docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md` — accepted Stage 2 complete-toolchain Registration/Locator contract and temporary-proof boundary.
4. `docs/workbuddy/v2/ACCEPTANCE-MATRIX.md` — evidence meanings and gates.
5. `docs/workbuddy/v2/DRIFT-GUARD.md` — stop rules and Git lifecycle.
6. `docs/workbuddy/v2/MODULE-DISPOSITION.md` — historical V1 capability disposition.

Git history preserves retired plans, prompts, reports, and evidence; they are not active authority.
