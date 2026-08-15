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
SUPERSEDED
DONE
```

状态缺失、证据不完整或对象不一致时使用`BLOCKED`或`INCOMPLETE`说明，不得猜测完成。

## 2. 当前项目状态

```text
governance_docs: DONE
stage_1: READY_NOT_STARTED
stage_1_start_authorized_after_document_review: NO
v2_branch_created: NO
v2_worktree_created: NO
code_modified: NO
workbuddy_run: NO
provider_call: NO
media_generated: NO
next_authorized_task: NONE
```

用户需要先审阅本套文档。后续若明确授权启动阶段1，才把`V2-S1-T0`改为`IN_PROGRESS`。

## 3. 八阶段总账

| Stage | Task ID | 目标 | 状态 | 依赖 | 当前非证明 |
|---|---|---|---|---|---|
| 前置治理 | `V2-GOV-001` | 固化章程、防漂移、账本、阶段1计划和验收矩阵 | `DONE` | 用户要求 | 不等于阶段1开始 |
| 1 | `V2-S1` | 冻结V2架构和旧模块处置 | `READY_NOT_STARTED` | 文档审阅与新授权 | 无V2分支、无实现 |
| 2 | `V2-S2` | 建立Core Registration合同 | `PLANNED` | `V2-S1 PASS_ACCEPTED` | 无Schema、验证器、活动对象 |
| 3 | `V2-S3` | 建立Launcher会话环境绑定 | `PLANNED` | `V2-S2 PASS_ACCEPTED` | 无V2 Launcher |
| 4 | `V2-S4` | 重写生产Skill和Onboarding交接 | `PLANNED` | `V2-S3 PASS_ACCEPTED` | 无V2 Skill |
| 5 | `V2-S5` | 建立渐进式Runtime | `PLANNED` | `V2-S4接口冻结` | 旧完整Runtime不等于V2 |
| 6 | `V2-S6` | 缩减CLI/MCP和重复任务状态 | `PLANNED` | `V2-S3/S4/S5通过` | 旧CLI/MCP测试不等于V2 |
| 7 | `V2-S7` | 重构安装、升级、回滚和迁移 | `PLANNED` | `V2-S2至S6通过` | 旧W4.1包不等于V2包 |
| 8 | `V2-S8` | 执行Gate A至D及可选E | `PLANNED` | `V2-S7 PASS_ACCEPTED` | 历史真实运行不等于V2验收 |

## 4. 阶段1任务

| Task ID | 内容 | 状态 | 允许路径 | 前置 |
|---|---|---|---|---|
| `V2-S1-T0` | 建立固定分支和独立worktree | `READY_NOT_STARTED` | Git worktree元数据和目标空目录 | 用户再次授权 |
| `V2-S1-T1` | 建立V2文档入口和权威关系 | `BLOCKED` | `docs/workbuddy/v2/**` | T0 |
| `V2-S1-T2` | 冻结职责和目标架构 | `BLOCKED` | V2架构文档 | T1 |
| `V2-S1-T3` | 逐模块处置矩阵 | `BLOCKED` | `MODULE-DISPOSITION.md` | T2 |
| `V2-S1-T4` | 冻结验收矩阵和状态模型 | `BLOCKED` | `ACCEPTANCE-MATRIX.md` | T2 |
| `V2-S1-T5` | 同步账本、状态和工作日志 | `BLOCKED` | V2文档、`PROJECT-STATE.md`、`WORK-LOG.md` | T3/T4 |
| `V2-S1-T6` | 独立只读Reviewer | `BLOCKED` | 零写入 | Builder提交 |
| `V2-S1-GATE` | 用户阶段1 Gate | `BLOCKED` | 零写入 | Reviewer APPROVE |

T0至T5可由一个有界的文档Builder任务串行完成；T6必须是独立任务。阶段1不得修改生产代码。

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
baseline_commit:
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
- 没有最终退出、对象漂移或证据缺失不得进入`REVIEW_PASS`。
- 后一步不得在前一步`PASS_ACCEPTED`前开始，除非章程明确允许的同阶段非重叠离线工作。
