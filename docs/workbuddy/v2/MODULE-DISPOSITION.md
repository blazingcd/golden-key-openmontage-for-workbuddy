# WorkBuddy Shell V2 旧资产处置

状态：`STAGE_1_PASS_ACCEPTED / MAPPING_ONLY / NOT_IMPLEMENTED`

固定来源：`2a2bf09832d558388dc2816c54b32a2dce4aa607`

本文件只把 V1 文件或能力映射到章程中的六个模块、`DROP`或`HISTORICAL`。裁决不授权整文件复制；只有表内最小能力可在后续任务重新证明。

## 1. 关键调用链证据

- `setup.py`把普通入口和 MCP 入口分别绑定到`cli:main`与`mcp_server:main`；`cli.py`继续消费`doctor/gate/paths/security/runtime/model_config/runtime_prepare/tasks`。
- `runtime.py`直接导入执行包内的`lib.checkpoint`、`lib.pipeline_loader`和`schemas.artifacts`，并由CLI、MCP与`tasks.py`消费；`tasks.py`又调用Stage检查和Tool执行。这是V1 Shell形成第二生产控制面的直接证据。
- 两个 Skill 经`WORKBUDDY-RUNTIME.json -> launcher -> CLI`消费上述能力；历史真实客户端同时证明“Skill 已安装”不等于“自然路由成功”。
- 安装、包、运行时、凭据、回滚和卸载测试只证明对应旧合同资产，不证明 V2 的真实 WorkBuddy、OpenMontage Agent流程或业务效果。

## 2. 分组裁决

裁决含义：`KEEP`仅保留边界完全一致的最小能力；`ADAPT`调整既有边界；`REWRITE`保留问题但重建实现；`DROP`不进入 MVP；`HISTORICAL`只作来源或回归参考。

| V1 来源 | 真实消费者 / 调用链 | V2 归属 / 裁决 | 最小保留能力 | 禁止迁移逻辑 | 后续消费者证据 | 最小验收 |
|---|---|---|---|---|---|---|
| `__init__.py`、`__main__.py`、`cli.py` | 包导入、`python -m`、控制台入口、Launcher、两个Skill | 会话Launcher / `REWRITE` | 稳定包身份和受控Launcher入口 | Project/Stage/Tool/Artifact/Checkpoint命令、任意Shell、生产任务FSM | 正式入口只调用六模块合同，OpenMontage Agent不依赖旧命令 | 入口、退出码和未知命令拒绝 |
| `doctor.py`、`paths.py`、`gate.py` | CLI/MCP/Skill与维护者CI | OpenMontage 执行包登记与定位 / `REWRITE`；静态gate仅`HISTORICAL`参考 | 只读Package Registration、执行包身份和规范化路径报告 | 硬编码版本/Pipeline、扫盘、隐式准备、把doctor/gate当产品PASS | Locator与Launcher消费唯一活动Package Registration | 无登记或执行包漂移fail closed，零写入 |
| `runtime_prepare.py`、Runtime locks、`subprocess_guard/**` | doctor、CLI runtime、安装repair、运行时/离线测试 | Runtime按需准备 / `ADAPT` | 分层plan/prepare、hash、staging、所有权、幂等；离线guard只作受控夹具 | 一次准备完整环境、未授权下载、Shell选择生产方案或永久阻断已授权Provider | OpenMontage Agent会话实际缺口触发对应层 | plan零写入；只准备获批且缺失组件 |
| `security.py` | CLI/MCP/runtime/tasks 输出 | 六模块横切 / `KEEP` | 纯函数脱敏 | 读取或记录明文凭据；用脱敏掩盖对象或退出状态 | 安装、Launcher 与状态回执共同消费同一边界 | 明文 canary 不出现在输出 |
| `tasks.py` | CLI task、MCP、生产Skill，并调用`runtime.py` | 状态与结果转交 / `REWRITE` | 单真实执行锁、进程身份、原子状态记录与结果指针 | Stage/Tool校验、生产FSM、自动重试、强杀OpenMontage Agent、伪称Checkpoint | 一个Launcher会话持有一个执行锁，OpenMontage Agent拥有恢复语义 | 竞争锁、退出/死亡与结果指针可审计 |
| `runtime.py` | CLI、MCP、tasks；直连执行包内业务模块 | `DROP` | 无 | 导入执行包内业务实现、创建Project、操作Stage/Tool/Artifact/Checkpoint及写生产状态 | OpenMontage Agent公开入口自行形成原生调用链 | Shell对Agent业务内部导入和Artifact/Checkpoint写入为零 |
| `mcp_server.py`及旧 MCP 配置 | `setup.py`可选入口和 17 工具测试 | `DROP` | 无；CLI/MCP 都不是独立 MVP 模块 | 以 MCP 镜像或重建 Project/Stage/Tool/Artifact/Checkpoint/Task 控制面 | MVP 主链只经显式 WorkBuddy 入口和受控 Launcher | 包与活动配置中无生产 MCP 主链 |
| `model_config.py` | CLI config、MCP、两个Skill | `DROP` | 无 | Shell维护、推荐、排序或探测Provider/模型；把Key存在当能力 | Provider事实与选择只由活动执行包启动的OpenMontage Agent在授权内消费 | Shell的Provider/模型选择为零 |
| 两个`workbuddy-skill/**/SKILL.md` | WorkBuddy 显式生产入口与新手入口 | WorkBuddy入口 / `REWRITE` | 显式触发、原话转交、必要授权提示、结果呈现和有界 onboarding 交接 | CLI/MCP 生产步骤、全局截获、重复OpenMontage Agent澄清、技术控制词进入`user_message` | 新 WorkBuddy 会话命中正确入口并经 Locator/Launcher 到活动执行包启动的Agent | literal 消息不变且入口不作生产决策 |
| 安装/卸载/升级/回滚脚本，便携包构建，Manifest/Lock，`setup.py`、`requirements.txt` | 用户安装入口、构建器、安装记录及安装测试 | 安装与生命周期 / `ADAPT` | 白名单、hash、staging、所有权、原子活动执行包指针、数据保留和失败恢复 | Shell与执行包混装、覆盖外来对象、内嵌未登记执行包、静默下载/降级、删除用户数据 | 安装记录、Package Registration、包清单和实际执行包身份一致 | fresh/repair/upgrade/rollback/uninstall保持所有权与数据边界 |
| Provider凭据脚本与Launcher注入段 | 隐藏输入向导和OpenMontage Agent子进程 | 六模块横切 / `ADAPT` | 当前用户加密、最小进程注入、只报告存在状态 | 明文进入聊天/参数/日志；Shell选Provider；Key存在代替调用与费用授权 | 单独授权后，仅活动执行包启动的Agent进程消费所需凭据 | 明文canary为零，授权彼此独立 |
| 历史Core sync命名、旧tests、W0/报告/Prompt/架构文档 | 维护者发布、回归和历史追溯 | `HISTORICAL` | 外部包合同来源、消费者和故障夹具参考 | 继续同步旧上游main；为保留旧测试而恢复第二控制面；用历史PASS改变V2状态 | 后续任务必须为保留能力建立新消费者与当前执行包证据 | 可追溯但不计作V2实现或Gate PASS |

## 3. 收口

全部旧资产已映射到六个模块、`DROP`或`HISTORICAL`，无`UNKNOWN`。CLI/MCP 不是独立 MVP 模块；其中只允许受控入口适配，其生产编排能力一律`DROP`。
