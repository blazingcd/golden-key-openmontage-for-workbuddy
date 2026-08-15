# WorkBuddy Shell V2 模块处置矩阵

状态：`STAGE_1_REVIEW_READY / BUILDER_ADJUDICATION_ONLY`

基线：`2a2bf09832d558388dc2816c54b32a2dce4aa607`

本矩阵只冻结后续阶段的模块边界，不授权代码迁移或实现。`KEEP`只表示该最小能力已有真实消费者和调用链证据；它不表示文件可整份复制。`ADAPT`和`REWRITE`都必须按本表限定的最小能力重新核验，测试通过不能替代消费者证据。

## 1. 裁决规则

- `KEEP`：职责与V2一致，且有明确消费者；只保留列出的最小能力。
- `ADAPT`：职责大体可用，但对象、接口、授权或生命周期必须按V2调整。
- `REWRITE`：真实问题仍存在，但当前模块边界或控制权错误，不能以原文件为迁移单位。
- `REMOVE_FROM_V1`：不进入V2首版主链；未来恢复必须新立任务和证据。
- `HISTORICAL_ONLY`：只保留来源、审计或回归参考，不作为运行时能力。
- `UNKNOWN`：证据不足时的唯一允许结论；不得据此迁移。

## 2. 固定证据摘要

- `setup.py`把`golden-key-workbuddy`和`golden-key-workbuddy-mcp`分别绑定到`cli:main`和`mcp_server:main`。
- `cli.py`消费`doctor`、`gate`、`paths`、`security`，并延迟导入`runtime`、`model_config`、`runtime_prepare`和`tasks`。
- `mcp_server.py`再次暴露`doctor`、Pipeline目录、Project、Stage、Tool、Artifact、Checkpoint和Task调用面。
- `runtime.py`直接导入`lib.checkpoint`、`lib.pipeline_loader`和`schemas.artifacts`；这证明旧消费层确实拥有第二套生产控制面，而不是仅做环境启动。
- `tasks.py`直接调用`runtime.inspect_current_stage`和`runtime.execute_stage_tool`；其持久任务状态与Core生产状态耦合。
- 两个Skill通过`WORKBUDDY-RUNTIME.json -> launcher -> CLI`消费上述能力；真实客户端证据同时证明新手Skill“已安装”不等于“自然路由成功”。
- 安装、包、DPAPI、回滚、卸载和运行时准备分别有`test_portable_bundle.py`、`test_runtime_prepare.py`等消费者测试；这些只证明合同/实现资产，不证明V2真实WorkBuddy或业务效果。

## 3. 逐模块处置

| current_path | current_consumer | real_problem_solved | v2_verdict | minimum_reusable_capability | forbidden_logic | target_stage | required_consumer_evidence | required_tests |
|---|---|---|---|---|---|---|---|---|
| `golden_key_openmontage_workbuddy/__init__.py` | Python包导入与打包清单 | 提供稳定消费方包身份 | `KEEP` | 仅包身份/版本导出 | 不导入Core业务模块，不触发环境或生产副作用 | S2/S3 | 安装包和Launcher能导入精确Shell包 | 包身份、无副作用导入 |
| `golden_key_openmontage_workbuddy/__main__.py` | `python -m golden_key_openmontage_workbuddy -> cli.main` | 提供确定性命令入口 | `ADAPT` | 转交到缩减后的Launcher命令面 | 不恢复Project/Stage/Tool/Artifact/Checkpoint命令 | S3/S6 | 已安装Launcher调用该入口且返回真实退出码 | 入口路由、退出码、未知命令拒绝 |
| `golden_key_openmontage_workbuddy/cli.py` | `setup.py`控制台入口、两个Skill、Launcher、CLI测试 | 统一诊断和本地调用 | `REWRITE` | 仅`inspect / prepare / session / exec / status`的Shell命令面 | Pipeline选择、Project创建、Stage检查、Tool执行、Artifact校验、Checkpoint提交、生产Task FSM | S3/S6 | 正式Skill只经Launcher消费缩减命令；Core调用链不依赖旧命令 | 命令allowlist、任意Shell拒绝、环境回执、真实退出码 |
| `golden_key_openmontage_workbuddy/doctor.py` | `cli.py`、`gate.py`、`mcp_server.py`、两个Skill | 暴露环境和安装缺口 | `REWRITE` | 对Registration、CoreRoot、Python、Guide、DataRoot和已授权运行时做只读`inspect` | 硬编码v0.3.21、四Pipeline、把doctor结果当产品PASS、隐式准备依赖 | S2/S3/S5 | Locator/Launcher对登记对象的只读报告被正式Skill消费 | 对象漂移、解释器漂移、缺Guide、零写入、非证明文案 |
| `golden_key_openmontage_workbuddy/gate.py` | `cli gate`、公开CI、`test_ci_contract.py` | 检查消费层禁入路径和direct-agent隔离 | `ADAPT` | 维护者静态边界检查 | 进入普通用户主链；用静态Gate代替安装、WorkBuddy或成片验收 | S6/S7 | CI/Reviewer明确消费V2禁止导入规则 | Shell不导入Core业务内部、禁止第二Director/FSM、非证明断言 |
| `golden_key_openmontage_workbuddy/mcp_server.py` | `setup.py`可选入口、旧MCP配置、MCP测试 | 提供17个结构化CLI镜像工具 | `REMOVE_FROM_V1` | 无；只保留历史接口清单供兼容性评估 | 以MCP重建Project/Stage/Tool/Artifact/Checkpoint/Task控制面，或把MCP设为首版依赖 | S6 | 若未来恢复，需证明比Skill+Launcher更可靠且没有第二权威 | 首版包中无活动MCP；未来需独立真实WorkBuddy对照 |
| `golden_key_openmontage_workbuddy/model_config.py` | `cli config`、MCP、两个Skill、配置向导测试 | 汇总Provider和凭据配置提示 | `REMOVE_FROM_V1` | Provider事实只从锁定Core公开合同转交；本文件不迁移 | Shell维护Provider目录、推荐/排序Provider、探测状态或把Key存在写成能力可用 | S4/S6 | Core公开能力/Provider报告由WorkBuddy直接消费；Shell只传递授权 | Shell零Provider选择、零联网、Key存在非PASS |
| `golden_key_openmontage_workbuddy/paths.py` | `cli.py`和`mcp_server.py`默认根目录 | 提供仓库根和DataRoot默认值 | `REWRITE` | 只从安装记录/Registration解析显式ShellRoot、CoreRoot、RuntimeRoot、DataRoot、ProjectsRoot | 以包源码位置充当Core身份、扫盘、猜最新目录、硬编码维护者D盘 | S2/S3 | Locator读取单一活动Registration并返回规范化绝对路径 | 路径穿越、盘根拒绝、无登记fail closed、路径所有权 |
| `golden_key_openmontage_workbuddy/runtime.py` | `cli.py`、`mcp_server.py`、`tasks.py` | 在消费层直接创建Project并操作Core Stage/Tool/Artifact/Checkpoint | `REMOVE_FROM_V1` | 无；仅把已发现的路径封闭需求重新落到Launcher边界 | 导入`lib.checkpoint`、`lib.pipeline_loader`、`schemas.artifacts`或Tool Registry；任何生产决策/状态写入 | S3/S6 | Core原生入口自行创建Artifact/Checkpoint；Shell只得到退出和结果指针 | 静态禁止导入、Core原生调用链、Shell零Artifact/Checkpoint写入 |
| `golden_key_openmontage_workbuddy/runtime_prepare.py` | `doctor.py`、`cli runtime`、两个Skill、安装repair、运行时测试 | 固定hash、所有权、D盘缓存与幂等准备 | `ADAPT` | 分层`plan/prepare`、锁定下载、staging、所有权marker、幂等复用 | 首次使用前一次准备完整Python/FFmpeg/Node/Remotion/HyperFrames/浏览器；未授权下载；Shell选择具体生产方案 | S5 | Core/会话声明的实际缺口触发对应层准备，用户逐类授权 | plan零写入、分层授权、断点/hash、幂等、失败回滚、无需组件不下载 |
| `golden_key_openmontage_workbuddy/security.py` | `cli.py`、`mcp_server.py`、`runtime.py`、`tasks.py`输出边界 | 统一脱敏敏感环境值和结构化payload | `KEEP` | 纯函数脱敏能力及调用前后无副作用 | 读取/记录明文凭据、用脱敏结果掩盖对象或退出状态 | S2-S8横切 | Launcher日志、状态回执和安装报告均调用同一脱敏边界 | 明文canary、嵌套payload、异常文本、不可反推 |
| `golden_key_openmontage_workbuddy/tasks.py` | `cli task`、17工具MCP、生产Skill | 持久化本地Tool任务、并发1、恢复和观察超时 | `REWRITE` | 单真实执行锁、进程身份、原子状态/结果转交 | Stage/Tool输入校验、生产任务FSM、自动重试、强杀Core、伪称Checkpoint状态 | S3/S6 | Launcher会话锁只包围一个Core执行；Core拥有生产恢复语义 | 竞争锁、进程死亡、退出码、残留、无自动重试、无Stage字段 |
| `golden_key_openmontage_workbuddy/subprocess_guard/__init__.py`、`offline_guard.cjs`、`sitecustomize.py` | `runtime._deny_local_tool_network`经`PYTHONPATH`/`NODE_OPTIONS`注入 | 证明离线负测可阻止Python/Node子进程联网 | `ADAPT` | 仅作为明确零网络Gate的测试/受控执行夹具 | 永久封锁API/Hybrid、改变Core批准后的Provider路径、作为生产能力证明 | S7/S8 | Gate A-D的零网络边界或离线测试显式启用；正常Provider会话不继承 | Python/Node socket负测、环境恢复、Provider授权隔离 |
| `workbuddy-skill/golden-key-openmontage/SKILL.md` | 安装器注册后的正式显式产品入口 | 让WorkBuddy定位Launcher并进入生产 | `REWRITE` | 显式触发、Locator、literal `user_message`转交、授权提示、结果呈现 | 十几条CLI/MCP生产步骤、Pipeline/Stage/Tool/Artifact/Checkpoint编排、技术控制词进入用户消息 | S4 | 新WorkBuddy会话从目标Skill到Registration、Launcher、Core Guide的完整调用链 | 触发边界、literal消息逐字、controls隔离、无生产控制面、真实路由 |
| `workbuddy-skill/golden-key-openmontage-onboarding/SKILL.md` | 安装器注册的新手入口；历史真实客户端自然路由失败 | 把模糊意愿转成业务请求和素材交接 | `ADAPT` | 结果导向引导、一次一个问题、素材/参考/无素材分支、具体请求后交给生产Skill | 全局截获、把CLI/runtime完整准备当对话前置、重复Core澄清、技术术语进入用户消息 | S4 | 真实WorkBuddy能区分模糊引导与显式生产Skill且不互相抢占 | Skill触发、交接、无项目创建、无Provider、用户话术边界 |
| `packaging/workbuddy/install-to-workbuddy.*`、`install-workbuddy.ps1` | 中文双击入口、ZIP注册、Skill/Locator写入、安装测试 | 安全注册拥有权明确的程序与Skill | `ADAPT` | manifest白名单、staging、所有权、同版本repair、DataRoot分离 | Shell/Core同目录不可分、安装时准备全部大型Runtime、根据文件名猜Core、覆盖外来Skill | S2/S7 | 安装后Registration唯一指向锁定Core；Skill locator与安装记录一致 | fresh/repair/冲突、未知文件忽略、对象SHA、数据保留、无隐式下载 |
| `scripts/workbuddy/build_portable_bundle.py`、`setup.py`、`requirements.txt` | 维护者构建和Python入口；普通ZIP排除`setup.py` | 构建可校验便携包并约束白名单 | `ADAPT` | 可复现staging、逐文件hash、Shell包身份 | 把某一Core快照内嵌成永久身份、把构建成功写成安装或V2 PASS | S7 | 构建产物Manifest、Core Registration和来源Release三方一致 | 可复现构建、额外/缺失文件、包边界、构建非证明 |
| `WORKBUDDY-BOOTSTRAP-RUNTIME.lock.json`、`WORKBUDDY-PRODUCTION-RUNTIME.lock.json`及安装Manifest/Lock | 构建器、安装器、runtime_prepare、doctor | 固定下载资产、组件版本、hash和所有权 | `ADAPT` | Shell/Core/Runtime分别有身份与生命周期；Lock可复核 | 单一“完整生产环境”锁成为所有任务前置；Lock替代真实安装或执行证据 | S2/S5/S7 | Registration引用的Core Manifest/Lock与安装实例和实际解释器一致 | schema、SHA、原子活动指针、缺失/漂移/降级负测 |
| `packaging/workbuddy/configure-provider-keys.ps1`、`配置API密钥.cmd`、`golden-key-workbuddy.ps1`凭据段 | 本地隐藏输入向导与Launcher进程注入 | DPAPI保护、密钥不进聊天/参数/日志 | `ADAPT` | 当前用户加密、最小进程注入、只报告存在状态 | Shell推荐Provider、读取/打印明文、Key存在等同联网/费用授权、把凭据写入`user_message` | S4/S7 | 经用户单独授权后，Launcher只向锁定Core进程注入所需引用 | DPAPI用户隔离、日志canary、零参数明文、授权分离 |
| `install-workbuddy.ps1`的版本比较、升级和rollback段 | 安装器、`test_portable_bundle.py` | 向前升级、失败恢复旧程序/Skill、保留DataRoot | `ADAPT` | 原子安装新Core Registration、验证后切换、失败恢复活动指针 | merge/rebase或拉取Core `main`、原地覆盖活动Core、回滚用户数据、静默降级 | S7 | 两个不可变Core对象间的真实活动指针切换和恢复证据 | 前向升级、坏新Core、断电/中断、指针原子性、数据哨兵 |
| `packaging/workbuddy/uninstall-workbuddy.ps1`、`从WorkBuddy卸载.cmd` | 用户自卸载入口、安装所有权记录、卸载测试 | 只移除自有程序/Skill并默认保留数据 | `ADAPT` | 所有权核验、移出活动位置、延迟清理、DataRoot默认保留 | 删除未登记Core、外来Skill、Projects/素材/配置/模型/输出；把目标正式Skill算作残留 | S7 | 安装记录精确列出可删除对象；保留项和protected项可审计 | 盘根拒绝、外来Skill、正式Skill移除、DataRoot哨兵、进程残留 |
| `scripts/core_sync/sync_workbuddy_core.py`、`config/openmontage.sync.json`、`docs/workbuddy/CORE-SYNC-POLICY.md` | v0.3.21维护者Release镜像与W0审计 | 证明不可变Release、lock、managed scope和公开lineage | `HISTORICAL_ONLY` | 只保留设计证据；V2用新的Core Registration/安装合同实现对象锁定 | 继续同步v0.3.21、四Pipeline或private/main；把同步器变成用户运行时或活动Core选择器 | S2/S7 | 新Release提供独立ZIP/SHA/Lock/Manifest；消费者明确引用Registration | 新合同另测；历史同步测试不自动沿用为V2 PASS |
| `tests/workbuddy/**` | CI、维护者回归、旧W1-W4 Gate | 为旧消费层、安装、安全和运行时提供回归 | `ADAPT` | 保留安装所有权、路径、脱敏、DPAPI、hash、回滚、数据保护夹具；重写调用链断言 | 用旧CLI/MCP/Project/Stage测试证明V2必要性或真实WorkBuddy；保留第二控制面只为让测试通过 | S2-S8 | 每个保留测试绑定新的真实消费者和Gate；无消费者的旧断言降为历史 | 静态合同、故障注入、安装矩阵、真实WorkBuddy分层且分别报告 |
| `scripts/workbuddy/w0_audit.py`、历史W0/报告/Prompt/旧架构文档 | 维护者审计与来源追溯 | 记录发布、包、真实运行和已知偏差 | `HISTORICAL_ONLY` | 只作来源和非证明边界；不得直接改变V2状态 | 把历史PASS、旧MP4、validation-only包、旧Prompt当当前授权或V2验收 | S1/S8 | 当前任务引用精确Git对象和最新最终状态 | 文档链接/对象可读性；不作为运行测试 |

## 4. 跨模块禁止迁移清单

无论来源模块的裁决是什么，以下能力均不得进入Shell V2：

- Pipeline、Stage、Provider、模型、媒体方案或创意方向的选择、推荐、排序或替换；
- Brief、Script、Scene Plan、Asset Manifest、Edit Decisions等Artifact的创建或修订；
- Reviewer判断、Checkpoint推进或与Core Stage同构的FSM；
- 任意Shell字符串、嵌套Agent、Supervisor、Director或Agent Host；
- 把CoreRoot、Python、Pipeline、Stage、测试编号、重试预算或PASS条件写入literal `user_message`；
- 以ZIP、doctor、registry、静态测试、旧MP4或历史成功代替当前对象的真实Gate。

## 5. 未决项

本轮没有因证据不足使用`UNKNOWN`。这只表示模块处置可以进入独立Reviewer，不表示任何后续实现、真实WorkBuddy、Provider、媒体、业务效果或发布已经通过。
