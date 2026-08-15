# WorkBuddy Shell V2 权威入口

状态：

```text
STAGE_1_PASS_ACCEPTED
STAGE_2_PASS_ACCEPTED
STAGE_3_PLANNING_GRANTED
STAGE_3_IMPLEMENTATION_NOT_GRANTED
```

本仓库只实现WorkBuddy Shell V2。WorkBuddy负责用户对话，外部已验证执行包中的OpenMontage Agent负责生产，Shell只负责六模块。当前仓库卫生清理不是阶段3实现。

## 权威文档

- `TASK-REGISTER.md`：实时任务、精确Git对象、授权与下一任务的唯一状态权威。
- `PROJECT-CHARTER.md`：产品角色、六模块职责和非目标。
- `PACKAGE-REGISTRATION-CONTRACT.md`：阶段2已接受的Package Registration与Locator稳定合同。
- `ACCEPTANCE-MATRIX.md`：证据与Gate语义。
- `DRIFT-GUARD.md`：停止条件、范围保护和Git生命周期。
- `MODULE-DISPOSITION.md`：V1能力处置的历史映射，不是当前实现授权。

## Git任务生命周期

- Builder分支只是一项任务的临时隔离，不是长期交付分支。
- Reviewer必须独立且只读；Reviewer无需建立长期分支。
- 用户接受或Reviewer批准不等于已经交付到仓库正式主线。
- 任务或阶段只有在已审结果进入`origin/codex/workbuddy-shell-v2`后，才算仓库完成。
- 正式主线只允许fast-forward到已审集成结果；不得把推进中的`main`或旧长期分支merge/rebase回来。
- 推广后，所有已完全合入且无未合入commit的临时远端分支必须删除。
- 本地分支仅在对应worktree关闭后安全删除。
- 下一阶段接管只能使用正式主线最新精确commit，不能使用任务分支。

当前状态与下一步不得从Git历史、旧Prompt、旧任务包或聊天推断；只读`TASK-REGISTER.md`。
