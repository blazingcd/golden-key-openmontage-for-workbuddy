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
Once the requested business result actually exists and has received the minimum
validation needed for an honest claim, present that result and finish the current
reply. Do not delay user-visible delivery for optional workspace memory, Skill
creation or correction, or other reusable-workflow accumulation. This production
path is already covered by the installed Skill; a routine result is not a new
workflow to persist. Perform additional persistent wrap-up only when the user
explicitly requests it or when it is necessary to complete the requested result.
The fixed entry also records the complete receipt at the managed
`Results/golden-key-openmontage/latest-launcher-receipt.json` location. Use that
receipt as the checkable first-call result when the host does not display native
stdout. If the first call fails, read the managed
`Results/golden-key-openmontage/latest-launcher-failure.json` diagnostic when it
is present; never replay the user's request merely to recover transport output.

The fixed entry owns package lookup, release binding, validation, lifecycle
state, and receipt delivery. Do not ask the user or model for commands, JSON,
paths, hashes, environment names, evidence records, or internal controls. Do
not create another Agent, Skill, router, MCP surface, retry/replay path,
Provider choice, renderer choice, media workflow, consent decision, or recovery
decision. Those decisions remain outside this Shell adapter.

GOLDEN_KEY_WORKBUDDY_SKILL_IDENTITY=<installer:skill_identity>
GOLDEN_KEY_WORKBUDDY_RELEASE_IDENTITY=<installer:release_identity>
