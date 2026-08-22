# Golden Key WorkBuddy Shell V2

WorkBuddy Shell V2 connects Tencent WorkBuddy to a verified, versioned Golden Key OpenMontage Package. WorkBuddy is the only running Agent; after reading the verified Package Guide it assumes the OpenMontage production role. The Shell is limited to six modules: installation/lifecycle, Package Registration/Locator, runtime preparation, session Launcher, WorkBuddy entry, and status/result relay.

Current status:

- Stage 1: `PASS_ACCEPTED`
- Stage 2 Registration/Locator implementation: `PASS_ACCEPTED`
- Stage 2 real temporary-Package validation: `PASS_ACCEPTED`; retained final Release: `NOT_MATERIALIZED`; production Package Registration: `NOT_CREATED`
- Repository hygiene: `PASS_ACCEPTED`; the historical Wave C anchor `20ddab75825c1b6e7de5a51603afe8b6fd82eceb` had 33 files, and the current accepted tree tracks exactly 40 files
- Stage 3 planning and implementation: `PASS_ACCEPTED`
- Stage 4 planning and implementation: `PASS_ACCEPTED`
- Stage 5: `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`
- Stage 6 status/result relay: `NOT_GRANTED`
- Final Package/PackageRoot/production Registration/Activation/final installed Skill: `NOT_MATERIALIZED / NOT_CREATED`
- Real WorkBuddy `LauncherReceiptV1`: `NOT_PROVED`

Live status, exact Git objects, and task authorization are recorded only in [`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md). The original R01, Sandbox Refresh1, and Expert Entry Feasibility records remain `HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT`. R01 entry-surface acceptance is preserved, and HY3 remains current-test-only/cost-avoidance and product-model-neutral, while R02 is closed as `BLOCKED_PACKAGE_RELEASE`: the published `blazingcd/golden-key-openmontage` candidate identity matches, but no safe fixed tool or release-specific `PackageToolDefinitionV1`/Manifest/Lock binding is present. No next task is authorized; R03-R08 remain blocked by chain. Stage 5 is still incomplete, and no client, Package, registration, or `LauncherReceiptV1` proof is claimed.

Stage 2 Registration/Locator, Stage 3 runtime preparation, and Stage 4 session Launcher implementations are accepted. Stage 2 also proved one real temporary Package containing Python, FFmpeg, and Node, but that temporary Package was deleted. This does not prove a retained final Release, installed production PackageRoot, production Registration, Installer, or final distribution. The Stage 2 boundary is in [`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md).

This repository must not run or direct video Pipelines, Providers, or media production. WorkBuddy performs those functions under the validated Package contract; there is no second OpenMontage Agent process.

The Golden Key delivery must bundle and register its complete package-private required toolchain: a usable Python 3.10+ environment with locked core dependencies, FFmpeg plus ffprobe, and Node.js plus npm/npx. Node must satisfy the highest Package requirement, currently 22+ because HyperFrames requires it; freezing only the general README minimum of 18+ is insufficient. The exact `gyan.dev` FFmpeg asset is a Package-assembly supply-chain candidate subject to source, hash, license, and distribution review—not a Stage 3 end-user download.

Stage 3 has one accepted public entry: `prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`. Its result set is exactly `DETECTION_REPORT / CONSENT_REQUIRED / INTEGRATED / SKIPPED / BLOCKED`. It performs bounded detection of optional Remotion and HyperFrames capabilities, produces zero-download plans for missing or incompatible items, and integrates only a capability explicitly approved by the user. It never chooses the renderer, discovers/downloads/replaces Python/FFmpeg/Node, scans drives, or runs video. Optional downloads require approved mainland-China mirrors without automatic overseas fallback.

Stage 4 has one accepted public entry: `launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`. It accepts only a release-specific immutable `PackageToolDefinitionV1` from the approved Package definition/final-delivery Installer owner, spawns exactly one fixed Package tool, and returns a recursively immutable `LauncherReceiptV1` limited to nine outcomes. It remains Provider- and runtime-opaque and never selects Remotion, HyperFrames, or another Provider/runtime.

Stage 5 is not complete: the entry code is delivered, but real integration is incomplete. Completion requires all five evidence classes: a retained final Release/PackageRoot; production Registration+Activation with new-process Locator; one final Installer-stamped Skill with no placeholders; a HY3 real WorkBuddy session yielding a real `LauncherReceiptV1`; and independent review/formal Git/CI plus unambiguous live authority. Provider calls, media/video generation, optional Remotion/HyperFrames installation, Stage 6 conversion code, and full business E2E are not Stage 5 completion prerequisites. After Stage 5, Stage 6 should first attempt direct receipt reuse; the whole-project business E2E remains a separate post-Stage5 effort, not a Stage 7.

Historical evidence may describe superseded Stage 3 signatures, Package-bound capability models, or pre-implementation Stage 4 gates. Those records are historical only and do not override the current accepted interfaces and status above.
