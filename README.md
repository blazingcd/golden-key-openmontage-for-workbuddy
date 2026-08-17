# Golden Key WorkBuddy Shell V2

WorkBuddy Shell V2 connects Tencent WorkBuddy to a verified, versioned Golden Key OpenMontage Package. WorkBuddy is the only running Agent; after reading the verified Package Guide it assumes the OpenMontage production role. The Shell is limited to six modules: installation/lifecycle, Package Registration/Locator, runtime preparation, session Launcher, WorkBuddy entry, and status/result relay.

Current status:

- Stage 1: `PASS_ACCEPTED`
- Stage 2: `REOPENED_PACKAGE_REFRESH_REQUIRED` (previous Package: `PASS_ACCEPTED_HISTORICAL`)
- Repository hygiene: `PASS_ACCEPTED` at `20ddab75825c1b6e7de5a51603afe8b6fd82eceb`, exact 33-file tree
- Stage 3 planning: `RUNTIME_SCOPE_CORRECTED_FOR_REVIEW`
- Stage 3 implementation: `NOT_GRANTED`
- Stage 4 Launcher: `NOT_GRANTED`
- Stage 5 WorkBuddy entry: `NOT_GRANTED`
- Stage 6 status/result relay: `NOT_GRANTED`
- Stage 2/3 runtime correction docs: `REVIEW_READY`

The current task reconciles the reopened Stage 2 prerequisites, corrected Stage 3 runtime scope, and WorkBuddy-only Agent model across existing authorities; it is not implementation authorization. Live status and exact Git objects are recorded only in [`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md).

The only production implementation is Registration and Locator for the previous Package. It remains historical accepted evidence, not current-Package acceptance. The refresh adjudication is in [`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md).

This repository must not run or direct video Pipelines, Providers, or media production. WorkBuddy performs those functions under the validated Package contract; there is no second OpenMontage Agent process.

The Golden Key delivery must bundle a Manifest/Lock-pinned private Python so ordinary users do not need system Python. Stage 3 discovers and prepares only the closed runtime set: private Python dependencies, FFmpeg, Node, Remotion, HyperFrames, and the locked browser they require. Discovery is limited to managed paths, explicitly registered host tools, and normal PATH command resolution; it never scans drives. Missing components require an identity-locked missing-only plan, explicit user consent, and approved mainland-China mirrors, with no default Git/GitHub, Google, npmjs, or PyPI fallback.

Stage 4 binds the verified Package and Runtime to one WorkBuddy-owned session; it does not launch a second Agent. Stage 5 exposes one explicit WorkBuddy entry, and Stage 6 reuses the Launcher receipt unless a proven format gap requires one deterministic conversion.
