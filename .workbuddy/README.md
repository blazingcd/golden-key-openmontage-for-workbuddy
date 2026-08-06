# WorkBuddy project configuration

This directory is a consumer-owned placeholder for the WorkBuddy integration.

- The current path is **Skill-first**: import `workbuddy-skill/golden-key-openmontage-onboarding` for the optional new-user conversation and `workbuddy-skill/golden-key-openmontage` for production. WorkBuddy remains the only Agent.
- Onboarding is an independent WorkBuddy consumer development task, not a Golden Key Core stage. The release registers it beside the production Skill because users need it after installation; this does not move its product logic into the installer. It can explain how to attach relevant local source/reference materials or begin without them, but it does not inventory a SaaS material library. It stops as soon as the user gives a concrete production request, then hands off to the production Skill.
- No active repository-level `mcp.json` is shipped before W4 packaging. The W2 real WorkBuddy comparison passed and fixed MCP as **optional**: the direct CLI remains the canonical fallback, while local stdio MCP adds structured Schema discovery and avoids shell command construction.
- W4 uses a portable ZIP plus a PowerShell registration script, not Setup.exe/MSI. The archive may be extracted anywhere; registration writes `WORKBUDDY-RUNTIME.json` beside each installed Skill so WorkBuddy can find the stable launcher and actual data root.
- WorkBuddy owns the conversation-model configuration. Golden Key production Provider references are generated under the registered `<data_root>/Config`; this directory never stores credential values.
- Direct CLI long tasks use `golden-key-workbuddy task submit/status/run/cancel/recover` and persist under the registered `<data_root>/Jobs`. Queued tasks can be cancelled; running blocking Tools are explicitly not claimed cancelable, and interrupted tasks are failed without automatic retry.
- `doctor` scans Core/Pipeline identity, Python packages, Node and FFmpeg; `config inspect` scans safe Provider references. Both are local/read-only and attempt zero Provider or network calls.
- v0.3.21 is included only as the first package-build validation baseline while Core undergoes a major revision; it is not the final Core release.

Current status is Pre-Alpha. This directory is not evidence that installation or real WorkBuddy acceptance has passed.
