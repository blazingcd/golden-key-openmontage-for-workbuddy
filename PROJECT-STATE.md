# Project State

更新时间：2026-08-17

## 当前状态

```text
product: WorkBuddy Shell V2
formal_branch: origin/codex/workbuddy-shell-v2
formal_baseline: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
stage_1: PASS_ACCEPTED
stage_2: PASS_ACCEPTED
repository_hygiene: PASS_ACCEPTED
repository_tracked_files: 33
stage_3_planning: GRANTED
stage_3_implementation: NOT_GRANTED
stage_4_launcher: NOT_GRANTED
stage_5_workbuddy_entry: NOT_GRANTED
stage_6_status_result_relay: NOT_GRANTED
current_task: V2-S3-S6-SCOPE-DOCS1
current_task_status: REVIEW_READY
current_result: THIS_COMMIT
next: V2-S3-S6-SCOPE-DOCS-REVIEW1
```

WorkBuddy负责用户对话，外部已验证执行包中的OpenMontage Agent负责生产，Shell只负责六模块。阶段3至阶段6的缩减范围已经写入现有章程、处置表、验收矩阵和防漂移规则，等待独立只读Reviewer；这不是任何实现授权。

## 已接受对象

- 阶段1已审对象：`041c6600dc8eb9094b5c93cb4a4ed088894578af`；正式集成边界：`fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9`。
- 阶段2最终实现：`ab1eddf474233859c6a3b32056a503f82ecdc117`；正式集成：`ca6e93b7da108732f2034239da340a986ba3da3a`。
- 仓库卫生最终树：`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`；tracked精确33并受固定白名单保护。
- 阶段2只证明Package Registration与Locator，不证明或授权Installer、Runtime、Launcher、真实WorkBuddy、Provider、SaaS或媒体E2E。

## 阶段3至阶段6最小链路

```text
LocatorResult
-> Runtime readiness or one authorized missing component
-> one controlled Agent process
-> one explicit WorkBuddy entry
-> unchanged exit facts and result pointer
```

- 阶段3没有真实额外Runtime缺口时以`STAGE_3_NO_ADDITIONAL_RUNTIME_REQUIRED`零代码结束。
- 阶段4只允许一次受控进程启动，不接受任意Shell、不自动重试、不进入Agent业务内部。
- 阶段5只允许一种真实WorkBuddy显式入口，用户原话与执行控制严格分离。
- 阶段6优先直接复用Launcher回执；无需独立转换时以`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`零代码结束。

详细实时字段只以`docs/workbuddy/v2/TASK-REGISTER.md`为准；Git历史中的Wave A/B/C记录不是当前任务授权。
