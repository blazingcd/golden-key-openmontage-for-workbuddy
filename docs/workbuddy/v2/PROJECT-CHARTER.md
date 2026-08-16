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
| Runtime按需准备 | 只核验本次真实Runtime缺口；仅在执行包声明、身份锁定且用户逐项授权后准备首个已证明的组件类型；没有额外缺口时零代码结束 | 输入：活动Package Registration、受验证的具体缺口和匹配授权；输出：`READY_REUSED`、单组件`READY_PREPARED`或失败事实 | 首次一次全装；通用下载/包管理/repair框架；选择组件或版本；修改系统Python/PATH；把Provider配置当调用授权 |
| 会话Launcher | 绑定精确环境并启动一次已验证OpenMontage Agent公开入口 | 输入：有效Package Registration、Runtime就绪事实、分离的用户消息与执行控制；输出：一次会话回执、真实退出码、结果指针和残留事实 | 解析用户意图；接受任意Shell；自动重试；调度多任务；导入Agent业务内部；创建Artifact或推进Checkpoint |
| WorkBuddy入口 | 只提供一种真实WorkBuddy显式入口，收集当前必要授权并保持用户原话不变 | 输入：用户显式请求、素材和独立授权；输出：经Locator/Launcher交给活动执行包所启动Agent的原话及面向用户的回执 | 多套生产入口；全局截获；第二聊天Agent；选择Pipeline/Stage/Provider/模型/媒体/创意；把技术控制词写入用户消息 |
| 状态与结果转交 | 优先直接转交Launcher的安装、会话、进程、退出、错误和Agent结果指针；只有真实格式缺口时才做一次确定性转换 | 输入：生命周期/Launcher事实与Agent公开结果指针；输出：不改写语义的可审计回执 | 独立任务数据库/轮询/流式平台；解释Artifact业务语义；复制Agent Stage/FSM；自动重试或伪造成功 |

安全、凭据保护、日志脱敏、路径所有权和单真实执行锁是六个模块的横切约束，不是独立模块，也不得发展为生产控制面。

### 4.1 阶段3至阶段6最小实现规则

阶段3至阶段6形成唯一顺序链路：

```text
LocatorResult
-> Runtime readiness or one authorized missing component
-> one controlled Agent process
-> one explicit WorkBuddy entry
-> unchanged exit facts and result pointer
```

- 每阶段最多一个公共入口、一个生产模块和一个直接测试文件；不能为了阶段编号制造文件。
- 没有已验证输入或直接下游消费者时必须零代码退出，不得用通用框架替代缺失合同。
- 阶段3没有额外Runtime缺口时返回`STAGE_3_NO_ADDITIONAL_RUNTIME_REQUIRED`；第一版不得联网下载、执行第三方安装脚本或管理系统环境。
- 阶段4只启动一个进程一次；不提供任意命令、常驻服务、队列、调度、自动重试或Checkpoint恢复。
- 阶段5只保留一种经真实WorkBuddy合同确认的入口形式；在格式确认前不得猜测Skill目录或同时建立CLI/MCP入口。
- 阶段6优先直接复用Launcher回执；可直接消费时返回`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`且不新增生产代码。
- 新能力必须同时有当前上游输入、当前下游消费者和直接验收；“以后可能需要”不是实现理由。

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
