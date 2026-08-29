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
baseline. Recording it does not authorize implementation, installation, Provider
configuration, WorkBuddy execution, or media production.

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

M1.2 resolves inventory order by following the verified Package Guide: verify
PackageRoot and Guide identity, discover the registry, present the compact
`provider_menu_summary()` first, and request relevant `provider_menu()` detail only
when needed. `support_envelope()` remains diagnostic or detail evidence rather than
the default first-user display. The configuration entries are handoffs only:
M1.2 does not install, save credentials, call a Provider, validate a selected
configuration, or retest it. Its local implementation is limited to the existing
WorkBuddy Skill instructions; real WorkBuddy acceptance remains M1.4.
