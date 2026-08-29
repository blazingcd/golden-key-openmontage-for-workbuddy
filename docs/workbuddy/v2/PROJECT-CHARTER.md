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

On first use, WorkBuddy performs a light capability inventory after PackageRoot
verification. It explains the basic readiness state and relevant optional
enhancements, including Remotion, HyperFrames, external video generation, and
TTS, then lets the user continue or configure selected items. WorkBuddy owns the
conversation, relevance, Provider/model choice, cost/privacy explanation,
credentials, consent, connection testing, and recovery. Shell runtime preparation
may only detect and apply an exactly approved mechanical plan.

Later natural-language requests containing `金钥匙智能体` may inspect, configure,
change, or retest capabilities. This is an open intent, not a fixed configuration
language or second control plane.

The verified Package's formal declarations determine which Providers M1 shows.
Current static evidence includes Seedance, Kling, and MiniMax; Seedance is the
current default recommendation. Undeclared Providers do not appear in M1.
WorkBuddy explains user value before technical Provider details, while
Shell remains Provider-opaque. Static adapter presence never proves live account
or model availability.

Natural language starts and controls both configuration mechanisms. A local
capability is complete only after approved download, managed installation,
rediscovery, Package recognition, and actual invocation. An API-key Provider is
complete only after secure input outside ordinary chat, safe local storage, exact
allowlisting, non-disclosing relay, and an authorized connection test.

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
baseline. Its earlier recording authorized no execution. The current narrow M1.2
deployment/readiness exception is stated below and in the Task Register; Provider
configuration and media production remain outside it.

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

M1.2 owns the unified first-use scan, ordinary-language explanation, honest
Provider state, and continue/configure entry. M1.3 owns the selected local or
API-key configuration, consent, secure handling, validation, failure recovery,
and later retest. Planned wording and steps may change after real WorkBuddy
evidence; acceptance follows the completed user goal and safety boundaries rather
than exact rehearsal of the planning examples.

M1.2 presents a compact current summary and expands only the details relevant to
the user's goal or choice. The verified Package Guide's
`provider_menu_summary()` is the leading candidate when WorkBuddy-owned discovery
is proved feasible; it is not a fixed acceptance step or a requirement imposed on
a different factual-relay design. Do not dump raw Package data by default. The
configuration entries are handoffs only: M1.2 does not install, save credentials,
call a Provider, validate a selected configuration, or retest it.

M1.2 is a user-result contract, not a Skill-text deliverable. It is complete only
when trustworthy current facts can reach WorkBuddy, those facts are translated
into an honest ordinary-user explanation, and the continue/local/API-key/defer
choices actually work at the authorized evidence level. The corrected execution
contract probes WorkBuddy's verified Package discovery first because the Package
already exposes compact capability facts. A prompt that tells WorkBuddy to scan
is not proof that scanning exists. If the bounded probe cannot prove that fact
path, the task stops; bounded Shell factual relay is a separately authorized
fallback design, not work silently absorbed into the probe. M1.4 may integrate the
M1 result but must not retroactively fill missing M1.2 evidence.

The one authorized WorkBuddy-owned discovery probe did not prove that route.
WorkBuddy reached the verified Package and attempted its compact summary, but the
facts did not reach the user conversation; an ad-hoc file carrier is not an
acceptable product path. A separately authorized zero-write audit may now find
the smallest existing Shell mechanical factual-relay boundary. It must preserve
WorkBuddy's explanation, relevance, Provider/model, consent, and recovery
ownership and cannot itself authorize implementation.

That zero-write audit is complete. It found that the smallest candidate is not a
new protocol: extend the existing validated `fixed-child-handoff` with the
verified Package's bounded compact summary. Shell relays the facts without
interpreting, recommending, ranking, or selecting them. The Owner has authorized
the exact two-file implementation and focused local proof. That local contract is
not M1.2 completion; only later real WorkBuddy evidence can prove that ordinary
users receive the explanation and four choices.

That two-file implementation is pushed at `33f49fb...` and is
`VERIFIED_LOCAL_FACTUAL_RELAY_CONTRACT`. The immutable final PackageRoot was later
assembled, registered, activated, and bound to the single installed Skill. A
following WorkBuddy attempt was cancelled on creation of a normal empty task
workspace before the Skill/Shell ran; the unchanged old LauncherReceipt proves
the new relay was not invoked. That attempt is
`NOT_PROVED_PREMATURE_HARD_STOP / NEW_SKILL_NOT_INVOKED`, not a relay failure.

An empty task workspace is allowed harness behavior. A workspace relay file,
copy/rewrite of the managed handoff or summary, persistent memory, or new user
Skill remains prohibited. The current authorization ends before WorkBuddy: it
permits only the six-document correction, a one-file Skill consumer instruction,
an uninstalled candidate ZIP bound to the active PackageRoot, their independent
zero-write reviews, commits, and ordinary pushes. Installing/replacing the Skill
or running WorkBuddy needs fresh action-time Owner authorization. Exact paths and
Git state remain authority only in the Task Register.

One temporary branch, `codex/workbuddy-m1-capability-onboarding`, carries all
separately authorized M1.2–M1.4 commits. M1.4 closeout first fast-forwards the
reviewed head into `codex/workbuddy-capability-onboarding`, then removes the exact
recorded implementation worktree, local/remote temporary branch, and task-owned
temporary directories only after clean/ref/unique-work verification. M1 remains
incomplete until that cleanup is verified; the frozen historical baseline and
user data are never cleanup targets.
