# WorkBuddy Shell V2 — Project Charter

## Purpose

Make Golden Key OpenMontage usable by an ordinary user through one natural-language
WorkBuddy conversation. The user should only need to describe the business need
and provide optional business materials. The internal execution method belongs to
WorkBuddy and the verified Package, not to the user.

## Ownership

- **WorkBuddy:** the only Agent, conversation owner, and production decision-maker.
  It reads the verified OpenMontage Package Guide and follows its production
  semantics, asks business questions, chooses tools and steps, and presents results.
- **OpenMontage Package:** source of production meaning: Guide, Manifest, Pipeline,
  Stage, Artifact, Checkpoint, Reviewer, Tool, and Provider contracts.
- **Shell V2:** installation/lifecycle, Package Registration/Locator, runtime
  preparation, fixed mechanical invocation, WorkBuddy entry, and status/receipt
  relay.

Shell is not a second Agent or control plane. It does not decide creative content,
Pipeline/Stage order, Provider, renderer, recovery, or business acceptance. Do not
add an MCP, router, workflow engine, media framework, or second conversation path.

## User path

The only wake condition is that the original user message contains the literal
`金钥匙智能体`. Any additional natural-language business description, questions,
constraints, or material paths remain user input. Do not require a fixed complete
prompt. Do not require the user to see or operate path/hash/schema/env/argv/pipe
or command mechanics.

WorkBuddy is a harness Agent. The same input may lead to different internal
reasoning, tools, steps, wording, and intermediate conclusions. Do not make an
evaluator-invented transcript the product contract. A bounded fixed sequence is
acceptable when actual WorkBuddy behavior, consent, secure secret entry, or
reliable installation requires it. The user must still begin from ordinary natural
language and must not operate internal technical mechanics.

For future WorkBuddy runs, use an available `0.00x` model row first. Waiting may
switch among available `0.00x` rows. Use a positive multiplier only when every
`0.00x` row is unavailable, choosing the smallest multiplier first and recording
the reason. Model switching does not authorize replay or a second task.

The external OpenMontage `AGENT_GUIDE.md` is read by WorkBuddy only after
Registration/Locator has returned and verified the PackageRoot and Guide identity.

## Capability readiness

FFmpeg is the minimum production baseline. An ordinary user with an FFmpeg-ready
installation can continue to basic production even when optional enhancements are
not installed or configured.

On first use, verified current facts reach WorkBuddy after PackageRoot
verification. It tells the user that the FFmpeg basic path can work now and
explicitly introduces Remotion, HyperFrames, external AI image/video, and TTS as
optional capabilities that may be configured. Extra catalogue or technical detail
is a UX issue unless it prevents understanding or safe continuation. WorkBuddy
owns the conversation, relevance, later Provider/model
choice, cost/privacy explanation, credentials, consent, connection testing, and
recovery. Shell runtime preparation may only detect and apply an exactly approved
mechanical plan.

Integration is not readiness. A capability may have Package source, an adapter,
and a dependency lock while its local dependencies are absent; it is then
"integrated, not ready", not "ready" and not an OpenMontage incapability. “Ready”
requires necessary dependencies, a true runtime state, and real Package invocation
evidence; partial counts, adapter presence, and available Provider names are not
enough. First-use guidance explicitly names Remotion and HyperFrames as optional
local enhancements the user may choose to configure. Each still keeps source
integration, project dependencies, runtime readiness, and real invocation separate in
the internal truth model. First-use guidance compresses those layers into an
ordinary status such as “本机动画增强尚未配置完成”. It should normally expand
technical detail only after the user asks or chooses that path; earlier technical
detail is a UX finding unless it prevents safe continuation. WorkBuddy does not expose raw
environment names, paths, commands, URLs, or installation instructions in
first-use guidance.

Later natural-language requests containing `金钥匙智能体` may inspect, configure,
change, or retest capabilities. This is an open intent, not a fixed configuration
language or second control plane.

The verified Package's formal declarations determine which Providers M1 may show.
Undeclared Providers do not appear in M1, and Provider names/details wait until
they are relevant to a selected configuration path rather than becoming the
first-use inventory. WorkBuddy should normally lead with a short recommended set
suited to the confirmed goal—two or three image/video-generation choices or one
or two TTS choices—and offer more choices. This is a progressive-disclosure
default, not a hard acceptance count; additional relevant declared choices do not
prevent the user from continuing configuration. Current static evidence
includes Seedance, Kling, and MiniMax;
the actual recommendation must come from current verified facts and user context,
not a Shell ranking table. WorkBuddy explains user value before technical
Provider details, while Shell remains Provider-opaque. Static adapter presence
never proves live account or model availability.

Natural language starts and controls both configuration mechanisms. A local
capability is complete only after approved download, managed installation,
rediscovery, Package recognition, and actual invocation. An API-key Provider is
complete only after secure input outside ordinary chat, safe local storage, exact
allowlisting, non-disclosing relay, and an authorized connection test.

Optional local capability distribution follows measured product constraints.
The Owner's 80 MiB compressed-increment ceiling rejects direct base-Package
Remotion bundling: measured external Remotion core/CLI is already 66.64 MiB as a
level-9 ZIP and the required locked Headless Shell archive is 115.33 MiB alone.
This does not remove Remotion from M1; it selects the managed, consent-controlled
on-demand installation route. A machine-level external Remotion command is not
Package readiness until the locked project dependencies, browser, Package
recognition, and actual invocation are proved.

The corresponding base-package slimming is complete as one independently
reviewed, unregistered, and unactivated successor candidate. It removes only
unused FFmpeg player/documentation payload and leaves the current active package
and rollback material unchanged. Its historical final-readiness promotion route
was executed and superseded. The current documentation-only reset authorizes no
candidate promotion, activation, installation, or WorkBuddy action; any future
use requires a new Owner-approved implementation gate. Slimming itself is not
capability or user-result acceptance.

## Four product results

1. **Installable Shell product — COMPLETE.** The final PackageRoot/binding,
   private runtime, Installer lifecycle, and data protection are represented by
   the accepted commit/release facts in the Task Register.
2. **WorkBuddy natural-language result — COMPLETE.** A real WorkBuddy 5.3.14 /
   Hy3 run invoked the single Skill and Shell from the ordinary request
   `用金钥匙智能体给我做新店开业视频` and returned a concrete business reply plus
   a checkable LauncherReceipt. No video file was required for this result.
3. **Real playable Golden Key video — COMPLETE.** WorkBuddy 5.3.14 with
   `Hy3 0.00x` produced and played a real 46.6-second MP4 through the ordinary-user
   path; the independent review passed with no findings.
4. **Formal closeout — COMPLETE.** R3 already contains ordinary-user product
   acceptance. The frozen R4 candidate passed its one independent zero-write
   review and was ordinarily fast-forwarded and pushed. R4 records the final
   repository/project state and does not run WorkBuddy or produce another video.

## Acceptance philosophy

Judge each result by what an ordinary user can accomplish and observe. WorkBuddy
may read the Guide, ask questions, call tools, retry, and adjust internal steps.
Its internal methods are not a failure. A failure is a missing required user-visible
result, technical burden on the ordinary user, a second control plane, or a false
result.

Each result gets one executor and one independent review after a real user-visible
result. Do not add packet/pre-review loops or technical gates that are not required
by that result.

## Out of scope

The R3-passing Skill remains the rollback baseline. Separately named candidates
may retain the proven v3 receipt relay while narrowly correcting the
WorkBuddy-facing result-delivery boundary. This does not authorize optional
frameworks, a fixed production script, a second Agent, two simultaneously
installed Golden Key Skills, or generalized orchestration. The v4 comparison did
not close that stability work: it delivered a real result but still wrote optional
workspace memory before the final answer. The Owner nevertheless retains v4 for
its improved first-call and delivery mechanics; the preserved R3 baseline remains
rollback evidence. Historical R3 remains complete.

The next-phase capability-onboarding plan is separate from the completed R1-R4
baseline. Its earlier recording authorized no execution. The current M1.2 gate is
the documentation-only product-flow reset stated below and in the Task Register;
implementation, Provider configuration, WorkBuddy, and media production remain
outside it.

Its M0 contract is the Task Register's bounded master roadmap. `R1` through `R4`
remain frozen historical result identifiers; future work uses M1–M3 for Must,
S1–S5 for Should, and C1–C2 for Could. M1 capability readiness requires a
read-only route audit before any exact write allowlist is proposed, then a separate
Owner decision on the implementation branch name and scope. M2 clarification and
material readiness, M3 production/quality/delivery, S1–S5 maturity work, and
C1–C2 deferred expansion must not be absorbed into M1.

M2 may begin after M1.2 first-use readiness. M1.3 is nevertheless a required M1
product capability with one representative local-install path and one
representative API-key path; only its use by a particular user is conditional.
M3 requires completed M1.4 and M2.

M1.2 owns the first-use readiness projection, ordinary-language explanation, and
next-intent handoff. It does not own a Provider catalogue or technical readiness
report. M1.3 owns the selected local or API-key configuration, short recommended
Provider menu, consent, secure handling, validation, failure recovery, and later
retest. Planned wording and steps may change after real WorkBuddy evidence;
acceptance follows the completed user goal and safety boundaries rather than exact
rehearsal of the planning examples.

M1.3 is one product journey with two mechanisms, not two new task series. Its
first implementation gate must prove a private structured action carrier from
WorkBuddy and a secure non-chat credential-entry route. Shell may validate and
execute an approved action but may not parse prose, explain value, rank Providers,
or silently substitute. The local representative reuses the existing bounded
Remotion/HyperFrames preparation and proves managed installation through actual
Package invocation. The API representative uses only a verified Package
declaration and proves secure storage, exact allowlisting, non-disclosure, and a
Package-owned connection test. Missing optional configuration never removes the
FFmpeg baseline.

M1.2 presents trustworthy current facts and the next available intents. The latest
relay was about 25.95 KB with 24 capability rows and 63 setup offers; the resulting
technical/catalogue overload is a UX finding, not proof that the user cannot
continue. Shell preserves its mechanical role. The configuration entries are
handoffs only: M1.2 does not install, save credentials, call a Provider, validate
a selected configuration, or retest it.

M1.2 is a user-result contract, not a Skill-text deliverable. It is complete when
trustworthy facts reach WorkBuddy, the user understands that basic production
works now, Remotion, HyperFrames, external AI image/video, and TTS are explicitly
introduced, and understandable continue/local/API-key/defer or detail entries are
visible. A particular defer reply is not required. The latest run proved this core
boundary; M1.3 later proves the two configuration mechanisms, and M2 proves direct
continuation into business clarification. M1.4 integrates and closes the M1 result.

The historical WorkBuddy-owned discovery probe did not prove that route.
WorkBuddy reached the verified Package and attempted its raw registry summary, but the
facts did not reach the user conversation; an ad-hoc file carrier is not an
acceptable product path. A later separately authorized zero-write audit was allowed to find
the smallest existing Shell mechanical factual-relay boundary. It must preserve
WorkBuddy's explanation, relevance, Provider/model, consent, and recovery
ownership and cannot itself authorize implementation.

The following historical zero-write audit found that the smallest carrier was not a
new protocol: extend the existing validated `fixed-child-handoff` with the
verified Package's raw factual summary. Shell relays the facts without
interpreting, recommending, ranking, or selecting them. The Owner then authorized
the exact two-file implementation and focused local proof. That local contract is
not M1.2 completion; only later real WorkBuddy evidence can prove that ordinary
users receive the explanation and four choices.

That two-file implementation was pushed at `33f49fb...` and is
`VERIFIED_LOCAL_FACTUAL_RELAY_CONTRACT`. The immutable final PackageRoot was later
assembled, registered, activated, and bound to the single installed Skill. A
following WorkBuddy attempt was cancelled on creation of a normal empty task
workspace before the Skill/Shell ran; the unchanged old LauncherReceipt proves
the new relay was not invoked. That attempt is
`NOT_PROVED_PREMATURE_HARD_STOP / NEW_SKILL_NOT_INVOKED`, not a relay failure.

An empty task workspace is allowed harness behavior. A workspace relay file,
copy/rewrite of the managed handoff or summary, persistent memory, or new user
Skill remains prohibited. The reviewed consumer candidate was installed after
the Owner manually removed the old same-name Skill. Its authorized probe proved
the factual relay reached dialogue, but independent review rejected the user
result `REJECT / P0=0 / P1=3 / P2=0` for false Remotion readiness, exposed
configuration mechanics, and missing choices.

The historical WorkBuddy consumer-correction authorization permitted only its six-document
synchronization, a one-file Skill correction, one newly named uninstalled
candidate ZIP bound to the unchanged active PackageRoot, their independent
zero-write reviews, commits, and ordinary pushes. The separate package-size
checkpoint changes only successor distribution assembly and does not authorize
WorkBuddy or activation. Installing the correction or running WorkBuddy
again needs fresh action-time Owner authorization. Exact paths and Git state
remain authority only in the Task Register. The candidate installed for the
rejected historical probe has
SHA256 `437b02c60aa234197fb419275ac64c5df804c5f477fdba16fde3278f772e68d2`;
its earlier artifact review does not satisfy M1.2 user acceptance. The Owner later
manually uninstalled that same-name Skill; execution must inspect current state.

The corrected one-file consumer is pushed at
`5229964ac681d7b34949480326e6f24a0c53913f`; its newly named candidate passed
independent zero-write review `APPROVE / P0=0 / P1=0 / P2=0` and remains
uninstalled. At that historical checkpoint this closed correction preparation
only, not M1.2 user acceptance.

The later semantic-correction candidate at implementation commit
`a884124718eab4bcdb0f98c59ae67acc7008f2fd` reached the managed facts, FFmpeg
baseline, and four choices in one WorkBuddy run. Independent review still rejected
the ordinary-user result `REJECT / P0=0 / P1=3 / P2=0`: partially configured
groups were shown as ready, the first-use response expanded a broad Provider/
configuration catalogue, and Remotion/HyperFrames were not separately explained
across source, dependency, runtime, and invocation layers. That was the historical
review outcome under the then-current contract.

That next bounded correction was executed at `666c9d4...`.
Its tighter Skill wording did not prevent WorkBuddy from exposing technical and
unrelated catalogue detail because the underlying first-use payload remained
about 25.95 KB with 24 capability rows and 63 setup offers. Independent review
returned `REJECT / P0=0 / P1=1 / P2=1` under the superseded hard-compactness
contract. The Owner now retains the excessive catalogue and technical wording as
non-blocking UX findings while accepting that the run proved M1.2 core guidance
and its configuration entries. M1.3 implementation remains unproved and not started: it must
separately demonstrate that WorkBuddy can take a natural-language selection into
one completed local-install path and one completed API-key path. This document
correction authorizes no implementation, candidate, installation, or WorkBuddy
action.

At the planning checkpoint, the later read-only prerequisite review found a feasible candidate route within
current WorkBuddy: its built-in `library` Skill proves a similar fixed-mode/
canonical-stdin script pattern; Windows native credential entry/current-user
Credential Manager is the candidate secret route; and the Package can be
extended to declare and own a non-media connection test. Golden Key has not yet
proved the first two routes, and the connection test did not yet exist. An
independent minimality review froze the reduced existing-file write set and
removed `run.ps1` and `tools/base_tool.py`. This scope freeze is planning evidence,
not implementation authorization. At that historical checkpoint, implementation
had not started, the
retained M1 branch is reused, and action-time permission is still
required before WorkBuddy, installation, secret handling, Provider/network calls,
or actual Package invocation.

The first bounded implementation is now pushed as Shell `a89e062c...` and Package
`503f0967...`. It establishes only a local code/test contract for the private
action, WinCred boundary, secret-safe environment injection, and Ark `/ping`
dispatch. It is not an M1.3 product result: Package optional-capability
definitions are still empty, so Remotion/HyperFrames stop before installation,
and no real WorkBuddy, credential, Provider, installation, rediscovery, or Package
invocation occurred.

The later local-route audit supersedes the idea that the next prerequisite is
only a Package definition update. Remotion needs a complete version-locked npm
installation, while the current Shell preparation handles only fixed downloaded
assets and the current Package renderer recognizes only dependencies below
PackageRoot. Definitions alone cannot complete installation or use.

The corrected M1.3 plan lets Windows resolve the standard location for the
user-approved scope at execution time. System-wide is the default; current-user
scope requires an explicit informed choice. No product
rule assumes `C:`, `D:`, or the developer machine layout. WorkBuddy explains and
confirms scope and permission impact; Shell installs, records, and rediscovers the
resolved runtime path; Package consumes that verified path without choosing a
location. Mainland npm installation uses the complete locked closure from
`registry.npmmirror.com` without silent overseas fallback. Success still requires
Package recognition and one real Package-mediated invocation. This correction is
planning only and runs no WorkBuddy, installation, product code, test, credential,
Provider, or media action.

One temporary branch, `codex/workbuddy-m1-capability-onboarding`, carries all
separately authorized M1.2–M1.4 commits. M1.4 closeout first fast-forwards the
reviewed head into `codex/workbuddy-capability-onboarding`, then removes the exact
recorded implementation worktree, local/remote temporary branch, and task-owned
temporary directories only after clean/ref/unique-work verification. M1 remains
incomplete until that cleanup is verified; the frozen historical baseline and
user data are never cleanup targets.
