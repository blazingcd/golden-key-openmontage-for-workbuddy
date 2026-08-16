# WorkBuddy Shell V2 任务账本

状态：`ACTIVE AUTHORITY / V2_REPO_HYGIENE_REMAINING_SEQUENCE_REVIEW_READY`

更新时间：2026-08-16

## 当前任务

```text
task_id: V2-REPO-HYGIENE-SEQUENCE-AUTHORITY-FIX1
task_status: REVIEW_READY
authority_id: V2-REPO-HYGIENE-REMAINING-SEQUENCE
authority_commit: THIS_COMMIT
authority_lifetime: ONE_TIME_BOUNDED
pre_activation_status: REVIEW_READY
activation_condition: origin/codex/workbuddy-shell-v2 == THIS_COMMIT AND independent_reviewer == APPROVE
post_activation_status: ACTIVE_SEQUENCE_AUTHORITY
start_commit: 385a20bbff9624703682eecba3b38fc3c6d2d6b9
result_commit: THIS_COMMIT
branch: codex/v2-repo-hygiene-sequence-authority-fix1
review_range: 385a20bbff9624703682eecba3b38fc3c6d2d6b9..THIS_COMMIT
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_at_start: 385a20bbff9624703682eecba3b38fc3c6d2d6b9
completed_wave_a_status: PASS_PROMOTED
completed_wave_a_result: 830d44ab7b910e20bfc9093bf2c505850860880a
completed_wave_a_reviewer: 01a0065c-d83a-78d3-a36e-8386c08036ed / APPROVE
completed_wave_a_promotion: 01a00932-5403-7880-8214-680eebcda050 / PASS
completed_wave_a_closeout: 385a20bbff9624703682eecba3b38fc3c6d2d6b9
completed_wave_a_closeout_reviewer: 01a00940-fe94-7883-bcc0-e7d396b56a3a / APPROVE
completed_wave_a_closeout_promotion: 01a00943-8a3e-7b81-a2d8-03f192fed82e / PASS
tracked_at_sequence_start: 2160
authorized_sequence:
  1. V2-REPO-HYGIENE-WAVE-B-BUILDER1
  2. V2-REPO-HYGIENE-WAVE-B-REVIEW1
  3. V2-REPO-HYGIENE-WAVE-B-PROMOTE1
  4. V2-REPO-HYGIENE-WAVE-C-BUILDER1
  5. V2-REPO-HYGIENE-WAVE-C-REVIEW1
  6. V2-REPO-HYGIENE-WAVE-C-PROMOTE1
  7. V2-REPO-HYGIENE-MAIN-WORKTREE-NORMALIZE1
  8. V2-REPO-HYGIENE-FINAL-AUDIT1
  9. V2-REPO-HYGIENE-FINAL-GATE
sequence_rule: 必须按authorized_sequence的编号严格顺序执行，不得跳过或并行越级。
failure_rule: 任一步非PASS/APPROVE则停止，仅允许最小FIX+复审；不得跳到后续。
branch_rule: Builder使用临时分支；Reviewer只读；正式主线只允许fast-forward；推广后删除已完全合入且无未合入commit的远端临时分支；本地临时分支等待对应worktree关闭后再删除。
wave_b_contract: start=本authority激活后的正式主线；change_shape=D54/A2/M2；tracked=2108；tests=registration+TRANSITION。
wave_c_contract: start=Wave B已推广后的正式主线；change_shape=D2075/M1；tracked=33；tests=registration+FINAL。
final_gate: 正式主线、远端和D盘工作区一致；exact_tracked=33；tests=PASS；远端临时分支已清理；Stage3实现=NOT_GRANTED。
stage3_planning: GRANTED
stage3_implementation: NOT_GRANTED
stage3_all_modules: NOT_GRANTED
dynamic_path_or_test_relaxation: NOT_GRANTED
production_code_changes: 0
test_changes: 0
```

本次只建立一次性、有界、条件激活的剩余仓库卫生序列权威，不实施Wave B、Wave C或Stage3。`THIS_COMMIT`表示本记录与本次结果在同一个不可变提交中；Reviewer必须用结果分支的精确40位SHA解析该语义占位符并只读审阅。只有独立Reviewer给出`APPROVE`且同一结果被fast-forward推广至正式主线后，上述序列才从`REVIEW_READY`自动成为`ACTIVE_SEQUENCE_AUTHORITY`，无需再提交自引用closeout。该序列不得授权任何Stage3实现，也不得根据当时的工作树动态放宽已列明的路径、数量或测试合同。

## 阶段状态

```text
stage_1_status: PASS_ACCEPTED
stage_2_status: PASS_ACCEPTED
stage_3_planning_authorization: GRANTED
stage_3_implementation_authorization: NOT_GRANTED
stage_3_launcher_authorization: NOT_GRANTED
stage_3_workbuddy_entry_authorization: NOT_GRANTED
stage_3_status_result_handoff_authorization: NOT_GRANTED
stage_3_other_module_authorization: NOT_GRANTED
repository_hygiene_is_stage_3_implementation: NO
```

## 已接受对象与证据边界

```text
immutable_v1_code_baseline: 2a2bf09832d558388dc2816c54b32a2dce4aa607
stage_1_reviewed_commit: 041c6600dc8eb9094b5c93cb4a4ed088894578af
stage_1_integrated_boundary: fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9
stage_1_reviewer_task: 01a004a6-aab1-7992-abe0-6dcbe8490a71
stage_1_reviewer_verdict: APPROVE / P0=0 / P1=0 / P2=0
stage_2_contract_commit: 5dd144e40ff1bf8682c8b43ac9973e40fc0be946
stage_2_final_implementation_commit: ab1eddf474233859c6a3b32056a503f82ecdc117
stage_2_gate_prep_commit: 104fe684c0bae6604c278fcf756579700bd8e1e0
stage_2_integration_commit: ca6e93b7da108732f2034239da340a986ba3da3a
stage_2_final_reviewer_task: 01a005c3-692c-7761-9f11-45e178c0d599
stage_2_final_reviewer_verdict: APPROVE / P0=0 / P1=0 / P2=0
stage_2_integration_reviewer_task: 01a00606-a1d3-7ab3-ab75-8d16efd064fa
stage_2_integration_reviewer_verdict: APPROVE / P0=0 / P1=0 / P2=0
stage_1_stage_2_consolidation_audit: 01a00617-e037-72a3-b1e5-d88b3d0be19f / APPROVE
repository_hygiene_audit: 01a00621-f896-7ce1-865d-7bd581bfef7e / CLEANABLE
repository_hygiene_plan_review2: 01a00617-e037-72a3-b1e5-d88b3d0be19f / APPROVE / P0=0 / P1=0 / P2=0
```

Stage2实现只证明Package Registration与Locator合同及其测试；不证明Installer、Runtime、Launcher、真实WorkBuddy、OpenMontage生产、Provider、SaaS、网络或媒体E2E。

## Wave A不可变边界

```text
package_registration_start_blob: d0676fb6a0ec22135ade8bc1462337ced05beec0
test_package_registration_start_blob: 7f3f0e7cf1a16fbe63ee0bb8669797bc88c78ec6
```

Wave A只删除活动树中的历史Prompt、旧任务文档和旧docs证据，新增无执行历史的登记合同，并最小重写Shell V2治理入口。Git历史仍保留删除内容；仓库内不得建立archive、legacy或quarantine副本。
