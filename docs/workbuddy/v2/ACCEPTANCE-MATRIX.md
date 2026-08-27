# WorkBuddy Shell V2 — Acceptance Matrix

Acceptance is product-result specific. A technical state is relevant only when it
prevents the stated user-visible result. WorkBuddy's internal harness behavior is
not a user failure.

| Result | Ordinary-user goal | Minimum observable evidence | Current state |
|---|---|---|---|
| R1 | Install the Shell product and complete its lifecycle without losing user data. | Final release identity; installation, Registration, Activation, Uninstallation, Reinstallation, and data-protection evidence. | `COMPLETE` |
| R2 | Type a natural-language request containing `金钥匙智能体` and start a real WorkBuddy business interaction. | WorkBuddy 5.3.14 / Hy3; the single Skill and Shell actually invoked; concrete business reply; checkable LauncherReceipt. | `COMPLETE` |
| R3 | Continue the same ordinary-user path to a real Golden Key production result. | One natural-language entry; real WorkBuddy execution; real playable video; checkable receipt and result location; no manual technical workaround. | `NEXT / NOT_STARTED` |
| R4 | Use the result as an ordinary user and close the product formally. | Ordinary-user acceptance record and formal repository/project closeout. | `NOT_STARTED` |

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

## R3 boundary

The only wake condition remains the original-message substring `金钥匙智能体`.
Do not replace it with one fixed full prompt. Candidate materials are:

- `D:\BlazingCD\Personal\测试素材\头头象花浴头疗素材\店内环境`
- `D:\BlazingCD\Personal\Golden Key Digital Human\resources\assets\default\_bgm`

They may be supplied by the ordinary user in a natural-language request. Their
presence is not a new technical protocol.

R3 fails only when a required user-visible condition is absent: the user must
operate technical commands/paths/schema/env, the Skill/Shell is not actually
called, no real playable video or checkable receipt exists, or Shell becomes a
second Agent/production decision-maker. WorkBuddy may choose internal commands,
tools, retries, and corrections.

## Review rule

One executor and one independent result reviewer per result. Review occurs after a
real user-visible result. The reviewer first tests the row's ordinary-user goal;
it may not import a different result's artifact requirement or invent a technical
architecture gate. It must not compare the run with an evaluator-invented
transcript, step sequence, or imagined intermediate output. No packet, pre-review,
multi-round review, or cleanup-review system is part of this matrix.
