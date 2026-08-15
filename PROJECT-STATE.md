# Project State

更新时间：2026-08-16

## 当前状态

```text
product: WorkBuddy Shell V2
formal_branch: origin/codex/workbuddy-shell-v2
formal_baseline: ca6e93b7da108732f2034239da340a986ba3da3a
stage_1: PASS_ACCEPTED
stage_2: PASS_ACCEPTED
stage_3_planning: GRANTED
stage_3_implementation: NOT_GRANTED
current_task: V2-REPO-HYGIENE-WAVE-A-BUILDER1
current_task_status: REVIEW_READY
current_result: THIS_COMMIT
next: V2-REPO-HYGIENE-WAVE-A-REVIEW1
```

WorkBuddy负责对话，外部已验证执行包中的OpenMontage Agent负责生产，Shell只负责六模块。当前仓库卫生清理不构成阶段3实现。

## 已接受对象

- 阶段1已审对象：`041c6600dc8eb9094b5c93cb4a4ed088894578af`；正式集成边界：`fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9`；生产代码变化0。
- 阶段2最终实现：`ab1eddf474233859c6a3b32056a503f82ecdc117`；正式集成：`ca6e93b7da108732f2034239da340a986ba3da3a`。
- 阶段2只新增`package_registration.py`及其测试；不证明或授权Installer、Runtime、Launcher、WorkBuddy入口、Provider、SaaS或媒体E2E。

## Wave A

- 起点：`ca6e93b7da108732f2034239da340a986ba3da3a`。
- 临时分支：`codex/v2-repo-hygiene-wave-a1`。
- 删除57个历史Prompt、旧任务文档和旧docs证据；新增`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`；结果tracked=2160。
- 最多修改15个既定Shell V2治理入口；生产代码与测试变化均为0。
- 删除内容只从活动树移除，Git历史保留；没有仓库内archive、legacy或quarantine副本。
- `THIS_COMMIT`的精确SHA由提交后的本地/远端临时分支锁定。正式主线仍须保持`ca6e93b7…`，直到独立Reviewer批准并另行推广。

详细实时字段只以`docs/workbuddy/v2/TASK-REGISTER.md`为准。
