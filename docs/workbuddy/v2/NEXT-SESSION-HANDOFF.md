# WorkBuddy Shell V2 新统筹会话交接

状态：`HANDOFF_READY / STAGE_1_READY_NOT_STARTED`

更新时间：2026-08-15

## 1. 交接目的

当前对话只负责把治理、阶段1任务和接管Prompt固化到仓库。后续执行统筹必须在新的Codex会话中进行，避免继续依赖当前长对话的上下文。

新会话是统筹者，不亲自执行Builder或Reviewer工作。它负责核验对象、派发任务、跟踪状态、组织独立审阅、集成已批准文档和提交用户Gate。

## 2. 当前项目身份

```text
project_path: D:\BlazingCD\Personal\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2
branch: codex/workbuddy-shell-v2
immutable_code_baseline: 2a2bf09832d558388dc2816c54b32a2dce4aa607
governance_review_gate: PASS_ACCEPTED
stage_1: READY_NOT_STARTED
stage_1_start_authorization: GRANTED_FOR_NEXT_SESSION_AFTER_TAKEOVER_GATES
```

精确`EXPECTED_HANDOFF_COMMIT`由当前对话完成本文件提交并推送后，在用户复制的新会话Prompt中提供。新会话必须核验本地HEAD、远端分支和该40位commit三者一致。

## 3. 新会话必读顺序

1. 根`AGENTS.md`；
2. 根`AGENT_GUIDE.md`；
3. 本文件；
4. `docs/workbuddy/v2/README.md`；
5. `docs/workbuddy/v2/TASK-REGISTER.md`；
6. `docs/workbuddy/v2/STAGE-1-TASK-PACKETS.md`；
7. `docs/workbuddy/v2/STAGE-1-EXECUTION-PLAN.md`；
8. `docs/workbuddy/v2/PROJECT-CHARTER.md`；
9. `docs/workbuddy/v2/DRIFT-GUARD.md`；
10. `docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`；
11. `PROJECT-STATE.md`和`WORK-LOG.md`的最新Shell V2段落。

上述文档足以接管。此前多个Codex审阅任务只作历史证据；除非当前文档出现无法解释的矛盾，新会话不要重读或重审那些旧任务。

## 4. 用户授权边界

用户已经授权：

- 在新会话完成接管核验后启动阶段1统筹；
- 创建`V2-S1-BUILDER1`独立文档Builder任务；
- Builder完成后创建`V2-S1-T6`独立只读Reviewer任务；
- 在每个任务完成时更新权威账本和日志。

用户没有授权：

- 修改生产代码、Skill、安装器、测试、配置、lock或Core；
- 运行测试、安装、真实WorkBuddy、Provider或媒体生成；
- 启动或细化阶段2；
- merge/rebase `main`或旧长期分支；
- 改变WorkBuddy/Core/Shell最高职责原则。

## 5. 新会话第一轮必须完成

1. 只读核验项目、分支、HEAD、远端、clean状态和祖先关系；
2. 用不超过10行向用户报告接管结果、阶段1边界和唯一下一任务；
3. 若核验通过，直接创建`V2-S1-BUILDER1`，不再要求用户重复批准阶段1；
4. Builder Prompt必须引用`EXPECTED_HANDOFF_COMMIT`和`STAGE-1-TASK-PACKETS.md`；
5. Builder只完成T1至T5，使用独立worktree/任务分支，最多推进到`REVIEW_READY`；
6. 统筹等待并核验Builder结果，然后再创建T6 Reviewer；不得提前创建Reviewer。

## 6. 接管失败处理

如果项目、分支、commit、远端、工作树或治理状态不一致：

- 不创建Builder；
- 返回`INCOMPLETE_CONTEXT_MISMATCH`；
- 列出期望值、实际值和最小恢复动作；
- 不删除、重置、stash、merge或rebase任何现场。

## 7. Prompt使用说明

当前对话最终回复会提供一份包含精确`EXPECTED_HANDOFF_COMMIT`的完整Prompt。用户应在本Shell V2项目中新建Codex任务并原样粘贴。不要把Prompt发到旧项目或旧长期分支。
