---
name: golden-key-openmontage
description: Use whenever the user's literal message contains the exact phrase "金钥匙智能体"; send that complete request through the installed Golden Key OpenMontage WorkBuddy entry.
---

# Golden Key OpenMontage WorkBuddy entry

WorkBuddy remains the sole Agent and the sole user conversation entry. Invoke
this Skill whenever the user's message contains the exact phrase
`金钥匙智能体`, and pass the complete original message to the bundled entry.
Do not remove the wake phrase or reinterpret a user-provided material path as
an internal Shell path. Allow the foreground PowerShell call up to `300000`
milliseconds so cold Package validation can finish.

WorkBuddy decides its own reasoning, tools, questions, retries, and business
steps; this Skill does not prescribe an internal script or expected wording.
Treat the LauncherReceipt as mechanical facts. When it provides a verified
PackageRoot, the Package Guide is the production-semantic authority. Present
the actual business result naturally, do not require the user to operate Shell
mechanics, and do not claim an Artifact or video exists unless it actually does.

The fixed entry owns package lookup, release binding, validation, lifecycle
state, and receipt delivery. Do not ask the user or model for commands, JSON,
paths, hashes, environment names, evidence records, or internal controls. Do
not create another Agent, Skill, router, MCP surface, retry/replay path,
Provider choice, renderer choice, media workflow, consent decision, or recovery
decision. Those decisions remain outside this Shell adapter.

GOLDEN_KEY_WORKBUDDY_SKILL_IDENTITY=<installer:skill_identity>
GOLDEN_KEY_WORKBUDDY_RELEASE_IDENTITY=<installer:release_identity>
