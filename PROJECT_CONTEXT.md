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

## Current implementation

- `golden_key_openmontage_workbuddy/package_registration.py`: Stage 2 Package Registration and Locator implementation.
- `tests/workbuddy/test_package_registration.py`: its contract evidence.
- `docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`: previous-package behavior plus the current refresh adjudication.

Stage 3 implementation and Stages 4-6 are not authorized. The runtime scope is now corrected from historical evidence: private Python is bundled in the Golden Key Package; Stage 3 performs closed-set discovery and missing-only preparation for Python dependencies, FFmpeg, Node, Remotion, HyperFrames, and the locked browser, with explicit consent and mainland-China-only end-user download sources. Stage 4 binds one WorkBuddy-owned session and does not launch a second Agent. No Launcher, WorkBuddy entry, runtime preparation, or status/result relay implementation may be inferred from documentation authorization.

## Authority order

1. `docs/workbuddy/v2/TASK-REGISTER.md` — live state, exact objects, authorization, next task.
2. `docs/workbuddy/v2/PROJECT-CHARTER.md` — product roles and six-module responsibilities.
3. `docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md` — previous-package Stage 2 contract and current refresh boundary.
4. `docs/workbuddy/v2/ACCEPTANCE-MATRIX.md` — evidence meanings and gates.
5. `docs/workbuddy/v2/DRIFT-GUARD.md` — stop rules and Git lifecycle.
6. `docs/workbuddy/v2/MODULE-DISPOSITION.md` — historical V1 capability disposition.

Git history preserves retired plans, prompts, reports, and evidence; they are not active authority.
