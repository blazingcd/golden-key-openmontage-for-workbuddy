# WorkBuddy Shell V2 防漂移与Git生命周期

状态：`ACTIVE / FAIL_CLOSED`

```text
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_head_resolution: LIVE_REMOTE_REF_REQUIRED
formal_tree_resolution: LIVE_REMOTE_REF_TREE_REQUIRED
mirror_result: THIS_COMMIT
mirror_effect: ZERO_PRODUCT_STATE_CHANGE
mirror_repository_delivery_resolution: zero-write APPROVE exists AND LIVE_REMOTE_REF contains THIS_COMMIT
```

## 立即停止

出现以下任一情况时停止并报告`INCOMPLETE`或明确的范围冲突，不得顺手修复：

- 当前HEAD、实时正式远端、任务起点、允许路径、tracked计数或锁定blob不一致；
- 需要修改任务未授权路径，或与其他任务/用户改动重叠；
- 需要Shell选择或运行Pipeline、Stage、Provider、模型、媒体或创意；
- 需要实现未授权的Runtime、Launcher、WorkBuddy入口、状态结果转交或其他阶段；
- 需要扫描磁盘、猜测“最新”执行包、读取未验证Package Guide或修改外部执行包；正常PATH命令解析不等于扫盘，但只能产生待核验候选；
- 把阶段2的Registration/Locator实现和一次真实临时Package验证误报为“最终Release已保留”“生产Package已安装/登记”，或接受缺少Python私有环境、FFmpeg/ffprobe、Node/npm/npx任一必带项的最终Package；
- 需要把PackageRoot、Python、cwd、测试编号、重试或证据控制拼入literal `user_message`；
- 命令超时、输出截断、没有最终退出、证据缺失，或文档与任务账本冲突；
- 需要reset、stash、merge、rebase或改写已审对象。

以下范围扩张直接报告`STOPPED_SCOPE_EXPANSION`，不得以“预留”“通用化”或“后续复用”为理由继续：

- 没有已验证上游输入或直接下游消费者仍新增生产代码；
- 阶段3发现、下载、替换或回退到系统Python/FFmpeg/Node，借此补偿阶段2必带工具链不完整；
- 阶段3自动安装Remotion或HyperFrames、替WorkBuddy/OpenMontage选择渲染器，或准备用户未逐项批准的浏览器/附属资产；
- 把Remotion或HyperFrames写成必带Runtime，或因能力缺失、用户拒绝/暂缓集成而阻塞Package、项目、最终交付或其他已有/基础能力；
- 阶段3从默认Git/GitHub、Google、npmjs或其他未批准海外源下载，在批准大陆镜像失败后静默回退；
- 阶段3把PATH命中直接判为可用而不核验版本、路径、能力和登记身份，扫描盘符，或覆盖未知/外来目录；
- 把历史阶段3前置Gate重新激活，或否认已正式推广的Stage3实现/closeout；重新增加Package、Registration、Package绑定能力元数据、task-only登记验证或Stage 5输入Gate；
- 阶段3接受能力定义外的任意URL、命令或目标，或把批准OpenMontage能力定义扩张成通用包管理框架；
- 阶段3实现已标记`SUPERSEDED`的旧`prepare_runtime_on_demand(...)`签名、旧全闭集Runtime Lock或旧任务包，或恢复`host_tools.py`、通用下载器、CLI/MCP、服务、数据库等第二入口；
- 阶段3把可选能力写入Package、系统目录或必带工具链目录，修改系统PATH/注册表，要求管理员权限，或在失败后遗留staging/cache临时对象；
- 阶段3准备前为了发现或互斥而创建Runtime、缓存、锁文件或staging，或在没有该能力最终`PRESENT`或`INTEGRATED`证据时让阶段4把完整或不完整的已发布对象视为可执行能力；
- 阶段4接受任意Shell/命令、改写literal `user_message`、解析意图、读取未验证Package Guide、启动多个Agent、安装Runtime、选择渲染器、自动重试/重放、建立队列/调度/常驻服务/数据库、执行媒体生产、创建Artifact、推进Checkpoint或进入Agent业务内部；
- 阶段4基础固定工具调用未绑定有效Registration和必带工具链，或执行Remotion/HyperFrames时没有Stage 3对该能力给出的`PRESENT`或`INTEGRATED`证据；
- 阶段5并存多套生产入口、全局截获用户意图或成为第二聊天Agent；
- 阶段6在Runtime计划/准备事实或Launcher回执可直接消费时仍建立独立服务、数据库、轮询/流式平台，或自行安装Runtime、解释Artifact业务语义；
- 把建设顺序`阶段3 -> 阶段4 -> 阶段5 -> 阶段6`误写成最终用户调用顺序，或在阶段3准备后自动重试原生产请求；
- 改写已接受Stage3的一个公共入口、一个新增生产模块、`__init__.py`导出、一个直接测试及两项验收基础设施闭集；其他阶段超过其未来任务包明示的最小文件范围且没有单独的新授权与消费者证据。

## 产品边界

腾讯WorkBuddy是唯一运行中的Agent，读取已验证Package Guide后承担OpenMontage生产角色；不存在由Shell另行启动的OpenMontage Agent进程。Shell只负责六模块。仓库Agent不得运行视频Pipeline、Provider或媒体生产。SaaS Core不是Package Registration对象，也不在Shell V2当前实现范围。

金钥匙版交付包必须自带Manifest/Lock锁定的完整必带私有工具链：可用Python 3.10+环境及核心依赖、FFmpeg/ffprobe、Node/npm/npx；Node满足当前Package最高要求，当前不得低于HyperFrames所需的22。阶段2已经接受Registration/Locator实现，并以一次随后清理的真实临时Package完成组装、register、task-only activate和new-process locate验证；清理不重开、不重做阶段2，但也不等于最终Release、已安装生产PackageRoot或生产Registration已经存在。最终Package的持久组装、安装与生产登记仍是强制交付要求，但只属于后续最终交付或Installer收口任务，最迟在阶段5真实WorkBuddy生产验收前完成，绝不是阶段3或阶段4编码/规划前置。FFmpeg `gyan.dev`候选只属于Package组装供应链、hash、许可和分发审查，不再是阶段3面向终端用户的下载例外。

阶段3只对Remotion和HyperFrames执行有界探测、事实报告、零下载计划和用户逐能力批准后的受管集成。探测仅允许受管DataRoot、明确登记/配置候选路径和正常命令解析；禁止遍历盘符、系统软件清单、全局npm状态或猜目录。结果闭集为`DETECTION_REPORT/CONSENT_REQUIRED/INTEGRATED/SKIPPED/BLOCKED`，能力事实为`PRESENT/MISSING/INCOMPATIBLE/NOT_INTEGRATED`。缺失、拒绝或暂缓不是失败；Shell不选择渲染器，OpenMontage从实际可用能力中决定生产使用。唯一入口为`prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`。实现`a3f8959682d296301dc573c2835f8c705a52e8b2`和closeout `7c15aae4e77c579309312b21c79076f930970214`已正式推广，Stage3现为`PASS_ACCEPTED`；证据层为55 direct、10 hygiene、199 full，全部退出0且无skip，不包含真实下载、生产DataRoot、WorkBuddy、Stage4、Provider或媒体/视频E2E。

阶段3已接受Builder只编辑三个产品路径及`tests/workbuddy/test_repository_hygiene.py`、`.github/workflows/ci.yml`两项验收基础设施，当时正式树tracked精确35；Stage4随后严格按其五路径新增一个生产模块和一个直接测试并同步两项验收基础设施，Stage5 entry-code又使当前正式树tracked精确40。这不改变每阶段“一个生产模块、一个公共入口”的产品边界。

Stage4规划和实现均已`PASS_ACCEPTED`，`PackageToolDefinitionV1`固定工具身份合同及唯一`launch_session_tool(...)`和九值递归不可改写`LauncherReceiptV1`合同均已冻结。Stage4实现结果`fa9adb8470ab94b88ec9900ede03cb26f7de0ebd`经第八轮独立零写审查`APPROVE / P0=0 / P1=0 / P2=0`，严格在既定五路径内将tracked从35迁移到37并普通fast-forward；首个正式CI run `32367792637`仅暴露测试夹具错误假定GitHub `setup-python`包含`pyvenv.cfg`，不是生产Launcher finding。单测试路径修复`13a3227b0c55bbe9039b46d7e92eba822b48f57e`也经独立`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward，正式Ubuntu CI run `32369588814`为`357 passed / 1 skipped / exit 0`；Windows最终证据为158 direct、11 hygiene、358 combined，全部exit 0且无skip。Stage4 closeout固定历史锚点`b63d8c2bc2214bc39f18378dbe47057ef538301e`、tree `02814c6a4a483913e7b1abe3e9ee6d025236c951`已经独立`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward，closeout CI run `32371507874`在Ubuntu 24.04 / Python 3.11.16上`357 passed / 1 skipped`；其中`current_task=NONE / current_task_status=NO_ACTIVE_TASK / next_authorized_task=NONE`是`HISTORICAL_STAGE4_CLOSEOUT_CONTEXT`，不覆盖当前Stage5 authority。`mirror_result/mirror_effect/mirror_repository_delivery_resolution`只自解析镜像仓库交付，不形成当前任务、不改变或重新门禁既有Stage4 `PASS_ACCEPTED`。当前Locator仍只重验Registration、PackageRoot、必带工具链、Guide、Manifest和Lock；Stage4从批准Package定义及最终交付/Installer owner提供的release-specific定义取得工具身份，不得猜Guide、重开Stage2、选择Provider/Runtime或扩大路径。缺具体Release定义实例时必须fail closed且spawn 0。WSL只用于临时Linux等价验证并已清理关闭，不是运行依赖。真实生产WorkBuddy/Launcher会话、Stage6、Provider/媒体执行及final Package物化/生产登记仍为`NOT_GRANTED`或未证明。

[HISTORICAL / SUPERSEDED_BY_V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1] 前一轮Stage5规划收口候选只记录如下后续镜像：独立Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 并普通fast-forward进入正式分支后，Stage5 planning 才成为`PASS_ACCEPTED`；随后`current_task=NONE`，下一任务精确为`V2-S5-WORKBUDDY-ENTRY-BUILDER1`。用户已明确授权“启动阶段五实施”，但Builder必须从届时最新formal接管，并只使用已冻结的五路径实现白名单；该候选不授权真实WorkBuddy生产验收、Provider/媒体、final Package/Registration或Stage6。当前实施结果及本轮六文档closeout状态以紧接的当前镜像为准。

外部Package Guide只有在Registration身份完整验证、Locator返回已验证身份后，才可由对应下游消费者读取。本仓库根`AGENT_GUIDE.md`只治理Shell V2，不能替代或预先信任外部Guide。

`user_message`只包含用户真实会说的业务请求、素材、事实、授权和期望结果。包身份、路径、Python、cwd、命令、测试、停止条件和证据采集只进入独立的`executor_controls`。

## Git任务生命周期

- Builder分支是单任务临时隔离；不得发展为长期分支。
- Reviewer独立只读，不建立长期审阅分支，不修改结果制造APPROVE。
- 用户接受或Reviewer批准不等于已交付。
- 任务或阶段只有在已审结果进入`origin/codex/workbuddy-shell-v2`后才算仓库完成。
- 正式主线只允许fast-forward到已审集成结果；不得merge/rebase推进中的`main`或旧长期分支。
- 推广后，所有已完全合入且无未合入commit的临时远端分支必须删除。
- 本地分支仅在对应worktree关闭后安全删除；不得清理其他任务的worktree、branch、stash、tracked、untracked或ignored现场。
- 下一阶段接管只能使用正式主线最新精确commit，不能使用任务分支。

只精确暂存授权路径，禁止`git add .`。正式状态只以`TASK-REGISTER.md`为准；Git历史保存旧Prompt、计划、报告和证据，但不恢复其活动授权。

## 证据边界

静态检查、单元测试、Package Registration成功、ZIP、Guide读取或旧运行历史都不能证明真实Installer、Runtime、Launcher、WorkBuddy、OpenMontage生产、Provider、媒体、SaaS或业务效果。任何Gate对象不一致或无最终退出一律不是PASS。

## [HISTORICAL / SUPERSEDED_BY_V2-S5-R00-REMAINDER-PLAN-STATE-CORRECTION1] Stage 5实施与入口收口守卫 (2026-08-21)

本段是当前收口镜像，不能把候选状态提前写成正式交付：Stage 5 planning 已为 `PASS_ACCEPTED`；`V2-S5-WORKBUDDY-ENTRY-BUILDER1` 已 `CONSUMED_COMPLETE`，正式实施结果为 commit `0e7a0be65877b03fb386e1c6c6bc258c0b27db6c`、tree `85c266edb7349c940e8cd45870cc0538c95726c0`、parent `aa70c2cf9b6b4a29517d7354f0239ea0cdc9a5d3`，tracked 从 37 到 40，精确五路径。独立实施 Reviewer 为 `APPROVE / P0=0 / P1=0 / P2=0`；Windows 最终证据为 direct 19 passed、hygiene 11 passed、full 377 passed，均 final exit 0；正式 CI run `32489111184` 为 completed/success，headSha 为上述实施 commit，Ubuntu / Python 3.14.7，376 passed / 1 skipped / final exit 0。

当前任务 `V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1` 只允许 `DOCS_ONLY / EXACT_6_PATHS / ZERO_PRODUCT_STATE_CHANGE`。只有该候选经独立 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 并普通 fast-forward 进入正式分支后，`stage_5_implementation` 才可成为 `PASS_ACCEPTED`；候选本身不得自称已交付。收口完成后镜像必须为 `current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE`，不得自动授权真实 WorkBuddy production acceptance、final Installer-stamped Skill、final Package materialization/Registration、Provider/media 或 Stage6。

实施入口边界仍是 WorkBuddy 唯一 Agent/用户入口，一个 Skill 到 package-private fixed CLI，再到一次且仅一次 Stage4 调用；无 console script、subcommands、router、MCP、第二 Agent、retry 或 replay。实施的精确五路径为：`.github/workflows/ci.yml`、`workbuddy-skill/golden-key-openmontage/SKILL.md`、`golden_key_openmontage_workbuddy/workbuddy_entry_cli.py`、`tests/workbuddy/test_workbuddy_entry_cli.py`、`tests/workbuddy/test_repository_hygiene.py`。本六文档收口期间禁止代码、测试、CI、真实客户端、Stage4/Provider/media、final Package/Registration 和 Stage6 操作；静态/direct/hygiene/CI 证据与真实 WorkBuddy、业务和 E2E 证据必须分层，后者仍 `NOT_PROVED / NOT_GRANTED`。

## [HISTORICAL / CONSUMED_BY_V2-S5-R01] Stage 5剩余计划守卫（V2-S5-R00，2026-08-21）

当前唯一live状态为 `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`。入口代码/CLI/LauncherReceiptV1/Reviewer/CI是已交付子项；不得把它们或旧closeout候选写成Stage5整体PASS。整体PASS必须同时有：retained final Release+PackageRoot、production Registration+Activation+new-process Locator、zero-placeholder唯一final Skill、HY3真实WorkBuddy真实`LauncherReceiptV1`、以及独立Review+formal Git/CI+无歧义live authority。

R00 已正式推广并消费；其 `current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE` 是历史交接状态。R01 已于 2026-08-22 单独授权并执行；最终结果为 `BLOCKED_EXTERNAL_CONTRACT`，独立审查已批准并正式 fast-forward，因此依赖严格 `R01 -> R02 -> R03 -> R04 -> R05 -> R06 -> R07 -> R08` 在 R01 停止，R02-R08 未启动、未授权。

## [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / ORIGINAL R01 / FORMALLY CLOSED / PRESERVED] 当前 Stage 5 R01 防漂移守卫（2026-08-22）

产品目标回读与范围扩张审计均为 `PASS`：WorkBuddy 仍是唯一 Agent/user entry，Shell 仍只负责六模块；固定 CLI 只允许作为唯一 Skill 内部桥梁，不得演变为任意 CLI/Shell 旁路。R01 使用 WorkBuddy `5.3.14`、HY3（不使用 Auto）和唯一临时 probe Skill；上传安全扫描未跳过，基线两个 Skill 未触碰。客户端仅暴露 Bash/PowerShell，未产生独立原生 bundled-script invocation/tool event，协调者在任何 shell/terminal 执行前停止。

因此 R01 不得把 Skill 上传/安装、模型文字、marker、JSON 或截图当作脚本执行证据；不运行 nonzero/timeout，不记录或复述物理 cwd，不伪造 stdout/stderr/exit/timeout。R01 结果固定为 `BLOCKED_EXTERNAL_CONTRACT`，独立 zero-write Review 已 `APPROVE / P0=0 / P1=0 / P2=0` 并正式 fast-forward；用户已卸载临时 Skill，WorkBuddy 显示安装技能数为 `2`，任务历史保留，D 盘精确隔离 probe folder/ZIP 已删除，基线两个 Skill 保持不变。R02-R08 必须保持 `NOT_STARTED / NOT_AUTHORIZED_BY_CHAIN`。

## [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT] 当前 R01 Sandbox Refresh1 防漂移守卫（2026-08-22，独立文档审查已通过）

本 refresh1 独立于原始 R01 已关闭记录。产品目标回读与范围扩张审计均为 `PASS`：WorkBuddy 是唯一 Agent/user entry，固定 CLI 只可作为唯一 Skill 内部桥梁，不构成 blanket CLI ban、第二入口或第二控制面。官方 134420 已确认 enterprise Skill scripts 在客户端沙箱执行。受控 WorkBuddy 客户端观察将 PowerShell 记录为 `ELIGIBLE_CANDIDATE_SURFACE`，不是官方精确执行合同；禁止再把 PowerShell 非原生当作阻断。134432 只证明 Skill 脚本/工作流打包、上传和调用形态；134516 必须保持 CodeBuddy `PRODUCT_MISMATCH_NOT_CONTRACT_PROOF`。合同仍缺 Skill-root cwd、bundled-relative resource resolution、stdin/stdout/stderr/final-exit/timeout 精确语义。

```text
task: V2-S5-R01-WORKBUDDY-SANDBOX-REFRESH1 / accepted_blocked_external_contract / no_active_task
accepted_result: 6c20371f1c72ee9d55147e1ad7feb8ede201858f / tree 9eb4643f09d03cc9f39b0b46906773e5bcc9125d / docs_review=APPROVE_P0_0_P1_0_P2_0
base: 932bcabc5baf90d0190101b1039e4ccf087b2b08 / tree 2ed2cd0e67dd8628b7f0b1acf84df0a7d8b0d0fd / tracked 40
client: WorkBuddy 5.3.14 / HY3_ONLY / NEVER_AUTO / baseline_skills=agent-browser,find-skills
probe: ISOLATED_D_DRIVE_TEMP_ROOT / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / CLEANUP_COMPLETE / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
hashes: SKILL=A369E89912B51C1627C972A7DE8F82111E55E2909622CB2E0E3276B45331FFF9 / SCRIPT=8A1D38A65945CC99C4B7F8EE95FDF4FF744D105303BC9904E5915E630DF58359 / ZIP=2284E6D6FE8FFD38689A357DD0A6653CEB23B923F0C531BF9EAC376178E9A28A
install_identity: safety_scan_not_skipped / no_non_high_risk_auto_install_selected / count_3 / workbuddy-skill-1787379691395 / SKILL_MD_NO_METADATA_NAME / body_first_line_match
native_read: SKILL_MD_AND_scripts\\r01_contract_probe.py_READ / physical_install_path_exposed / sensitive_minimization_contract_deviation / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
success_attempt: relative=.\\scripts\\r01_contract_probe.py / SESSION_WORKSPACE_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / no_cd / no_absolute_path / no_guessing / no_command_mutation / skill_root_cwd=NOT_EXPOSED / bundle_relative=NOT_EXPOSED
stop_and_result: UI_USER_CANCELLED / POWERSHELL_NOT_STARTED / NO_SCRIPT_STDOUT_STDERR_FINAL_EXIT_CWD_TIMEOUT / BLOCKED_EXTERNAL_CONTRACT
reason: MISSING_SKILL_ROOT_CWD_AND_BUNDLE_RELATIVE_RESOLUTION / NOT_POWERSHELL_NON_NATIVE
review_chain: APPROVE_P0=0_P1=0_P2=0 / nonzero=NOT_RUN / timeout=NOT_RUN / R02-R08=NOT_STARTED_NOT_AUTHORIZED
reviewer_independent_observation: WORKBUDDY_5.3.14 / HY3 / USER_CANCELLED / NO_SUCCESS_STDOUT_STDERR_EXIT_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
cleanup: COMPLETE / USER_UNINSTALLED_TEMPORARY_SKILL / TEMP_SKILL_ID=workbuddy-skill-1787379691395_NOT_IN_INSTALLED_LIST / WORKBUDDY_MY_INSTALLED_SKILLS_2=agent-browser,find-skills / TASK_HISTORY_RETAINED / BASELINE_UNTOUCHED / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
computer_use: LOW_IMPACT_OPERATIONAL_ANOMALY / EXPLORER_MISTAKEN_FOR_FILE_PICKER / ALT+N_MAY_OPEN_TAB_OR_WINDOW / NO_PATH_INPUT_NO_FILE_SELECTION_NO_WRITE_DELETE / STOPPED_RECOVERED
```

任何后续执行若缺少 Skill-root cwd 或 bundled-relative event，必须立即 `BLOCKED_EXTERNAL_CONTRACT`；不得以模型文字、物理路径、PowerShell shell transcript、marker、JSON、截图或推理替代。候选不授权 R02-R08、Provider、媒体、Package、Stage4、Stage6 或生产流程。

## [HISTORICAL / CONSUMED_BY_V2-S5-R02] 当前 Stage 5 R01 验收契约纠正防漂移守卫（2026-08-22）

原始 R01、Sandbox Refresh1 和 Expert Entry Feasibility 记录已标为 `HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT`；旧阻断/不完整事实保留，不作为当前 R01 入口面硬门。本节是用户基于最初产品目标作出的验收归属纠正，不是新官方证据。

```text
r01_acceptance: ENTRY_SURFACE_ACCEPTED / EXECUTION_PROOF_DEFERRED_TO_R03_R07
r01_entry_surface: SKILL_PACKAGING / UPLOAD / INSTALL / IDENTITY_APPEARED / SELECTION_HIT / CLIENT_SANDBOX_SCRIPTS / POWERSHELL_ELIGIBLE_CANDIDATE_SURFACE
r01_deferred_contract: SKILL_ROOT_CWD / BUNDLED_RELATIVE_RESOURCE_RESOLUTION / STDIN / STDOUT / STDERR / FINAL_EXIT / TIMEOUT / NOT_R01_HARD_GATE / DEFERRED_TO_R03_R07
deferred_chain: LOCATOR -> FIXED_POWERSHELL_OR_PRIVATE_CLI -> LAUNCHER_RECEIPT / IMPLEMENTATION_AND_REAL_PROOF_DEFERRED_TO_R03_R07 / NOT_CURRENTLY_PROVED
no_overclaim: NO_SCRIPT_EXECUTION / NO_STDOUT_STDERR_EXIT_CWD_TIMEOUT / NO_LAUNCHER_RECEIPT / NO_STAGE5_PASS
hy3_policy: CURRENT_TEST_MODEL_ONLY / COST_AVOIDANCE / PRODUCT_MODEL_NEUTRAL / USER_SELECTED_MODEL / NOT_A_SKILL_OR_EXPERT_OR_SYSTEM_DEPENDENCY
current_task: HISTORICAL / NONE / NO_ACTIVE_TASK / R01_CORRECTED_ACCEPTED_ENTRY_SURFACE
next_authorized_task: HISTORICAL / V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1 / R02_AUTHORIZED_ONLY / R03-R08_NOT_AUTHORIZED
```

安全边界不降低：仍只有一个 WorkBuddy Skill 和一个用户入口；固定 CLI 只能是该 Skill 内部桥；禁止任意 CLI、路径猜测、扫盘、PATH fallback、MCP、第二 Skill、第二 Agent、router、retry 和 replay。最终 Skill 必须使用 Installer-stamped locator；实际 Locator 到固定 PowerShell/private CLI 再到 receipt 的实现与真实证据只能在 R03/R07 受相应授权时形成。授权客户端测试若使用模型，遵守用户指定 HY3/NEVER_AUTO，但 HY3 仅为当前测试模型与成本控制，不锁定产品模型或系统依赖。

## Current Stage 5 R02 Package Release/Tool Definition Binding1 stop guard (2026-08-22)

R02 的 published candidate 身份与批准 source subtree 匹配，但不是可绑定的 final Release。远程递归树完整且 `2614` entries 中绑定相关路径为 `0`，本地同树不可变审计为 `2155` blobs；Release/lock 元数据没有真实 safe fixed tool 或 release-specific `PackageToolDefinitionV1`/Manifest/Lock binding。禁止从上千媒体工具中随意选择，禁止造 fixture/definition 或修改外部 Package。

```text
task_id: V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1
r02_result: BLOCKED_PACKAGE_RELEASE / PUBLISHED_CANDIDATE_IDENTITY_VERIFIED / MISSING_SAFE_FIXED_TOOL_AND_RELEASE_SPECIFIC_DEFINITION
current_task: NONE / NO_ACTIVE_TASK / R02_CLOSED_BLOCKED_PACKAGE_RELEASE
next_authorized_task: NONE / PACKAGE_OWNER_RELEASE_BINDING_REAUTHORIZATION_REQUIRED / R03-R08_NOT_AUTHORIZED_BY_CHAIN
unblock_condition: SEPARATE_PACKAGE_OWNER_APPROVAL_AND_INDEPENDENT_SAFE_FIXED_TOOL_DEFINITION_MANIFEST_LOCK_VERIFICATION / THEN_REAUTHORIZE_R02
product_goal_anti_expansion: PASS / WorkBuddy_ONLY_AGENT_USER_ENTRY / FIXED_CLI_ONLY_SOLE_SKILL_INTERNAL_BRIDGE / NO_ARBITRARY_MEDIA_TOOL_SELECTION_OR_FIXTURE_OR_DEFINITION_OR_EXTERNAL_PACKAGE_MODIFICATION
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
side_effects: NO_CLIENT / NO_PACKAGE_MATERIALIZATION / NO_REGISTRATION / NO_STAGE4 / NO_PROVIDER_MEDIA_STAGE6_OR_PRODUCTION
```

## 项目级架构纠偏审计 Phase A 防漂移镜像（A7 docs-only 已正式推广，2026-08-22）

本节是 A0-A6 独立批准结论的防漂移落点。A7 docs-only 结果已正式推广；本节只固化审计结果和纠偏计划，不把审计完成写成产品完成。

```text
task_id: V2-PROJECT-ARCHITECTURE-RECOVERY-PHASE-A1
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_baseline_parent: f338d9d50cad2cccf1398438ad4a8c8d45127a21 / tree 5ef5e8e524412f6220ad31f2cc38448c6b1dac8b
phase_a_audit_commit: 4727c5efda6ae53194ff2c16dd224c67178e8d8d
phase_a_audit_tree: ac6206950b36f71663eddfb89b7e311aa85b53e6
phase_a_status: A0-A6_APPROVED / A7_DOCS_FORMALLY_PROMOTED
scope: EXACT_SIX_EXISTING_AUTHORITY_FILES / DOCS_ONLY
effect: ZERO_PRODUCT_STATE_CHANGE
review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_ZERO_WRITE
formal_promotion: ORDINARY_FAST_FORWARD / FORMALLY_PROMOTED / commit=4727c5efda6ae53194ff2c16dd224c67178e8d8d / tree=ac6206950b36f71663eddfb89b7e311aa85b53e6 / ci_run=32615371879 / completed=success / headSha=4727c5efda6ae53194ff2c16dd224c67178e8d8d
task_artifacts_cleanup: ORIGINAL_PHASE_A_WORKTREE_LOCAL_AND_REMOTE_TASK_BRANCH_CLEANED
state_closeout: THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR
verification: NOT_RUN_DOCS_ONLY (except mechanical diff/status/object checks)
phase_b: NOT_AUTHORIZED / A7_HISTORICAL_SNAPSHOT
```

### 不可漂移的架构判断

唯一运行 Agent 是 WorkBuddy；OpenMontage Agent 只是 WorkBuddy 读取已验证 Guide 后承担的逻辑角色。Shell 只保留六模块，固定 CLI 只能是唯一 Skill 内部的无智能 transport。任何第二 Agent、第二 Director、FSM、Supervisor、Router、MCP、任意 CLI、Provider/Renderer 选择、媒体控制面或自动 retry/replay 都是禁止扩张。

Guide-read 的 fail-closed 顺序必须是：`Registration identity validation -> Locator verified PackageRoot/Guide identity/hash -> WorkBuddy reads Guide/Manifest/Pipeline/Stage Skills -> WorkBuddy decides -> fixed transport -> deterministic child -> mechanical receipt -> WorkBuddy result`。缺少可独立观察的 WorkBuddy/client Guide-read、identity/hash、决策主体或顺序证据时，状态为 `INCOMPLETE/NOT_PROVED`；模型自报、child 自报、普通日志、静态测试、CI、Skill 命中、CLI 启动或 receipt 不能替代。

### 历史 PASS 与当前状态分离

```text
stage_1_current_disposition: KEEP
stage_2_current_disposition: KEEP_WITH_NARROWING
stage_3_current_disposition: KEEP_WITH_NARROWING
stage_4_historical_contract: PASS_ACCEPTED_MECHANICAL_CONTRACT
stage_4_current_disposition: HISTORICAL_PASS_ONLY
stage_5_current_disposition: REWORK / REAL_INTEGRATION_INCOMPLETE
stage_6_current_disposition: INSUFFICIENT_EVIDENCE
```

不得把 Stage 4 测试/CI 的历史合同 PASS 改写为失败，也不得把它升级为真实 WorkBuddy/业务 E2E PASS。Stage 2 临时 assembled-Package proof 不得升级为 final PackageRoot、生产 Registration/Activation 或 Installer proof。Stage 3 不得探测、下载或替换 Node/npm/npx；最终 Package 必须始终自带 Node.js `22+`、npm、npx 和其他必需 private toolchain。

### [HISTORICAL / SUPERSEDED_BY_2026-08-24_REBASELINE] R02 责任归属守卫

```text
r02_live_status: R02_CLOSED_BLOCKED_PACKAGE_RELEASE
recommended_reclassification: SHELL_INSTALLER_ADAPTER_BINDING_REQUIRED + REAL_FIXED_CHILD_UNVERIFIED
recommended_reclassification_state: NOT_YET_EFFECTIVE
binding_delivery_owner: V2 Final-delivery Installer / Release Assembly Owner
binding_carrier: FINAL_WORKBUDDY_PACKAGEROOT / INDEPENDENT_SHELL_ADAPTER_SUBTREE
shell_owns: BINDING_SCHEMA_AND_CONSUMER
0_3_24: IMMUTABLE / NO_WORKBUDDY_ADAPTER_EMBEDDING
```

不得直接改写 R02 live 状态。历史 0.3.24 对象缺少 WorkBuddy 专用 adapter/definition 的观察不等于共享 Package 应内置该职责；当前纠偏应由最终 Installer 在 final PackageRoot 中装配独立 adapter、fixed child 和 Manifest/Lock/hash。任何修改历史 0.3.24 源码、Release、Lock、Guide 或将 WorkBuddy 入口嵌入其中，立即 `BLOCKED_SCOPE_VIOLATION`；未来调用/验证只允许使用当前 B01 镜像登记的 0.3.25 输入。

### [HISTORICAL / SUPERSEDED_BY_2026-08-24_REBASELINE] B01-B07 纠偏任务串行守卫

A7 当时的 B01-B07 顺序及 21 字段只作历史 provenance，已无执行效力；当前唯一顺序是本文末尾重基线守卫中的 C01-C07。

```text
B01: freeze_binding_and_Guide_read_contract
B02: implement_one_Skill_one_fixed_transport_one_deterministic_child
B03: final_PackageRoot_Installer_lifecycle_and_production_Registration
B04: official_fixed_control_group_real_acceptance
B05: same_Shell_same_assembly_0_3_25_switch_acceptance
B06: Stage5_closeout_only_HANDOFF_TO_B07_ONLY
B07: external_portrait_business_gate
after_B07_only: PROMOTE_AND_CLEANUP / ordinary_fast_forward_only
```

B04 必须先用固定 official control package，B05 只能替换 Package 为固定 0.3.25，并保持 Shell、Installer assembly、Skill、Launcher、用户请求和验收方法一致；不能同时修改 Shell 和 Package，不能复用旧 PackageRoot/Registration。B06 不得推广、删除、开发 Stage 6；B07 之前不得执行唯一 promotion/cleanup 路径。B07 失败或证据缺失时保持 `INCOMPLETE`，不猜测。

### Git、残留对象和 A7 边界

旧 Stage 2 分支 `codex/v2-s2-official-package-alignment-b1`（HEAD `86a7902465d8e215e0830b9640e7222d7c7f5188`）只保留历史，禁止合并或删除；两个 dirty detached worktree `C:\Users\blazi\.codex\worktrees\aef5\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2` 与 `C:\Users\blazi\.codex\worktrees\df76\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2`（均在 `4d74d6576773dc9d383efec091bdc8d42f0d480c`）不复制、不提交、不回收、不删除。它们不是权威状态。

A7 状态收口仍只涉及以下六个现有文件：`AGENT_GUIDE.md`、`PROJECT-STATE.md`、`docs/workbuddy/v2/TASK-REGISTER.md`、`docs/workbuddy/v2/PROJECT-CHARTER.md`、`docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`、`docs/workbuddy/v2/DRIFT-GUARD.md`。禁止新文件、代码、测试、CI、Package、外部仓库、客户端、Provider、媒体、Registration、Activation、DataRoot。审计结果已由用户批准并以普通 fast-forward 正式推广；本次状态收口使用 `THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR`，测试标签固定为 `NOT_RUN_DOCS_ONLY`。原 Phase A 任务工作树、本地任务分支和远端任务分支已清理；A7 的 `NOT_AUTHORIZED` 与下方 B01-only 都只作历史，当前权威是 2026-08-24 重基线的 `PAUSED_BY_OWNER`；旧 Stage 2 分支和 dirty worktrees 仍需保留，除非另有授权。

## [HISTORICAL / SUPERSEDED_BY_2026-08-24_REBASELINE] Phase B 执行镜像：B01 已授权（2026-08-23）

本节只保存 2026-08-23 当时的 B01-only 授权和 package 输入，已被 2026-08-24 重基线取代，不提供当前执行授权。

```text
phase_b_authorization: USER_AUTHORIZED_2026-08-23 / B01_ONLY
current_task: B01 / CURRENT_DOCS_ONLY_CONTRACT_FREEZE
b01_scope: FREEZE_BINDING_GUIDE_READ_CONTRACT + PACKAGE_INPUT_MIGRATION + AUTHORIZATION_MIRROR
b01_effect: ZERO_PRODUCT_STATE_CHANGE / DOCS_ONLY
b01_not_do: NO_PRODUCT_CODE_EXECUTION_OR_B02_B03_B04_B05_B06_B07_EXECUTION / NO_PACKAGE_OR_EXTERNAL_REPO_CHANGE / NO_CLIENT_SKILL_REGISTRATION_ACTIVATION_PROVIDER_MEDIA_DATAROOT
b01_tests: NOT_RUN_DOCS_ONLY
official_current_input: checkout=D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-main-cd9f3c1f / commit=cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / tree=6cd1961d552dd9d2bcfba990b80ac06edfe4b061 / state=DETACHED_CLEAN
golden_key_current_input: release=0.3.25 / checkout=D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673 / commit=73cab67322451601a824875c0e426067d736dd44 / tree=29231e0464fa4bc7533c1928415849e9b3a48e7c / parents=ef5f5b58fa1c2b494b0154989cf0e4e36615a701+cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / state=DETACHED_CLEAN
historical_only_inputs: official_old=4eab34c5cfcccaa4f1970554928feccce73ee930,95e1c3d0ab93482159818560f6a8c8e866b9139f / Golden_Key_0.3.24=ef5f5b58fa1c2b494b0154989cf0e4e36615a701 / provenance_only / NEVER_FUTURE_CALL_OR_VERIFY
b01_result: THIS_COMMIT
b01_review_gate: INDEPENDENT_ZERO_WRITE_APPROVE_REQUIRED / NO_RESULT_PREWRITTEN
b01_repository_delivery_resolution: INDEPENDENT_ZERO_WRITE_APPROVE + LIVE_FORMAL_REF_CONTAINS_THIS_COMMIT + EXACT_HEAD_CI_SUCCESS
next: B02_ONLY_IF_B01_DELIVERED
b02_b07: BLOCKED_BY_CHAIN
builder_boundary: NO_FORMAL_PROMOTION
```

## [HISTORICAL / SUPERSEDED_WHEN_D_ROUTE_CANDIDATE_IS_FORMALLY_PROMOTED] 纠偏重基线防漂移守卫（2026-08-24）

```text
phase_b: PAUSED_BY_OWNER
execution_authority: NONE
historical_only_next_candidate: C01_WORKBUDDY_NATIVE_INTERACTION_PROOF / SUPERSEDED_WHEN_D_ROUTE_CANDIDATE_IS_FORMALLY_PROMOTED
authorization_rule: OWNER_EXPLICIT_PER_TASK
review_rule: POST_STEP_GOAL_AUDIT + INDEPENDENT_ZERO_WRITE_REVIEW
historical_promotion_rule: ONLY_AFTER_C07 + SEPARATE_OWNER_APPROVAL + ORDINARY_FAST_FORWARD / SUPERSEDED_WHEN_D_ROUTE_CANDIDATE_IS_FORMALLY_PROMOTED
```

每个未来任务开始前必须重读最初 V2 handoff 和 exact official `AGENT_GUIDE.md`；结束后必须回答五个问题：普通用户是否仍只说业务需求；WorkBuddy 是否仍是唯一 Agent 和决策者；是否真实读取并遵守 Guide/manifest/Stage Skills；Shell 是否仍只是六模块机械支持；本步证据是否足以证明所声明的状态。任一答案为否或未证明，立即停止，不能用下一步补证或修复。

硬停止条件：

- 模型需要拼 transport JSON、hash、schema、绝对路径、环境白名单，或写/运行辅助脚本；
- “一个入口”再次被解释成“整个生产请求只能一次固定 child/spawn”；
- Shell 或 fixed child 承担 Pipeline/Stage/Reviewer/Checkpoint/Provider/Renderer/媒体决策；
- WorkBuddy sandbox 注入的宿主环境变量被当作产品错误，而不是在 child 构造边界收敛；
- direct WorkBuddy fallback、mock、self-report、静态测试或 receipt 被升级成真实 OpenMontage 成功；
- B03/B04 旧 assembly、Registration、Skill 或 evidence 被复用为 fresh acceptance；
- official/GK exact identity 变化，或使用历史 official/0.3.24 作为未来调用输入；
- 台账未先更新真实状态、未独立审查、越过 Owner 授权或扩大到 Package/Provider/media。

不得 reset、删除或改写 A7/B01-B04 历史。旧合同可保留为 provenance，但不得继续提供执行授权。

禁止再以 `A0-A6_APPROVED` 这一聚合字符串替代逐项证据。任何未来纠偏计划必须分别给出 A0-A7 的事实、未证明项、处置与因果影响；Reviewer 只能批准 exact 候选内容，不能把“文档内部一致”升级为“产品目标已经证明正确”。

## 新任纠偏路线候选防漂移守卫（2026-08-24）

Append-only precedence：本候选未正式推广时不改变正式 ref 中暂停的 C 路线；本候选经 Reviewer、Owner plan-promotion approval、ordinary fast-forward 和远端对象核验后，所有较早的 C01-C07 `current/next/only/promotion_rule` 字段立即成为历史，禁止再用于路由。最新 D 路线仍无执行 authority，D01 必须另获授权。

```text
candidate_status: NOT_FORMAL / DOCS_ONLY
execution_authority: NONE
current_product_task: NONE
forbidden_old_route: C01 -> C07 / SUPERSEDED_CANDIDATE / NEVER_EXECUTE
only_candidate_route: D01 -> D02 -> D03 -> D04 -> D05 -> D06 -> D07 -> D08
plan_promotion_rule: REVIEWER_APPROVE + OWNER_PLAN_PROMOTION_APPROVAL + FORMAL_REF_CONTAINS_PLAN
authorization_rule: FORMAL_PLAN_PROMOTION_THEN_OWNER_EXPLICIT_PER_TASK
review_rule: DIFFERENT_WORKER_AND_ZERO_WRITE_REVIEWER + PLAN_GATE_OR_EXECUTION_GATE_Q1_Q10
per_task_result_promotion_rule: EACH_D_TASK_REVIEWER_APPROVE + SEPARATE_OWNER_RESULT_PROMOTION_APPROVAL + ORDINARY_FAST_FORWARD
project_closeout_promotion_cleanup_rule: ONLY_AFTER_D08 + SEPARATE_OWNER_APPROVAL + ORDINARY_FAST_FORWARD + MANIFEST_BOUNDED_CLEANUP
```

新的硬停止条件：

- D01 未以无 Package、无产品代码的 probe 证明 native surface，就开始冻结接口或修改代码；
- Skill ZIP 因 official/GK 切换而改变，或任何 Package identity/hash/path/environment 出现在模型可见 Skill/提示中；
- Installer 继续只存在 D 盘临时脚本、evidence helper 或一次性 assembly，而不是版本化本仓库产品；
- Shell/adapter 决定 Pipeline、Stage、调用顺序、Reviewer、Checkpoint、Provider、Renderer 或媒体内容；
- D06 使用 `framework-smoke`、只到 receipt/首个 Artifact、没有两次完整本地成片，或把 D07/D08 当作修复窗口；
- D07 除 Package-derived root/Registration/hidden binding/resource identity 外改变任何 control 输入、Skill 字节或方法；
- D08 在业务验收中修代码、补媒体逻辑、静默使用 Provider/费用，或同时执行推广/清理；
- 把 Reviewer 的规划批准写成产品 PASS、D01 授权或正式 authority；
- 任一任务没有 exact input commit/tree、允许路径、正反测试、named owner、零写 Reviewer、十问结果及下游阻断条件。

每一步开始时重读届时正式 `AGENT_GUIDE.md`、TASK-REGISTER、原始 V2 handoff 和 exact external authority；只能从最新正式 HEAD 建新分支/worktree。每一步结束先记录事实与十问 `EXECUTION_GATE`，再由独立 Reviewer 审查 exact 候选；任何 repair 必须留在当前任务并重审，不得转嫁下游。D08 之后仍只生成 promotion/cleanup manifest，实际 fast-forward、远端/CI 核验和限定清理须另获 Owner 授权。

## D01 合同纠偏候选 Replacement1 防漂移补充（2026-08-24）

这是六文档 append-only 候选守卫，不是正式 authority。只有独立零写 Reviewer 通过、单独 Owner plan-promotion approval、ordinary fast-forward 进入 live formal ref 且远端对象核验完成后，才可成为最新 planning mirror；之后仍需单独 Owner D01 execution authorization。基线必须保持 `99bc5c3d727671d7d2ea7313c6851792583efe66` / tree `b995a9a02add77f1e61769f364dd86b341137403`；当前为 `DOCS_ONLY / CANDIDATE_NOT_FORMAL / NOT_RUN_DOCS_ONLY`。独立纠偏 Reviewer 通过 exact final six-doc diff 后才可形成候选 commit；push 与正式推广分别等待后续决定。禁止 pytest、WorkBuddy/probe/Product/Package/Provider/media 行动。

漂移硬门按固定顺序执行：Gate0 只读核验 live formal、正式 authority 与当前 WorkBuddy binary identity；B04 read scope 仅限 `D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B04_official_evidence\workbuddy-client\` 下 TASK-REGISTER 规定的 13 个文件。canonical `B04NegativeEvidenceManifestV1` 写入固定 manifest path，manifest 不含 self-hash，完整字节 SHA256 另记 Gate-0 takeover，且不读 PackageRoot/assembly；Gate1 必须在 import 前由独立零写 Reviewer 对 exact source tree/fixtures/ZIP listing+bytes+hash、两条 literal ordinary-language prompts、permissions/evidence plan 返回 `PRE_RUN_APPROVE`；Gate2 才允许 Owner import/permissions/two sessions；Gate3 冻结证据并返回 `APPROVE_FOR_TASK_CLEANUP`；Gate4 只能在该 token 后由 Owner 卸载 exact Skill、关闭两 sessions、删除 exact source+ZIP、记录 after-state，再由 Closeout Worker 写 result 与十问，最后由独立零写 Reviewer 对 exact final evidence/docs 返回 `FINAL_APPROVE`。缺任一 Gate/token、出现清单项缺失、manifest 额外项或漂移、提前 cleanup、终审后改 evidence/docs、Package/产品动作或下游 repair，立即停止并保持 D02-D08 未授权。

## Owner 紧急目标重置防漂移硬门（2026-08-24）

1. 当前只允许 `READ_ONLY_FACT_AUDIT + EXACT_SIX_PLANNING_DOCS_CORRECTION`；任何 WorkBuddy/probe、产品代码、Package、Provider、媒体或 D02-D08 动作立即停止。
2. 现有 D01-D08 一律为 `UNTRUSTED_PENDING_REAUDIT / DO_NOT_CONTINUE`；旧授权、token、Reviewer 结论和 Gate 不可继承。
3. 每项计划先写出“具体消除的普通用户门槛”和用户可见验收结果；没有这两项不得进入技术合同。
4. WorkBuddy 必须保持唯一 Agent 和生产决策者；Shell 只能提供降低门槛所需的支撑与引导。
5. PowerShell/Bash/CLI 不是自动失败条件；不得再发明未由 Owner 目标、official OpenMontage authority 或真实用户场景要求的技术表面。
6. 不得让用户或模型猜路径、哈希、绑定、环境白名单、命令拼装或其他内部路由。
7. D01 raw observation 可保留，但 `BLOCKED_WORKBUDDY_SURFACE` 不再是产品结论；当前唯一有效分类是 `D01_TEST_DESIGN_MISALIGNED`。
8. Reviewer 必须先核对 Owner 原始目标与事实，再核对合同一致性；仅合同自洽不能通过。
9. 任一事实缺失、目标关系不能证明或六文档不一致，立即 `STOP_MISALIGNED`，禁止带病进入下一步。
10. 当前重审候选不得 commit、push、推广或恢复产品执行，除非 Owner 后续分别明确授权。

### E 路线追加守卫

- 唯一候选顺序是 `E01 -> E02 -> E03 -> E04 -> E05 -> E06 -> E07`；当前只允许 E01 docs-only 候选。
- E02 必须先把每个源码改动映射到真实用户阻断；未映射路径禁止进入 E03/E04 allowlist。
- E03 不得新增 OpenMontage semantic-operation adapter 或复制 Pipeline/Stage/Reviewer/Checkpoint/Tool Registry。
- E04 只产品化安装/装配/生命周期，不得以 identical Skill ZIP 或 byte-perfect official/GK comparison 取代用户验收。
- E05/E06 的成功标准是普通用户被引导完成完整本地视频；PowerShell/Bash/CLI 的存在或缺少专用 native event 都不是单独 PASS/FAIL。
- E07 业务验收失败不得现场修 Shell/Core；`FORMAL_DELIVERY` 与清理仍是两个后续独立 Owner 闸门。

### E 系列执行包 fail-closed 守卫（2026-08-25 候选）

1. 当前规划对话是唯一逐任务 packet 规划者；fresh 执行对话只允许 `TAKEOVER -> EXECUTE_ONE_PACKET -> STOP_AND_REPORT`。执行窗口补计划、扩 allowlist 或临场 repair 一律 `STOP_PACKET_MISMATCH`。
2. 每项固定顺序为 `FORMAL_AUTHORITY -> USER_VALUE -> INPUT_IDENTITY -> EXACT_PACKET -> PRE_EXECUTION_REVIEW -> OWNER_TASK_EXECUTION_AUTHORIZATION -> BOUNDED_EXECUTION -> EVIDENCE_FREEZE -> RESULT_REVIEW -> CLEANUP_REVIEW -> OWNER_CLEANUP_AUTHORIZATION -> CLEANUP/AFTER_STATE -> FINAL_CLOSEOUT_REVIEW -> GIT_STATE_MACHINE`。Owner 单任务 token 必须绑定 task、packet SHA256、formal object、动作、路径、有效范围和禁止项；Package/client/Provider/rollback/cleanup token 分离。任一 Gate 失败阻断本任务和下游。
3. E02 必须生成带 SHA256 的 minimal-change packet；E03/E04 只能消费其 exact allowlist。不存在的 future SHA/path/client state 只能 `NOT_PROVED_FUTURE_INPUT / BLOCKS_EXECUTION`。
4. E05/E06 运行前必须冻结 client、Skill、Registration、literal prompts、fixture/brief、scenario、before-state 和 evidence schema。模型自报、child 自报、普通日志、receipt 或孤立 MP4 不证明 WorkBuddy 读 Guide、完成 Pipeline 或产生完整产品结果。
5. 失败证据先冻结和审核，后清理；无 `EVIDENCE_APPROVE_FOR_CLEANUP` 不卸载、不删除、不关闭需保全会话。cleanup 只使用 exact manifest，rollback 失败立即停止，after-state 必须捕获。
6. 唯一 Git 状态机为 `REVIEW_APPROVE -> OWNER_COMMIT_AUTHORIZATION -> CANDIDATE_COMMIT -> OWNER_PUSH_AUTHORIZATION -> CANDIDATE_PUSH -> OWNER_FORMAL_DELIVERY_AUTHORIZATION -> ORDINARY_FAST_FORWARD_FORMAL_REF -> REMOTE_COMMIT_TREE_VERIFICATION -> CI_HEADSHA_SUCCESS_IF_REQUIRED -> FORMALLY_DELIVERED -> OWNER_NEXT_TASK_AUTHORIZATION_SEPARATE`。更早历史节中的旧交付标签不得用于 E 路线，也不是额外动作。禁止 force-push、merge、rebase。
7. Planner/Audit Coordinator、Execution Worker、Closeout Worker、Reviewer 四方分离，E02 也无例外。Worker 不能写 authority closeout；Closeout Worker 不运行产品；Reviewer 永远零写且与前三者不同。失败回 Planner/named owner，不在下游修。

路线候选 commit `533fb410fda837259afa29e2bb2fdee76caca599` 已在远端专用分支，正式 ref 仍为 `b7bd6bc201f821f83d019c5b7addd8ec198d7ecf`。本次执行包规划是新的未提交六文档 diff；不得据此运行 E02-E07 或进行 Git/清理动作。

### E01 文档正式收口守卫（2026-08-25）

- E 路线和逐任务执行包的首次正式结果固定为 commit `1ad4aa136b99d73e76a6f8847b7deb7d064649d0`、tree `6db61922d6c07c3ff337dbaa761ca6d65c080bbf`；formal ref 已 ordinary fast-forward 并由 CI run `32809470079` 在 exact `headSha` 上 `completed/success`，395 passed / 1 skipped。
- 上方仍出现的 `formal_delivery: NOT_DONE`、`UNCOMMITTED`、旧 formal HEAD 或禁止 Git 动作均为 `HISTORICAL_PRE_CLOSEOUT_SNAPSHOT`，不得覆盖本节。
- 本 closeout 只允许 exact six authority docs；结果使用 `THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR`。只有独立零写 `APPROVE`、live formal ref 包含该 commit、远端 tree 精确且 exact-head CI success 同时成立，E01 才是最终 `FORMALLY_DELIVERED`。
- closeout 期间及完成后都不得自动启动 E02；E02-E07 固定 `NOT_STARTED / NOT_AUTHORIZED`，需 Owner 在新任务中单独授权。WorkBuddy、产品/测试代码、Package、Registration、Installer、Provider、媒体、客户端和 cleanup 均不在范围内。
