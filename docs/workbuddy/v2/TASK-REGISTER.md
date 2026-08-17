# WorkBuddy Shell V2 任务账本

状态：`ACTIVE AUTHORITY / V2_S2_S3_RUNTIME_CORRECTION_REVIEW_READY`

更新时间：2026-08-17

## 当前任务

```text
task_id: V2-S2-S3-RUNTIME-CORRECTION-DOCS1
task_status: REVIEW_READY
task_kind: DOCUMENTATION_CONTRACT_CORRECTION
user_authorization: 2026-08-17 / 固化包内Python、宿主运行时发现、缺失项安装、大陆镜像及临时gyan.dev FFmpeg例外；阶段2全部完成且启动审计通过后可启动阶段3
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
next_authorized_task: V2-S2-S3-RUNTIME-CORRECTION-DOCS-REVIEW1
```

本任务把老项目中已经实现和验证过的产品结论选择性固化到V2：金钥匙版Package自带私有Python；其余闭集Runtime先发现、后对缺失项制定计划；只有用户明确同意后才从批准的中国大陆镜像或唯一经直连验证的FFmpeg临时例外准备；WorkBuddy是唯一运行中的Agent。它不新增治理文档，不恢复V1大型Runtime实现，不实现Runtime、Launcher、WorkBuddy入口或状态结果转交。`THIS_COMMIT`由独立Reviewer解析为结果分支的精确40位SHA；只有Reviewer `APPROVE`且同一结果fast-forward进入正式分支后，本次文档收口才算仓库完成。

## 当前正式状态

```text
formal_branch: codex/workbuddy-shell-v2
formal_handoff_commit: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
stage_1_status: PASS_ACCEPTED
stage_2_status: REOPENED_PACKAGE_REFRESH_REQUIRED
stage_2_previous_package_status: PASS_ACCEPTED_HISTORICAL
stage_2_integration_commit: ca6e93b7da108732f2034239da340a986ba3da3a
repository_hygiene_status: PASS_ACCEPTED
repository_final_tree_commit: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
repository_final_audit: APPROVE
repository_final_audit_source: USER_ACCEPTED_HANDOFF_2026_08_17
repository_tracked_files: 33
stage_3_planning_authorization: GRANTED_FOR_CORRECTION_ONLY
stage3_planning: RUNTIME_SCOPE_CORRECTED_FOR_REVIEW
stage_3_implementation_authorization: NOT_GRANTED
stage_3_conditional_authorization: GRANTED_AFTER_ALL_START_GATES_PASS
stage_3_start_gate: WAITING_STAGE_2_AND_PLANNING_PROMOTION
stage_3_execution_packet: FROZEN_FOR_INDEPENDENT_REVIEW
stage3_implementation: NOT_GRANTED
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
stage_3_to_6_scope_reduction: SUPERSEDED_BY_RUNTIME_CORRECTION
runtime_correction: FROZEN_FOR_INDEPENDENT_REVIEW
```

阶段2此前通过的是旧金钥匙版Package登记合同和实现，不是更新后的当前Package。官方OpenMontage输入更新后，必须先重新组装带锁定私有Python的金钥匙版Package，再重新登记、独立审阅和推广。精确新版Package、Python版本/兼容性、Manifest、Lock和hash没有完成前，阶段2不得继续显示当前`PASS_ACCEPTED`，阶段3不得启动实现。

仓库卫生最终树的可重复本地事实是：正式本地分支、origin tracking、实时远端与D盘工作区均为`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`，工作树clean，tracked精确33且等于固定白名单。`repository_final_audit`来自用户提供并再次确认的正式交接身份；本次Reviewer仍须核对当前文档是否忠实记录该交接且无前后冲突。

## 阶段3至阶段6建设与交付顺序

```text
Stage 3: Runtime Preparation on Demand
Stage 4: Session Launcher
Stage 5: WorkBuddy Entry
Stage 6: Status and Result Relay
```

该顺序只表示建设、审阅和正式交付顺序，不是最终用户运行时的调用顺序。每个阶段都从当时最新的`origin/codex/workbuddy-shell-v2`精确提交开始，经单一有界Builder、独立只读Reviewer、普通非force fast-forward推广、远端临时分支清理和本地worktree关闭后，下一阶段才可接管。规划接受、Builder提交或Reviewer批准均不等于正式交付。

最终用户实际运行从`用户 -> 阶段5显式WorkBuddy入口 -> 阶段2 Locator重验 -> 阶段3闭集检查`开始。若Runtime已就绪，则`阶段4固定工具调用 -> 阶段6事实转交`；若阶段3发现缺失/不兼容项，则`阶段6转交完整missing-only计划 -> 用户另行明确授权 -> 阶段3准备全部确认项 -> 阶段6转交准备事实 -> 停止`。原生产请求不得自动重试，只能由用户稍后再次显式调用WorkBuddy并重新检查。

阶段3至阶段6共同约束：每阶段最多一个公共入口；没有可验证输入或直接下游消费者时必须零代码退出；不得预建通用Runtime管理器、CLI/MCP镜像、任务平台、后台服务、第二Agent Host、生产FSM或状态数据库。WorkBuddy是唯一运行中的Agent；所谓OpenMontage Agent只能指WorkBuddy读取已验证Package Guide后承担的逻辑生产角色。

## 阶段授权与零代码出口

```text
stage_3_scope: 单一闭集接口；包内私有Python固定不扫描；发现Python私有依赖、FFmpeg、Node、Remotion、HyperFrames和锁定浏览器，返回ready或missing/incompatible事实，并只准备用户另行确认的missing-only计划中的全部缺失/不兼容项；准备后不自动重试原请求。
stage_3_zero_code_exit: STAGE_3_NO_ADDITIONAL_RUNTIME_REQUIRED
stage_3_download_policy: APPROVED_MAINLAND_CHINA_MIRRORS / TEMP_LOCKED_GYAN_FFMPEG_EXCEPTION_PENDING_DIRECT_ACCESS_PROBE / NO_AUTOMATIC_OVERSEAS_FALLBACK
stage_4_scope: 只接受有效Runtime就绪回执，为一次WorkBuddy会话绑定精确Package和Runtime并调用一个固定工具入口；缺少就绪回执返回RUNTIME_NOT_READY；不启动第二Agent，无任意Shell、无自动重试。
stage_5_scope: 用户实际运行起点；只保留一种真实WorkBuddy显式入口，literal user_message不变，技术控制独立。
stage_6_scope: 直接转交Runtime计划/准备事实与Launcher回执；仅有真实格式转换缺口时才允许独立实现；不解释、不安装、不重试。
stage_6_zero_code_exit: STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE
```

上述范围是规划边界，不是实现授权。任何需要阶段3扫描盘符、扫描/下载包内Python、选择渲染引擎/版本、使用未批准海外默认源、把FFmpeg临时例外扩展到其他组件、未通过直连验证即使用gyan.dev或覆盖外来目录，阶段4启动第二Agent、解析意图或调度任务，阶段5建立第二聊天Agent，阶段6解释Artifact或自动重试的方案，必须停止并返回`STOPPED_SCOPE_EXPANSION`。

## 阶段3待执行任务包

阶段3的唯一目标是把阶段2交付的已验证Package和私有Python，与当前机器上闭集Runtime的真实状态绑定，并返回可被阶段4消费的Runtime就绪事实。它不运行WorkBuddy、不进入OpenMontage生产、不制作视频。

### 启动Gate

只有以下条件全部满足，才能把`stage_3_implementation_authorization`从`NOT_GRANTED`更新为`GRANTED`并建立阶段3Builder；任一失败都只报告阻断，不写阶段3代码：

1. 本次规划纠偏已经独立Reviewer `APPROVE`并普通fast-forward进入`origin/codex/workbuddy-shell-v2`；
2. 当前新版阶段2为`PASS_ACCEPTED`，其已审结果已经进入同一正式分支，旧Package历史PASS不得替代；
3. `locate_active_package`对当前Package、Manifest、Lock、Guide和包内私有Python完成全身份重验；
4. 包内私有Python可真实启动，版本/架构兼容，并能在不使用系统Python的情况下执行锁定依赖bootstrap和import探针；
5. 当前Package提供完整、可核验的依赖输入，且版本、来源、SHA-256、大小、许可证、目标和能力探针信息足以在阶段3第一步冻结新版Runtime Lock；
6. 当前正式本地、origin tracking、实时远端、任务起点、tracked白名单和工作树完全一致，无重叠改动。

FFmpeg `gyan.dev`直连结果不是编写阶段3阻断逻辑的启动前置，但决定真实下载和完整Runtime验收：未验证时只能实现并测试`BLOCKED_SOURCE_ACCESS_UNVERIFIED`，不得执行FFmpeg下载或通过全闭集`READY_PREPARED`；直连失败时保持`BLOCKED_SOURCE_UNREACHABLE`并等待新来源裁决。

### 冻结实现路径

```text
public_entry: prepare_runtime_on_demand(locator_result, data_root, runtime_lock, confirmation=None)
production_module: golden_key_openmontage_workbuddy/runtime_prepare.py
runtime_lock: WORKBUDDY-PRODUCTION-RUNTIME.lock.json
direct_test: tests/workbuddy/test_runtime_prepare.py
managed_root: <DataRoot>/Runtime
cache_root: <DataRoot>/Caches
```

阶段3最多新增上述一个生产模块、一个数据锁和一个直接测试文件；状态文档只作必要更新。若阶段2最终接口证明这些路径不能成立，必须先返回规划纠偏，不得临时增加`host_tools.py`、通用下载器、CLI/MCP、服务、数据库或其他生产文件。

### 执行步骤

1. 从最新正式提交建立单一有界Builder，固定精确base、允许路径和Reviewer范围；
2. 用阶段2 Locator结果冻结新版Runtime Lock，旧锁只能提供渠道和结构参考，不能直接冒充当前版本；
3. 实现零写入发现：只核验受管目录、已有明确登记记录和正常PATH候选；PATH命中仍须验证路径、版本、能力和身份；
4. 生成完整missing-only计划，包含Package/Runtime/计划SHA、全部缺失/不兼容项、版本、来源、hash、下载量、安装量、许可证和目标；
5. 将`confirmation`与三项SHA精确绑定；无确认、确认过期或身份变化时保持零下载、零安装；
6. 使用包内私有Python及批准来源，仅在`<DataRoot>/Runtime`准备确认计划中的全部缺失项；执行同卷staging、hash核验、所有权检查、原子发布、失败回滚和清理；
7. 重新核验全部闭集并返回`READY_PREPARED`或真实失败；准备完成后停止，不调用阶段4、不自动重试原生产请求；
8. 完成直接测试、静态边界检查、独立只读Reviewer和普通fast-forward推广，推广前不得宣称阶段3交付。

### 输出与失败边界

- `READY_REUSED`：全部闭集已验证就绪，零下载、零修改；
- `MISSING_OR_INCOMPATIBLE`：只返回身份锁定的完整计划，零写入；
- `READY_PREPARED`：确认计划内全部项目准备并复核通过；
- `BLOCKED_SOURCE_UNAPPROVED`、`BLOCKED_SOURCE_ACCESS_UNVERIFIED`、`BLOCKED_SOURCE_UNREACHABLE`或其他真实错误：保持失败事实，不换源、不伪造就绪；
- `STAGE_3_NO_ADDITIONAL_RUNTIME_REQUIRED`：阶段2最终交付和真实下游合同证明无需阶段3生产实现时的合法零代码出口。

阶段3不创建或修改Package，不扫描盘符，不使用系统Python，不修改系统PATH/注册表，不要求管理员权限，不覆盖外来目录，不让用户选择渲染方案，不启动WorkBuddy/第二Agent，不执行OpenMontage生产，不建立通用包管理器或自动重试。

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

老项目可迁移证据：`347272c`固定包内便携Python；`899592d`固定完整Runtime、hash、许可、DataRoot和大陆PyPI/npm/Node/浏览器镜像；`639978d`增加`managed`、`registered_host`、`PATH_host`、`missing`发现与missing-only准备。用户于2026-08-17临时批准继续使用旧锁中的精确FFmpeg 9.0 `gyan.dev`资产，并将在不使用代理/VPN的中国大陆网络验证直连。验证前为`BLOCKED_SOURCE_ACCESS_UNVERIFIED`；失败为`BLOCKED_SOURCE_UNREACHABLE`，不得自动换用其他海外源。
