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
- `tests/workbuddy/test_package_registration.py`: its contract evidence.
- `docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`: accepted Stage 2 Registration/Locator contract and its non-Installer boundary.

Stage 2 has accepted the Registration/Locator implementation and one real temporary-Package validation containing the complete required private toolchain: a usable Python 3.10+ environment with locked core dependencies, FFmpeg/ffprobe, and Node/npm/npx at the highest current Package floor (currently Node 22+). The temporary Package was cleaned up. No retained final Release, installed production PackageRoot, or production Package Registration currently follows from that PASS; Installer/final distribution remains a separate pre-Stage-3 Gate.

Stage 3 planning is now narrowed to one optional capability already selected by WorkBuddy/OpenMontage: `none`, Remotion, or HyperFrames. The Package owns the exact capability Lock; Shell only verifies it and prepares missing assets under managed `DataRoot` paths. Stage 3 does not assemble the final Package, create production Registration, touch Python/FFmpeg/Node, select a renderer, scan drives, run video, or automatically replay a business request. Optional end-user downloads require an exact missing-only plan, explicit consent, and approved mainland-China mirrors with no automatic overseas fallback. The exact `gyan.dev` FFmpeg candidate belongs to Package assembly, not Stage 3.

The proposed single public entry is `prepare_optional_capability(data_root, capability_request, authorization_receipt=None)`. It returns only `NO_OPTIONAL_CAPABILITY_REQUIRED`, `READY_REUSED`, `CONSENT_REQUIRED`, `READY_PREPARED`, or `BLOCKED`. The maximum future code surface is one new `runtime_prepare.py`, an export-only `__init__.py` edit, and one direct `test_runtime_prepare.py`; documentation planning is not implementation authorization.

Stage 3 implementation and Stages 4-6 remain `NOT_GRANTED`. Stage 3 can start only from the latest exact formal commit after a final Release is retained, a production PackageRoot is installed and registered, Locator revalidates it in a new process, Package-owned capability Locks are Manifest-covered, and the real WorkBuddy consumer contract freezes pause/consent/continue behavior. Stage 5 is the end-user entry; it invokes Stage 2 Locator, Stage 4 may make a base fixed-tool call with the bundled prerequisites, and only optional Remotion/HyperFrames execution additionally requires a Stage 3 receipt bound to the same Registration and capability Lock. Stage 6 relays facts only. If WorkBuddy cannot continue the same session after consent, it asks for a new explicit invocation; Shell never auto-replays.

The previous Stage 3 execution packet, `prepare_runtime_on_demand(...)` signature, Shell-owned all-component Runtime Lock, and conditional authorization are `SUPERSEDED`.

## Authority order

1. `docs/workbuddy/v2/TASK-REGISTER.md` — live state, exact objects, authorization, next task.
2. `docs/workbuddy/v2/PROJECT-CHARTER.md` — product roles and six-module responsibilities.
3. `docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md` — accepted Stage 2 complete-toolchain Registration/Locator contract and temporary-proof boundary.
4. `docs/workbuddy/v2/ACCEPTANCE-MATRIX.md` — evidence meanings and gates.
5. `docs/workbuddy/v2/DRIFT-GUARD.md` — stop rules and Git lifecycle.
6. `docs/workbuddy/v2/MODULE-DISPOSITION.md` — historical V1 capability disposition.

Git history preserves retired plans, prompts, reports, and evidence; they are not active authority.
