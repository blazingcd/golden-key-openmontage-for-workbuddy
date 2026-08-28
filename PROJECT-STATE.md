# WorkBuddy Shell V2 — Current Project State

Date: 2026-08-28

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
No implementation, WorkBuddy run, media production, or capability installation is
authorized by this planning record.

## Current task

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
workspace-memory file remains, no extra user Skill was created, and v3 remains
the only installed Golden Key Skill.

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

The next product path begins with capability readiness, not a claim that
OpenMontage becomes incapable when an enhancement is absent. FFmpeg is the basic
production baseline. WorkBuddy performs a light first-use inventory, tells the
ordinary user that basic production is ready when FFmpeg is ready, and presents
relevant optional enhancements such as Remotion, HyperFrames, external video
generation, and TTS as choices that may be configured now or later.

WorkBuddy remains the only conversation and decision owner. It may use its own
current capabilities and the verified Package semantics to decide what is
relevant, explain cost/privacy/credentials, obtain consent, and recover from a
failed optional configuration. Shell runtime preparation remains bounded
mechanical detection and exactly approved integration. Later natural-language
requests containing `金钥匙智能体` may inspect, configure, change, or retest the
same capabilities without a fixed configuration grammar.

Planned order: capability readiness and configuration entry; progressive business
clarification and material readiness; stable production, preview, and delivery.
Implementation and real-user acceptance require separate Owner authorization.

## Non-goals

Do not preserve old route plans, packet/pre-review systems, extra Agents, MCP/
routers, Shell-side renderer/Provider selection, or generic framework work. The
planned WorkBuddy capability inventory and optional configuration entry do not
authorize Shell production decisions or implementation. Git history remains the
place for provenance.
