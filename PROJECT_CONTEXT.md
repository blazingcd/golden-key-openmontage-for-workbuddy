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
verified external OpenMontage Package -> OpenMontage Agent production
```

Shell V2 owns installation/lifecycle, Package Registration/Locator, runtime preparation, Launcher, WorkBuddy entry, and status/result relay. It verifies and binds external Package identity but does not select or execute Pipeline, Stage, Provider, model, media, or creative work.

## Current implementation

- `golden_key_openmontage_workbuddy/package_registration.py`: Stage 2 Package Registration and Locator implementation.
- `tests/workbuddy/test_package_registration.py`: its contract evidence.
- `docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`: stable behavior and wire contract.

Stage 3 implementation and Stages 4-6 are not authorized. The reduced plan is also fail-closed on necessity: Stage 3 and Stage 6 may complete with zero production code, Stage 4 is one controlled process launch, and Stage 5 is one explicit WorkBuddy entry. No Launcher, WorkBuddy entry, runtime preparation, or status/result relay implementation may be inferred from planning or scope-review authorization.

## Authority order

1. `docs/workbuddy/v2/TASK-REGISTER.md` — live state, exact objects, authorization, next task.
2. `docs/workbuddy/v2/PROJECT-CHARTER.md` — product roles and six-module responsibilities.
3. `docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md` — accepted Stage 2 contract.
4. `docs/workbuddy/v2/ACCEPTANCE-MATRIX.md` — evidence meanings and gates.
5. `docs/workbuddy/v2/DRIFT-GUARD.md` — stop rules and Git lifecycle.
6. `docs/workbuddy/v2/MODULE-DISPOSITION.md` — historical V1 capability disposition.

Git history preserves retired plans, prompts, reports, and evidence; they are not active authority.
