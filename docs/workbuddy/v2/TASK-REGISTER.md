# WorkBuddy Shell V2 — Task Register

## Authority

This is the live task, product-result, authorization, and Git-state authority.
Read it together with `AGENT_GUIDE.md`, `PROJECT-CHARTER.md`,
`ACCEPTANCE-MATRIX.md`, and `DRIFT-GUARD.md`. If any of the six documents conflict,
stop. Old routes, chat statements, tests, and Git history cannot authorize work.

Formal delivery ref: `refs/heads/codex/workbuddy-shell-v2`.
No legacy route label or future lettered series is current.

## Product contract

The only product path is:

`ordinary user -> WorkBuddy -> golden-key-openmontage Skill -> Shell mechanics -> WorkBuddy result`

WorkBuddy is the only Agent, user-facing conversation owner, and production
decision-maker. OpenMontage Package Guide/Manifest/Pipeline/Stage/Tool semantics
are the production source. Shell owns only installation/lifecycle,
Registration/Locator, runtime preparation, fixed mechanical invocation, WorkBuddy
entry, and status/receipt relay. Shell cannot become a second Agent, Director,
workflow engine, provider/renderer selector, media control plane, MCP, router, or
general framework.

The only wake condition is the literal presence of `金钥匙智能体` in the original
user message. The rest of the user's business request and any material paths are
open input and must not be turned into a fixed full-prompt protocol. Ordinary users
do not operate internal path/hash/schema/env/argv/pipe/command mechanics.

WorkBuddy is a harness Agent. For the same input, its internal reasoning, tool
path, steps, wording, and intermediate conclusions may vary. A Skill or prompt
must not force a preset script. WorkBuddy may read the Package Guide, ask business
questions, call tools, retry, and adjust internal steps. These variations matter
only if they directly cause product failure, add ordinary-user technical burden,
create a second control plane, or produce a false result.

## Product results

### R1 — Installable Shell product: COMPLETE

- Commit: `869358810ee41a0a61d10cec10c1b3b93c2c3450`
- Tree: `3a623cb1eab9fee0d90854c0df271450f9779b9a`
- Release SHA256: `7e5585298e50a5c5713ecd8fc4df57cfb6e88381b39453364cec62fdea1c6280`
- Scope passed: installation, Registration, Activation, Uninstallation,
  Reinstallation, and user-data protection.

### R2 — WorkBuddy natural-language result: COMPLETE

- Client/model: WorkBuddy `5.3.14` / `Hy3`.
- Real user input: `用金钥匙智能体给我做新店开业视频`.
- Observed: the single `golden-key-openmontage` Skill and Shell were invoked;
  the ordinary user received a concrete business reply and a checkable
  LauncherReceipt.
- Skill ZIP SHA256:
  `c96ec03522b744e8771eb16f22f5521102c4007af50ccb27d895efb82b1fe3a6`.
- Evidence root:
  `D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\evidence\product2-workbuddy-user-flow-20260826`.

The observed receipt state `INCOMPLETE / RESULT_POINTER_INVALID` means only that
the run did not create a video file. A file and valid result pointer are required
by R3, not R2. The raw independent review `REJECT / P0=0 / P1=1 / P2=0` is kept as
a fact about the mismatched review; its only P1 used the R3 artifact standard.
Owner corrected the acceptance level, so R2 is complete and has no second review.

### R3 — Real playable Golden Key video: COMPLETE

- Client/model: WorkBuddy `5.3.14` / `Hy3 0.00x`.
- Entry: one ordinary-language request containing `金钥匙智能体`.
- Result: WorkBuddy displayed and played
  `D:\BlazingCD\Personal\测试素材\头头象花浴头疗素材\成片\头头象花浴头疗_新店开业宣传.mp4`.
- Media: 46.6-second H.264/AAC MP4, 1920x1080, 25 fps.
- Receipt evidence:
  `D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\gk_debug_run.log`;
  `EXITED_SUCCESS`, `launched=true`, `spawn_count=1`, and a valid result pointer.
- Independent review: `PASS / P0=0 / P1=0 / P2=0`.

The first Skill wrapper invocation returned exit code 1 and did not create the
managed `latest-launcher-receipt.json`. WorkBuddy recovered within the same user
task and completed the real video. This does not invalidate R3, but it leaves a
known first-call relay-stability limitation before formal closeout.

### Stability candidate — COMPLETE / REJECTED

Owner authorization dated 2026-08-28 preserves the R3-passing Skill as the usable
rollback baseline:

- original:
  `D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\Integrations\WorkBuddy\golden-key-openmontage-0.3.25.zip`;
- rollback copy:
  `D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\Integrations\WorkBuddy\golden-key-openmontage-0.3.25-r3-pass-baseline.zip`;
- both SHA256:
  `e7ecfd69a22b2f601215860a83f849584c50f29328c011622a42fdd2e63d4bab`.

Build the receipt-stability change as the separate artifact
`golden-key-openmontage-0.3.25-receipt-v2.zip`, SHA256
`bd35b98087cd7a03f909dc17bbd6048388a7c46e2251c3893a3f9f056d653249`;
never overwrite either baseline.
The candidate may capture and persist first-call stdout, stderr, exit status, and
the canonical receipt. It may not replay the request, add production decisions,
or install a second Golden Key Skill.

After focused checks, replace the installed baseline with the candidate and make
one ordinary-user `Hy3 0.00x` comparison. Acceptance is a checkable result from
the first Skill call without WorkBuddy bypassing the Skill to recover transport
output. After the visible result, run one independent zero-write review. On
failure, reinstall the preserved baseline and stop without another production
attempt or Package rebuild.

The one comparison ran in WorkBuddy `5.3.14` with the `Hy3 0.00x` row visibly
selected. Candidate acceptance failed. The installed `run.ps1` evaluated
`Split-Path -Parent -LiteralPath` before entering its protected block; that
PowerShell parameter combination is invalid, so the first call returned exit
code 1 and wrote neither `latest-launcher-receipt.json` nor
`latest-launcher-failure.json`. WorkBuddy then bypassed the Skill and invoked the
Python entry directly.

The same ordinary-user task nevertheless produced
`C:\Users\blazi\WorkBuddy\2026-08-28-11-36-00\outputs\toutouxiang\头头象花浴头疗_新店开业宣传.mp4`.
It is a real 37.12-second, 1080x1920, 25 fps H.264/AAC MP4. Full decode succeeded,
audio is non-silent, and the independent user-result review returned
`PASS / P0=0 / P1=0 / P2=0`. Keep that product result separate from the rejected
candidate stability verdict.

After the video and frame checks, WorkBuddy wrote two unrequested persistent
side effects: `C:\Users\blazi\WorkBuddy\2026-08-28-11-36-00\.workbuddy\memory\2026-08-28.md`
and `C:\Users\blazi\.workbuddy\skills\golden-key-local-footage-promo\SKILL.md`.
The running task was stopped. They have not been deleted, the candidate remains
installed, and the preserved baseline has not been reinstalled because those
destructive/install actions require fresh Owner confirmation. Do not run a second
production comparison or rebuild the Package.

### Stability candidate v3 — COMPLETE / COMPARISON NOT ACCEPTED

The Owner manually uninstalled the rejected `golden-key-openmontage` candidate
and the unrequested `golden-key-local-footage-promo` Skill. Read-only cache
inspection found no remaining directory for either Skill. The unrequested
workspace memory still exists and is not authorized for deletion.

Fresh Owner authorization permits one new candidate derived from the preserved
R3 baseline ZIP. Do not build on or patch the rejected candidate implementation.
The allowed change is the minimum first-call receipt/diagnostic stability
correction; it may not add request replay, production decisions, a second control
plane, or fixed WorkBuddy reasoning. Preserve both baseline ZIPs byte-for-byte and
publish the new artifact under a separate `receipt-v3` name.

After focused local checks and one independent zero-write candidate review,
install v3 as the only Golden Key Skill and make one ordinary-user comparison in
WorkBuddy `5.3.14` with `Hy3 0.00x`. Review the visible result once. If v3 fails,
stop and ask the Owner whether to perform the full baseline rollback; do not make
another production attempt.

The candidate artifact is
`D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\Integrations\WorkBuddy\golden-key-openmontage-0.3.25-receipt-v3.zip`,
SHA256
`aa421dfbb00111392d37da6f6590e456b534a79e308560b441b4afd5d7b044a2`.
Focused checks passed and the independent zero-write candidate review returned
`APPROVE / P0=0 / P1=0 / P2=0`. WorkBuddy installed it as the only Golden Key
Skill and the one permitted `Hy3 0.00x` ordinary-user prompt ran.

The first Skill call produced a managed `EXITED_SUCCESS` receipt with a valid
result pointer, `spawn_count=1`, and `retry_count=0`. WorkBuddy later produced
`C:\Users\blazi\WorkBuddy\2026-08-28-13-33-53\头头象花浴头疗_新店开业宣传.mp4`.
It is a 37-second, 1920x1080, 30 fps H.264/AAC MP4; full decode succeeded and its
audio is non-silent. Before giving the ordinary user a final answer or artifact
card, WorkBuddy planned an unrequested workspace-memory update and another user
Skill. The task was stopped. Final UI state is `用户已取消`, the artifact pane is
`暂无内容`, an empty workspace-memory file remains, and no extra user Skill was
created.

The independent user-result review returned `TODO`: a valid local file exists,
but WorkBuddy did not deliver its path or a playable artifact in the final visible
result. Keep this comparison failure separate from historical R3, which remains
complete. V3 remains installed pending Owner direction on full baseline rollback.
Do not run a third comparison.

### Stability candidate v4 — COMPLETE / COMPARISON NOT ACCEPTED

Fresh Owner authorization dated 2026-08-28 permits one new candidate derived
from `receipt-v3`, while retaining both R3 baseline ZIPs and the v3 ZIP
byte-for-byte. The only allowed change is the WorkBuddy-facing result-delivery
boundary: after a real requested result receives the minimum validation needed
for an honest claim, WorkBuddy should present it and finish without delaying the
user-visible result for optional workspace-memory or new-Skill accumulation.
This must not prescribe a production script, alter WorkBuddy's production
ownership, add replay, or create a second control plane.

The separately named artifact is
`D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\Integrations\WorkBuddy\golden-key-openmontage-0.3.25-delivery-v4.zip`,
SHA256 `d838cba0735d7a2df3d81029a7d7469551a28219d91f0e8ea2fe08b0f152845d`.
It retains the v3 wrapper and first-call receipt behavior. Focused local checks
passed with `21 passed, 1 skipped`, Skill validation passed, and `git diff
--check` passed. The one independent zero-write candidate review returned
`APPROVE / P0=0 / P1=0 / P2=0`. Do not install v4, uninstall v3, or run another
WorkBuddy comparison without separate action-time Owner confirmation. Historical
R3 remains complete and R4 remains unauthorized.

The Owner then gave action-time confirmation to install v4 and run once. WorkBuddy
`5.3.14` visibly used `Hy3 0.00x`; v4 remained the only installed Golden Key Skill.
The first call produced `EXITED_SUCCESS`, a valid result pointer,
`spawn_count=1`, and `retry_count=0`. The handoff retained
`decision_owner=WorkBuddy` and `media_executed=false`.

WorkBuddy completed a final answer and attached the 9.6 MB file
`D:\BlazingCD\Personal\测试素材\头头象花浴头疗素材\成片\头头象花浴头疗_新店开业宣传.mp4`.
Its SHA256 is
`e9da5db0d4fae5f6725214d82875a80bb389968fbbf60009771eb779af1641e7`.
The H.264 video stream is 1920x1080, 25 fps, 66.28 seconds and 1657 frames;
the AAC audio and container are 72 seconds. The independent ordinary-user result
review returned `TODO / P0=0 / P1=1 / P2=0`: the closing title visibly overflows
the frame and is clipped on both sides.

Keep that result review separate from v4's stability verdict. V4 is not accepted
as the stable Skill because WorkBuddy wrote the optional 978-byte
`C:\Users\blazi\WorkBuddy\2026-08-28-15-40-28\.workbuddy\memory\2026-08-28.md`
after validating the video and before its final reply. No extra user Skill was
created. V4 remains the single installed Golden Key Skill. Do not retry, repair
the video, delete the memory, or roll back without fresh Owner authorization.
Historical R3 remains complete.

### R4 — Formal closeout: REVIEW_APPROVED / COMMIT_PENDING

R3 already contains ordinary-user product acceptance. R4 records the final
authority documents, evidence, and formal Git state only; it does not run
WorkBuddy or produce another video. Owner authorization dated 2026-08-28 retains
v4 as the installed Skill because its first-call receipt and final-delivery
mechanics improved. The clipped creative output from one harness run is not by
itself attributed to the Skill. The preserved R3 baseline remains rollback
evidence, and the optional workspace-memory side effect remains a known limit.

#### Frozen R4 result

R4 is complete only when the current bounded change set is documented, verified,
independently reviewed once, committed once, and is the exact local and remote
`refs/heads/codex/workbuddy-shell-v2` by ordinary fast-forward. It does not change
the product, generate another user result, or claim that WorkBuddy is deterministic.

#### Allowed paths

R4 may retain and close only the existing modifications in these 11 paths:

- `AGENT_GUIDE.md`
- `PROJECT-STATE.md`
- `docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`
- `docs/workbuddy/v2/DRIFT-GUARD.md`
- `docs/workbuddy/v2/PROJECT-CHARTER.md`
- `docs/workbuddy/v2/TASK-REGISTER.md`
- `golden_key_openmontage_workbuddy/installer.py`
- `tests/workbuddy/test_installer.py`
- `tests/workbuddy/test_repository_hygiene.py`
- `workbuddy-skill/golden-key-openmontage/SKILL.md`
- `workbuddy-skill/golden-key-openmontage/scripts/run.ps1`

No new file or additional path is allowed. External ZIPs, receipts, videos,
installed Skills, and workspace memories are read-only evidence.

#### Execution sequence

1. Verify the starting Git gate: current detached HEAD, the local formal ref, and
   `origin/codex/workbuddy-shell-v2` are all `895773f62b8c678d075898c6b40361f3060d797b`;
   the separate formal-branch worktree is clean; the current dirty set is exactly
   the 11 allowed paths.
2. Align the six authority/state documents with the retained-v4 decision and this
   frozen plan. Do not rewrite historical R1-R3 evidence.
3. Read the complete implementation/test diff. Verify the two preserved R3
   baseline ZIPs, v3 ZIP, v4 ZIP, current launcher receipt/handoff, installed
   single-Skill state, and absence of any additional Golden Key Skill. Do not
   mutate external evidence.
4. Run only
   `tests/workbuddy/test_installer.py` and
   `tests/workbuddy/test_repository_hygiene.py` with the project `.venv`, the
   existing Skill quick validation, `git diff --check`, and the exact allowed-path
   check. Do not run full CI.
5. After the final R4 candidate exists, one `luna_worker` independently reviews it
   with zero writes. It returns `APPROVE` or `TODO` and P0/P1/P2 counts. It judges
   document agreement, path scope, retained identities, tests, product boundary,
   and fast-forward safety; it does not rerun WorkBuddy or invent a transcript.
6. Only on `APPROVE / P0=0 / P1=0 / P2=0`, create one closeout commit from the
   detached execution worktree, ordinary-fast-forward the clean formal-branch
   worktree to it, push that branch, and verify local ref, remote-tracking ref,
   remote advertised ref, and both worktree states. Otherwise stop without commit
   or push.

#### Hard stops and anti-inflation boundary

Stop on any authority conflict, unexpected path, changed retained hash, second
installed Golden Key Skill, failed focused check, review finding, dirty formal
worktree, non-fast-forward requirement, or remote divergence. R4 must not start
WorkBuddy, generate or repair media, install/uninstall a Skill, delete memory or
user evidence, rebuild the Package, revisit E/B/C/D/F routes, add a control plane,
create branches/worktrees, clean old task objects, or run unrelated audits/CI.

#### Execution record before review

- Starting detached HEAD, local formal ref, and remote-tracking formal ref:
  `895773f62b8c678d075898c6b40361f3060d797b`.
- Separate formal-branch worktree: clean.
- Dirty path gate: exactly the 11 allowed paths; no additions.
- R3 baseline ZIP pair: byte-identical SHA256
  `e7ecfd69a22b2f601215860a83f849584c50f29328c011622a42fdd2e63d4bab`.
- v3 ZIP SHA256:
  `aa421dfbb00111392d37da6f6590e456b534a79e308560b441b4afd5d7b044a2`.
- retained v4 ZIP SHA256:
  `d838cba0735d7a2df3d81029a7d7469551a28219d91f0e8ea2fe08b0f152845d`.
- Installed state: one `golden-key-openmontage` Skill; its two files match the
  v4 ZIP entries byte-for-byte; no second Golden Key Skill.
- Current launcher evidence: `EXITED_SUCCESS`, valid result pointer, one spawn,
  zero retry; handoff keeps `decision_owner=WorkBuddy` and
  `media_executed=false`.
- Focused tests: `21 passed, 1 skipped` with the project `.venv`.
- Skill quick validation: passed.
- `git diff --check`: passed.

The candidate then entered its one independent zero-write R4 review. No commit or
push was allowed before `APPROVE / P0=0 / P1=0 / P2=0`.

#### Independent review

The one independent zero-write R4 review returned
`APPROVE / P0=0 / P1=0 / P2=0`. It confirmed authority agreement, the exact
11-path scope, retained identities, single installed v4, honest known limits,
WorkBuddy/Shell ownership, focused checks, and detached-commit to clean-formal-
worktree fast-forward safety. No second review is required. Only the reviewed
commit, ordinary fast-forward, push, and final exact-ref verification remain.

## Acceptance rules

1. Each result has one executor and one independent result review, performed only
   after a real user-visible result exists.
2. Do not create packet, pre-review, multi-round review, or role-separation
   machinery. A reviewer starts from the result's user-visible goal and may not
   invent an architecture gate or preset internal process.
3. WorkBuddy may use its own harness reasoning, Guide reading, questions, tools,
   retries, and internal corrections. These are not failures unless they make a
   required product result absent, burden the user technically, create a second
   control plane, or produce a false result.
4. R3 fails if an ordinary user must operate technical commands/paths/schema/env,
   the Skill/Shell is not actually called, no real playable video and receipt
   exist, or Shell makes production decisions as a second Agent.

## Engineering constraints

- Project Python only: `D:\BlazingCD\Personal\.venvs\golden-key-openmontage-workbuddy-w0\Scripts\python.exe`.
- Temporary task files only on D:; remove exact temporary material after review;
  preserve user data.
- Remotion and HyperFrames may be deferred and are not R3 prerequisites.
- No second Agent, MCP, router, or generic framework.

## Repository closeout result

Owner authorization dated 2026-08-27 covered:

- shrink and align the current authority, entry, contract, and work-log documents;
- verify the existing R2 changes;
- perform one independent read-only result review;
- commit/push the reviewed candidate and ordinary-fast-forward the formal ref;
- delete only precisely verified abandoned branches, closed worktrees, and task
  directories with no unique or unmerged work;
- create a clean follow-up Codex task for later planning.

The repository candidate passed its one independent read-only review:
`APPROVE / P0=0 / P1=0 / P2=0`. Focused verification passed with
`56 passed, 1 skipped`; `git diff --check --` passed. This repository result is
complete only when the commit containing this register is the exact formal ref by
ordinary fast-forward. External closeout then only removes precisely verified
abandoned task objects and opens the clean follow-up Codex task. That completed
closeout did not authorize R3, WorkBuddy, media, or a Package rebuild. The later
R3 result and current stability-candidate authorization are recorded above.

## Delivery state fields

```text
formal_ref: refs/heads/codex/workbuddy-shell-v2
result_1: COMPLETE
result_2: COMPLETE / REAL_WORKBUDDY_NATURAL_LANGUAGE_RESULT_AND_RECEIPT_OBSERVED
result_3: COMPLETE / REAL_PLAYABLE_VIDEO / REVIEW_PASS
result_4: REVIEW_APPROVED / COMMIT_PENDING
current_task: R4_COMMIT_FAST_FORWARD_PUSH
baseline_skill: USABLE / RETAINED / SHA256_E7ECFD69A22B2F601215860A83F849584C50F29328C011622A42FDD2E63D4BAB
candidate_skill: V4_INSTALLED / RETAINED_WITH_KNOWN_WORKSPACE_MEMORY_LIMIT
workbuddy_or_media_in_current_task: FORBIDDEN
closeout_review: APPROVE / P0=0 / P1=0 / P2=0
r4_review: APPROVE / P0=0 / P1=0 / P2=0
formal_delivery: COMPLETE_WHEN_THIS_REGISTER_COMMIT_IS_EXACT_FORMAL_REF
```
