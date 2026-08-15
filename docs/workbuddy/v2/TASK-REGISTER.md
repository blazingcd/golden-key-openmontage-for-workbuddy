# WorkBuddy Shell V2 任务账本

状态：`ACTIVE AUTHORITY / V2_REPO_HYGIENE_WAVE_A_REVIEW_READY`

更新时间：2026-08-16

## 当前任务

```text
task_id: V2-REPO-HYGIENE-WAVE-A-BUILDER1
task_status: REVIEW_READY
start_commit: ca6e93b7da108732f2034239da340a986ba3da3a
result_commit: THIS_COMMIT
branch: codex/v2-repo-hygiene-wave-a1
remote: origin/codex/v2-repo-hygiene-wave-a1
review_range: ca6e93b7da108732f2034239da340a986ba3da3a..THIS_COMMIT
next_authorized_task: V2-REPO-HYGIENE-WAVE-A-REVIEW1
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_expected_unchanged: ca6e93b7da108732f2034239da340a986ba3da3a
deleted_tracked_files: 57
added_tracked_files: 1
expected_tracked_files: 2160
modified_files_maximum: 15
production_code_changes: 0
test_changes: 0
tests_run: 0
installer_runs: 0
workbuddy_runs: 0
provider_calls: 0
media_runs: 0
```

`THIS_COMMIT`表示本记录与本次Wave A结果在同一个不可变提交中；提交后的本地和远端分支指针提供精确40位SHA。Reviewer必须以该SHA替换语义占位符后审阅，不得把工作树状态当结果对象。

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
