# Golden Key WorkBuddy Shell V2

WorkBuddy Shell V2 connects WorkBuddy to a verified, versioned external OpenMontage Package. WorkBuddy owns the conversation, the OpenMontage Agent owns production, and the Shell is limited to six modules: installation/lifecycle, Package Registration/Locator, runtime preparation, session Launcher, WorkBuddy entry, and status/result relay.

Current status:

- Stage 1: `PASS_ACCEPTED`
- Stage 2: `PASS_ACCEPTED`
- Repository hygiene: `PASS_ACCEPTED` at `20ddab75825c1b6e7de5a51603afe8b6fd82eceb`, exact 33-file tree
- Stage 3 planning: `GRANTED`
- Stage 3 implementation: `NOT_GRANTED`
- Stage 4 Launcher: `NOT_GRANTED`
- Stage 5 WorkBuddy entry: `NOT_GRANTED`
- Stage 6 status/result relay: `NOT_GRANTED`
- Reduced Stage 3-6 scope: `REVIEW_READY`

The current task only reconciles the reduced Stage 3-6 scope across existing authorities; it is not implementation authorization. Live status and exact Git objects are recorded only in [`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md).

The only current production implementation is Package Registration and Locator. Its stable contract is [`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md); its implementation evidence is `tests/workbuddy/test_package_registration.py`.

This repository must not run or direct video Pipelines, Providers, or media production. Those capabilities belong to the OpenMontage Agent in a validated external Package.

For Stages 3-6, no verified input or direct consumer means no production code. Stage 3 may close with no additional Runtime, Stage 4 launches one controlled Agent process once, Stage 5 exposes one explicit WorkBuddy entry, and Stage 6 reuses the Launcher receipt unless a proven format gap requires one deterministic conversion.
