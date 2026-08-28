# WorkBuddy Shell V2 — Acceptance Matrix

Acceptance is product-result specific. A technical state is relevant only when it
prevents the stated user-visible result. WorkBuddy's internal harness behavior is
not a user failure.

| Result | Ordinary-user goal | Minimum observable evidence | Current state |
|---|---|---|---|
| R1 | Install the Shell product and complete its lifecycle without losing user data. | Final release identity; installation, Registration, Activation, Uninstallation, Reinstallation, and data-protection evidence. | `COMPLETE` |
| R2 | Type a natural-language request containing `金钥匙智能体` and start a real WorkBuddy business interaction. | WorkBuddy 5.3.14 / Hy3; the single Skill and Shell actually invoked; concrete business reply; checkable LauncherReceipt. | `COMPLETE` |
| R3 | Continue the same ordinary-user path to a real Golden Key production result. | One natural-language entry; real WorkBuddy execution; real playable video; checkable receipt and result location; no manual technical workaround. | `COMPLETE` |
| R4 | Close the accepted product formally. | Final authority documents, retained evidence, formal branch state, and explicit closeout record. No new WorkBuddy run. | `COMPLETE` |

## R1 evidence

- Commit `869358810ee41a0a61d10cec10c1b3b93c2c3450`.
- Tree `3a623cb1eab9fee0d90854c0df271450f9779b9a`.
- Release SHA256 `7e5585298e50a5c5713ecd8fc4df57cfb6e88381b39453364cec62fdea1c6280`.

## R2 evidence

- Client/model: WorkBuddy `5.3.14` / `Hy3`.
- User input: `用金钥匙智能体给我做新店开业视频`.
- Skill/Shell: the single `golden-key-openmontage` Skill and Shell were actually
  invoked.
- User-visible result: a concrete business reply and a checkable LauncherReceipt.
- Skill ZIP SHA256:
  `c96ec03522b744e8771eb16f22f5521102c4007af50ccb27d895efb82b1fe3a6`.
- Evidence root:
  `D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\evidence\product2-workbuddy-user-flow-20260826`.

`INCOMPLETE / RESULT_POINTER_INVALID` in that receipt means no video file was
created in the R2 run. It is an R3 artifact condition, not an R2 failure. The raw
review `REJECT / P0=0 / P1=1 / P2=0` is retained as a mismatched review fact; its
P1 applied the R3 file-pointer standard. Owner correction makes R2 complete and
does not require a second review.

## R3 evidence

The only wake condition remains the original-message substring `金钥匙智能体`.
Do not replace it with one fixed full prompt. Candidate materials are:

- `D:\BlazingCD\Personal\测试素材\头头象花浴头疗素材\店内环境`
- `D:\BlazingCD\Personal\Golden Key Digital Human\resources\assets\default\_bgm`

They were supplied naturally in the successful run; they are not a fixed prompt
or technical protocol. WorkBuddy displayed and played
`D:\BlazingCD\Personal\测试素材\头头象花浴头疗素材\成片\头头象花浴头疗_新店开业宣传.mp4`.
The file is a 46.6-second H.264/AAC MP4, and the independent review returned
`PASS / P0=0 / P1=0 / P2=0`.

The R3-passing Skill is retained as the usable rollback baseline. Its first
wrapper invocation did not persist the managed receipt, although WorkBuddy
recovered within the same user task and completed the product result. The current
stability candidate is accepted only if it improves that first-call relay without
adding automatic replay or changing WorkBuddy's production ownership.

The one 2026-08-28 candidate comparison did not satisfy that rule. Its first call
exited before the diagnostic guard because of an invalid PowerShell `Split-Path`
parameter combination, wrote no managed receipt/diagnostic, and WorkBuddy bypassed
the Skill. The later 37.12-second MP4 independently passed the ordinary-user video
goal (`P0/P1/P2=0/0/0`), but the candidate stability verdict remains `FAIL`.
Unrequested workspace-memory and user-Skill writes are also visible negative side
effects, not internal transcript differences.

The Owner subsequently uninstalled both Skills and authorized one new candidate
derived from the preserved R3 baseline. Its acceptance rule is unchanged: one
first-call checkable receipt/diagnostic, no WorkBuddy bypass caused by relay loss,
and no new persistent control plane. Product-result review remains user-visible;
it does not require a predetermined WorkBuddy transcript.

The v3 comparison produced the checkable first-call receipt and a valid local
37-second 1920x1080 H.264/AAC MP4. It still does not pass the ordinary-user result
review: WorkBuddy planned unrequested persistent memory and another user Skill,
the task was stopped, and the final visible state contains neither a completed
answer nor an artifact card. Independent review is `TODO`. This does not revoke
the earlier accepted R3 result; it rejects only the v3 comparison as proof of a
stable user delivery.

The separately named `delivery-v4` candidate retains v3's proven first-call
receipt behavior and changes only the result-delivery boundary. Candidate review
checks that the Skill still leaves production reasoning to WorkBuddy, requires a
real result before any claim, and prevents optional memory or Skill accumulation
from delaying the user's result. Local review does not prove WorkBuddy behavior.
Installation and a real comparison require separate action-time authorization.
The local candidate review is `APPROVE / P0=0 / P1=0 / P2=0`; this approves the
bounded Skill artifact only and does not claim real WorkBuddy behavior.

The separately authorized v4 comparison is now complete in WorkBuddy `5.3.14`
with `Hy3 0.00x`. The first call produced a successful managed receipt, a valid
result pointer, one spawn, and no retry. WorkBuddy gave a final answer and attached
a real H.264/AAC MP4. The independent ordinary-user result review is
`TODO / P0=0 / P1=1 / P2=0` because the closing title is clipped on both sides.
V4 also fails its separate stability goal: it wrote optional workspace memory
after validating the video and before the final answer. No extra user Skill was
created. This comparison does not revoke the earlier accepted R3 result and does
not authorize another run. The Owner retains v4 for its improved first-call and
final-delivery mechanics; the one clipped creative output is not treated as proof
of a Skill regression. R4 reviews the retained state only.

## R4 acceptance

R4 passes only when the six authority/state documents agree, the retained
baseline/v3/v4 identities are verified, the installed state contains only v4,
the existing 11-path change set passes its focused checks and one independent
zero-write review, and the reviewed commit is the exact local and remote formal
ref by ordinary fast-forward. R4 does not require or permit another WorkBuddy run,
video repair, Skill installation, Package rebuild, persistent-side-effect cleanup,
old-route work, or full CI.

The frozen R4 candidate passed its one independent zero-write review with
`APPROVE / P0=0 / P1=0 / P2=0`. Completion required the reviewed commit to be the
exact local and remote formal ref by ordinary fast-forward. Reviewed commit
`70cf63be51774de9151fb0fee24cf78591ff1993` reached both refs; this later
Owner-authorized record changes documentation status only.

## Review rule

One executor and one independent result reviewer per result. Review occurs after a
real user-visible result. The reviewer first tests the row's ordinary-user goal;
it may not import a different result's artifact requirement or invent a technical
architecture gate. It must not compare the run with an evaluator-invented
transcript, step sequence, or imagined intermediate output. No packet, pre-review,
multi-round review, or cleanup-review system is part of this matrix.
