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

Stage 3 implementation and Stages 4-6 are not authorized. The Golden Key Package must bundle a usable private Python 3.10+ environment and locked core dependencies, FFmpeg/ffprobe, and Node/npm/npx at the highest current Package floor (currently Node 22+). Reopened Stage 2 must register and locate this complete required toolchain; the previous Python-only implementation is historical evidence. Stage 3 may prepare only one optional Remotion or HyperFrames capability already selected and locked by WorkBuddy/OpenMontage, plus assets explicitly declared by that capability. It does not choose a renderer or compensate for missing Package prerequisites. Optional end-user downloads require consent and approved mainland-China mirrors; the exact `gyan.dev` FFmpeg candidate belongs to Package assembly, not Stage 3. No Launcher, WorkBuddy entry, runtime preparation, or status/result relay implementation may be inferred from documentation authorization.

The previous Stage 3 execution packet, `prepare_runtime_on_demand(...)` signature, all-component Runtime Lock, and conditional authorization are `SUPERSEDED` or suspended. A new exact task packet can be frozen only after Stage 2's complete required-toolchain output is independently accepted and the real WorkBuddy/OpenMontage consumer contract defines when and how it submits one locked optional-capability request. The same-session pause/consent/continue boundary must also be proven there; the Shell must not guess it or automatically replay the original request.

## Authority order

1. `docs/workbuddy/v2/TASK-REGISTER.md` — live state, exact objects, authorization, next task.
2. `docs/workbuddy/v2/PROJECT-CHARTER.md` — product roles and six-module responsibilities.
3. `docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md` — previous-package Stage 2 contract and current refresh boundary.
4. `docs/workbuddy/v2/ACCEPTANCE-MATRIX.md` — evidence meanings and gates.
5. `docs/workbuddy/v2/DRIFT-GUARD.md` — stop rules and Git lifecycle.
6. `docs/workbuddy/v2/MODULE-DISPOSITION.md` — historical V1 capability disposition.

Git history preserves retired plans, prompts, reports, and evidence; they are not active authority.
