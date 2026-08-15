# WorkBuddy Shell V2 统筹文档入口

状态：`GOVERNANCE_BASELINE_ACTIVE / STAGE_1_READY_NOT_STARTED`

更新时间：2026-08-15

## 1. 文档用途

本目录是“金钥匙 OpenMontage for WorkBuddy Shell V2”重构项目的权威统筹入口。

项目状态、任务授权、职责边界和 Gate 结论不得依赖聊天记忆。聊天、旧 Prompt、历史报告和 Codex 任务只能作为证据输入；只有本目录的受版本控制文档及其明确引用的 Git 对象可以改变 V2 项目状态。

当前尚未启动阶段1实现。当前唯一允许的下一动作是：用户审阅并接受本套统筹文档后，另行授权 `V2-S1-T0`。

## 2. 权威优先级

发生冲突时按以下顺序 fail closed：

1. `TASK-REGISTER.md`：实时任务状态、依赖、授权和下一任务；
2. `PROJECT-CHARTER.md`：目标、职责、功能范围和架构不变量；
3. `DRIFT-GUARD.md`：停止条件、禁止模式和范围变更程序；
4. 当前阶段的执行计划；阶段1为 `STAGE-1-EXECUTION-PLAN.md`；
5. `ACCEPTANCE-MATRIX.md`：Gate、证据、PASS/FAIL/INCOMPLETE；
6. `PROJECT-STATE.md` 与 `WORK-LOG.md`：仓库级摘要和追加历史；
7. 旧架构、Roadmap、Prompt、handoff和历史审计：仅作证据，不直接授权V2任务。

任何下游文档不得静默覆盖上游文档。发现矛盾时必须停止并登记 `STOPPED_CONTRACT_CONFLICT`。

## 3. 当前固定事实

- 协调仓库：`D:\BlazingCD\Personal\Golden_Key_OpenMontage_for_WorkBuddy`
- 当前长期分支：`codex/w4.1-portable-python`
- V2治理内容提交：`def921a2e29b4858f289c44c3e9183619ba31ce6`
- 已批准的V2代码基线：`2a2bf09832d558388dc2816c54b32a2dce4aa607`
- 计划分支：`codex/workbuddy-shell-v2`
- 计划工作树：`D:\BlazingCD\Personal\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2`
- 上述V2分支和工作树尚未建立。
- 阶段1若从固定代码基线建立工作树，必须显式选择性迁移上述治理内容提交；不得因此改用长期分支推进后的全部HEAD作为代码基线。
- 长期工作区既有未跟踪文件必须原样保护：
  - `.codex/config.toml`
  - `docs/workbuddy/WORKBUDDY-SHELL-V2-REFACTOR-HANDOFF-2026-08-15.md`
- 官方固定对象：`4eab34c5cfcccaa4f1970554928feccce73ee930`
- Golden Key v0.3.23固定Core源码对象：`613d51abe02e0dff5caf83813c275612010a3e6f`
- v0.3.23既有安装候选是`validation_only`，不是正式Release或V2验收通过证明。

## 4. 文档地图

| 文档 | 权威内容 |
|---|---|
| `PROJECT-CHARTER.md` | 项目目标、职责模型、范围和非目标 |
| `DRIFT-GUARD.md` | 防漂移停止规则、禁止实现、范围变更程序 |
| `TASK-REGISTER.md` | 八阶段任务表、todo/done、依赖、授权、结果 |
| `STAGE-1-EXECUTION-PLAN.md` | 阶段1可直接派发的步骤、路径、产物和Gate |
| `ACCEPTANCE-MATRIX.md` | 分层验收、证据边界和状态定义 |

## 5. 历史文档处理

下列文件继续保留，但其v0.3.21、四Pipeline、完整运行时和CLI/MCP生产链描述不能自动进入V2：

- `docs/workbuddy/ARCHITECTURE.md`
- `docs/workbuddy/ROADMAP.md`
- `docs/workbuddy/PACKAGING-DECISION.md`
- `docs/workbuddy/CORE-SYNC-POLICY.md`
- `docs/workbuddy/LOCAL-STORAGE-POLICY.md`
- 两个现有WorkBuddy Skill
- 当前消费层Python实现

阶段1必须逐项裁决为 `KEEP / ADAPT / REWRITE / REMOVE_FROM_V1 / HISTORICAL_ONLY`，不得整分支、整模块或整文档迁移。

## 6. 更新纪律

- 统筹任务负责更新本目录和任务状态，不承担实现任务。
- 执行任务最多把自身状态推进到`REVIEW_READY`，不得自判`PASS_ACCEPTED`。
- 独立Reviewer只给出`APPROVE / REQUEST_CHANGES / INCOMPLETE`。
- Gate只有在证据核验和用户要求的批准完成后才可进入`PASS_ACCEPTED`。
- 每次状态变化必须记录精确commit、允许路径、证据和非证明项。
- 需要长期保留的权威文档必须提交并推送，不能只存在本地或聊天中。
