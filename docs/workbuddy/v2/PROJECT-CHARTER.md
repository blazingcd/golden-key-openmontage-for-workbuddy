# WorkBuddy Shell V2 项目章程

状态：`STAGE_1_PASS_ACCEPTED / SIX_MODULE_MVP`

## 1. 产品目标

普通用户在真实 WorkBuddy 中显式调用“金钥匙短视频智能体”，只提供业务需求、素材和必要授权；Shell 隐藏安装、执行包定位和运行环境细节，把生产决策与执行交给从已验证 OpenMontage 执行包运行的 OpenMontage Agent。

最高边界：WorkBuddy负责对话，OpenMontage Agent负责生产，Shell只负责把WorkBuddy与已验证执行包可靠连接起来。Shell不得成为第二个Director、FSM、Supervisor或生产控制面。

## 2. 术语裁决

| 术语 | 唯一含义 | 本项目边界 |
|---|---|---|
| SaaS Core | 金钥匙SaaS架构中的Core组件 | 不属于Shell V2的登记、安装、定位或执行对象；Shell不得登记或实现SaaS Core |
| OpenMontage Package / OpenMontage 执行包 | 本地安装、版本化、可验证的OpenMontage Release ZIP及其Manifest、Lock、bundled Python、`AGENT_GUIDE.md`和managed files | 阶段2唯一登记对象；模块名为`OpenMontage Package Registration & Locator / OpenMontage 执行包登记与定位` |
| OpenMontage Agent | 从已验证执行包运行，唯一拥有Pipeline、Stage、Artifact、Checkpoint、Reviewer、Tool、Provider、模型、媒体和创意决策 | Shell只启动和转交，不复制其生产权威 |
| Shell | 安装与登记执行包、绑定环境、提供会话入口并转交状态和结果 | 不登记SaaS Core，不拥有生产决策 |

既有外部包合同中的反引号字面量`core.contract_id`、`core.tag`、`core.source_commit`、`core.file_count`、`managed_core`、`golden-key-core`、`golden-key-workbuddy-callable-core-v1`和`GOLDEN_KEY_WORKBUDDY_CORE.lock.json`保持原样；它们是历史wire vocabulary，不代表SaaS Core，也不授权Shell创建SaaS Core概念。

## 3. 外部角色边界

| 外部角色 | 必要职责 | Shell 不得替代 |
|---|---|---|
| WorkBuddy | 唯一对话Agent；接收用户原话、调用显式入口、读取已验证执行包的Guide并呈现结果 | 媒体生产和OpenMontage Agent决策 |
| OpenMontage Agent | 从已验证执行包运行；唯一拥有Pipeline、Stage、Artifact、Checkpoint、Reviewer、Tool、Provider、模型、媒体和创意决策 | 安装、Shell执行包登记和WorkBuddy产品入口 |
| Provider | 仅在OpenMontage Agent原生合同及用户单独授权内执行具体能力 | 绕过OpenMontage Agent；把Key存在或可配置冒充真实调用 |

## 4. Shell V2 MVP 内部模块

本表是模块职责的唯一权威位置。其他文档只能映射旧资产或定义验收，不得另立模块职责。

| 模块 | 职责 | 输入 / 输出 | 明确禁止 |
|---|---|---|---|
| 安装与生命周期 | 安装、同版本修复、升级、失败回滚和默认保留数据的卸载；维护对象所有权 | 输入：锁定的Shell包、OpenMontage 执行包、清单及用户动作；输出：已安装对象、所有权记录和原子活动执行包指针 | 运行生产流程；覆盖外来对象；静默下载、降级或删除用户数据 |
| OpenMontage 执行包登记与定位 | 登记并核验唯一活动执行包及其Release、commit、Manifest、Lock、SHA、PackageRoot、bundled Python和Guide | 输入：已安装执行包身份；输出：规范化Package Registration、身份核验和确定路径 | 扫盘、猜“最新”、按目录名推断身份、修改执行包或执行生产；登记/实现SaaS Core |
| Runtime按需准备 | 只准备当前OpenMontage Agent会话声明缺少且用户已授权的运行时层 | 输入：活动Package Registration所对应会话的实际缺口与逐类授权；输出：所需组件的准备/复用/失败结果 | 首次使用前一次全装；选择生产方案；把Provider配置当调用授权 |
| 会话Launcher | 绑定PackageRoot、package Python、DataRoot、ProjectsRoot、cwd和最小环境，调用受控OpenMontage Agent入口 | 输入：有效Package Registration、运行时结果、分离的用户消息与执行控制；输出：会话绑定回执、Agent退出码、结果指针和残留事实 | 解析用户意图；接受任意Shell；导入OpenMontage Agent业务内部；创建Artifact或推进Checkpoint |
| WorkBuddy入口 | 提供显式产品入口、必要授权提示、用户原话转交和结果呈现 | 输入：用户显式请求、素材和授权；输出：经Locator/Launcher交给活动执行包所启动Agent的原话及面向用户的结果 | 全局截获；选择Pipeline/Stage/Provider/模型/媒体/创意；把技术控制词写入用户消息 |
| 状态与结果转交 | 原样转交安装、会话、进程、退出、错误和OpenMontage Agent结果指针 | 输入：生命周期/Launcher状态与Agent公开结果；输出：可审计状态、错误和结果位置 | 解释Artifact业务语义；复制Agent Stage/FSM；自动重试或伪造成功 |

安全、凭据保护、日志脱敏、路径所有权和单真实执行锁是六个模块的横切约束，不是独立模块，也不得发展为生产控制面。

## 5. 消息与授权边界

`user_message`只包含用户真实会说的业务请求、素材、事实、授权和期望结果。执行包/Shell身份、路径、Python、cwd、测试编号、重试预算、停止条件以及证据采集只属于独立的`executor_controls`，两者禁止拼接。

下载、安装、网络、Provider、费用和重要降级分别授权；一个授权不得推导另一个授权。Shell只向活动执行包启动的OpenMontage Agent进程传递最小必要凭据，日志不得暴露明文。

## 6. MVP 明确非目标

- 不选择、推荐、排序或替换 Pipeline、Stage、Provider、模型、媒体方案或创意方向；
- 不创建或修改 Brief、Script、Scene Plan、Asset Manifest、Edit Decisions 等 Artifact，不判断 Reviewer 或推进 Checkpoint；
- 不以 CLI/MCP、嵌套 Agent、Supervisor、Director、任意 Shell 或 Shell 任务 FSM 建立第二控制面；
- 不把完整大型 Runtime、Web UI、SaaS、多租户、计费后台、外部发布或中文 fork 作为首版前置；
- 不在Shell修复OpenMontage Agent的素材方向、画幅、剪辑、成片质量或安全删除语义。

## 7. 代码与数据边界

- 生产代码谱系固定于 `2a2bf09832d558388dc2816c54b32a2dce4aa607`；V2 不 merge/rebase 推进中的 `main` 或旧长期分支，只允许带来源与消费者证据的选择性迁移。
- Shell、OpenMontage 执行包、Runtime、DataRoot和Projects分离；路径必须来自Package Registration，不得扫描盘符猜测。
- 开发、测试、缓存、构建和临时文件优先放 D 盘；升级和卸载默认保留 Projects、素材、配置、模型和输出。
- 阶段1只冻结本章程、旧资产处置和验收口径；`PASS_ACCEPTED`不构成阶段2授权。
