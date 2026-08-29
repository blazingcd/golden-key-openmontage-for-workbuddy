# WorkBuddy Shell V2 — Current Project State

Date: 2026-08-29

The live authority is `docs/workbuddy/v2/TASK-REGISTER.md`. This file is a compact
state snapshot, not a second task ledger.

## Product

An ordinary user writes a natural-language request in WorkBuddy containing
`金钥匙智能体`. WorkBuddy is the only Agent and production decision-maker. The
OpenMontage Package supplies production semantics. Shell V2 supplies installation,
lifecycle, Registration/Locator, runtime preparation, fixed mechanical invocation,
WorkBuddy entry, and status/receipt relay. Shell is never a second control plane.

WorkBuddy is a harness Agent: the same input may yield different internal thoughts,
tool paths, steps, wording, and intermediate conclusions. Skills and prompts must
not force a preset internal script. Acceptance follows the user's observed result;
process variation is acceptable unless it causes product failure, technical burden,
a second control plane, or a false result.

Future WorkBuddy executions prefer any available `0.00x` model row. Waiting may
switch among `0.00x` rows. A positive multiplier is allowed only when every
`0.00x` row is unavailable, and is selected from the smallest upward. Record the
chosen row and, for any non-`0.00x` choice, the unavailable `0.00x` evidence.

## Four results

| Result | Current state | Evidence / next boundary |
|---|---|---|
| 1. Installable Shell | `COMPLETE` | Commit `869358810ee41a0a61d10cec10c1b3b93c2c3450`; tree `3a623cb1eab9fee0d90854c0df271450f9779b9a`; Release SHA256 `7e5585298e50a5c5713ecd8fc4df57cfb6e88381b39453364cec62fdea1c6280`. Lifecycle and data protection passed. |
| 2. WorkBuddy natural-language result | `COMPLETE` | WorkBuddy `5.3.14` / Hy3; exact ordinary request ran through the single Skill and Shell and returned a concrete business reply plus LauncherReceipt. |
| 3. Playable Golden Key video | `COMPLETE` | WorkBuddy 5.3.14 / `Hy3 0.00x` displayed and played a real 46.6-second MP4; independent review `PASS / P0=0 / P1=0 / P2=0`. |
| 4. Formal closeout | `COMPLETE` | Frozen 11-path candidate passed `APPROVE / P0=0 / P1=0 / P2=0`; reviewed commit `70cf63be51774de9151fb0fee24cf78591ff1993` was fast-forwarded and pushed, followed only by the Owner-authorized completion record. |

Result 2 evidence: Skill ZIP SHA256
`c96ec03522b744e8771eb16f22f5521102c4007af50ccb27d895efb82b1fe3a6`; evidence
root `D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\evidence\product2-workbuddy-user-flow-20260826`.
The receipt's `INCOMPLETE / RESULT_POINTER_INVALID` means no video file was made
in that run. It is a Result 3 artifact condition, not a Result 2 failure.

## Repository state

The completed historical delivery target is
`refs/heads/codex/workbuddy-shell-v2` at
`aa9cabfa0d4f75d93e22317466709b6bad3bc3b4`. It is retained unchanged as the
R1-R4 baseline. The authorized next-phase documentation branch is
`refs/heads/codex/workbuddy-capability-onboarding`, created from that exact commit.
That branch creation record alone authorized no implementation. The later exact
two-file implementation authorization is recorded below; it still excludes a
WorkBuddy run, media production, and capability installation.

## Current task

At preparation start, planning local/tracking/advertised refs were
`e0aab40b4500e70d63b058df2d9731415e30fe0d`. The retained implementation branch
was clean at local `fd0a3f8cac41540ff25a3dd113828c7a5f39f7a6`, two commits ahead
of tracking/advertised `33f49fb385b103489772d3f8ce2f7cb2486b08dc`. Historical
baseline local/remote remains
`aa9cabfa0d4f75d93e22317466709b6bad3bc3b4`.

The immutable final PackageRoot is already registered and active at
`D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\m1.2-final-factual-relay-33f49fb-20260829\PackageRoot`;
its `fixed_child.py` SHA256 is
`66defdd34ea984b4b2ccf6d79753f90bf1c45f4b387f226552035c4e2ae136bf`.
Do not rebuild, reregister, or reactivate it.

The authorized next chain stops before WorkBuddy: one six-document correction,
zero-write review, commit, and planning push; ordinary merge into the retained M1
branch; one minimal `SKILL.md` consumer instruction; one newly named uninstalled
Skill ZIP bound to the active PackageRoot; zero-write candidate review; one
implementation commit and ordinary push. Installing/replacing the Skill or
operating WorkBuddy needs fresh action-time Owner authorization.

The uninstalled candidate is now built at
`D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\Integrations\WorkBuddy\golden-key-openmontage-0.3.25-m1.2-handoff-consumer-33f49fb.zip`,
SHA256 `437b02c60aa234197fb419275ac64c5df804c5f477fdba16fde3278f772e68d2`.
Its independent zero-write review passed `APPROVE / P0=0 / P1=0 / P2=0`; the
single Skill source commit is `c8eeb91e221ec96a406543c183091eea7ea6ac3c`.
The installed single Golden Key Skill remains byte-identical and no WorkBuddy
action has been taken.

The probe passes only when the ordinary dialogue visibly explains the continuing
FFmpeg basic path, gives honest Remotion/HyperFrames/external-video/TTS and
Package-declared Provider states, offers continue/local/API-key/defer, and honors
the deferred non-mutating boundary. Optional installation, chat secrets,
Provider/connection calls, media, M1.3, Shell fallback, retry, source repair,
workspace relay files or managed-summary copies, old-root edits, and
historical-asset overwrite remain
forbidden. Failure is terminal `NOT_PROVED`, not a repair loop.

The rejected v2 candidate ZIP SHA256 is
`bd35b98087cd7a03f909dc17bbd6048388a7c46e2251c3893a3f9f056d653249`.
The preserved baseline ZIP and byte-identical `r3-pass-baseline` copy still have
SHA256 `e7ecfd69a22b2f601215860a83f849584c50f29328c011622a42fdd2e63d4bab`.
The v3 candidate built afresh from that baseline has ZIP SHA256
`aa421dfbb00111392d37da6f6590e456b534a79e308560b441b4afd5d7b044a2`. Its only
WorkBuddy `5.3.14` / `Hy3 0.00x` comparison produced a managed first-call
`EXITED_SUCCESS` receipt with a valid result pointer, one spawn, and no retry.
WorkBuddy created a valid 37-second 1920x1080 H.264/AAC MP4 at
`C:\Users\blazi\WorkBuddy\2026-08-28-13-33-53\头头象花浴头疗_新店开业宣传.mp4`,
but planned an unrequested workspace-memory update and another user Skill before
the final reply. The task was stopped. Final UI state is `用户已取消` with no
artifact card or final path; independent result review is `TODO`. An empty new
workspace-memory file remains, no extra user Skill was created, and v3 was the
only installed Golden Key Skill at that historical comparison point.

Fresh Owner authorization permits a separately named `delivery-v4` candidate
derived from v3 while preserving the R3 baseline and v3 archives. V4 changes only
the WorkBuddy result-delivery stop boundary and retains the proven v3 receipt
relay. Its built ZIP SHA256 is
`d838cba0735d7a2df3d81029a7d7469551a28219d91f0e8ea2fe08b0f152845d`.
Focused checks passed and the one independent zero-write candidate review returned
`APPROVE / P0=0 / P1=0 / P2=0`.

The one action-time-authorized WorkBuddy `5.3.14` / `Hy3 0.00x` comparison is
complete. The first call returned `EXITED_SUCCESS`, a valid result pointer, one
spawn, and no retry. WorkBuddy gave a final answer and attached the 9.6 MB MP4 at
`D:\BlazingCD\Personal\测试素材\头头象花浴头疗素材\成片\头头象花浴头疗_新店开业宣传.mp4`.
The independent result review is `TODO / P0=0 / P1=1 / P2=0` because the closing
title is clipped. V4 is not accepted as the stability solution: WorkBuddy wrote
an optional 978-byte workspace memory before the final answer. No extra user
Skill was created. The Owner retains v4 for its improved first-call and
final-delivery mechanics; the clipped output from one harness run is not treated
as a Skill regression. The preserved R3 baseline remains rollback evidence.
Historical Result 3 and the formal Result 4 closeout are complete under the frozen
plan in the Task Register.

## Next-phase planning

M0 freezes the complete next-phase master roadmap and the execution contract for
the first Must task on `codex/workbuddy-capability-onboarding`. It records the
evidence gap, dependency order, read-only route boundary, user-visible acceptance,
anti-inflation stops, review method, and the gate that requires the Owner to
confirm both the implementation branch name and exact write allowlist after the
route audit. At the M0 freeze, no implementation branch existed; the later M1
branch history is recorded below.
The initial capability-onboarding contract remains preserved at
`4c0cbd3447546c3dcc0079f2392a3b43e7542e69`; the later Owner authorization adds
one documentation-only master-roadmap amendment without rewriting that commit.

`R1` through `R4` remain frozen historical result identifiers; no future task uses
the R series. M1–M3 are Must tasks, S1–S5 are Should tasks, and C1–C2 are Could
tasks. M1.1–M1.4 are steps within M1, not M0 subtasks.

The next product path begins with capability readiness, not a claim that
OpenMontage becomes incapable when an enhancement is absent. FFmpeg is the basic
production baseline. WorkBuddy performs a light first-use inventory, tells the
ordinary user that basic production is ready when FFmpeg is ready, and presents
relevant optional enhancements such as Remotion, HyperFrames, external video
generation, and TTS as choices that may be configured now or later.

M1 now derives its visible Provider set from the verified Package's formal
declarations. Current static evidence includes Seedance, Kling, and MiniMax;
Seedance is the current default recommendation. Undeclared Providers do not appear
in the M1 user experience or acceptance scope. This snapshot is not a Shell
routing table and does not prove credentials, account permission,
balance, connectivity, regional availability, or live model availability.

The configuration journey has two required mechanisms. Local capabilities such
as Remotion and HyperFrames require approved download, managed installation,
rediscovery, Package recognition, and actual Package-mediated invocation. API-key
Providers require a secret-safe input/store path outside ordinary chat, exact
Package allowlisting, non-disclosing relay, and an authorized connection test.
M1.3 must obtain one representative result for each mechanism.

WorkBuddy remains the only conversation and decision owner. It may use its own
current capabilities and the verified Package semantics to decide what is
relevant, explain cost/privacy/credentials, obtain consent, and recover from a
failed optional configuration. Shell runtime preparation remains bounded
mechanical detection and exactly approved integration. Later requests containing
`金钥匙智能体` may inspect, configure, change, or retest the same capabilities:
natural language remains the entry and intent carrier, while WorkBuddy may use a
bounded guided sequence when secure input or reliable installation requires it.
That sequence must not make the user operate internal commands or technical details.

Planned dependency: M1.1 fact audit then M1.2 first-use readiness; M2 may start
after M1.2. M1.3 is still a required product capability with representative local
installation and API-key paths, but a particular user may defer configuration
until M2 establishes relevance or continue on FFmpeg without using an enhancement.
M3 starts only after M1.4 and M2 are complete. S1–S4 then cover revision/version/rollback,
one additional platform/aspect, export/share/reuse, and cross-machine lifecycle.
S5 qualifies only an enhancement selected for a real user goal. C1 broad
Provider/model coverage beyond the verified Package's formal declarations and C2
automatic routing/direct publishing remain deferred. Implementation and real-user
acceptance require separate Owner authorization.

Owner authorization dated 2026-08-29 permits only this six-document Provider-scope
correction, one independent zero-write document review, one commit, and one
ordinary push on `codex/workbuddy-capability-onboarding`. It does not authorize
M1.2/M1.3 implementation or any Package, test, WorkBuddy, installation,
credential, Provider-call, or media action.

The Owner's later 2026-08-29 direction authorizes one documentation-only M1.2
execution-contract freeze under the same six-document, one-review, one-commit,
ordinary-push boundary. The future implementation branch name is
`codex/workbuddy-m1-capability-onboarding`; one branch serves M1.2–M1.4 instead
of creating a branch per subtask. This task does not create it or authorize
implementation, tests, WorkBuddy, installation, credentials, Provider calls,
Package changes, or media.

The same Owner direction requires M1 cleanup to be part of completion. After the
reviewed M1.4 result, the M1 head first ordinary-fast-forwards and pushes
`codex/workbuddy-capability-onboarding`. Only after exact refs, clean worktrees,
and absence of unique/unmerged work are verified may the recorded implementation
worktree, local/remote temporary branch, and exact task-owned temporary directories
be removed. Dirty or unrecorded targets, user data, divergence, or a force
requirement stop cleanup as `CLEANUP_BLOCKED`. M1 cannot be `COMPLETE` before the
post-cleanup absence and retained-baseline checks pass.

The Owner accepted the failed probe and authorized a separate zero-write Shell
factual-relay audit. That audit is complete with
`PROPOSE_BOUNDED_SHELL_FACTUAL_RELAY`: the Package already exposes the compact
facts, and the existing validated `fixed-child-handoff` is the smallest reusable
carrier. No implementation or test occurred in the audit.

The Owner now authorizes this six-document status/contract update, one independent
zero-write document review, one commit, and one ordinary planning-branch push,
followed without another approval pause by the exact two-file implementation in
the retained M1 branch. Only `golden_key_openmontage_workbuddy/fixed_child.py`
and `tests/workbuddy/test_installer.py` may change. Only the focused direct test,
text/scope checks, one independent zero-write implementation review, one commit,
and one ordinary implementation-branch push are authorized. WorkBuddy, Skill
installation/build, optional installation, credentials, Provider calls, media,
M1.3, extra source files, new protocols, and cleanup remain unauthorized.

Natural-language interaction examples remain planning hypotheses. Real WorkBuddy
evidence may require different wording, tools, or a bounded fixed confirmation
sequence. That variation is acceptable when the ordinary user can still start and
complete configuration without internal technical work and all safety boundaries
remain intact.

### M1.1 accepted fact audit

The Owner accepted the M1.1 factual conclusion. Locator revalidated the registered
PackageRoot and FFmpeg baseline. The Shell already contains bounded Remotion/
HyperFrames preparation, but no production caller uses it; `user_entry` sends an
empty local-capability evidence list, and the verified Package tool definition
declares no required local capabilities or Provider/secret allowlist. Later static
inspection found direct Package routes for Seedance, Kling, and MiniMax. Current
WorkBuddy tools, actual optional-capability
readiness, video/TTS Provider accounts, prices, credentials, balances,
connectivity, regional/model availability, first-use dialogue, natural-language
re-entry, and recovery remain `NOT_VERIFIED`.

M1.1 is `FACT_AUDIT_COMPLETE / OWNER_ACCEPTED / ZERO_WRITE_DEVIATION_RECORDED`.
The deviation is that its independent sub-audit created and removed the exact
temporary file `D:\DevCache\Temp\m11-rg.txt`; the repository stayed clean and the
path was confirmed absent at closeout.

M1.2 is `VERIFIED_LOCAL_FACTUAL_RELAY_CONTRACT /
CONSUMER_CANDIDATE_PREPARATION_AUTHORIZED / WORKBUDDY_ACTION_NOT_AUTHORIZED /
M1_3_BLOCKED`. The contract at
`f11e7118e2f652b6e0ceb31b1bc88e617dcf8174` incorrectly combined an authoritative
inventory requirement with a Skill-only write allowlist, despite the accepted
M1.1 facts that local evidence was empty, optional preparation had no production
caller, and WorkBuddy's required discovery ability was unverified. Its tests could
not prove the missing fact flow.

The implementation branch completed the exact two-file factual relay and is clean;
its pushed relay ceiling is
`33f49fb385b103489772d3f8ce2f7cb2486b08dc`. Its current local head is
`fd0a3f8cac41540ff25a3dd113828c7a5f39f7a6`; tracking/advertised remain
`33f49fb...`. The installed Skill remains the only Golden Key Skill and must not
be replaced before fresh action-time authorization.

The single bounded probe verified PackageRoot/Guide and reached attempts to call
`provider_menu_summary()`, but no capability facts reached the ordinary-user
dialogue. The required FFmpeg explanation, honest optional states, and four
choices were absent. WorkBuddy instead created
`C:\Users\blazi\WorkBuddy\2026-08-29-16-27-10` and a zero-byte
`gk_menu_summary.json`, then queued another file write; the task was cancelled.
The file and exact task directory
`D:\DevCache\Temp\workbuddy-m12-readiness-probe-3ab9` were removed under Owner authorization, but
the now-empty C: directory remains `CLEANUP_BLOCKED_IN_USE` because WorkBuddy
holds it open. Do not force-delete it.

The zero-write audit confirmed the minimum route: read the verified Package's
`provider_menu_summary()` at the fixed-child boundary and place the bounded raw
facts inside the existing handoff/receipt carrier. Shell must not interpret,
recommend, sort, or select; WorkBuddy remains the explanation, relevance,
Provider/model, consent, and recovery owner. The authorized implementation may
prove only that local carrier contract. M1.3 remains blocked until a later real
WorkBuddy result completes M1.2.

A later attempt created only the normal empty WorkBuddy task directory
`C:\Users\blazi\WorkBuddy\2026-08-29-19-32-28` and was cancelled immediately.
The latest LauncherReceipt remained the older 16:28 receipt for
`product2-result-pointer-fix-install-20260827\PackageRoot` and old
`fixed_child.py` SHA256 `3a1f9c...`; the new relay was not invoked. The attempt is
`NOT_PROVED_PREMATURE_HARD_STOP / NEW_SKILL_NOT_INVOKED`. Empty workspace creation
alone is allowed; copying the managed summary there or creating a relay file is
not. The empty directory is preserved as evidence.

## Non-goals

Do not preserve old route plans, packet/pre-review systems, extra Agents, MCP/
routers, Shell-side renderer/Provider selection, or generic framework work. The
planned WorkBuddy capability inventory and optional configuration entry do not
authorize Shell production decisions or implementation. Git history remains the
place for provenance.
