# WorkBuddy Shell V2 旧资产处置

状态：`STAGE_3_PASS_ACCEPTED / STAGE_4_PLANNING_PASS_ACCEPTED / STAGE_4_IMPLEMENTATION_PASS_ACCEPTED / STAGE_5_IN_PROGRESS_ENTRY_CODE_COMPLETE_REAL_INTEGRATION_INCOMPLETE / MAPPING_ONLY / TRACKED_40`

固定来源：`2a2bf09832d558388dc2816c54b32a2dce4aa607`

本文件只把 V1 文件或能力映射到章程中的六个模块、`DROP`或`HISTORICAL`。裁决不授权整文件复制；只有表内最小能力可在后续任务重新证明。

## 1. 关键调用链证据

- `setup.py`把普通入口和 MCP 入口分别绑定到`cli:main`与`mcp_server:main`；`cli.py`继续消费`doctor/gate/paths/security/runtime/model_config/runtime_prepare/tasks`。
- `runtime.py`直接导入执行包内的`lib.checkpoint`、`lib.pipeline_loader`和`schemas.artifacts`，并由CLI、MCP与`tasks.py`消费；`tasks.py`又调用Stage检查和Tool执行。这是V1 Shell形成第二生产控制面的直接证据。
- 两个 Skill 经`WORKBUDDY-RUNTIME.json -> launcher -> CLI`消费上述能力；历史真实客户端同时证明“Skill 已安装”不等于“自然路由成功”。
- 安装、包、运行时、凭据、回滚和卸载测试只证明对应旧合同资产，不证明 V2 的真实 WorkBuddy生产流程或业务效果。

## 2. 分组裁决

裁决含义：`KEEP`仅保留边界完全一致的最小能力；`ADAPT`调整既有边界；`REWRITE`保留问题但重建实现；`DROP`不进入 MVP；`HISTORICAL`只作来源或回归参考。

| V1 来源 | 真实消费者 / 调用链 | V2 归属 / 裁决 | 最小保留能力 | 禁止迁移逻辑 | 后续消费者证据 | 最小验收 |
|---|---|---|---|---|---|---|
| `__init__.py`、`__main__.py`、`cli.py` | 包导入、`python -m`、控制台入口、Launcher、两个Skill | 会话Launcher / `REWRITE_PASS_ACCEPTED` | 唯一入口`launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`先用Stage2 Locator重验，只消费release-specific immutable `PackageToolDefinitionV1`，恰好调用一个固定Package工具并返回九值闭集、递归不可改写的`LauncherReceiptV1`；基础调用不依赖可选能力 | 恢复CLI平台；改写用户原话；读未验证Guide；启动第二Agent；Project/Stage/Tool/Artifact/Checkpoint命令；任意Shell/命令；Runtime安装；Provider或渲染器选择；自动重试/重放；队列/服务/数据库/多进程调度；媒体生产 | 批准Package定义/最终交付Installer owner提供工具身份；Stage5 entry-code 已正式交付并仅消费已冻结接口；R03/R04/R05/R06 等后续实现仍须分别授权 | Stage4规划与实现均`PASS_ACCEPTED`；真实生产WorkBuddy/Launcher、Provider和媒体执行未证明；Stage5整体为`IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`，Stage6仍未授权/未证明 |
| `doctor.py`、`paths.py`、`gate.py` | CLI/MCP/Skill与维护者CI | OpenMontage 执行包登记与定位 / `REWRITE`；静态gate仅`HISTORICAL`参考 | 只读Package Registration、完整必带工具链身份和规范化路径报告 | 硬编码版本/Pipeline、扫盘、隐式准备、把doctor/gate当产品PASS | Locator与Launcher消费唯一活动Package Registration | Python/核心依赖、FFmpeg/ffprobe、Node/npm/npx任一未登记或漂移即fail closed，零写入 |
| `runtime_prepare.py`、`host_tools.py`、Runtime locks、`subprocess_guard/**` | doctor、CLI runtime、安装repair、宿主工具发现、missing-only准备、运行时/离线测试 | Runtime按需准备 / `REWRITE_PASS_ACCEPTED_AT_A3F8959682D296301DC573C2835F8C705A52E8B2` | 唯一入口`prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`有界探测Remotion/HyperFrames；结果闭集为`DETECTION_REPORT/CONSENT_REQUIRED/INTEGRATED/SKIPPED/BLOCKED`，能力事实为`PRESENT/MISSING/INCOMPATIBLE/NOT_INTEGRATED`；缺失/不兼容时零下载计划，逐能力批准后才受管集成 | 迁移Python核心依赖、FFmpeg或Node准备逻辑；把可选能力当必带Runtime；恢复旧全闭集Lock、旧入口签名、Shell-owned Lock、独立`host_tools.py`/`subprocess_guard`框架；扫盘；通用包管理；自动安装；Shell选择渲染器；修改系统Python/PATH/注册表 | Stage4仅在`PackageToolDefinitionV1`声明要求时消费同一capability+definition的完整批准定义和未改写`PRESENT`或`INTEGRATED`原始事实；基础调用不依赖可选能力 | 55 direct、10 hygiene、199 full全部退出0无skip；真实下载、生产DataRoot、WorkBuddy、Provider和媒体/视频E2E不在该证据层 |
| `security.py` | CLI/MCP/runtime/tasks 输出 | 六模块横切 / `KEEP` | 纯函数脱敏 | 读取或记录明文凭据；用脱敏掩盖对象或退出状态 | 安装、Launcher 与状态回执共同消费同一边界 | 明文 canary 不出现在输出 |
| `tasks.py` | CLI task、MCP、生产Skill，并调用`runtime.py` | 状态与结果转交 / `REWRITE` | 优先直接转交Runtime计划/准备事实与Launcher回执；仅保留真实需要的一次确定性格式转换 | Runtime安装、任务数据库、轮询/流式平台、Stage/Tool校验、生产FSM、自动重试、强杀Agent、伪称Checkpoint | 真实WorkBuddy证明不能直接消费Runtime或Launcher事实后才允许独立实现 | 可直用时零代码；否则计划、准备、退出、死亡、错误与结果指针原样可审计 |
| `runtime.py` | CLI、MCP、tasks；直连执行包内业务模块 | `DROP` | 无 | 导入执行包内业务实现、创建Project、操作Stage/Tool/Artifact/Checkpoint及写生产状态 | WorkBuddy读取已验证Guide后自行形成原生调用链 | Shell对Package业务内部导入和Artifact/Checkpoint写入为零 |
| `mcp_server.py`及旧 MCP 配置 | `setup.py`可选入口和 17 工具测试 | `DROP` | 无；CLI/MCP 都不是独立 MVP 模块 | 以 MCP 镜像或重建 Project/Stage/Tool/Artifact/Checkpoint/Task 控制面 | MVP 主链只经显式 WorkBuddy 入口和受控 Launcher | 包与活动配置中无生产 MCP 主链 |
| `model_config.py` | CLI config、MCP、两个Skill | `DROP` | 无 | Shell维护、推荐、排序或探测Provider/模型；把Key存在当能力 | Provider事实与选择只由WorkBuddy依据已验证Package合同并在授权内消费 | Shell的Provider/模型选择为零 |
| 两个`workbuddy-skill/**/SKILL.md` | WorkBuddy 显式生产入口与新手入口 | WorkBuddy入口 / `REWRITE` | 只保留一种遵守已冻结结果到动作接口的显式Skill，作为用户实际运行起点；原话转交、必要授权提示和结果呈现 | 同时恢复两个Skill或CLI/MCP生产入口；全局截获；第二聊天Agent；技术控制词进入`user_message` | 阶段5真实新会话命中唯一入口，经Locator重验必带工具链；需要声明支持的可选能力时提交单一请求，用户同意后再次调用并验证继续/固定降级 | literal消息不变、入口唯一、必带工具链不完整不启动、可选能力未就绪不执行对应能力、Shell不作技术选型；真实WorkBuddy证据只在阶段5形成 |
| 安装/卸载/升级/回滚脚本，便携包构建，Manifest/Lock，`setup.py`、`requirements.txt` | 用户安装入口、构建器、安装记录及安装测试 | 安装与生命周期 / `ADAPT` | 白名单、hash、staging、所有权、原子活动执行包指针、数据保留、失败恢复，以及完整私有Python/核心依赖、FFmpeg/ffprobe、Node/npm/npx工具链的组装和分发 | Shell与执行包混装、覆盖外来对象、内嵌未登记执行包、静默下载/降级、缺少任一Prerequisite仍发布、删除用户数据 | 安装记录、Package Registration、Package清单和全部必带工具链实际身份一致 | fresh/repair/upgrade/rollback/uninstall保持所有权与数据边界；普通用户无需预装三项Prerequisites |
| Provider凭据脚本与Launcher注入段 | 隐藏输入向导和WorkBuddy受控工具进程 | 六模块横切 / `ADAPT` | 当前用户加密、最小进程注入、只报告存在状态 | 明文进入聊天/参数/日志；Shell选Provider；Key存在代替调用与费用授权 | 单独授权后，仅WorkBuddy当前会话的固定工具进程消费所需凭据 | 明文canary为零，授权彼此独立 |
| 历史Core sync命名、旧tests、W0/报告/Prompt/架构文档 | 维护者发布、回归和历史追溯 | `HISTORICAL` | 外部包合同来源、消费者和故障夹具参考 | 继续同步旧上游main；为保留旧测试而恢复第二控制面；用历史PASS改变V2状态 | 后续任务必须为保留能力建立新消费者与当前执行包证据 | 可追溯但不计作V2实现或Gate PASS |

## 3. 收口

全部旧资产已映射到六个模块、`DROP`或`HISTORICAL`，无`UNKNOWN`。CLI/MCP不是独立MVP模块；其中只允许受控入口适配，其生产编排能力一律`DROP`。`347272c`的包内Python结论和`899592d`中Python核心依赖、FFmpeg、Node的锁定/组装模式移交Package交付与阶段2登记，不再进入阶段3；Stage3实现和closeout已经正式推广并`PASS_ACCEPTED`，旧全闭集入口、Shell-owned Lock和第二框架已`SUPERSEDED`。Stage4的`PackageToolDefinitionV1`、唯一`launch_session_tool(...)`与九值递归不可改写`LauncherReceiptV1`已经规划、实现、独立审查并正式推广为`PASS_ACCEPTED`；Stage5入口代码已正式交付但整体仍`IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`，当前正式树tracked精确40。最终Package/PackageRoot/Registration/Activation、最终安装Skill和真实WorkBuddy回执仍未创建或证明。

## 当前Stage 5映射边界（非实施授权）

已交付的 Stage 5 entry-code 只映射到现有五个实现/验收路径：`.github/workflows/ci.yml`、`workbuddy-skill/golden-key-openmontage/SKILL.md`、`golden_key_openmontage_workbuddy/workbuddy_entry_cli.py`、`tests/workbuddy/test_workbuddy_entry_cli.py`、`tests/workbuddy/test_repository_hygiene.py`。这些文件的存在和 tracked=40 不是对后续 R03/R04/R05/R06 实施的授权。R03 的 executable Skill bundle、R04 的 Installer/lifecycle 生产实现及其具体路径，必须在各自任务接管时从最新 formal 重新冻结；不得由本映射预造路径、模块或通用框架。

## [ORIGINAL R01 / FORMALLY CLOSED / PRESERVED] 当前 R01 证据边界（非实施授权）

R01 的临时 `golden-key-openmontage-r01-controlled-probe` 只用于核验 WorkBuddy bundled-script 执行合同，不改变六模块映射，也不新增生产模块、入口或 CLI/MCP 控制面。WorkBuddy `5.3.14` 的 HY3 受控路径没有产生独立原生 bundled-script invocation/tool event；协调者在 Bash/PowerShell 执行前停止。因此 R01 最终为 `BLOCKED_EXTERNAL_CONTRACT`，独立审查已批准并正式 fast-forward；用户已卸载临时 Skill，WorkBuddy 显示安装技能数为 `2`，任务历史保留，probe folder/ZIP 已删除。不产生脚本、Launcher、Package、Registration、Provider、媒体或 Stage6 证据。R02-R08 不得启动。

## 当前 R01 Sandbox Refresh1 映射边界（正式结果镜像，2026-08-22）

该 refresh1 不修改六模块映射，也不增加入口、生产模块、CLI/MCP 控制面。产品目标和 anti-expansion 均 `PASS`：WorkBuddy 仍是唯一 Agent/user entry，固定 CLI 仍只能是唯一 Skill 内部桥梁。官方 134420 说明 enterprise Skill scripts 在客户端沙箱执行。受控 WorkBuddy 客户端观察将 PowerShell 记录为允许的 `ELIGIBLE_CANDIDATE_SURFACE`，不是官方精确执行合同；134432 说明脚本/工作流封装、上传和调用；134516 仍为 CodeBuddy `PRODUCT_MISMATCH_NOT_CONTRACT_PROOF`。本轮阻断来自 Skill-root cwd/bundled-relative resource resolution 及精确 stdin/stdout/stderr/final-exit/timeout 合同缺失，而不是 PowerShell 非原生。

```text
task: V2-S5-R01-WORKBUDDY-SANDBOX-REFRESH1 / ACCEPTED_BLOCKED_EXTERNAL_CONTRACT / NO_ACTIVE_TASK
accepted_result: 6c20371f1c72ee9d55147e1ad7feb8ede201858f / tree 9eb4643f09d03cc9f39b0b46906773e5bcc9125d / docs_review=APPROVE_P0_0_P1_0_P2_0
base: 932bcabc5baf90d0190101b1039e4ccf087b2b08 / tree 2ed2cd0e67dd8628b7f0b1acf84df0a7d8b0d0fd / tracked 40
client: WorkBuddy 5.3.14 / HY3_ONLY / NEVER_AUTO / baseline=agent-browser,find-skills
probe: ISOLATED_D_DRIVE_TEMP_ROOT / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / hashes=A369E89912B51C1627C972A7DE8F82111E55E2909622CB2E0E3276B45331FFF9,8A1D38A65945CC99C4B7F8EE95FDF4FF744D105303BC9904E5915E630DF58359,2284E6D6FE8FFD38689A357DD0A6653CEB23B923F0C531BF9EAC376178E9A28A
install: safety_scan_not_skipped / no_non_high_risk_auto_install_selected / count_3 / client_id=workbuddy-skill-1787379691395 / SKILL_MD_NO_METADATA_NAME / body_first_line_match
read_and_attempt: SKILL_MD_AND_scripts\\r01_contract_probe.py_READ / physical_install_path_exposed_contract_deviation / SESSION_WORKSPACE_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / relative=.\\scripts\\r01_contract_probe.py / no_cd_no_absolute_no_guessing_no_mutation / skill_root_and_bundle_relative_not_exposed
result: USER_CANCELLED / POWERSHELL_NOT_STARTED / NO_SCRIPT_OR_IO_EXIT_TIMEOUT_EVIDENCE / BLOCKED_EXTERNAL_CONTRACT
review_and_chain: APPROVE_P0=0_P1=0_P2=0 / nonzero=NOT_RUN / timeout=NOT_RUN / R02-R08=NOT_STARTED_NOT_AUTHORIZED
reviewer_independent_observation: WORKBUDDY_5.3.14 / HY3 / USER_CANCELLED / NO_SUCCESS_STDOUT_STDERR_EXIT_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
cleanup: TEMP_SKILL_STILL_INSTALLED / USER_ACTION_REQUIRED / TASK_HISTORY_RETAINED / BASELINE_UNTOUCHED
computer_use: LOW_IMPACT_OPERATIONAL_ANOMALY / EXPLORER_MISTAKEN_FOR_FILE_PICKER / ALT+N_MAY_OPEN_TAB_OR_WINDOW / NO_PATH_INPUT_NO_FILE_SELECTION_NO_WRITE_DELETE / STOPPED_RECOVERED
```

该候选不产生脚本、Launcher、Package、Registration、Provider、媒体、Stage4或Stage6证据，也不改变 Stage5 `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`。旧 R01 的“Bash/PowerShell-only”事实只作为已关闭历史保留。
