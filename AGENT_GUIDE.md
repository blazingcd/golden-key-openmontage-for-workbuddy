# WorkBuddy Shell V2 Agent Guide

## Mandatory routing

Read this file completely before acting in this repository or responding about it.
`docs/workbuddy/v2/TASK-REGISTER.md` is the current state and authorization authority.
`PROJECT-CHARTER.md` defines the product boundary, `ACCEPTANCE-MATRIX.md` defines
user-visible acceptance, and `DRIFT-GUARD.md` defines stop and Git rules. If the
six authority documents disagree, stop and report the conflict; do not infer from
chat history, old plans, tests, or Git history.

The completed historical baseline is `refs/heads/codex/workbuddy-shell-v2` at
`aa9cabfa0d4f75d93e22317466709b6bad3bc3b4`; do not advance or rewrite it. The
authorized documentation branch for the next phase is
`refs/heads/codex/workbuddy-capability-onboarding`. That branch records planning
only until the Owner separately authorizes implementation.

The initial M0 capability-onboarding contract was frozen at
`4c0cbd3447546c3dcc0079f2392a3b43e7542e69`. The Owner's later master-roadmap
authorization permits one additional documentation-only amendment on the same
planning branch, limited to the six authority/state documents, one independent
zero-write document review, one commit, and an ordinary push. It does not select
or create an implementation branch, authorize code/tests/WorkBuddy, or turn its
read-only route list into a write allowlist.

The master-roadmap amendment was completed and pushed at
`204d6b36c6b19b8a601f6d791aa2bd9609eabbd1`. The Owner then accepted the M1.1
fact-audit conclusion and delegated its minimum preservation. That permits one
documentation-only closeout affecting `AGENT_GUIDE.md`, `PROJECT-STATE.md`, the
Task Register, Acceptance Matrix, and Drift Guard, followed by one independent
zero-write document review, one commit, and one ordinary push. It does not
authorize M1.2 or any implementation action.

Owner authorization dated 2026-08-29 permits one further documentation-only
correction on `codex/workbuddy-capability-onboarding` to record the initial
mainland-China video-Provider scope and its effect on M1.2/M1.3. It is limited to
the six authority/state documents, one independent zero-write document review,
one commit, and one ordinary push. It does not authorize implementation, Package
changes, tests, WorkBuddy, installation, credentials, Provider calls, or media.

The Owner's later 2026-08-29 direction permits one documentation-only correction
of that scope: M1 shows only Providers formally declared by the verified Package,
omits undeclared Providers, and plans both local installation and
API-key configuration. Natural-language examples are hypotheses, not a required
transcript. Real WorkBuddy evidence may justify a bounded fixed sequence when it
is needed for security or reliable completion. The same six-document, one-review,
one-commit, ordinary-push limit applies; implementation remains unauthorized.

The Owner's subsequent 2026-08-29 direction permits one documentation-only freeze
of the M1.2 execution contract on the same planning branch and under the same
six-document, one-review, one-commit, ordinary-push limit. The single future M1
implementation branch is named `codex/workbuddy-m1-capability-onboarding` but
must not be created by this documentation task. It is shared by M1.2–M1.4 rather
than replaced for every subtask. M1.2 implementation, tests, WorkBuddy,
installation, credentials, Provider calls, Package changes, and media remain
unauthorized.

The Owner's later direction requires the M1 branch lifecycle and cleanup gate to
be authority, not chat memory. This permits one documentation-only six-document
correction, one independent zero-write review, one commit, and one ordinary push.
After reviewed M1.4 closeout, the implementation head must ordinary-fast-forward
`codex/workbuddy-capability-onboarding`; only after exact ref and clean-state
verification may the recorded implementation worktree, local/remote temporary
branch, and task-owned temporary directories be removed. M1 is not `COMPLETE`
until that cleanup is verified. This documentation task performs no branch,
worktree, directory, implementation, test, or external action.

The Owner's current direction accepts the M1.2 hard stop, authorizes exact cleanup
of its two task-owned side-effect paths, permits one six-document status/model-
priority correction with one independent zero-write review, one commit, and one
ordinary planning-branch push, and authorizes one separate read-only audit of the
smallest existing Shell factual-relay route. It does not authorize Shell or Skill
implementation, tests, another WorkBuddy run, installation, credentials, Provider
calls, media, implementation-branch push, rollback, or branch/worktree deletion.

The Owner's subsequent direction accepts that audit's
`PROPOSE_BOUNDED_SHELL_FACTUAL_RELAY` conclusion and authorizes two consecutive
steps without another approval pause. First, update only the six authority/state
documents, obtain one independent zero-write document review, commit once, and
ordinarily push `codex/workbuddy-capability-onboarding`. Then ordinarily merge
that exact pushed head into the retained clean M1 implementation branch and
change only `golden_key_openmontage_workbuddy/fixed_child.py` and
`tests/workbuddy/test_installer.py`. Run only the focused direct test plus text/
scope checks, obtain one independent zero-write implementation review, commit
once, and ordinarily push the implementation branch. This authorizes no
WorkBuddy rerun, Skill install/build, optional installation, credential,
Provider, media, M1.3, extra source file, new protocol, or branch/worktree cleanup.

The earlier 2026-08-29 action-time direction completed the immutable final
PackageRoot/Release, registration/activation, and one bound Skill replacement.
The following WorkBuddy attempt was cancelled immediately after WorkBuddy created
its normal empty task workspace
`C:\Users\blazi\WorkBuddy\2026-08-29-19-32-28`. The latest LauncherReceipt stayed
on the old PackageRoot and old `fixed_child.py`; therefore the newly deployed
factual relay was never invoked. This attempt is
`NOT_PROVED_PREMATURE_HARD_STOP / NEW_SKILL_NOT_INVOKED`, not evidence that the
relay or WorkBuddy handoff consumption failed.

An empty WorkBuddy task directory alone is allowed harness mechanics. The actual
prohibitions are copying or rewriting the managed handoff/summary into that
workspace, creating a relay file, persistent memory or Skill creation, optional
installation, secret handling, Provider/media action, M1.3, fallback, retry, or
technical burden for the ordinary user.

The Owner's current direction authorizes preparation only up to the next
WorkBuddy action gate: update only the six authority/state documents, obtain one
independent zero-write document review, commit once, and ordinarily push the
planning branch; ordinarily merge that exact head into the retained M1 branch;
change only `workbuddy-skill/golden-key-openmontage/SKILL.md` so WorkBuddy reads a
valid LauncherReceipt `result_pointer` and consumes the bounded
`package_capability_summary` from the existing managed handoff without a
workspace copy; build and verify one newly named, uninstalled Skill ZIP bound to
the already active final PackageRoot; obtain one independent zero-write candidate
review; commit once and ordinarily push the implementation branch. Do not rebuild,
reregister, or reactivate the PackageRoot.

Installing or replacing the Skill in WorkBuddy, opening or operating WorkBuddy,
and running the next readiness probe are not authorized by this preparation.
Stop after the reviewed candidate and exact Git evidence and obtain fresh
action-time Owner authorization.

## Product boundary

The product goal is one ordinary-user path:

1. The user writes a natural-language business request in WorkBuddy.
2. The request contains the wake word `金钥匙智能体`.
3. WorkBuddy is the only Agent, conversation owner, and production decision-maker.
4. WorkBuddy uses the verified OpenMontage Package as the production-semantic source.
5. The Shell supplies only installation/lifecycle, Registration/Locator, runtime
   preparation, fixed mechanical invocation, WorkBuddy entry, and status/receipt relay.

The Shell is not a second Agent, conversation owner, Director, workflow engine,
provider/renderer selector, media control plane, MCP/router, or general framework.
The OpenMontage Package is not a second running Agent. Its external `AGENT_GUIDE.md`
may be read by WorkBuddy only after a verified PackageRoot has been returned by
Registration/Locator.

The ordinary user never has to construct or operate internal paths, hashes,
schemas, environment variables, argv, pipes, or commands. WorkBuddy is a harness
Agent with its own reasoning. For the same natural-language input, its thought
process, tool path, steps, wording, and intermediate conclusions may vary. Do not
judge it against an evaluator-invented creative or production transcript.
Configuration may nevertheless use a bounded ordered sequence when actual
WorkBuddy behavior, consent, secure secret entry, or reliable installation needs
one. The sequence must still begin from ordinary natural language and must not make
the user operate internal commands or turn Shell into a control plane.

For every future WorkBuddy execution in this project, prefer an available model
row marked `0.00x`. While waiting, the executor may switch among available
`0.00x` rows. Only when every `0.00x` row is unavailable may it choose a positive
multiplier, from the smallest upward. Record the selected row; a non-`0.00x`
choice must also record why all `0.00x` rows were unavailable. Model switching
must not replay a user request or create a second task merely to change models.

## Capability readiness

FFmpeg is the minimum production baseline. When it is ready, OpenMontage can
produce a basic result; an absent optional enhancement must never be described as
OpenMontage lacking production capability or block that basic path.

On first use, after PackageRoot verification, WorkBuddy should perform a light
capability inventory using its own current tools and the verified Package
semantics. It explains the FFmpeg baseline and the status of relevant optional
enhancements such as Remotion, HyperFrames, external video generation, and TTS,
then lets the user continue immediately or configure selected enhancements.
WorkBuddy owns the dialogue, relevance, Provider/model choice, cost/privacy
explanation, consent, and recovery decision. The Shell may only perform bounded
detection, exactly approved preparation, and factual status relay.

Later requests containing `金钥匙智能体` may naturally ask to inspect, configure,
change, or retest capabilities. Do not introduce a fixed command language,
prescribed transcript, Shell Provider selector, broad disk scan, or second control
plane.

M1 displays only capabilities and Providers formally declared by the verified
Package. Current static evidence includes Seedance, Kling, and MiniMax; undeclared
Providers do not appear in the M1 user experience or acceptance scope. Seedance
remains the current default recommendation. Do not hard-code this
snapshot into Shell: future verified Package declarations may change the visible
set. Adapter presence never proves account permission, credentials, balance,
connectivity, regional availability, or current model availability.

M1 must plan two configuration mechanisms as one WorkBuddy journey. Local
capabilities such as Remotion and HyperFrames are complete only after approved
download, managed installation, rediscovery, Package recognition, and a real
Package-mediated invocation. API-key configuration is complete only after
secret-safe input and storage, exact Package allowlisting, non-disclosing relay,
and an authorized connection test. Natural language owns selection and consent;
the secret value must never be entered in ordinary chat.

## Next-phase task map

`R1` through `R4` are frozen historical result identifiers and must not be
continued. M0 is planning only. The future product roadmap uses M1–M3 for Must,
S1–S5 for Should, and C1–C2 for Could. M1.1–M1.4 are execution steps owned by M1;
they are not M0 subtasks or a separate task series.

The executable dependency is M1.1 fact audit followed by M1.2 first-use readiness.
M2 clarification may start after M1.2. M1.3 remains a required M1 product
capability with one representative local-install path and one representative
API-key path, but an individual user may defer
configuration until M2 establishes relevance or continue on FFmpeg without using
an enhancement. M3 starts only after both M1.4 and M2 are complete. S1 adds
revision/version/rollback; S2 adds one additional
aspect/platform and safe-area quality; S3 adds export/share/reuse; S4 adds
cross-machine lifecycle; S5 conditionally qualifies one user-needed enhancement.
C1 broad Provider/model coverage and C2 automatic multi-Provider routing/direct
publishing remain deferred. C1 covers Providers beyond the verified Package's
formal declarations; M1 does not invent unsupported Provider entries. The complete
dependency and acceptance authority is the Task Register.

M1.1 is complete as a fact audit and its conclusions are Owner-accepted. It did
not pass the strict zero-write process gate because an independent sub-audit
created and then removed `D:\DevCache\Temp\m11-rg.txt`; the repository remained
clean and the path no longer exists.

The M1.2 contract frozen at `f11e7118e2f652b6e0ceb31b1bc88e617dcf8174` is
withdrawn as an execution authority. It required an authoritative capability
inventory while allowing changes only to
`workbuddy-skill/golden-key-openmontage/SKILL.md`, even though M1.1 had already
proved that the production route had no `prepare_optional_capabilities` caller,
`user_entry.py` supplied empty local-capability evidence, and WorkBuddy's ability
to perform the required Package discovery was `NOT_VERIFIED`. The contract's
focused checks could verify wording and packaging but not the required fact flow.

Commit `4cbf8ff3c15dd686a893842ca189ce49fa83023d` on
`codex/workbuddy-m1-capability-onboarding` is therefore only a partial Skill
guidance candidate. It must not be called M1.2 complete or
`VERIFIED_LOCAL_CONTRACT`, merged into the formal ref, promoted as complete, or
used to authorize M1.3. Preserve the branch and worktree while M1.2 is paused; do
not delete or rewrite them.

M1.2 remains the ordinary-user first-use readiness result: after verified
PackageRoot resolution, WorkBuddy must obtain trustworthy current facts, explain
that the FFmpeg baseline can continue, show relevant optional capability and
Package-declared Provider states honestly, and let the user continue, enter local
configuration, enter API-key configuration, or defer. A Skill instruction alone
is not evidence that discovery, state formation, or handoff works.

The corrected WorkBuddy-owned discovery probe has run once and stopped as
`NOT_PROVED_WORKBUDDY_DISCOVERY`. WorkBuddy verified PackageRoot/Guide and tried
to call `provider_menu_summary()`, but no capability facts, FFmpeg explanation,
optional-capability states, or continue/local/API-key/defer choices reached the
ordinary-user dialogue. WorkBuddy instead created an unapproved workspace and
attempted file-based relay, so the task was cancelled before further writes. No
media, optional installation, secret, Provider call, M1.3 action, Skill repair,
or Shell fallback occurred.

The bounded relay audit result was implemented in exactly `fixed_child.py` and
its direct installer test. Local/tracking/advertised implementation refs now all
equal `33f49fb385b103489772d3f8ce2f7cb2486b08dc`; the worktree is clean and the
result is `VERIFIED_LOCAL_FACTUAL_RELAY_CONTRACT`.

M1.2 is now `VERIFIED_LOCAL_FACTUAL_RELAY_CONTRACT /
CONSUMER_CANDIDATE_PREPARATION_AUTHORIZED / WORKBUDDY_ACTION_NOT_AUTHORIZED /
M1_3_BLOCKED`. The local result
cannot make M1.2 complete by itself. The WorkBuddy result must be separately
authorized and must still prove that facts reach the ordinary-user dialogue, the
FFmpeg explanation
and honest optional states appear, and continue/local/API-key/defer are actually
available. If completion needs a third source path, new carrier/protocol, live
repair, Provider/secret/media action, retry, or fallback, stop.

## Four product results

### Result 1 — COMPLETE

The installable Shell product is complete at commit
`869358810ee41a0a61d10cec10c1b3b93c2c3450`, tree
`3a623cb1eab9fee0d90854c0df271450f9779b9a`, Release SHA256
`7e5585298e50a5c5713ecd8fc4df57cfb6e88381b39453364cec62fdea1c6280`.
Installation, Registration, Activation, Uninstallation, Reinstallation, and user
data protection were completed.

### Result 2 — COMPLETE

In WorkBuddy 5.3.14 with Hy3, the ordinary-user input
`用金钥匙智能体给我做新店开业视频` actually invoked the single
`golden-key-openmontage` Skill and Shell. The user received a concrete business
reply and a checkable LauncherReceipt. The Skill ZIP SHA256 is
`c96ec03522b744e8771eb16f22f5521102c4007af50ccb27d895efb82b1fe3a6`; evidence is
under `D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\evidence\product2-workbuddy-user-flow-20260826`.

The receipt state `INCOMPLETE / RESULT_POINTER_INVALID` only says that this run
did not create a video file. A file and valid result pointer belong to Result 3;
they do not invalidate Result 2. The original independent review fact
`REJECT / P0=0 / P1=1 / P2=0` is retained only as history of a mismatched gate:
its P1 applied the Result 3 artifact standard. Owner correction is final and no
second Result 2 review is required.

### Result 3 — COMPLETE

In WorkBuddy 5.3.14 with `Hy3 0.00x`, one ordinary-language request containing
`金钥匙智能体` produced the real playable 46.6-second video
`头头象花浴头疗_新店开业宣传.mp4`. WorkBuddy displayed and played the file, and
the independent result review passed with `PASS / P0=0 / P1=0 / P2=0`.

The installed Skill completed the user goal after WorkBuddy recovered within the
same task, so it is the usable rollback baseline. Its first wrapper invocation
returned exit code 1 without the managed `latest-launcher-receipt.json`; this is a
known relay-stability limitation, not a reason to erase the successful baseline.

### Result 4 — COMPLETE

Formal project closeout only. R3 already contains the ordinary-user product
acceptance; R4 does not run WorkBuddy or produce another video. Owner authorization
dated 2026-08-28 retains v4 as the installed Skill with the preserved R3 baseline
as rollback evidence, freezes the R4 plan in `TASK-REGISTER.md`, and authorizes
that plan's bounded document, verification, review, commit, and ordinary
fast-forward push steps only. The exact 11-path gate, retained identities,
installed-v4 identity, `21 passed, 1 skipped` focused tests, Skill validation,
and `git diff --check` have passed. The single independent zero-write R4 review
returned `APPROVE / P0=0 / P1=0 / P2=0`. R4 is complete only after the reviewed
commit is the exact local and remote formal ref by ordinary fast-forward. The
reviewed implementation closeout commit `70cf63be51774de9151fb0fee24cf78591ff1993`
was fast-forwarded and pushed; the Owner then authorized this documentation-only
completion record. No product, Skill, test, or external evidence changed.

## Acceptance and execution rules

- The only wake condition is that the original user message contains
  `金钥匙智能体`; do not freeze a full prompt or business description.
- Each result has one executor and exactly one independent result review after a
  real user-visible result exists. Do not create packet/pre-review/multi-review
  systems or extra roles.
- The reviewer judges the product result's user-visible goal first. It may not
  invent an architecture gate or require a preset internal sequence/wording.
  It must not compare the run against an evaluator-invented transcript or
  imagined intermediate output.
  Process variation is allowed unless it directly causes product failure, adds
  technical burden to the ordinary user, creates a second control plane, or
  produces a false result.
- Result 3 passes only with one ordinary-language entry, a real WorkBuddy path,
  a real playable video, and a checkable receipt. User-facing technical burden,
  absent Skill/Shell invocation, absent video/receipt, or Shell production
  decision-making fails it. WorkBuddy's internal commands, tool choice, retries,
  and corrections are not failures.

## Engineering and safety constraints

- Use only the project Python: `D:\BlazingCD\Personal\.venvs\golden-key-openmontage-workbuddy-w0\Scripts\python.exe`.
- Put temporary files only on D: and record every task-owned temporary directory's
  exact absolute path when created. Remove those exact paths after final review;
  preserve user data and never broaden cleanup to a parent/cache/workspace root.
- Remotion, HyperFrames, external video generation, and TTS remain optional
  enhancements. Their installation or use may be deferred, but first-use
  inventory and a natural-language configuration entry belong to the planned
  next phase. Their absence must not block an FFmpeg-ready basic path.
- Do not add a second Agent, MCP, router, or general framework.
- Never force-push or reset hard. Advance the formal branch only by ordinary
  fast-forward. Before destructive cleanup, resolve exact paths, ensure no
  unmerged or unique work exists, and prefer recoverable deletion.
- One temporary implementation branch serves M1.2–M1.4. After M1.4, fast-forward
  and push the formal capability-onboarding ref first, verify all related worktrees
  clean and no unique/unmerged commits remain, then remove the exact recorded
  worktree, local/remote temporary branch, and task directories. Dirty state,
  user data, an unrecorded path, ref divergence, or any force requirement is
  `CLEANUP_BLOCKED`; stop without deletion. The historical baseline is never a
  cleanup target.

## Current stability-candidate result

Owner authorization dated 2026-08-28 preserves the R3-passing Skill ZIP as an
unchanged rollback baseline and permits one separately named receipt-stability
candidate. Do not overwrite the baseline archive or install two Golden Key Skills
at once. The candidate may improve first-call stdout/stderr and receipt persistence
only; it must not add retries, a second control plane, or fixed business reasoning.

The one permitted WorkBuddy `5.3.14` / `Hy3 0.00x` comparison has run. The
candidate is rejected: `run.ps1` used the incompatible PowerShell combination
`Split-Path -Parent -LiteralPath` before its protected block, so the first call
returned exit code 1 without either managed diagnostic. WorkBuddy then bypassed
the Skill to recover, produced a real 37.12-second H.264/AAC MP4, and the
independent user-result review returned `PASS / P0=0 / P1=0 / P2=0`; that product
success does not repair the candidate's failed first-call contract. The same task
was stopped after it wrote an unrequested workspace memory and user-level
`golden-key-local-footage-promo` Skill. Do not make another production attempt.
The preserved baseline archives remain intact. On 2026-08-28 the Owner manually
uninstalled both the rejected `golden-key-openmontage` candidate and the
unrequested `golden-key-local-footage-promo` Skill, then authorized one new
stability candidate derived afresh from the preserved R3 baseline. Do not reuse
the rejected candidate implementation. The new candidate may make only the
minimum first-call receipt/diagnostic correction, must remain the single installed
Golden Key Skill, and gets one WorkBuddy `5.3.14` / `Hy3 0.00x` ordinary-user
comparison. If it fails, stop and ask the Owner whether to perform the full
baseline rollback; do not make another production attempt. The unrequested
workspace memory remains present and is not authorized for deletion. R4 and
unrelated work remain unauthorized.

The separately named `receipt-v3` candidate has now completed its only permitted
comparison. Its ZIP SHA256 is
`aa421dfbb00111392d37da6f6590e456b534a79e308560b441b4afd5d7b044a2`. The first
Skill call produced a managed `EXITED_SUCCESS` receipt, valid result pointer,
`spawn_count=1`, and `retry_count=0`, so the first-call receipt relay improved.
WorkBuddy then produced a valid 37-second 1920x1080 H.264/AAC MP4 at
`C:\Users\blazi\WorkBuddy\2026-08-28-13-33-53\头头象花浴头疗_新店开业宣传.mp4`.
Before giving the ordinary user a final result, WorkBuddy planned an unrequested
workspace-memory update and another user Skill. The task was stopped; the final
visible state is `用户已取消`, the artifact pane is empty, an empty workspace
memory file remains, and no extra user Skill was created. Independent result
review is `TODO`: the valid file was not delivered through a final WorkBuddy
answer. Do not run a third comparison. The v3 candidate remains installed pending
Owner direction on full baseline rollback. Historical R3 remains complete; R4
remains unauthorized.

Fresh Owner authorization dated 2026-08-28 permits one separately named
`delivery-v4` candidate derived from `receipt-v3`. Preserve the R3 baseline and
v3 archives byte-for-byte. V4 may change only the WorkBuddy-facing result
delivery boundary: once a real requested result has received the minimum honest
validation, present it and finish without optional workspace-memory or new-Skill
accumulation. It must retain v3's successful first-call receipt behavior, must
not prescribe production steps, and must not add a second control plane. The v4
artifact may be built and locally checked now. Do not install it or run another
WorkBuddy comparison without separate action-time Owner confirmation. R4 remains
unauthorized.

The v4 artifact is built with SHA256
`d838cba0735d7a2df3d81029a7d7469551a28219d91f0e8ea2fe08b0f152845d`.
Focused checks passed and the one independent zero-write candidate review returned
`APPROVE / P0=0 / P1=0 / P2=0`.

The one action-time-authorized v4 comparison is complete in WorkBuddy `5.3.14`
with `Hy3 0.00x`. V4 was the only installed Golden Key Skill for that comparison.
Its first call
produced `EXITED_SUCCESS`, a valid result pointer, `spawn_count=1`, and
`retry_count=0`. WorkBuddy delivered a 9.6 MB MP4 and its path in the final answer.
The independent ordinary-user result review is `TODO / P0=0 / P1=1 / P2=0`:
the closing title is visibly clipped on both sides. Separately, v4 did not satisfy
its stability boundary because WorkBuddy wrote an optional 978-byte workspace
memory after validating the video and before the final answer. No extra user Skill
was created. The Owner now retains v4 because its first-call and final-delivery
mechanics improved; the clipped creative output from one harness run is not by
itself a Skill regression. Do not run another comparison, repair the video, delete
the memory, or roll back the installed Skill. Historical R3 remains complete.

The later M1.2 readiness authorization replaced the installed v4 artifact with
the separately named readiness-probe candidate. That candidate, not v4, is now the
only installed Golden Key Skill; its exact identities are recorded in the Task
Register. This does not change the historical v4 comparison facts or authorize a
rollback.
