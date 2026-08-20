# Golden Key WorkBuddy Shell V2

WorkBuddy Shell V2 connects Tencent WorkBuddy to a verified, versioned Golden Key OpenMontage Package. WorkBuddy is the only running Agent; after reading the verified Package Guide it assumes the OpenMontage production role. The Shell is limited to six modules: installation/lifecycle, Package Registration/Locator, runtime preparation, session Launcher, WorkBuddy entry, and status/result relay.

Current status:

- Stage 1: `PASS_ACCEPTED`
- Stage 2 Registration/Locator implementation: `PASS_ACCEPTED`
- Stage 2 real temporary-Package validation: `PASS_ACCEPTED`; retained final Release: `NOT_MATERIALIZED`; production Package Registration: `NOT_CREATED`
- Repository hygiene: `PASS_ACCEPTED`; the historical Wave C anchor `20ddab75825c1b6e7de5a51603afe8b6fd82eceb` had 33 files, and the current accepted Stage 3/4 tree tracks exactly 37 files
- Stage 3 planning and implementation: `PASS_ACCEPTED`
- Stage 4 planning and implementation: `PASS_ACCEPTED`
- Stage 5 WorkBuddy entry: `NOT_GRANTED`
- Stage 6 status/result relay: `NOT_GRANTED`
- Final Package materialization and production Registration: `NOT_MATERIALIZED / NOT_CREATED`

Live status, exact Git objects, and task authorization are recorded only in [`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md). The current maintenance only aligns entry documentation and CI action versions; it does not authorize Stage 5, Stage 6, or final Package work.

Stage 2 Registration/Locator, Stage 3 runtime preparation, and Stage 4 session Launcher implementations are accepted. Stage 2 also proved one real temporary Package containing Python, FFmpeg, and Node, but that temporary Package was deleted. This does not prove a retained final Release, installed production PackageRoot, production Registration, Installer, or final distribution. The Stage 2 boundary is in [`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md).

This repository must not run or direct video Pipelines, Providers, or media production. WorkBuddy performs those functions under the validated Package contract; there is no second OpenMontage Agent process.

The Golden Key delivery must bundle and register its complete package-private required toolchain: a usable Python 3.10+ environment with locked core dependencies, FFmpeg plus ffprobe, and Node.js plus npm/npx. Node must satisfy the highest Package requirement, currently 22+ because HyperFrames requires it; freezing only the general README minimum of 18+ is insufficient. The exact `gyan.dev` FFmpeg asset is a Package-assembly supply-chain candidate subject to source, hash, license, and distribution review—not a Stage 3 end-user download.

Stage 3 has one accepted public entry: `prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`. Its result set is exactly `DETECTION_REPORT / CONSENT_REQUIRED / INTEGRATED / SKIPPED / BLOCKED`. It performs bounded detection of optional Remotion and HyperFrames capabilities, produces zero-download plans for missing or incompatible items, and integrates only a capability explicitly approved by the user. It never chooses the renderer, discovers/downloads/replaces Python/FFmpeg/Node, scans drives, or runs video. Optional downloads require approved mainland-China mirrors without automatic overseas fallback.

Stage 4 has one accepted public entry: `launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`. It accepts only a release-specific immutable `PackageToolDefinitionV1` from the approved Package definition/final-delivery Installer owner, spawns exactly one fixed Package tool, and returns a recursively immutable `LauncherReceiptV1` limited to nine outcomes. It remains Provider- and runtime-opaque and never selects Remotion, HyperFrames, or another Provider/runtime.

Stage 5 remains the future end-user entry and is not implemented or authorized. It will revalidate the production Package through Stage 2 and pass the literal user request separately from technical controls; Stage 6 remains unimplemented and unapproved and may directly reuse the Stage 4 receipt if no real conversion gap exists. WorkBuddy owns pause, consent, and continuation, and Shell never auto-replays the original request. Real production WorkBuddy/Launcher sessions, Provider/media execution, Stage 5/6, and final Package materialization/production Registration remain unproven or `NOT_GRANTED`.

Historical evidence may describe superseded Stage 3 signatures, Package-bound capability models, or pre-implementation Stage 4 gates. Those records are historical only and do not override the current accepted interfaces and status above.
