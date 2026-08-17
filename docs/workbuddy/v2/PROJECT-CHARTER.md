# WorkBuddy Shell V2 项目章程

状态：`STAGE_1_PASS_ACCEPTED / SIX_MODULE_MVP`

## 1. 产品目标

普通用户在真实腾讯WorkBuddy中显式调用“金钥匙短视频智能体”，只提供业务需求、素材和必要授权；Shell隐藏安装、执行包定位和运行环境细节。WorkBuddy读取已验证的金钥匙版OpenMontage执行包Guide后，作为唯一运行中的Agent执行生产合同。

最高边界：WorkBuddy既负责对话，也是唯一运行中的生产Agent；OpenMontage执行包提供生产规则、Pipeline、Skills和Tools；Shell只负责把WorkBuddy与已验证执行包及运行环境可靠连接起来。Shell不得成为Director、FSM、Supervisor、第二Agent或生产控制面。

## 2. 术语裁决

| 术语 | 唯一含义 | 本项目边界 |
|---|---|---|
| SaaS Core | 金钥匙SaaS架构中的Core组件 | 不属于Shell V2的登记、安装、定位或执行对象；Shell不得登记或实现SaaS Core |
| 官方OpenMontage源码/Release | 上游项目原始发布物；公开Prerequisites为Python 3.10+、FFmpeg和Node.js 18+，但不替金钥匙普通用户携带这些环境 | 仅作为金钥匙版执行包的经验证上游输入，不直接作为阶段2登记成品 |
| Golden Key OpenMontage Package / 金钥匙版执行包 | 面向WorkBuddy交付的本地安装、版本化、可验证Release ZIP，包含Manifest、Lock、`AGENT_GUIDE.md`、managed files以及完整必带私有工具链：可用Python环境及核心依赖、FFmpeg/ffprobe、Node/npm/npx | 阶段2唯一登记对象；普通用户无需系统Python、FFmpeg或Node；Node锁定版本必须满足当前Package最高要求，不能只按18+最低线 |
| OpenMontage Agent角色 | WorkBuddy读取已验证Package Guide后承担的逻辑生产角色，拥有Pipeline、Stage、Artifact、Checkpoint、Reviewer、Tool、Provider、模型、媒体和创意决策 | 不是另一个Agent、Agent Host或独立模型进程；Shell不得启动或复制它 |
| Shell | 安装与登记执行包、绑定环境、提供会话入口并转交状态和结果 | 不登记SaaS Core，不拥有生产决策 |

既有外部包合同中的反引号字面量`core.contract_id`、`core.tag`、`core.source_commit`、`core.file_count`、`managed_core`、`golden-key-core`、`golden-key-workbuddy-callable-core-v1`和`GOLDEN_KEY_WORKBUDDY_CORE.lock.json`保持原样；它们是历史wire vocabulary，不代表SaaS Core，也不授权Shell创建SaaS Core概念。

## 3. 外部角色边界

| 外部角色 | 必要职责 | Shell 不得替代 |
|---|---|---|
| WorkBuddy | 唯一运行中的Agent；接收用户原话、读取已验证执行包Guide、承担OpenMontage生产角色并呈现结果 | Shell安装、执行包登记、运行时准备和伪造成功 |
| OpenMontage Package | 向WorkBuddy提供Pipeline、Stage、Artifact、Checkpoint、Reviewer、Tool、Provider、模型、媒体和创意合同 | 自行成为第二Agent；安装Shell；绕过WorkBuddy对话和用户授权 |
| Provider | 仅在WorkBuddy依据OpenMontage合同且取得用户单独授权后执行具体能力 | 绕过WorkBuddy；把Key存在或可配置冒充真实调用 |

## 4. Shell V2 MVP 内部模块

本表是模块职责的唯一权威位置。其他文档只能映射旧资产或定义验收，不得另立模块职责。

| 模块 | 职责 | 输入 / 输出 | 明确禁止 |
|---|---|---|---|
| 安装与生命周期 | 安装、同版本修复、升级、失败回滚和默认保留数据的卸载；维护对象所有权 | 输入：锁定的Shell包、OpenMontage 执行包、清单及用户动作；输出：已安装对象、所有权记录和原子活动执行包指针 | 运行生产流程；覆盖外来对象；静默下载、降级或删除用户数据 |
| OpenMontage 执行包登记与定位 | 登记并核验唯一活动金钥匙版执行包及其Release、commit、Manifest、Lock、SHA、PackageRoot、完整必带私有工具链和Guide | 输入：已安装执行包身份；输出：规范化Package Registration、Python/FFmpeg/ffprobe/Node/npm/npx身份核验和确定路径 | 扫盘、猜“最新”、按目录名推断身份、修改执行包或执行生产；依赖任何系统Python/FFmpeg/Node；登记/实现SaaS Core |
| Runtime按需准备 | 只读发现已由WorkBuddy/OpenMontage锁定的可选渲染能力，并对用户确认计划中的缺失项进行受控准备 | 输入：活动Package Registration、经验证的可选能力要求、Optional Runtime Lock、受管/登记宿主/PATH候选及用户对计划的明确授权；输出：所选能力来源与状态、`READY_REUSED`、`READY_PREPARED`或失败事实 | 扫盘；发现/下载/替换必带Python/FFmpeg/Node工具链；一次安装所有可选能力；由Shell或普通用户替OpenMontage选择Remotion/HyperFrames；通用包管理器；未授权下载；海外默认源回退；修改系统PATH/注册表 |
| 会话Launcher | 为一次WorkBuddy拥有的会话绑定精确Package、完整必带工具链和当前实际需要的已验证可选能力，并调用一个固定工具入口 | 输入：有效Package Registration、阶段2必带工具链就绪事实、执行所选可选能力时对应的阶段3就绪事实、分离的用户消息与执行控制；输出：一次调用回执、真实退出码、结果指针和残留事实 | 启动第二Agent/模型进程；解析用户意图；接受任意Shell；自动重试；调度多任务；创建Artifact或推进Checkpoint |
| WorkBuddy入口 | 只提供一种真实WorkBuddy显式入口，收集当前必要授权并保持用户原话不变 | 输入：用户显式请求、素材和独立授权；输出：经Locator/Launcher绑定到活动执行包的原话及面向用户的回执 | 多套生产入口；全局截获；第二聊天Agent；由Shell选择Pipeline/Stage/Provider/模型/媒体/创意；把技术控制词写入用户消息 |
| 状态与结果转交 | 优先直接转交Runtime计划/准备事实、Launcher的会话/进程/退出/错误和WorkBuddy结果指针；只有真实格式缺口时才做一次确定性转换 | 输入：生命周期/Runtime/Launcher事实与WorkBuddy公开结果指针；输出：不改写语义的可审计回执 | 独立任务数据库/轮询/流式平台；解释Artifact业务语义；复制OpenMontage Stage/FSM；自动重试或伪造成功 |

安全、凭据保护、日志脱敏、路径所有权和单真实执行锁是六个模块的横切约束，不是独立模块，也不得发展为生产控制面。

### 4.1 阶段3至阶段6最小实现规则

阶段编号表示建设、审阅和正式交付顺序，固定为`阶段3 -> 阶段4 -> 阶段5 -> 阶段6`。这不是最终用户的一次运行调用顺序。最终用户实际运行从阶段5的WorkBuddy入口开始：

```text
User
-> Stage 5: one explicit WorkBuddy entry
-> Stage 2: revalidate required private Python / FFmpeg / Node toolchain
-> Stage 4: one WorkBuddy-owned bound tool call with required toolchain
-> WorkBuddy/OpenMontage: lock the actual render capability
   -> package FFmpeg capability: continue with bundled FFmpeg
   -> Remotion or HyperFrames capability missing
      -> Stage 3: relay one capability-specific missing-only plan
      -> separate explicit user consent
      -> Stage 3: prepare only the locked optional capability
      -> continue only through the future verified session contract
-> Stage 6: unchanged preparation, exit, error and result facts
```

- 每阶段最多一个公共入口、一个生产模块和一个直接测试文件；不能为了阶段编号制造文件。
- 没有已验证输入或直接下游消费者时必须零代码退出，不得用通用框架替代缺失合同。
- Python及核心依赖、FFmpeg/ffprobe、Node/npm/npx是阶段2登记前置，不属于阶段3发现或下载对象。阶段3只处理经WorkBuddy/OpenMontage实际选择的Remotion或HyperFrames能力，以及该能力锁精确声明的浏览器等附属资产；没有可选能力要求时返回`STAGE_3_NO_OPTIONAL_CAPABILITY_REQUIRED`。
- 阶段3只有一个按需准备接口，不是“扫描所有可选能力后全部安装”。Shell不决定Remotion或HyperFrames，普通用户也不承担技术选型；WorkBuddy依据已验证Package合同形成能力要求，用户只确认对应下载量、目标和许可证。
- 阶段3面向最终用户的可选能力下载只使用Optional Runtime Lock批准的中国大陆镜像，不得在失败后自动选择海外源。FFmpeg `gyan.dev`不再是阶段3终端用户下载源；它属于必带Package组装供应链并由阶段2核验。
- 阶段4启动固定工具前必须接受阶段2的完整必带工具链就绪事实；所选可选渲染能力在实际执行前还必须接受对应阶段3就绪事实。缺少相应事实时返回`RUNTIME_NOT_READY`。它不启动第二Agent，不提供任意命令、常驻服务、队列、调度、自动重试或Checkpoint恢复。
- 阶段5只保留一种经真实WorkBuddy合同确认的入口形式，是用户实际运行的起点；在格式确认前不得猜测Skill目录或同时建立CLI/MCP入口。
- 阶段6直接转交Runtime计划/准备事实和Launcher回执；可直接消费时返回`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`且不新增生产代码。它不得解释、安装或自动重试。
- 新能力必须同时有当前上游输入、当前下游消费者和直接验收；“以后可能需要”不是实现理由。

### 4.2 中国大陆镜像合同

老项目已经验证的大陆镜像先例只用于冻结渠道类别；新版Runtime Lock仍必须给出精确版本URL、大小和SHA-256：

| 组件 | 终端用户下载渠道 |
|---|---|
| Python解释器及核心依赖 | 终端用户不下载；随金钥匙版Package交付并由阶段2登记 |
| FFmpeg/ffprobe | 终端用户不下载；随Package交付。当前候选组装资产仍为精确锁定的`gyan.dev` FFmpeg 9.0 ZIP，必须在Package构建、许可证和分发证据中核验 |
| Node/npm/npx | 终端用户不下载；随Package交付。锁定版本必须至少满足OpenMontage 18+且满足当前HyperFrames 22+，因此当前下限取22+ |
| Remotion可选依赖 | `https://registry.npmmirror.com`，仅在已选Remotion能力缺失时按锁准备 |
| HyperFrames可选依赖 | `https://registry.npmmirror.com`，仅在已选HyperFrames能力缺失时按锁准备 |
| 可选浏览器资产 | 只有所选能力的当前锁明确要求时，才使用批准大陆镜像的精确资产；不得预设为所有用户必装 |

不得把“大陆镜像失败”解释为可以回退海外官方源。可选能力仍须以Optional Runtime Lock中的版本、文件名、大小和SHA-256校验。必带FFmpeg和Node在Package组装时解决来源与分发，不能转嫁为终端用户阶段3下载。

### 4.3 阶段3重新规划边界

上一版`prepare_runtime_on_demand(...)`及其把Python依赖、FFmpeg、Node列为阶段3目标的Runtime Lock已失效，不得实施。新版阶段3入口必须等待两个真实输入：阶段2返回完整必带工具链身份，以及WorkBuddy/OpenMontage返回已经锁定的可选能力要求。届时仍限制为一个生产模块、一个公共入口、一个Optional Runtime Lock和一个直接测试文件。

Remotion的受管目标可位于`<DataRoot>/Runtime/Composition/Remotion`，HyperFrames可位于`<DataRoot>/Runtime/Composition/HyperFrames`；浏览器只有被当前能力锁要求时才位于`<DataRoot>/Runtime/Browsers/<capability>`，缓存为`<DataRoot>/Caches`。阶段3不得创建`Runtime/Python`、`Runtime/FFmpeg`或`Runtime/Node`作为Package必带工具链的替代品。

每个可选准备动作仍必须使用同卷staging、来源与SHA-256核验、产品所有权标记、原子发布、失败回滚和临时文件清理。现有目标不属于本产品或身份不匹配时必须保留原物并fail closed。

## 5. 消息与授权边界

`user_message`只包含用户真实会说的业务请求、素材、事实、授权和期望结果。执行包/Shell身份、路径、Python、cwd、测试编号、重试预算、停止条件以及证据采集只属于独立的`executor_controls`，两者禁止拼接。

下载、安装、网络、Provider、费用和重要降级分别授权；一个授权不得推导另一个授权。Shell只向WorkBuddy当前受控会话及其固定工具进程传递最小必要凭据，日志不得暴露明文。

## 6. MVP 明确非目标

- 不选择、推荐、排序或替换 Pipeline、Stage、Provider、模型、媒体方案或创意方向；
- 不创建或修改 Brief、Script、Scene Plan、Asset Manifest、Edit Decisions 等 Artifact，不判断 Reviewer 或推进 Checkpoint；
- 不以 CLI/MCP、嵌套 Agent、Supervisor、Director、任意 Shell 或 Shell 任务 FSM 建立第二控制面；
- 不把完整大型 Runtime、Web UI、SaaS、多租户、计费后台、外部发布或中文 fork 作为首版前置；
- 不在Shell修复WorkBuddy依据OpenMontage合同作出的素材方向、画幅、剪辑、成片质量或安全删除语义。

## 7. 代码与数据边界

- 生产代码谱系固定于 `2a2bf09832d558388dc2816c54b32a2dce4aa607`；V2 不 merge/rebase 推进中的 `main` 或旧长期分支，只允许带来源与消费者证据的选择性迁移。
- Shell、OpenMontage 执行包、Runtime、DataRoot和Projects分离；路径必须来自Package Registration，不得扫描盘符猜测。
- 老项目提交`347272c`证明包内便携Python引导；`899592d`证明锁定Runtime及大陆PyPI/npm/Node/浏览器镜像；`639978d`证明`managed`、`registered_host`、`PATH_host`、`missing`和missing-only准备。V2只迁移这些产品合同，不直接恢复旧大型实现。
- 开发、测试、缓存、构建和临时文件优先放 D 盘；升级和卸载默认保留 Projects、素材、配置、模型和输出。
- 阶段1只冻结本章程、旧资产处置和验收口径；`PASS_ACCEPTED`不构成阶段2授权。
