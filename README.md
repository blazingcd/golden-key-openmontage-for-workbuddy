# Golden Key WorkBuddy Shell V2

WorkBuddy Shell V2 connects Tencent WorkBuddy to a verified, versioned Golden Key OpenMontage Package. WorkBuddy is the only running Agent; after reading the verified Package Guide it assumes the OpenMontage production role. The Shell is limited to six modules: installation/lifecycle, Package Registration/Locator, runtime preparation, session Launcher, WorkBuddy entry, and status/result relay.

Current status:

- Stage 1: `PASS_ACCEPTED`
- Stage 2: `REOPENED_REQUIRED_TOOLCHAIN_PACKAGE_REFRESH` (previous Python-only Package: `PASS_ACCEPTED_HISTORICAL`)
- Repository hygiene: `PASS_ACCEPTED` at `20ddab75825c1b6e7de5a51603afe8b6fd82eceb`, exact 33-file tree
- Stage 3 planning: `REOPENED_OPTIONAL_CAPABILITY_RECLASSIFICATION_REQUIRED`
- Stage 3 implementation: `NOT_GRANTED`
- Stage 4 Launcher: `NOT_GRANTED`
- Stage 5 WorkBuddy entry: `NOT_GRANTED`
- Stage 6 status/result relay: `NOT_GRANTED`
- Required-toolchain correction docs: `REVIEW_READY`

The current task reconciles the reopened Stage 2 prerequisites, corrected Stage 3 runtime scope, and WorkBuddy-only Agent model across existing authorities; it is not implementation authorization. Live status and exact Git objects are recorded only in [`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md).

The only production implementation is Registration and Locator for the previous Package. It remains historical accepted evidence, not current-Package acceptance. The refresh adjudication is in [`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md).

This repository must not run or direct video Pipelines, Providers, or media production. WorkBuddy performs those functions under the validated Package contract; there is no second OpenMontage Agent process.

The Golden Key delivery must bundle and register its complete package-private required toolchain: a usable Python 3.10+ environment with locked core dependencies, FFmpeg plus ffprobe, and Node.js plus npm/npx. Node must satisfy the highest Package requirement, currently 22+ because HyperFrames requires it; freezing only the general README minimum of 18+ is insufficient. The earlier Python-only Stage 2 result is historical evidence, not acceptance for this delivery. The exact `gyan.dev` FFmpeg asset is now a Package-assembly supply-chain candidate subject to source, hash, license, and distribution review—not a Stage 3 end-user download.

Stage 3 owns only one optional capability already selected and locked by WorkBuddy/OpenMontage: Remotion or HyperFrames, plus only the assets explicitly declared by that capability's lock. It never chooses the renderer, installs both renderers speculatively, or discovers/downloads/replaces Python, FFmpeg, or Node. Optional end-user downloads require an exact missing-only plan, explicit consent, and approved mainland-China mirrors without automatic overseas fallback. The precise Stage 3-to-Stage 4 pause/continue contract must be derived from the real WorkBuddy consumer rather than guessed by the Shell.

The previous Stage 3 task packet, public-entry signature, and all-component Runtime Lock are `SUPERSEDED`; its conditional authorization is suspended. Stage 3 remains `NOT_GRANTED` until Stage 2 registers the complete required toolchain and the real WorkBuddy/OpenMontage optional-capability input contract is frozen into a new exact task packet.
