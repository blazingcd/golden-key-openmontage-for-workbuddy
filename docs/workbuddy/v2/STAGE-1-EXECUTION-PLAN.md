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

- V2代码基线：`2a2bf09832d558388dc2816c54b32a2dce4aa607`
- 当前分支：`codex/workbuddy-shell-v2`
- 当前worktree：`D:\BlazingCD\Personal\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2`
- 本目录的项目章程、防漂移规则、任务账本和验收矩阵；
- 当前仓库权威文件、两个现有Skill和消费层核心实现；
- 已列入项目交接的七个既有Codex证据任务；
- 官方对象`4eab34c5...`和v0.3.23对象`613d51a...`的只读事实。

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

允许创建或修改：

```text
docs/workbuddy/v2/**
PROJECT-STATE.md
WORK-LOG.md
```

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
6. 形成一个只含允许文档的提交并推送V2分支。

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
