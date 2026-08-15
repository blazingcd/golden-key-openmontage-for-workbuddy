# WorkBuddy Shell V2 任务账本

状态：`ACTIVE AUTHORITY`

更新时间：2026-08-15

## 1. 状态词

```text
PLANNED
READY_NOT_STARTED
IN_PROGRESS
REVIEW_READY
REQUEST_CHANGES
REVIEW_PASS
AWAITING_USER_GATE
PASS_ACCEPTED
BLOCKED
INCOMPLETE
SUPERSEDED
DONE
```

`BLOCKED`只用于执行或审阅开始前已有依赖、精确输入或授权未满足。任务或审阅一旦开始，出现对象不一致、无最终退出、证据缺失或环境干扰，必须使用`INCOMPLETE`，不得退回`BLOCKED`、不得猜测完成。

## 2. 当前项目状态

```text
governance_docs: DONE
governance_docs_commit: def921a2e29b4858f289c44c3e9183619ba31ce6
governance_docs_source_branch: codex/w4.1-portable-python
v2_governance_import_commits: ee60947, 3b62728
v2_source_branch: codex/workbuddy-shell-v2
v2_governance_fix_branch: codex/v2-gov-fix1
v2_worktree: D:\BlazingCD\Personal\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2
immutable_code_baseline: 2a2bf09832d558388dc2816c54b32a2dce4aa607
stage_1_builder_start_commit: PENDING_REVIEW_PASS_AND_COORDINATOR_LOCK
v2_bootstrap: DONE
stage_1: READY_NOT_STARTED
stage_1_start_authorized_after_document_review: NO
v2_branch_created: YES
v2_worktree_created: YES
code_modified: NO
workbuddy_run: NO
provider_call: NO
media_generated: NO
wrong_project_review: INCOMPLETE_WRONG_PROJECT_CONTEXT
v2_gov_review1: REQUEST_CHANGES
v2_gov_review1_thread: 01a00433-bad9-71c1-8fa5-468f676bd054
v2_gov_review1_findings: P0=0, P1=5, P2=1
v2_gov_fix1: REVIEW_READY
next_authorized_task: V2-GOV-REVIEW2
```

为让独立审阅在本项目、本分支发生，统筹已从固定代码基线`2a2bf09832d558388dc2816c54b32a2dce4aa607`建立V2工作树，并只选择性迁移治理文档。该前置引导不等于阶段1启动，不得把长期分支后续HEAD整体作为V2代码起点。

`immutable_code_baseline`固定且不可变，只约束生产代码谱系；它不是阶段1 Builder的checkout目标。`stage_1_builder_start_commit`当前必须保持`PENDING_REVIEW_PASS_AND_COORDINATOR_LOCK`，只有`V2-GOV-REVIEW2`通过后才由统筹锁定为完整40位提交。未锁定前不得启动`V2-S1-T1`；执行者不得直接checkout固定代码基线而丢失治理文档，也不得使用任意`HEAD`。

当前先执行 `V2-GOV-REVIEW2`。后续若审阅通过、统筹完成上述对象锁定且用户明确授权启动阶段1，才把`V2-S1-T1`改为`IN_PROGRESS`。

## 3. 八阶段总账

| Stage | Task ID | 目标 | 状态 | 依赖 | 当前非证明 |
|---|---|---|---|---|---|
| 前置治理 | `V2-GOV-001` | 固化章程、防漂移、账本、阶段1计划和验收矩阵 | `DONE` | 用户要求 | 不等于阶段1开始 |
| 前置引导 | `V2-GOV-BOOTSTRAP` | 从固定基线建立V2分支/worktree并只迁入治理文档 | `DONE` | 用户要求独立审阅须在本项目本分支 | 不等于阶段1开始或代码实现 |
| 前置审阅 | `V2-GOV-REVIEW1` | 在V2项目/分支独立只读审阅治理文档 | `REQUEST_CHANGES` | `V2-GOV-BOOTSTRAP DONE` | Reviewer任务`01a00433-bad9-71c1-8fa5-468f676bd054`；P0=0、P1=5、P2=1；不等于阶段1批准 |
| 治理修订 | `V2-GOV-FIX1` | 有界关闭REVIEW1的六项finding | `REVIEW_READY` | `V2-GOV-REVIEW1 REQUEST_CHANGES` | 不等于APPROVE或阶段1批准 |
| 修订复审 | `V2-GOV-REVIEW2` | 独立只读审阅FIX1精确提交 | `READY_NOT_STARTED` | `V2-GOV-FIX1 REVIEW_READY` | 由统筹另行创建；当前任务不得创建 |
| 1 | `V2-S1` | 冻结V2架构和旧模块处置 | `READY_NOT_STARTED` | `V2-GOV-REVIEW2 APPROVE`、统筹锁定`stage_1_builder_start_commit`、用户明确授权 | 无生产实现 |
| 2 | `V2-S2` | 建立Core Registration合同 | `PLANNED` | `V2-S1 PASS_ACCEPTED` | 无Schema、验证器、活动对象 |
| 3 | `V2-S3` | 建立Launcher会话环境绑定 | `PLANNED` | `V2-S2 PASS_ACCEPTED` | 无V2 Launcher |
| 4 | `V2-S4` | 重写生产Skill和Onboarding交接 | `PLANNED` | `V2-S3 PASS_ACCEPTED` | 无V2 Skill |
| 5 | `V2-S5` | 建立渐进式Runtime | `PLANNED` | `V2-S4 PASS_ACCEPTED` | 旧完整Runtime不等于V2 |
| 6 | `V2-S6` | 缩减CLI/MCP和重复任务状态 | `PLANNED` | `V2-S3 PASS_ACCEPTED`、`V2-S4 PASS_ACCEPTED`、`V2-S5 PASS_ACCEPTED` | 旧CLI/MCP测试不等于V2 |
| 7 | `V2-S7` | 重构安装、升级、回滚和迁移 | `PLANNED` | `V2-S2 PASS_ACCEPTED`至`V2-S6 PASS_ACCEPTED`逐项成立 | 旧W4.1包不等于V2包 |
| 8 | `V2-S8` | 执行Gate A至D及可选E | `PLANNED` | `V2-S7 PASS_ACCEPTED` | 历史真实运行不等于V2验收 |

## 4. 阶段1任务

| Task ID | 内容 | 状态 | 允许路径 | 前置 |
|---|---|---|---|---|
| `V2-S1-T0` | 建立固定分支和独立worktree | `SUPERSEDED` | 无 | 已由前置 `V2-GOV-BOOTSTRAP` 完成，不计为阶段1启动 |
| `V2-S1-T1` | 建立V2文档入口和权威关系 | `BLOCKED` | `docs/workbuddy/v2/README.md`；`docs/workbuddy/v2/TASK-REGISTER.md`；`docs/workbuddy/v2/STAGE-1-EXECUTION-PLAN.md` | `V2-GOV-REVIEW2 APPROVE`、统筹锁定`stage_1_builder_start_commit`且用户明确授权阶段1 |
| `V2-S1-T2` | 冻结职责和目标架构 | `BLOCKED` | `docs/workbuddy/v2/PROJECT-CHARTER.md` | T1 `REVIEW_READY` |
| `V2-S1-T3` | 逐模块处置矩阵 | `BLOCKED` | `MODULE-DISPOSITION.md` | T2 |
| `V2-S1-T4` | 冻结验收矩阵和状态模型 | `BLOCKED` | `ACCEPTANCE-MATRIX.md` | T2 |
| `V2-S1-T5` | 同步账本、状态和工作日志 | `BLOCKED` | `docs/workbuddy/v2/README.md`；`docs/workbuddy/v2/TASK-REGISTER.md`；`PROJECT-STATE.md`；`WORK-LOG.md` | T3/T4 `REVIEW_READY` |
| `V2-S1-T6` | 独立只读Reviewer | `BLOCKED` | 零写入 | Builder提交 |
| `V2-S1-GATE` | 用户阶段1 Gate | `BLOCKED` | 零写入 | Reviewer APPROVE |

阶段1获准后从T1开始，T1至T5可由一个有界的文档Builder任务串行完成；T6必须是独立任务。阶段1不得修改生产代码。前置 `V2-GOV-REVIEW1` 与阶段1完成后的 `V2-S1-T6` 是两个不同审阅任务，不得互相冒充。

## 4.1 前置审阅记录

```text
incorrect_review_thread: 01a0042e-1a5a-7ce2-ac25-d85eb764c1ac
incorrect_review_verdict: INCOMPLETE_WRONG_PROJECT_CONTEXT
incorrect_review_effect: ZERO_CHANGE_ZERO_TEST_ZERO_ADJUDICATION
required_review_project: Golden_Key_OpenMontage_for_WorkBuddy-shell-v2
required_review_branch: codex/workbuddy-shell-v2
required_review_mode: independent_read_only
review1_task_id: V2-GOV-REVIEW1
review1_thread: 01a00433-bad9-71c1-8fa5-468f676bd054
review1_verdict: REQUEST_CHANGES
review1_findings: P0=0, P1=5, P2=1
fix1_task_id: V2-GOV-FIX1
fix1_status: REVIEW_READY
review2_task_id: V2-GOV-REVIEW2
review2_status: READY_NOT_STARTED
```

## 5. 阶段2至8任务包

| Task ID | 计划子任务 | 允许路径区 | 明确禁止 |
|---|---|---|---|
| `V2-S2` | Registration Schema、验证、原子活动指针、漂移负测、独立Review | 消费方包、config、V2 tests | 扫盘、Pipeline解析、静态验证冒充真实验证 |
| `V2-S3` | inspect/session/受控exec/status、环境回执、错误分类、独立Review | Launcher和V2 tests | 任意Shell、Agent、Director、Core业务导入 |
| `V2-S4` | 显式触发、Locator、Guide入口、提示边界、Onboarding交接 | `workbuddy-skill/`和测试 | CLI生产链、全局截获、技术化用户消息 |
| `V2-S5` | 基础Python、FFmpeg、动态合成、Provider/大型模型分层 | Runtime、锁、下载测试 | 完整环境一次全装、静默下载、混合授权 |
| `V2-S6` | 删除生产编排入口、缩减CLI/MCP/Jobs、证明Core链不依赖它们 | CLI/MCP/tasks和测试 | 保留第二套Stage FSM或17工具主链 |
| `V2-S7` | Shell/Core分离安装、原子切换、升级回滚、数据迁移 | installer/package/manifest/tests | 原地覆盖、降级、删除用户数据、Core main同步 |
| `V2-S8-A` | 对象、Skill、环境绑定真实验收 | D盘证据、测试卡 | Provider、媒体生成 |
| `V2-S8-B` | 原生Guide/Pipeline/首Artifact/Checkpoint | 新WorkBuddy会话/新项目 | Shell代替Core决策 |
| `V2-S8-C` | 无rotation争议的本地短成片 | 新WorkBuddy会话/新项目 | 临时渲染脚本、Provider |
| `V2-S8-D` | 新Core Release门店竖屏业务验收 | 锁定新Core和门店素材 | Shell方向补丁、技术化用户Prompt |
| `V2-S8-E` | 可选Provider真实能力 | 单独授权对象 | 默认阻塞本地V2完成 |

## 6. 每项任务必填记录

```text
task_id:
objective:
immutable_code_baseline:
stage_1_builder_start_commit:
allowed_paths:
forbidden_paths:
dependencies:
executor_thread:
status:
result_commit:
tests_and_exit_codes:
evidence_paths:
independent_review_thread:
review_verdict:
known_non_proofs:
files_changed:
next_authorized_task:
```

## 7. 状态更新规则

- 只有统筹任务更新本账本的跨任务状态。
- Builder开始后：`READY_NOT_STARTED -> IN_PROGRESS`。
- Builder完成并推送精确commit：`IN_PROGRESS -> REVIEW_READY`。
- Reviewer要求修改：`REVIEW_READY -> REQUEST_CHANGES`。
- Reviewer通过：`REVIEW_READY -> REVIEW_PASS`。
- 需要用户Gate：`REVIEW_PASS -> AWAITING_USER_GATE`。
- 用户接受：`AWAITING_USER_GATE -> PASS_ACCEPTED`。
- 任务或审阅开始后，没有最终退出、对象漂移、证据缺失或环境干扰必须进入`INCOMPLETE`，不得进入`BLOCKED`或`REVIEW_PASS`。
- 后一步不得在前一步`PASS_ACCEPTED`前开始；本修订不授权任何并行例外。
