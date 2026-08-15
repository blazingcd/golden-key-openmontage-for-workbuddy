# Golden Key WorkBuddy Shell V2

WorkBuddy Shell V2 connects WorkBuddy to a verified, versioned external OpenMontage Package. WorkBuddy owns the conversation, the OpenMontage Agent owns production, and the Shell is limited to six modules: installation/lifecycle, Package Registration/Locator, runtime preparation, session Launcher, WorkBuddy entry, and status/result relay.

Current status:

- Stage 1: `PASS_ACCEPTED`
- Stage 2: `PASS_ACCEPTED`
- Stage 3 planning: `GRANTED`
- Stage 3 implementation: `NOT_GRANTED`

The current repository-hygiene work is not Stage 3 implementation. The live status and exact Git objects are recorded only in [`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md).

The only current production implementation is Package Registration and Locator. Its stable contract is [`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md); its implementation evidence is `tests/workbuddy/test_package_registration.py`.

This repository must not run or direct video Pipelines, Providers, or media production. Those capabilities belong to the OpenMontage Agent in a validated external Package.
