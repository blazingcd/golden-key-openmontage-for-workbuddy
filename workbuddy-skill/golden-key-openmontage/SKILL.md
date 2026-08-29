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

## First-use capability readiness

After the fixed entry returns a verified PackageRoot and verified Package Guide
identity, establish capability readiness before the first production decision in
the conversation. Use WorkBuddy's current tools and that verified Guide to
discover the Package registry, then read `provider_menu_summary()` first. Read
`provider_menu()` only for a relevant item when the compact summary or the user's
choice needs more detail. Use `support_envelope()` only for necessary diagnosis
or detail, not as the default first-use display. Do not dump raw registry data.

Tell the user that the basic production path remains available whenever FFmpeg
is reported ready. Show only optional capabilities and Providers declared by the
verified Package, and keep installed, not installed, configurable, not
configured, not verified, connection failed, and connected states distinct. A
static declaration or adapter does not prove credentials, account permission,
balance, connectivity, regional availability, price, or current model
availability. Missing optional capability must not block the FFmpeg path or be
described as OpenMontage lacking production capability.

Offer natural-language choices to continue with the FFmpeg path, configure a
selected local capability, configure a selected API-key Provider, or handle it
later. WorkBuddy owns relevance, Provider/model choice, cost and privacy
explanation, consent, and recovery; wording may vary, and a bounded confirmation
step is allowed when needed for safe or reliable completion. Treat later messages
containing `金钥匙智能体` that ask to inspect, configure, change, or retest
capabilities as ordinary intent, not a fixed command language. In this readiness
step, do not install anything, request or save a secret in ordinary chat, call a
Provider, test a connection, validate a selected configuration, or retest it;
the user's selection is only a handoff to the separately authorized
configuration path.

The fixed entry owns package lookup, release binding, validation, lifecycle
state, and receipt delivery. Do not ask the user or model for commands, JSON,
paths, hashes, environment names, evidence records, or internal controls. Do
not create another Agent, Skill, router, MCP surface, retry/replay path,
Provider choice, renderer choice, media workflow, consent decision, or recovery
decision. Those decisions remain outside this Shell adapter.

GOLDEN_KEY_WORKBUDDY_SKILL_IDENTITY=<installer:skill_identity>
GOLDEN_KEY_WORKBUDDY_RELEASE_IDENTITY=<installer:release_identity>
