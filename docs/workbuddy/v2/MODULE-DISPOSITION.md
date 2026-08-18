# WorkBuddy Shell V2 旧资产处置

状态：`STAGE_1_PASS_ACCEPTED / MAPPING_ONLY / STAGE_3_REPLANNED_IMPLEMENTATION_NOT_GRANTED`

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
| `__init__.py`、`__main__.py`、`cli.py` | 包导入、`python -m`、控制台入口、Launcher、两个Skill | 会话Launcher / `REWRITE` | 一个固定入口为WorkBuddy会话调用一个已验证工具进程并返回真实退出事实 | 恢复CLI平台；启动第二Agent；Project/Stage/Tool/Artifact/Checkpoint命令；任意Shell；自动重试；生产任务FSM | 正式入口只调用六模块合同，WorkBuddy直接读取Package Guide并承担生产角色 | 一次调用、退出码、结果指针、残留事实和未知入口拒绝 |
| `doctor.py`、`paths.py`、`gate.py` | CLI/MCP/Skill与维护者CI | OpenMontage 执行包登记与定位 / `REWRITE`；静态gate仅`HISTORICAL`参考 | 只读Package Registration、完整必带工具链身份和规范化路径报告 | 硬编码版本/Pipeline、扫盘、隐式准备、把doctor/gate当产品PASS | Locator与Launcher消费唯一活动Package Registration | Python/核心依赖、FFmpeg/ffprobe、Node/npm/npx任一未登记或漂移即fail closed，零写入 |
| `runtime_prepare.py`、`host_tools.py`、Runtime locks、`subprocess_guard/**` | doctor、CLI runtime、安装repair、宿主工具发现、missing-only准备、运行时/离线测试 | Runtime按需准备 / `HISTORICAL_REFERENCE_REPLANNED_IMPLEMENTATION_NOT_GRANTED` | 只保留可选能力的missing-only、锁定来源/hash/许可、同卷staging、所有权、回滚和幂等模式；未来唯一入口只核验WorkBuddy/OpenMontage已经选择且当前Release声明支持的一个Remotion或HyperFrames及其Package-owned Lock声明附属资产，精确存在时返回`READY_REUSED`，缺失且获授权时才准备 | 迁移Python核心依赖、FFmpeg或Node准备逻辑；把两个可选能力当必带Runtime；处理Release未声明能力；恢复旧全闭集Lock、旧入口签名、大型文件、Shell-owned Lock、独立`host_tools.py`/`subprocess_guard`框架；扫盘；通用下载/包管理/公共resume/repair；同时安装两种渲染器；准备未声明浏览器；Shell选择渲染引擎/版本；修改系统Python/PATH/注册表 | 生产Package Registration、Release能力声明、声明能力对应的Manifest覆盖Package-owned Lock，以及已冻结接口给出的单一能力请求 | 未选择能力时零下载；未声明能力`BLOCKED`且零写入；已存在声明能力仍经阶段3核验并返回`READY_REUSED`；仅准备已选能力的确认缺失项；源/hash/许可/目标不全fail closed；大陆镜像；失败清理和幂等复用；必带工具链零修改 |
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

全部旧资产已映射到六个模块、`DROP`或`HISTORICAL`，无`UNKNOWN`。CLI/MCP不是独立MVP模块；其中只允许受控入口适配，其生产编排能力一律`DROP`。`347272c`的包内Python结论和`899592d`中Python核心依赖、FFmpeg、Node的锁定/组装模式移交Package交付与阶段2登记，不再进入阶段3；`639978d`的发现/missing-only模式仅可在真实可选能力合同证明需要后选择性迁移。阶段3已完成接管前重新规划，但实现仍为`NOT_GRANTED`；旧全闭集入口、Shell-owned Lock和第二框架已`SUPERSEDED`。没有已选可选能力时阶段3零下载，已有能力必须经阶段3身份核验后返回`READY_REUSED`，阶段6可直接复用Launcher回执时同样允许零代码退出。
