# WorkBuddy Shell V2 阶段1执行计划

状态：`READY_NOT_STARTED / START_NOT_AUTHORIZED_AFTER_DOC_REVIEW`

## 1. 阶段目标

阶段1只冻结V2架构、旧模块处置和验收口径，不修改生产代码，不运行测试、安装、WorkBuddy或Provider。

阶段1必须回答：

- Shell究竟负责什么、不负责什么；
- 当前模块哪些保留、适配、重写、退出首版或只作历史；
- V2的对象、会话、运行时和结果边界；
- 后续每个Gate用什么证据，什么不构成证明；
- 哪些问题必须交给Core、Host、Tool或Provider；
- 什么情况下必须停止而不是扩大范围。

## 2. 固定输入

- `immutable_code_baseline`：`2a2bf09832d558388dc2816c54b32a2dce4aa607`。该对象只冻结生产代码谱系，不是阶段1 Builder的checkout目标；
- `stage_1_builder_start_commit`：`PENDING_REVIEW_PASS_AND_COORDINATOR_LOCK`。只有`V2-GOV-REVIEW2`通过后，统筹才可锁定完整40位提交；未锁定不得启动T1；
- V2来源分支：`codex/workbuddy-shell-v2`
- 当前worktree：`D:\BlazingCD\Personal\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2`
- `stage_1_builder_start_commit`上的V2治理文件：`docs/workbuddy/v2/README.md`、`docs/workbuddy/v2/PROJECT-CHARTER.md`、`docs/workbuddy/v2/DRIFT-GUARD.md`、`docs/workbuddy/v2/TASK-REGISTER.md`、`docs/workbuddy/v2/STAGE-1-EXECUTION-PLAN.md`、`docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`、`PROJECT-STATE.md`、`WORK-LOG.md`；
- `immutable_code_baseline`上的仓库权威/历史输入：`AGENT_GUIDE.md`、`PROJECT_CONTEXT.md`、`PROJECT-STATE.md`、`WORK-LOG.md`、`docs/workbuddy/ARCHITECTURE.md`、`docs/workbuddy/ROADMAP.md`、`docs/workbuddy/PACKAGING-DECISION.md`、`docs/workbuddy/CORE-SYNC-POLICY.md`、`docs/workbuddy/LOCAL-STORAGE-POLICY.md`；
- `immutable_code_baseline`上的两个现有Skill：`workbuddy-skill/golden-key-openmontage/SKILL.md`、`workbuddy-skill/golden-key-openmontage-onboarding/SKILL.md`；
- `immutable_code_baseline`上的消费层实现：`golden_key_openmontage_workbuddy/__init__.py`、`golden_key_openmontage_workbuddy/__main__.py`、`golden_key_openmontage_workbuddy/cli.py`、`golden_key_openmontage_workbuddy/doctor.py`、`golden_key_openmontage_workbuddy/gate.py`、`golden_key_openmontage_workbuddy/mcp_server.py`、`golden_key_openmontage_workbuddy/model_config.py`、`golden_key_openmontage_workbuddy/paths.py`、`golden_key_openmontage_workbuddy/runtime.py`、`golden_key_openmontage_workbuddy/runtime_prepare.py`、`golden_key_openmontage_workbuddy/security.py`、`golden_key_openmontage_workbuddy/tasks.py`、`golden_key_openmontage_workbuddy/subprocess_guard/__init__.py`、`golden_key_openmontage_workbuddy/subprocess_guard/offline_guard.cjs`、`golden_key_openmontage_workbuddy/subprocess_guard/sitecustomize.py`；
- 七个既有Codex证据任务：`019ff59e-d36b-7383-bdf9-71249589ef61`、`019ffa29-1818-7262-ad48-2a0962ccdddf`、`019ffb32-afac-7f21-bbfc-e4b0636ead13`、`019fff0e-2e2a-7673-ac18-ab13fe31496b`、`019fff2f-77a9-7f20-9dc1-3afaafbffcda`、`019fff96-ed08-7e31-88e2-55299eb8e943`、`019fff63-4a94-7321-83d9-3566f0d57f0f`；它们只能作为证据，读取时必须核验最终状态；
- 上述七个ID的仓库证据来源：受保护的历史文件`D:\BlazingCD\Personal\Golden_Key_OpenMontage_for_WorkBuddy\docs\workbuddy\WORKBUDDY-SHELL-V2-REFACTOR-HANDOFF-2026-08-15.md`，SHA256=`12D986F12E0DDB118871377144D80BA27D498DCCFC26BF23AE4C1629A880AA63`。该未跟踪文件只读，不得修改、暂存或当作授权；
- 官方对象：路径`D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-audit-4eab34c5`，commit=`4eab34c5cfcccaa4f1970554928feccce73ee930`；
- Golden Key v0.3.23对象：路径`D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-e0-v0.3.23`，commit=`613d51abe02e0dff5caf83813c275612010a3e6f`。

阶段1派发时必须只读核验上述路径和Git对象。若任一精确输入不存在、对象不匹配或证据任务没有可读取的最终状态，开始前使用`BLOCKED`；任务开始后发现则使用`INCOMPLETE_MISSING_EXACT_INPUTS`。不得递归搜索相似名称、改用聊天摘要或猜测替代值。

T1启动对象规则：执行者只能checkout统筹锁定的完整`stage_1_builder_start_commit`并验证`HEAD`相等。直接checkout `immutable_code_baseline`会丢失治理文档，使用任意`HEAD`会失去对象约束，两者都禁止。

## 3. 前置引导：固定工作区（已完成，不计为阶段1启动）

1. 只读核验长期工作区分支、HEAD、远端和status；
2. 核验两个既有未跟踪文件未变化；
3. 确认目标目录原为空、不是worktree，目标分支原不存在；
4. 从精确`2a2bf098...`建立V2分支和worktree；
5. 只选择性迁移已批准的治理文档提交，并核验没有带入长期分支后续代码；
6. 不携带长期工作区的未跟踪文件；
7. 不merge、rebase、stash或复制working-tree现场。

该前置引导已完成并记录为 `V2-GOV-BOOTSTRAP=DONE`。它只提供V2审阅承载位置，不授权T1至T6。任一对象不一致时停止为`INCOMPLETE`，不得删除目标目录或自行换基线。

## 4. T1至T5：文档Builder

允许创建或修改的精确路径按任务固定如下，不允许使用目录通配符扩展：

| Task | 精确允许写路径 |
|---|---|
| `V2-S1-T1` | `docs/workbuddy/v2/README.md`；`docs/workbuddy/v2/TASK-REGISTER.md`；`docs/workbuddy/v2/STAGE-1-EXECUTION-PLAN.md` |
| `V2-S1-T2` | `docs/workbuddy/v2/PROJECT-CHARTER.md` |
| `V2-S1-T3` | `docs/workbuddy/v2/MODULE-DISPOSITION.md` |
| `V2-S1-T4` | `docs/workbuddy/v2/ACCEPTANCE-MATRIX.md` |
| `V2-S1-T5` | `docs/workbuddy/v2/README.md`；`docs/workbuddy/v2/TASK-REGISTER.md`；`PROJECT-STATE.md`；`WORK-LOG.md` |

禁止修改：

```text
golden_key_openmontage_workbuddy/**
workbuddy-skill/**
scripts/**
tests/**
config/**
*.lock.json
安装、打包和Core文件
.codex/**
```

Builder产物：

1. 更新V2权威入口；
2. 将`PROJECT-CHARTER.md`冻结为阶段1架构决策；
3. 新增`MODULE-DISPOSITION.md`；
4. 完善`ACCEPTANCE-MATRIX.md`；
5. 更新`TASK-REGISTER.md`、`PROJECT-STATE.md`和`WORK-LOG.md`；
6. 从统筹锁定的`stage_1_builder_start_commit`建立有界任务分支，形成一个只含允许文档的提交并推送该任务分支；不得推送或快进`codex/workbuddy-shell-v2`。

## 5. 模块处置矩阵最低字段

每个模块必须记录：

```text
current_path
current_consumer
real_problem_solved
v2_verdict
minimum_reusable_capability
forbidden_logic
target_stage
required_consumer_evidence
required_tests
```

裁决值只允许：

```text
KEEP
ADAPT
REWRITE
REMOVE_FROM_V1
HISTORICAL_ONLY
UNKNOWN
```

必须覆盖：doctor、runtime、runtime_prepare、tasks、cli、mcp_server、paths、security、两个Skill、安装器、打包、凭据、升级、回滚、卸载、Core同步和测试资产。

## 6. 阶段1硬Gate

必须同时满足：

- 所有变更都在允许路径；
- `git diff --check`通过；
- 无生产代码、Skill、安装器、配置、测试或Core变更；
- 章程明确WorkBuddy/Core/Shell唯一职责；
- Shell负面能力清单完整；
- Launcher没有任意Shell和业务编排权限；
- 模块处置逐项有消费者和禁止迁移证据；
- Gate矩阵区分所有状态和非证明；
- 中文fork、MCP、Provider和Publish没有扩大为首版前置；
- v0.3.23没有被描述为正式Release或V2通过对象；
- 长期工作区未跟踪文件原样保留；
- Builder提交和远端指针精确一致。

## 7. 独立Reviewer

Reviewer只读审查Builder精确commit，不修改任何文件，不运行实现任务。

重点搜索以下架构回归：

- Shell选择Pipeline、Provider、Stage或媒体方案；
- Shell创建Artifact或推进Checkpoint；
- Launcher成为Agent或任意命令入口；
- 用户消息包含技术路由或验收控制；
- MCP/CLI重新成为OpenMontage替代控制面；
- 完整大型Runtime重新成为开始前置；
- 静态测试、ZIP、doctor或MP4被写成最终PASS；
- 未经证据整模块迁移。

结论只能是`APPROVE / REQUEST_CHANGES / INCOMPLETE`。

## 8. 阶段1完成定义

Builder完成不等于阶段1完成。

```text
Builder commit pushed
  -> REVIEW_READY
Independent Reviewer APPROVE
  -> REVIEW_PASS
统筹核验对象和证据
  -> AWAITING_USER_GATE
用户接受
  -> PASS_ACCEPTED
```

阶段1`PASS_ACCEPTED`之前，不得细化或启动阶段2实现。

## 9. 状态和串行依赖

- `BLOCKED`只用于执行或审阅开始前的依赖、精确输入或授权未满足；
- 执行或审阅一旦开始，对象不一致、无最终退出、证据缺失或环境干扰必须为`INCOMPLETE`；
- 阶段5必须等待`V2-S4 PASS_ACCEPTED`；阶段6必须等待`V2-S3`、`V2-S4`、`V2-S5`逐项`PASS_ACCEPTED`；阶段7必须等待`V2-S2`至`V2-S6`逐项`PASS_ACCEPTED`；
- 未定义的“接口冻结”或“通过”不构成依赖满足；本修订不授权任何并行例外。
