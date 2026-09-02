---
name: golden-key-openmontage
description: Use whenever the user's message contains the exact phrase "金钥匙智能体" or directly asks to configure Remotion, including "请帮我配置 Remotion"; send that complete request through the installed Golden Key OpenMontage WorkBuddy entry.
---

# Golden Key OpenMontage WorkBuddy entry

WorkBuddy remains the sole Agent and the sole user conversation entry. Invoke
this Skill whenever the user's message contains the exact phrase
`金钥匙智能体` or directly asks to configure Remotion, and pass the complete
original message to the bundled entry.
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
the conversation. When LauncherReceipt reports `result_pointer.valid=true`, read
that exact managed handoff and consume its bounded `package_capability_summary`
first. Keep it in the managed Results location: do not copy or rewrite the
handoff or summary into the task workspace and do not create a relay file. Treat
an absent, invalid, failed, or `NOT_VERIFIED` summary honestly; do not invent a
ready state. For a broad first-use inventory request, the summary is the complete
display source: do not call `provider_menu()`, enumerate `setup_offers`, read a
visualization guide, or create a table, dashboard, SVG, or other artifact. Use
compact conversational prose. Read `provider_menu()` only after the user selects
a relevant configuration path and more detail is needed. Use `support_envelope()`
only for necessary diagnosis or detail, not as the default first-use display. Do
not dump raw registry data.

Tell the user that the basic production path remains available whenever FFmpeg
is reported ready. The visible first-use summary covers exactly five topics:
FFmpeg, Remotion, HyperFrames, external video generation, and TTS. Do not mention
or label other capability rows even when the summary contains them. Keep
installed, not installed, configurable, not configured, not verified,
connection failed, and connected states distinct. A static declaration or
adapter does not prove credentials, account permission, balance, connectivity,
regional availability, price, or current model availability. Missing optional
capability must not block the FFmpeg path or be described as OpenMontage lacking
production capability.

Keep source integration, project dependency installation, runtime readiness, and
real invocation verification as four separate facts. Give Remotion and
HyperFrames separate compact explanations; for each one, state those four layers
without merging the two engines. `composition_runtimes` governs runtime wording
over any generic tool or Provider rollup. State Remotion source integration only
when verified Package facts support it, and state HyperFrames source integration
as not verified unless equally direct facts support it.

FFmpeg runtime readiness establishes the usable basic path. An optional
capability may be called ready only when verified facts show its necessary
dependencies present, runtime true, and a real Package-mediated invocation
verified. If any layer is absent or unknown, state that layer honestly and do not
use “ready” for the capability. `configured < total`, adapter presence, or an
available Provider name can never make a whole group ready.

Unconfigured enhancements are available configuration choices, not things
OpenMontage "cannot do". Do not summarize them as product incapability, "only
material processing", or an equivalent limitation. Say instead that they are
not configured or not yet verified and can be enabled when relevant, while the
FFmpeg path remains available now. External video and TTS with declared choices
but zero configured entries are configurable, not configured, and not connection-
tested. Before the user selects API-key configuration, do not name Providers or
show setup offers; Provider details wait for that selected path and then remain
limited to relevant verified Package declarations. Do not expose environment
variable names, internal Provider identifiers, paths, commands, URLs, hashes,
schemas, or installation instructions in the first-use reply.

Always make four separate semantic choices visible: continue with the FFmpeg
path, configure a selected local capability, configure a selected API-key
Provider, or handle configuration later. WorkBuddy owns relevance,
Provider/model choice, cost and privacy
explanation, consent, and recovery; wording may vary, and a bounded confirmation
step is allowed when needed for safe or reliable completion. Treat later messages
containing `金钥匙智能体` that ask to inspect, configure, change, or retest
capabilities as ordinary intent, not a fixed command language. In this readiness
step, do not install anything, request or save a secret in ordinary chat, call a
Provider, test a connection, validate a selected configuration, or retest it.

## Confirmed configuration action

After WorkBuddy has selected the relevant Package-declared option, explained
cost and privacy, and obtained explicit consent, invoke this same Skill entry a
second time with one private canonical configuration action instead of ordinary
chat. Never display that action or ask the user to supply its fields. Bind
`package_release`, `package_commit`, and `package_definition_sha256` to the exact
verified handoff facts. The action is compact UTF-8 JSON with alphabetically
sorted keys, no whitespace, and exactly these fields:
`action`, `capability`, `capability_definitions`, `consent`, `package_commit`,
`package_definition_sha256`, `package_release`, `provider`, `schema_version`, and
`user_decisions`. Its schema is
`golden-key-workbuddy-configuration-action-v1`. It never contains a credential.

For a local Remotion choice, detect first, then explain that Windows resolves
the standard location for the selected scope, `registry.npmmirror.com` is the
approved npm source, the applicable license applies, npm dependency size may be
unknown, and the plan gives the exact browser archive size and mainland mirror.
Ask for explicit consent for each selected capability and reconfirm immediately
before any real download or installation. System scope is the default; mention
current-user scope only as an explicit user-selected alternative and never
hard-code a drive letter. After installation, rediscover and verify the managed
runtime. HyperFrames is not implemented in this route.
Only when OpenMontage decides to use Remotion may WorkBuddy pass the non-null
managed runtime object unchanged to `video_compose` as
`managed_remotion_runtime`; if it is absent, Remotion is not ready.

For local composition readiness, use
`action=prepare_optional_capabilities`, `capability=composition_runtime`, and
`provider=null`. Pass the exact closed Package-declared definition sequence only when it is
already present in verified Package facts; never invent URLs, hashes, sizes, or
versions. Use `consent=inspect` with `user_decisions=null` for detection and plan
creation. After the user confirms, use `consent=confirmed` with only the exact
plan-bound approve, decline, or defer decisions returned by the prior result.
The entry reuses the existing bounded optional-capability preparation contract.
Decline, defer, cancellation, or failure leaves the FFmpeg path available and
must not trigger retry, substitution, or installation outside that contract.

For an API-key path, select only a Provider present in the verified Package
declaration. The current declaration permits `provider=seedance_ark`,
`capability=video_generation`, `consent=confirmed`, and either
`action=configure_provider` or `action=retest_provider`; both optional list
fields are null. Configure opens the native masked Windows credential prompt
and stores the secret for the current Windows user. Retest reads that stored
credential. The Package then performs its single declared read-only non-media
connection check. Never put the secret in chat, JSON, arguments, output,
receipts, handoffs, logs, or error text. Report success only as the exact check
proved by `configuration_result`; it does not prove balance, generation access,
model availability, price, output quality, or a usable media result. A later
ordinary-language request to change the Provider follows the same selection,
explanation, consent, and private-action flow.

The fixed entry owns package lookup, release binding, validation, lifecycle
state, and receipt delivery. Do not ask the user or model for commands, JSON,
paths, hashes, environment names, evidence records, or internal controls. Do
not create another Agent, Skill, router, MCP surface, retry/replay path,
Provider choice, renderer choice, media workflow, consent decision, or recovery
decision. Those decisions remain outside this Shell adapter.

GOLDEN_KEY_WORKBUDDY_SKILL_IDENTITY=<installer:skill_identity>
GOLDEN_KEY_WORKBUDDY_RELEASE_IDENTITY=<installer:release_identity>
