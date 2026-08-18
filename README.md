# Golden Key WorkBuddy Shell V2

WorkBuddy Shell V2 connects Tencent WorkBuddy to a verified, versioned Golden Key OpenMontage Package. WorkBuddy is the only running Agent; after reading the verified Package Guide it assumes the OpenMontage production role. The Shell is limited to six modules: installation/lifecycle, Package Registration/Locator, runtime preparation, session Launcher, WorkBuddy entry, and status/result relay.

Current status:

- Stage 1: `PASS_ACCEPTED`
- Stage 2 Registration/Locator implementation: `PASS_ACCEPTED`
- Stage 2 real temporary-Package validation: `PASS_ACCEPTED`; retained final Release: `NOT_MATERIALIZED`; production Package Registration: `NOT_CREATED`
- Repository hygiene: `PASS_ACCEPTED` at `20ddab75825c1b6e7de5a51603afe8b6fd82eceb`, exact 33-file tree
- Stage 3 planning: `PASS_ACCEPTED`
- Stage 3 implementation: `NOT_GRANTED`
- Stage 4 Launcher: `NOT_GRANTED`
- Stage 5 WorkBuddy entry: `NOT_GRANTED`
- Stage 6 status/result relay: `NOT_GRANTED`
- Stage 3 pre-takeover plan docs: `PASS_ACCEPTED` after independent review and formal fast-forward

The current task freezes the narrowed Stage 3 pre-takeover plan across existing authorities; it is not implementation authorization. Live status and exact Git objects are recorded only in [`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md).

The only production implementation is Stage 2 Registration and Locator. It and one real temporary Package containing Python, FFmpeg, and Node have been accepted, but that temporary Package was deleted. This does not prove a retained final Release, installed production PackageRoot, production Registration, Installer, or final distribution. The contract boundary is in [`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md).

This repository must not run or direct video Pipelines, Providers, or media production. WorkBuddy performs those functions under the validated Package contract; there is no second OpenMontage Agent process.

The Golden Key delivery must bundle and register its complete package-private required toolchain: a usable Python 3.10+ environment with locked core dependencies, FFmpeg plus ffprobe, and Node.js plus npm/npx. Node must satisfy the highest Package requirement, currently 22+ because HyperFrames requires it; freezing only the general README minimum of 18+ is insufficient. The exact `gyan.dev` FFmpeg asset is a Package-assembly supply-chain candidate subject to source, hash, license, and distribution review—not a Stage 3 end-user download.

Stage 3 owns only one optional capability already selected and locked by WorkBuddy/OpenMontage: no optional capability, Remotion, or HyperFrames, plus only the assets explicitly declared by the Package-owned capability Lock. Its proposed sole entry is `prepare_optional_capability(data_root, capability_request, authorization_receipt=None)`; the maximum future code surface is one new module, one export-only edit, and one direct test file. It never chooses the renderer, installs both renderers speculatively, discovers/downloads/replaces Python/FFmpeg/Node, scans drives, or runs video. Optional downloads require an exact missing-only plan, explicit consent, and approved mainland-China mirrors without automatic overseas fallback.

Stage 5 is the end-user entry. It revalidates the production Package through Stage 2; Stage 4 may use the bundled required toolchain for a base fixed-tool call, while optional Remotion/HyperFrames execution additionally requires a Stage 3 receipt bound to the same Registration and capability Lock. WorkBuddy owns pause, consent, and continuation; Stage 6 only relays facts, and Shell never auto-replays the original request.

The previous Stage 3 task packet, public-entry signature, and Shell-owned all-component Runtime Lock are `SUPERSEDED`. Stage 3 remains `NOT_GRANTED` until the final Release is retained, installed and production-registered, Locator succeeds in a new process, Package-owned capability Locks and the real WorkBuddy pause/consent/continue contract are frozen, and an exact Builder packet is explicitly granted.
