# WorkBuddy Shell V2 项目章程

状态：`STAGE_1_REVIEW_READY / SIX_MODULE_MVP / NOT_PASS_ACCEPTED`

## 1. 产品目标

普通用户在真实 WorkBuddy 中显式调用“金钥匙短视频智能体”，只提供业务需求、素材和必要授权；Shell 隐藏安装、对象定位和运行环境细节，把生产决策与执行交给锁定的 OpenMontage Core。

最高边界：WorkBuddy 负责对话，Core 负责生产，Shell 只负责把二者可靠连接起来。Shell 不得成为第二个 Director、FSM、Supervisor 或生产控制面。

## 2. 外部角色边界

| 外部角色 | 必要职责 | Shell 不得替代 |
|---|---|---|
| WorkBuddy | 唯一对话 Agent；接收用户原话、调用显式入口、读取锁定 Core 的 Guide 并呈现结果 | 媒体生产和 Core 决策 |
| OpenMontage Core | 唯一拥有 Pipeline、Stage、Artifact、Checkpoint、Reviewer、Tool、Provider、模型、媒体和创意决策 | 安装、Shell 对象登记和 WorkBuddy 产品入口 |
| Provider | 仅在 Core 原生合同及用户单独授权内执行具体能力 | 绕过 Core；把 Key 存在或可配置冒充真实调用 |

## 3. Shell V2 MVP 内部模块

本表是模块职责的唯一权威位置。其他文档只能映射旧资产或定义验收，不得另立模块职责。

| 模块 | 职责 | 输入 / 输出 | 明确禁止 |
|---|---|---|---|
| 安装与生命周期 | 安装、同版本修复、升级、失败回滚和默认保留数据的卸载；维护对象所有权 | 输入：锁定的 Shell/Core 包、清单及用户动作；输出：已安装对象、所有权记录和原子活动指针 | 运行生产流程；覆盖外来对象；静默下载、降级或删除用户数据 |
| Core登记与定位 | 登记并核验唯一活动 Core 及其 Release、commit、Manifest、Lock、SHA、CoreRoot、Python 和 Guide | 输入：已安装 Core 身份；输出：规范化 Registration、身份核验和确定路径 | 扫盘、猜“最新”、按目录名推断身份、修改 Core 或执行生产 |
| Runtime按需准备 | 只准备当前 Core 会话声明缺少且用户已授权的运行时层 | 输入：已登记 Core 的实际缺口与逐类授权；输出：所需组件的准备/复用/失败结果 | 首次使用前一次全装；选择生产方案；把 Provider 配置当调用授权 |
| 会话Launcher | 绑定 CoreRoot、Python、DataRoot、ProjectsRoot、cwd 和最小环境，调用受控 Core 入口 | 输入：有效 Registration、运行时结果、分离的用户消息与执行控制；输出：会话绑定回执、Core 退出码、结果指针和残留事实 | 解析用户意图；接受任意 Shell；导入 Core 业务内部；创建 Artifact 或推进 Checkpoint |
| WorkBuddy入口 | 提供显式产品入口、必要授权提示、用户原话转交和结果呈现 | 输入：用户显式请求、素材和授权；输出：经 Locator/Launcher 交给锁定 Core 的原话及面向用户的结果 | 全局截获；选择 Pipeline/Stage/Provider/模型/媒体/创意；把技术控制词写入用户消息 |
| 状态与结果转交 | 原样转交安装、会话、进程、退出、错误和 Core 结果指针 | 输入：生命周期/Launcher 状态与 Core 公开结果；输出：可审计状态、错误和结果位置 | 解释 Artifact 业务语义；复制 Core Stage/FSM；自动重试或伪造成功 |

安全、凭据保护、日志脱敏、路径所有权和单真实执行锁是六个模块的横切约束，不是独立模块，也不得发展为生产控制面。

## 4. 消息与授权边界

`user_message`只包含用户真实会说的业务请求、素材、事实、授权和期望结果。Core/Shell 身份、路径、Python、cwd、测试编号、重试预算、停止条件以及证据采集只属于独立的`executor_controls`，两者禁止拼接。

下载、安装、网络、Provider、费用和重要降级分别授权；一个授权不得推导另一个授权。Shell 只向锁定 Core 进程传递最小必要凭据，日志不得暴露明文。

## 5. MVP 明确非目标

- 不选择、推荐、排序或替换 Pipeline、Stage、Provider、模型、媒体方案或创意方向；
- 不创建或修改 Brief、Script、Scene Plan、Asset Manifest、Edit Decisions 等 Artifact，不判断 Reviewer 或推进 Checkpoint；
- 不以 CLI/MCP、嵌套 Agent、Supervisor、Director、任意 Shell 或 Shell 任务 FSM 建立第二控制面；
- 不把完整大型 Runtime、Web UI、SaaS、多租户、计费后台、外部发布或中文 fork 作为首版前置；
- 不在 Shell 修复 Core 的素材方向、画幅、剪辑、成片质量或安全删除语义。

## 6. 代码与数据边界

- 生产代码谱系固定于 `2a2bf09832d558388dc2816c54b32a2dce4aa607`；V2 不 merge/rebase 推进中的 `main` 或旧长期分支，只允许带来源与消费者证据的选择性迁移。
- Shell、Core、Runtime、DataRoot 和 Projects 分离；路径必须来自登记对象，不得扫描盘符猜测。
- 开发、测试、缓存、构建和临时文件优先放 D 盘；升级和卸载默认保留 Projects、素材、配置、模型和输出。
- 阶段1只冻结本章程、旧资产处置和验收口径；`REVIEW_READY`不是 Reviewer 或用户 Gate 结论。
