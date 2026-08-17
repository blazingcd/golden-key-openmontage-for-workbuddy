# WorkBuddy Shell V2 任务账本

状态：`ACTIVE AUTHORITY / V2_S2_S3_REQUIRED_TOOLCHAIN_CORRECTION_REVIEW_READY`

更新时间：2026-08-18

## 当前任务

```text
task_id: V2-S2-S3-REQUIRED-TOOLCHAIN-CORRECTION-DOCS1
task_status: REVIEW_READY
task_kind: DOCUMENTATION_CONTRACT_CORRECTION
user_authorization: 2026-08-18 / 金钥匙Package必须自带Python、FFmpeg、Node三项官方Prerequisites；其他渲染能力按需可选安装
start_commit: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
result_commit: THIS_COMMIT
branch: codex/v2-s3-s6-scope-docs1
review_range: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb..THIS_COMMIT
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_at_start: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
allowed_paths:
  - PROJECT-STATE.md
  - PROJECT_CONTEXT.md
  - README.md
  - README_zh-CN.md
  - WORK-LOG.md
  - AGENT_GUIDE.md
  - docs/workbuddy/v2/README.md
  - docs/workbuddy/v2/TASK-REGISTER.md
  - docs/workbuddy/v2/PROJECT-CHARTER.md
  - docs/workbuddy/v2/MODULE-DISPOSITION.md
  - docs/workbuddy/v2/ACCEPTANCE-MATRIX.md
  - docs/workbuddy/v2/DRIFT-GUARD.md
  - docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md
production_code_changes: 0
test_changes: 0
tracked_files_expected: 33
verification: STATIC_CONSISTENCY_PASS
pytest: NOT_RUN_PROJECT_VENV_MISSING
next_authorized_task: V2-S2-S3-REQUIRED-TOOLCHAIN-CORRECTION-DOCS-REVIEW1
```

本任务纠正Required与Optional边界：金钥匙版Package自带完整必带私有工具链，阶段2登记Python、FFmpeg和Node；阶段3只准备WorkBuddy/OpenMontage已经选定的可选渲染能力。它不新增治理文档，不实现Runtime、Launcher、WorkBuddy入口或状态结果转交。`THIS_COMMIT`由独立Reviewer解析为结果分支的精确40位SHA；只有Reviewer `APPROVE`且同一结果fast-forward进入正式分支后，本次文档收口才算仓库完成。

## 当前正式状态

```text
formal_branch: codex/workbuddy-shell-v2
formal_handoff_commit: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
stage_1_status: PASS_ACCEPTED
stage_2_status: REOPENED_REQUIRED_TOOLCHAIN_PACKAGE_REFRESH
stage_2_previous_package_status: PASS_ACCEPTED_HISTORICAL
stage_2_integration_commit: ca6e93b7da108732f2034239da340a986ba3da3a
repository_hygiene_status: PASS_ACCEPTED
repository_final_tree_commit: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
repository_final_audit: APPROVE
repository_final_audit_source: USER_ACCEPTED_HANDOFF_2026_08_17
repository_tracked_files: 33
stage_3_planning_authorization: GRANTED_FOR_CORRECTION_ONLY
stage3_planning: REOPENED_OPTIONAL_CAPABILITY_RECLASSIFICATION_REQUIRED
stage_3_implementation_authorization: NOT_GRANTED
stage_3_conditional_authorization: SUSPENDED_PENDING_REPLAN
stage_3_start_gate: BLOCKED_STAGE_2_REQUIRED_TOOLCHAIN
stage_3_execution_packet: SUPERSEDED_BY_REQUIRED_TOOLCHAIN_CORRECTION
stage3_implementation: NOT_GRANTED
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
stage_3_to_6_scope_reduction: SUPERSEDED_BY_REQUIRED_TOOLCHAIN_CORRECTION
runtime_correction: REOPENED_REQUIRED_TOOLCHAIN_CORRECTION
```

阶段2此前通过的是旧金钥匙版Package登记合同和实现，不是更新后的当前Package。官方当前Quick Start明确列出Python 3.10+、FFmpeg和Node.js 18+三项基础Prerequisites；当前HyperFrames合同进一步要求Node.js 22+。金钥匙Package必须因此自带可用私有Python环境及核心依赖、FFmpeg/ffprobe、满足最高要求的Node/npm/npx，并在Manifest/Lock与Registration中逐项锁定。只登记Python的旧阶段2合同不足，必须修订、重新组装、独立审阅和推广；完成前阶段3不得启动。

仓库卫生最终树的可重复本地事实是：正式本地分支、origin tracking、实时远端与D盘工作区均为`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`，工作树clean，tracked精确33且等于固定白名单。`repository_final_audit`来自用户提供并再次确认的正式交接身份；本次Reviewer仍须核对当前文档是否忠实记录该交接且无前后冲突。

## 阶段3至阶段6建设与交付顺序

```text
Stage 3: Runtime Preparation on Demand
Stage 4: Session Launcher
Stage 5: WorkBuddy Entry
Stage 6: Status and Result Relay
```

该顺序只表示建设、审阅和正式交付顺序，不是最终用户运行时的调用顺序。每个阶段都从当时最新的`origin/codex/workbuddy-shell-v2`精确提交开始，经单一有界Builder、独立只读Reviewer、普通非force fast-forward推广、远端临时分支清理和本地worktree关闭后，下一阶段才可接管。规划接受、Builder提交或Reviewer批准均不等于正式交付。

上一版`阶段5 -> 阶段2 -> 阶段3全闭集检查 -> 阶段4`运行链路已失效，因为阶段3不再负责启动前必带工具链。新的最低关系是：阶段5触发阶段2对必带Python/FFmpeg/Node重验，阶段4据此启动固定工具；WorkBuddy/OpenMontage形成并锁定Remotion或HyperFrames能力要求后，才调用阶段3准备对应可选能力。阶段3与阶段4在真实会话中的精确调用/暂停合同必须等待WorkBuddy消费者证据后重新冻结，不能由Shell预先猜测。

阶段3至阶段6共同约束：每阶段最多一个公共入口；没有可验证输入或直接下游消费者时必须零代码退出；不得预建通用Runtime管理器、CLI/MCP镜像、任务平台、后台服务、第二Agent Host、生产FSM或状态数据库。WorkBuddy是唯一运行中的Agent；所谓OpenMontage Agent只能指WorkBuddy读取已验证Package Guide后承担的逻辑生产角色。

## 阶段授权与零代码出口

```text
stage_3_scope: 仅对WorkBuddy/OpenMontage已经锁定的可选Remotion或HyperFrames能力及其锁声明附属资产执行按需发现和用户确认后的准备；不得处理必带Python/FFmpeg/Node工具链。
stage_3_zero_code_exit: STAGE_3_NO_OPTIONAL_CAPABILITY_REQUIRED
stage_3_download_policy: OPTIONAL_CAPABILITY_APPROVED_MAINLAND_CHINA_MIRRORS / NO_AUTOMATIC_OVERSEAS_FALLBACK
stage_4_scope: 启动固定工具时必须接受阶段2必带工具链就绪事实；执行已选可选能力前还必须接受该能力对应的阶段3就绪事实；缺少相应事实返回RUNTIME_NOT_READY；不启动第二Agent，无任意Shell、无自动重试。
stage_5_scope: 用户实际运行起点；只保留一种真实WorkBuddy显式入口，literal user_message不变，技术控制独立。
stage_6_scope: 直接转交Runtime计划/准备事实与Launcher回执；仅有真实格式转换缺口时才允许独立实现；不解释、不安装、不重试。
stage_6_zero_code_exit: STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE
```

上述范围是规划边界，不是实现授权。任何需要阶段3扫描盘符、发现/下载/替换包内Python/FFmpeg/Node、一次安装全部可选能力、选择渲染引擎/版本、使用未批准海外默认源或覆盖外来目录，阶段4启动第二Agent、解析意图或调度任务，阶段5建立第二聊天Agent，阶段6解释Artifact或自动重试的方案，必须停止并返回`STOPPED_SCOPE_EXPANSION`。

## 阶段3重新规划前置

上一版阶段3执行包、`prepare_runtime_on_demand(...)`签名和`WORKBUDDY-PRODUCTION-RUNTIME.lock.json`全闭集形状全部标记为`SUPERSEDED`，不得交给Builder。阶段3重新冻结必须先得到：

1. 阶段2已审Package Registration，明确返回必带Python及核心依赖、FFmpeg/ffprobe、Node/npm/npx的精确身份和路径；
2. 当前Package提供的WorkBuddy/OpenMontage消费者合同，明确何时产生已锁定的`remotion`或`hyperframes`能力要求；
3. 对应可选能力的版本、npm锁、批准大陆镜像、hash、大小、许可证、目标和必要附属资产；
4. 阶段3与阶段4同一WorkBuddy会话中的调用、暂停、用户确认和继续边界；Shell不得自动重放原业务请求；
5. 最新正式Git对象、允许路径、一个公共入口、一个生产模块、一个Optional Runtime Lock和一个直接测试文件的精确任务包。

在这些输入齐全前，阶段3保持`REOPENED_OPTIONAL_CAPABILITY_RECLASSIFICATION_REQUIRED / NOT_GRANTED`。可以确定的边界只有：Remotion与HyperFrames不预装全部；只准备已选能力；浏览器仅在该能力锁明确要求时准备；Python/FFmpeg/Node及核心Python依赖绝不由阶段3扫描、下载或替换；阶段3不选择渲染器、不启动第二Agent、不执行视频生产。

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
repository_hygiene_wave_a_result: 830d44ab7b910e20bfc9093bf2c505850860880a
repository_hygiene_wave_a_closeout: 385a20bbff9624703682eecba3b38fc3c6d2d6b9
repository_hygiene_sequence_authority: cf04dc20d428233e2d328578a1e5d58ebaca2feb
repository_hygiene_wave_b_result: a9e660d5f059a2b8e20cd35dde761b941811494d
repository_hygiene_wave_b_ci_scope_fix: 2f70e426d52a2ea939f5b00e276f9da6bc108a69
repository_hygiene_final_ci_freeze: 2e4858bdd5142a8f041d708bdb385a197c4436a9
repository_hygiene_wave_c_result: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
```

旧Stage2只证明旧金钥匙版Package的Registration与Locator：明确路径输入、不可变登记对象、活动指针CAS、破损指针显式恢复和只读Locator。它不证明当前新版Package、Installer、Runtime、Launcher、真实WorkBuddy、Provider、SaaS、网络或媒体E2E。阶段3至阶段6不得读取未验证Package Guide、扫描磁盘猜测对象，或把技术控制词写入literal `user_message`。

老项目可迁移证据：`347272c`固定包内便携Python；`899592d`固定完整Runtime、hash、许可、DataRoot和大陆PyPI/npm/Node/浏览器镜像；`639978d`增加`managed`、`registered_host`、`PATH_host`、`missing`发现与missing-only准备。旧锁中的精确FFmpeg 9.0 `gyan.dev`资产现只作为必带Package组装候选；阶段2必须核验其来源、SHA-256、许可、分发和实际可获得性。它不再形成阶段3下载授权，也不得扩展为其他可选能力的海外回退权。
