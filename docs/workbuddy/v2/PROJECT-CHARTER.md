# WorkBuddy Shell V2 项目章程

状态：`STAGE_3_PASS_ACCEPTED / STAGE_4_PLANNING_PASS_ACCEPTED / STAGE_4_IMPLEMENTATION_PASS_ACCEPTED / STAGE_5_IN_PROGRESS_ENTRY_CODE_COMPLETE_REAL_INTEGRATION_INCOMPLETE / SIX_MODULE_MVP`

```text
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_head_resolution: LIVE_REMOTE_REF_REQUIRED
formal_tree_resolution: LIVE_REMOTE_REF_TREE_REQUIRED
mirror_result: THIS_COMMIT
mirror_effect: ZERO_PRODUCT_STATE_CHANGE
mirror_repository_delivery_resolution: zero-write APPROVE exists AND LIVE_REMOTE_REF contains THIS_COMMIT
```

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
| Runtime按需准备 | 有界探测Remotion和HyperFrames，报告存在、缺失或不兼容；仅按用户逐能力授权集成批准的缺失项 | 输入：DataRoot、经批准的OpenMontage能力定义、受管/明确登记或配置/正常命令候选及逐能力用户决定；输出：`DETECTION_REPORT`、`CONSENT_REQUIRED`、`INTEGRATED`、`SKIPPED`或`BLOCKED`事实，以及每项能力的`PRESENT/MISSING/INCOMPATIBLE/NOT_INTEGRATED`状态 | 扫盘或枚举系统软件；把Remotion/HyperFrames当必带Runtime；发现/下载/替换必带Python/FFmpeg/Node；未授权或全局安装；由Shell或用户替OpenMontage选择渲染器；通用包管理器；海外默认源回退；修改系统PATH/注册表 |
| 会话Launcher | 对一次WorkBuddy拥有的会话先调用`locate_active_package(data_root)`重验活动Package和完整必带工具链；验证release-specific不可变固定工具定义；仅在该定义声明本地能力要求时接收完整批准能力定义与未改写Stage3原始fact，并按fact的managed/explicit/PATH来源语义独立重验实际资产；随后启动恰好一个固定Package工具并返回递归不可改写真实进程回执 | 输入：DataRoot、分离的literal `user_message`与closed `executor_controls`、`PackageToolDefinitionV1`、完整approved capability definition+original Stage3 fact和取消事件；输出：绑定Registration/Package/Manifest/Lock/tool/interpreter身份的一次真实退出、结果指针、错误及残留事实 | 改写用户原话；读取未验证Package Guide；硬编码或选择Provider/Runtime；查询/执行registry routing；绕过source-aware验证；启动第二Agent；解析意图；接受任意Shell/命令/调用者argv；安装Runtime；自动重试/重放；队列/服务/数据库/多进程调度；媒体生产；创建Artifact或推进Checkpoint |
| WorkBuddy入口 | 只提供一种真实WorkBuddy显式入口，收集当前必要授权并保持用户原话不变 | 输入：用户显式请求、素材和独立授权；输出：经Locator/Launcher绑定到活动执行包的原话及面向用户的回执 | 多套生产入口；全局截获；第二聊天Agent；由Shell选择Pipeline/Stage/Provider/模型/媒体/创意；把技术控制词写入用户消息 |
| 状态与结果转交 | 优先直接转交Runtime计划/准备事实、Launcher的会话/进程/退出/错误和WorkBuddy结果指针；只有真实格式缺口时才做一次确定性转换 | 输入：生命周期/Runtime/Launcher事实与WorkBuddy公开结果指针；输出：不改写语义的可审计回执 | 独立任务数据库/轮询/流式平台；解释Artifact业务语义；复制OpenMontage Stage/FSM；自动重试或伪造成功 |

安全、凭据保护、日志脱敏、路径所有权和单真实执行锁是六个模块的横切约束，不是独立模块，也不得发展为生产控制面。

### 4.1 阶段3至阶段6最小实现规则

阶段编号表示建设、审阅和正式交付顺序，固定为`阶段3 -> 阶段4 -> 阶段5 -> 阶段6`。这不是最终用户的一次运行调用顺序。阶段2已经接受Registration/Locator实现和真实临时证明；它不重开，也不成为Stage 3编码输入。最终用户实际运行从阶段5的WorkBuddy入口开始：

`V2-FINAL-PACKAGE-MATERIALIZATION-AND-PRODUCTION-REGISTRATION-GATE1`是后续最终交付或Installer收口任务：它持久生成最终Release、安装PackageRoot、建立生产Registration/Activation并用新进程Locator验明身份，最迟在阶段5真实WorkBuddy生产验收前完成。它不是阶段3或阶段4编码/规划前置；不得把这些动作塞入Runtime或Launcher，也不得因规划或task-only候选验证已完成而自动视为最终交付。

```text
User
-> Stage 5: one explicit WorkBuddy entry
-> Stage 2: revalidate retained production Package and required toolchain
-> Stage 4: one base fixed-tool call with required toolchain
-> WorkBuddy/OpenMontage: lock the actual render capability
   -> package FFmpeg capability: continue with bundled FFmpeg
   -> Stage 3 bounded-detects Remotion and HyperFrames
      -> present: report and reuse
      -> missing or incompatible: return a zero-download integration plan
      -> user declines or defers: SKIPPED / NOT_INTEGRATED; other capabilities remain usable
      -> user explicitly approves named items: integrate only those items under managed DataRoot and verify
   -> OpenMontage decides which available capability production uses
-> Stage 6: unchanged preparation, exit, error and result facts
```

- 每阶段最多一个公共入口、一个生产模块和一个直接测试文件；不能为了阶段编号制造文件。
- 没有已验证输入或直接下游消费者时必须零代码退出，不得用通用框架替代缺失合同。
- Python及核心依赖、FFmpeg/ffprobe、Node/npm/npx是Package交付及阶段2登记前置，不属于阶段3探测或下载对象。Remotion和HyperFrames是OpenMontage候选能力，可存在、缺失、稍后集成或一直不集成；缺失、拒绝或暂缓不阻塞Package、项目或其他已有/基础能力。
- 阶段3只有一个按需准备接口。所谓“扫描”仅指受管DataRoot路径、明确登记或配置的候选路径、正常命令解析三类有界探测；禁止遍历盘符、枚举系统软件清单、全局npm状态或猜目录。
- 阶段3只使用经批准OpenMontage能力定义给出的大陆来源、版本、大小、hash、许可证和目标事实生成计划；失败时不得自动回退海外源。用户同意只授权下载/集成逐项列明的能力，不构成渲染器选择。
- 阶段4基础固定工具调用继续接受阶段2必带工具链事实。Stage4接口不硬编码Remotion、HyperFrames或任何Provider/Runtime；只有release-specific固定工具定义的`required_local_capabilities`非空时，才接收同一opaque capability的完整批准定义与未改写Stage3原始fact。复核严格按fact source：managed要求受管root和全部定义资产closed-tree，explicit要求定义候选root和全部定义资产但允许且保留额外外来文件，PATH要求绝对regular command且只核对entrypoint asset；未知source拒绝。Provider API key或外部服务配置不属于Stage3证据；缺少可选配置时由固定工具保留真实退出，Stage4不得自行安装或选择替代项。
- 阶段3前只冻结最小结果到WorkBuddy动作接口，不要求真实WorkBuddy已经跑通。阶段5只保留一种真实WorkBuddy Skill入口，是用户实际运行的起点；在阶段5验收中证明新会话命中、明确同意与同任务继续，不能继续时固定提示用户回复“继续刚才的任务”。在入口格式确认前不得猜测Skill目录或同时建立CLI/MCP入口。
- 阶段6直接转交Runtime计划/准备事实和Launcher回执；可直接消费时返回`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`且不新增生产代码。它不得解释、安装或自动重试。
- 新能力必须同时有当前上游输入、当前下游消费者和直接验收；“以后可能需要”不是实现理由。

### 4.2 中国大陆镜像合同

老项目已经验证的大陆镜像先例只用于冻结渠道类别；每项经批准OpenMontage能力定义必须给出精确版本URL、大小、SHA-256、许可证和受管目标：

| 组件 | 终端用户下载渠道 |
|---|---|
| Python解释器及核心依赖 | 终端用户不下载；随金钥匙版Package交付并由阶段2登记 |
| FFmpeg/ffprobe | 终端用户不下载；随Package交付。当前已接受临时证明使用`gyan.dev`的`.7z`资产，二进制实际报告`9.0.1-essentials_build`；下一交付门禁必须以任务账本和Registration合同中的精确URL、大小、SHA-256及许可证为权威，不得凭“9.0”标签或ZIP字样猜测 |
| Node/npm/npx | 终端用户不下载；随Package交付。锁定版本必须至少满足OpenMontage 18+且满足当前HyperFrames 22+，因此当前下限取22+ |
| Remotion可选依赖 | `https://registry.npmmirror.com`，仅在探测为缺失/不兼容且用户逐项批准时按批准能力定义集成 |
| HyperFrames可选依赖 | `https://registry.npmmirror.com`，仅在探测为缺失/不兼容且用户逐项批准时按批准能力定义集成 |
| 可选浏览器资产 | 只有批准能力定义明确列入当前计划且用户一并批准时才集成；不得预设为所有用户必装 |

不得把“大陆镜像失败”解释为可以回退海外官方源。可选能力必须以批准OpenMontage能力定义中的版本、文件名、大小、SHA-256、许可证和目标校验。必带FFmpeg和Node在Package组装时解决来源与分发，不能转嫁为终端用户阶段3下载。

### 4.3 阶段3重新规划边界

上一版`prepare_runtime_on_demand(...)`以及把Python依赖、FFmpeg、Node、Package身份元数据或Registration列为阶段3输入的形状全部失效。新阶段3唯一建议入口为`prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`；结果闭集为`DETECTION_REPORT`、`CONSENT_REQUIRED`、`INTEGRATED`、`SKIPPED`和`BLOCKED`，每项能力事实只取`PRESENT/MISSING/INCOMPATIBLE/NOT_INTEGRATED`。

`capability_definitions`只包含Remotion和HyperFrames经批准的OpenMontage定义：版本、入口、批准大陆来源、文件/资产、大小、SHA-256、许可证、受管目标，以及可选的明确登记/配置候选路径和正常命令名。调用方不能注入任意URL、任意命令或任意安装根。`user_decisions`只表达对精确`capability + definition_sha256 + plan_sha256`的逐能力`approve/decline/defer`决定；定义、计划或当前探测事实变化后旧批准失效。

实现顺序固定为有界只读探测、逐能力事实报告、缺失/不兼容项的零下载计划、WorkBuddy询问、逐能力授权复核、同卷staging与来源/hash/许可核验、受管发布、失败回滚和最终探针。受管目标为`<DataRoot>/Runtime/Composition/<capability>/<definition_sha256>/`，缓存为`<DataRoot>/Caches/optional-runtime/`；浏览器只有批准定义和本次授权明确包含时才位于`<DataRoot>/Runtime/Browsers/<capability>/<definition_sha256>/`。阶段3不得创建`Runtime/Python`、`Runtime/FFmpeg`或`Runtime/Node`。

已接受实现只有一个新`runtime_prepare.py`生产模块、`__init__.py`的一次导出编辑和一个`test_runtime_prepare.py`直接测试，并同步更新两项验收基础设施。实现`a3f8959682d296301dc573c2835f8c705a52e8b2`及closeout `7c15aae4e77c579309312b21c79076f930970214`均已正式推广，Stage 3现为`PASS_ACCEPTED`。

### 4.4 最小WorkBuddy消费者接口

阶段3前冻结的是结果与动作映射，不是提前实现阶段5，也不是真实客户端PASS：

| 阶段3结果 | 唯一WorkBuddy动作 |
|---|---|
| `DETECTION_REPORT` | 展示Remotion和HyperFrames的`PRESENT/MISSING/INCOMPATIBLE`事实；不替OpenMontage选择 |
| `CONSENT_REQUIRED` | 对每个缺失/不兼容项展示来源、版本、大小、许可证和目标并逐项询问；本次零下载 |
| `INTEGRATED` | 报告已按授权集成并验证的能力；是否用于生产仍由OpenMontage决定 |
| `SKIPPED` | 报告用户拒绝或暂缓的能力为`NOT_INTEGRATED`；继续使用其他已有/基础能力 |
| `BLOCKED` | 只报告无效定义、越界目标或已授权集成失败；能力单纯缺失或用户拒绝不是`BLOCKED` |

WorkBuddy只在用户明确同意后回传绑定`capability + definition_sha256 + plan_sha256`的逐能力批准事实；任一事实变化都必须重新询问。拒绝或暂缓同样作为明确决定传回并得到`SKIPPED/NOT_INTEGRATED`。阶段5用唯一Skill验证真实交互；Shell不得保存或自动重放原始业务消息。

### 4.5 阶段3唯一产品事务

阶段3不是启动前的全环境检查，也不是安装中心。它以同一套有界算法探测Remotion和HyperFrames，报告事实，并只对用户逐项批准的缺失/不兼容能力执行受管集成。能力是否用于生产始终由OpenMontage决定。

固定事务顺序为：

1. 验证Remotion和HyperFrames两项批准能力定义；定义必须闭合来源、版本、入口、大小、hash、许可证和受管目标，调用方不得覆盖目标或注入任意命令/URL。
2. 只按受管DataRoot目标、明确登记或配置的候选路径、批准定义中的正常命令解析做只读探测；命令命中只产生待验证候选，禁止扫盘、全局npm枚举、系统软件清单和猜目录。
3. 对每项能力报告`PRESENT/MISSING/INCOMPATIBLE`及入口、版本和来源事实。能力存在则复用；能力缺失或不兼容本身不是失败。
4. 对每个缺失/不兼容项生成确定性零下载计划，包含批准来源、版本、文件/资产、大小、SHA-256、许可证、受管目标、总下载量和`plan_sha256`，返回`CONSENT_REQUIRED`。
5. WorkBuddy逐项询问用户。`decline/defer`返回`SKIPPED/NOT_INTEGRATED`，不得下载，也不影响其他能力或基础能力。
6. 仅对绑定`capability + definition_sha256 + plan_sha256`的`approve`项重新探测和复核；事实变化使旧批准失效。
7. 有效批准后才可在DataRoot同卷创建该能力专用staging，使用阶段2必带Node/npm/npx和批准大陆来源只准备批准的缺失对象，逐项验证后原子发布；禁止全局安装和自动海外回退。
8. 从受管目标重新探针入口、版本和资产，确认未批准能力与必带工具链零变化后返回`INTEGRATED`；失败回滚并清理任务临时对象。

阶段3的五种公共结果是`DETECTION_REPORT/CONSENT_REQUIRED/INTEGRATED/SKIPPED/BLOCKED`。探测、报告、计划和拒绝/暂缓必须零下载、零写入。有效授权后的失败可发生网络和任务临时写入，但不得发布半成品，必须清除本任务staging、部分下载和临时对象，并保留所有外来对象。阶段3不得自动重放原始业务请求。

### 4.6 阶段3输入、计划和就绪回执

`capability_definitions`中每项最小闭合字段为：

```text
capability: remotion | hyperframes
definition_sha256
version
verified_entrypoint
approved_mainland_sources
assets: filename + size + sha256 + license + managed_target
explicit_registered_or_configured_candidate_paths: optional
normal_command_name: optional
```

能力定义来自批准的OpenMontage能力定义权威，不依赖Package绑定能力元数据。请求不得携带定义外URL、任意命令、任意安装根、盘符扫描请求或literal `user_message`。

`user_decisions`中每项决定的最小闭合字段为：

```text
decision: approve | decline | defer
capability
definition_sha256
plan_sha256
```

计划必须以规范JSON和稳定排序计算hash，至少包含能力、定义身份、受管目标、每个缺失对象的类型/文件名/大陆镜像URL/大小/SHA-256/许可证/目标/准备方式和总下载量。定义、现有探测状态、资产、来源、许可或目标任一变化导致计划变化时，旧授权立即失效。

`PRESENT`探测事实和`INTEGRATED`结果向阶段4交付的最小能力证据为：

```text
status: PRESENT | INTEGRATED
capability
definition_sha256
runtime_root
verified_entrypoint
version_evidence
asset_evidence
plan_sha256: INTEGRATED only
```

该证据不是布尔值，不能跨能力或跨定义复用。Stage4只有在固定工具定义声明要求时才接收完整批准能力定义和该未改写原始事实，并按原始source独立重验：managed为DataRoot受管安全目录、全部asset和closed-tree；explicit为定义明确候选安全绝对目录、全部定义asset但允许额外外来文件；PATH为`runtime_root == verified_entrypoint`的绝对安全regular command、只核对entrypoint asset。未知source拒绝；`INTEGRATED`只允许managed并保留plan identity。`version_evidence`只作审计，source profile的精确asset identity不能证明相容性时fail closed。缺失或不匹配时不得自行安装，OpenMontage可选择其他已有/基础能力。

### 4.7 阶段3受管数据和原子性

阶段3只允许使用：

```text
<DataRoot>/Runtime/Composition/<capability>/<definition_sha256>/
<DataRoot>/Caches/optional-runtime/
<DataRoot>/Runtime/Browsers/<capability>/<definition_sha256>/  # only when approved in the plan
```

准备前的只读路径不得为了加锁而创建缓存或目录。取得有效授权后，互斥锁、下载临时对象和staging都必须位于`Caches/optional-runtime`内并与当前能力和定义绑定。取得准备锁后必须重新探测，允许并发调用复用另一调用已经完成的精确对象。所有对象先完整进入同卷staging并通过验证，再以原子目录发布；任何不完整对象和任务临时对象必须清除。

阶段3禁止创建`Runtime/Python`、`Runtime/FFmpeg`、`Runtime/Node`，禁止写PackageRoot、Registration、Activation、系统PATH、注册表、系统安装目录或用户全局npm目录。未知或外来目标必须保留原物并`BLOCKED`；能力单纯缺失或用户拒绝/暂缓不属于此状态。

### 4.8 阶段3实现单元与后续交接

已接受物理生产实现只有`golden_key_openmontage_workbuddy/runtime_prepare.py`一个新模块。模块内部的定义验证、有界探测、事实报告、计划生成、逐能力授权、staging发布、清理和最终探针均为私有职责；`__init__.py`只导出唯一入口，`test_runtime_prepare.py`只提供阶段3直接测试。

产品运行衔接固定为：阶段5接收用户原话并触发阶段2重验；阶段4可先用必带工具链执行基础固定工具；阶段3有界探测并按用户逐能力批准集成；OpenMontage从实际可用能力中决定生产选择；阶段6原样转交探测、计划、用户决定、集成、退出和错误事实。建设顺序仍是`3 -> 4 -> 5 -> 6`，不得把它误写成用户运行顺序。

### 4.9 Stage 4规划接受、实现结果与收口边界

Stage 4规划为`PASS_ACCEPTED`，两个合同缺口已经冻结。Stage4实施授权已经消费完成，但始终不等于真实生产Launcher运行授权。当前Stage 2 `locate_active_package(data_root)`继续只负责返回并重验Registration SHA、PackageRoot、Python/FFmpeg/ffprobe/Node/npm/npx、Guide、Manifest和Lock身份，不新增工具入口字段、不重开Registration。

已接受规划用`PackageToolDefinitionV1`闭合固定工具身份来源、release-specific相对路径/hash/size/owner、解释器、固定argv、Manifest/Lock绑定和路径防替换规则；用`launch_session_tool(...)`及`LauncherReceiptV1`闭合唯一公共入口、单进程生命周期、输入/输出、结果闭集和不可改写回执。具体Release实例仍由批准Package定义/最终交付Installer owner提供；缺实例时真实调用preflight阻断，不要求编码前先物化最终Package。

这些合同已经`V2-S4-PLAN-REVIEW1`独立APPROVE、规划closeout审查并普通fast-forward。实现严格限定在已冻结五路径，将tracked从35精确迁移到37；最终实现对象`fa9adb8470ab94b88ec9900ede03cb26f7de0ebd`、tree `0809d1c4cccc9838180a016c75320b0d9fbce28a`经第八轮独立零写审查`APPROVE / P0=0 / P1=0 / P2=0`后普通fast-forward。首个正式CI run `32367792637`失败只因测试夹具错误假定GitHub `setup-python`环境存在`pyvenv.cfg`，不是生产Launcher缺陷；单测试路径修复`13a3227b0c55bbe9039b46d7e92eba822b48f57e`、tree `d3ac89ec89b66789cabe92d94c3e827f9c2cc22f`也经独立审查`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward，正式Ubuntu 24.04 / Python 3.11.16 CI run `32369588814`为`357 passed / 1 skipped / exit 0`。Windows最终证据为158 direct、11 hygiene、358 combined，全部exit 0且无skip。

Implementation Reviewer发现的secret nondisclosure不可表示P1已经由`V2-S4-SECRET-NONDISCLOSURE-CONTRACT-CLARIFICATION-BUILDER1`有界澄清，并在独立`APPROVE / P0=0 / P1=0 / P2=0`后普通fast-forward；该历史问题已关闭，没有重开其他规划合同。Stage4 closeout固定历史锚点为`b63d8c2bc2214bc39f18378dbe47057ef538301e`、tree `02814c6a4a483913e7b1abe3e9ee6d025236c951`，`V2-S4-IMPLEMENTATION-CLOSEOUT-REVIEW1`为`APPROVE / P0=0 / P1=0 / P2=0`，正式CI run `32371507874`在Ubuntu 24.04 / Python 3.11.16上`357 passed / 1 skipped`。Stage4实现已是`PASS_ACCEPTED`；其中`current_task=NONE / current_task_status=NO_ACTIVE_TASK / next_authorized_task=NONE`是`HISTORICAL_STAGE4_CLOSEOUT_CONTEXT`，不覆盖当前Stage5 authority。`mirror_result/mirror_effect/mirror_repository_delivery_resolution`只自解析镜像仓库交付，不形成当前任务、不重新门禁这一既有产品状态。真实生产WorkBuddy/Launcher会话、WorkBuddy新会话/入口/授权询问和同任务继续、Stage6、Provider/媒体执行及final Package物化/生产登记仍为`NOT_GRANTED`或未证明。WSL只用于临时Linux等价验证，已清理并关闭，不是Stage4运行依赖。

### 4.10 Stage 4冻结公共合同

Stage 4唯一公共入口固定为：

```python
launch_session_tool(
    data_root: str | os.PathLike[str],
    user_message: str,
    executor_controls: Mapping[str, Any],
    package_tool_definition: Mapping[str, Any],
    local_capability_evidence: Sequence[Mapping[str, Any]] = (),
    cancel_event: threading.Event | None = None,
) -> Mapping[str, Any]
```

`user_message`是原样业务文本；`executor_controls`只含`schema_version/session_id/request_id/timeout_seconds/termination_grace_seconds/result_root/provider_environment`七个closed字段。两者在函数参数和stdin envelope内保持不同字段。`provider_environment`所有非空value无条件属于Provider-secret来源，唯一授权sink是子进程环境；实现须在生成pre-cancel hints、stdin、receipt、日志或异常前保守提取这些来源并防止复制/派生。返回值及后代全部递归冻结。

固定工具身份只来自批准Golden Key OpenMontage Package定义与最终交付/Installer owner提供的release-specific immutable `PackageToolDefinitionV1`。其closed字段固定为`schema_version/definition_id/definition_sha256/definition_relative_path/authority_owner/package_release/package_commit/tool_id/relative_path/sha256/size/owner/execution_kind/interpreter_binding/fixed_argv_template/fixed_argv_placeholders/request_schema_sha256/result_schema_sha256/allowed_environment_names/secret_environment_names/required_local_capabilities`；本地requirement另固定`compatibility_basis=EXACT_ASSET_IDENTITY`。定义字节不含Registration/Manifest/Lock hash，避免定义文件由Manifest/Lock覆盖时形成hash环；当次Locator的Registration/Manifest/Lock身份由Stage4在preflight外部绑定并写入receipt。定义文件自身必须位于PackageRoot并由当前Manifest与Lock唯一覆盖，传入Mapping的规范JSON字节必须与该文件完全相同，Manifest owner必须等于`authority_owner`；因此调用者不能自造定义。Release实例中的relative path/hash/size/owner/fixed argv都是必填事实；它们不要求最终Package先物化才能规划或编码，但真实调用缺实例时必须preflight阻断，绝不从Guide、registry、目录或调用者命令推断。真实测试还必须用含定义与工具的Package fixture完成`register -> locate -> validate`往返，证明该合同可实例化而不把最终Package变成前置。

`execution_kind`只取`PACKAGE_PYTHON_SCRIPT/DIRECT_EXECUTABLE`，并分别绑定`LOCATOR_PACKAGE_PYTHON/SELF`。固定argv只允许Package定义中的literal token；Python脚本唯一占位符为恰好一次`{verified_tool_path}`，直接可执行文件没有占位符。所有业务数据走单个规范JSON stdin envelope；不存在任意argv、shell解释或命令字符串。

OpenMontage的capability/provider registry是动态业务权威。Stage 4不查询、不缓存、不复制该registry，不枚举Provider或合成运行时，不负责生图、生视频、TTS、音乐、stock、local GPU、FFmpeg、Remotion或HyperFrames的选择。`allowed_environment_names`只控制哪些已解析Provider配置可传入；Provider-secret source不得复制/派生进receipt/log，secret-independent常量或`TASK-REGISTER.md`字段级闭集内、可从Package/PackageToolDefinition/Manifest+Lock/实际工具与解释器字节独立重建的权威字段偶然相同不属于传播。`required_local_capabilities`使用opaque `capability_id+definition_sha256`，只有固定工具定义声明时才要求`golden-key-workbuddy-local-capability-evidence-v1`。每项证据必须携带完整批准capability definition、其canonical SHA、未改写的Stage3原始`PRESENT/INTEGRATED` fact及其canonical SHA；Stage4独立重算closed definition/fact hash，并source-aware重验实际字节：managed受管root核对全部assets和closed-tree；explicit定义候选root核对全部定义assets、允许且不改动额外文件；PATH要求runtime root等于绝对regular entrypoint并只核对entrypoint asset。未知source拒绝，`INTEGRATED`必须managed并保留`plan_sha256/reused`及完整fact identity。原始fact及所有由它派生的`plan_sha256/original_stage3_fact_sha256/status/source/reused/runtime_root/verified_entrypoint/version_evidence`均属动态域；因receipt local identity混合这些字段与资产事实，整个identity不得套authority例外。任一字段包含或派生Provider-secret时必须preflight fail closed、spawn 0并清空整个identity tuple。原始fact只作来源审计，调用者或fact的version_evidence不受信；若对应source profile的精确asset identity不足以唯一证明相容性则fail closed。当前Stage3的Remotion/HyperFrames定义与事实只是现有来源，未来能力扩展需另行授权；Provider配置不是本地能力证据，Stage5只能原样传递上述定义与原始fact，不得重包装摘要。

进程合同固定为：调用Locator并重验、核对定义与Manifest/Lock、逐路径组件拒绝symlink/junction/reparse/逃逸、spawn前再次复核全部身份、`cwd=verified PackageRoot`、最小环境白名单、`shell=False`、恰好一次spawn、无重试。timeout或取消只终止Launcher自有进程树并报告残留；stdout/stderr是不可信child输出，必须以完整secret UTF-8 bytes跨chunk检测，命中即`SECRET_DISCLOSURE_DETECTED`且固定常量例外不适用。未受污染的流只返回真实size/hash/truncated而不返回原文；受污染流返回合同固定的安全抑制摘要。exit 0还必须得到与session/request匹配的单个规范结果envelope和位于受控result root内的有效hash/size指针，才可成功。

不可改写receipt schema固定为`golden-key-workbuddy-launcher-receipt-v1`；根字段固定为`schema_version/outcome/reason_code/session/request/registration/package/manifest/lock/tool_definition/tool_file/interpreter/user_message/provider_environment_names/local_capability_evidence_identities/launched/spawn_count/pid/started_at_utc/ended_at_utc/duration_ms/exit_code/timed_out/cancelled/retry_count/stdout/stderr/result_pointer/error/residual_process`，任何输入/preflight/spawn/运行结果都总是返回该全字段递归冻结receipt。结果闭集仍为九值、reason仍为23个、裁决仍为11级。固定且secret-independent的schema/outcome/reason/field names/预冻结标识文本，及`TASK-REGISTER.md`精确字段闭集内的独立Package/definition authority字段，和secret偶然字节相同不算传播；不得为消除碰撞改闭集或类型。所有caller/child动态域在freeze前必须做provenance-aware non-propagation检查；`local_capability_evidence_identities`的item因含fact-derived字段而整体视为动态对象，任一item受污染时清空整个tuple。其他受污染值以字段已有的`None`、空tuple、固定安全文本或安全流摘要替换，不能删除字段或向`tuple[str]`写入`None`。入口已取消仍精确为`CANCELLED/CANCELLED_BEFORE_SPAWN`且Locator/spawn为0；若secret等于session/request，只清空相关hints，不得使固定取消receipt不可表示。exit 0+child `FAILED`仍精确为`CHILD_REPORTED_FAILURE/CHILD_REPORTED_FAILURE`，`retry_count`恒为0。完整字段类型、安全替换、reason闭集、stdin/result envelope及测试矩阵以`TASK-REGISTER.md`的Stage4执行任务包为live implementation authority。

Stage 5保留用户原话、形成controls并提供经授权Provider配置和Package工具定义；固定定义声明本地要求时，Stage5原样传递完整approved capability definition与original Stage3 fact。Stage 4按原始managed/explicit/PATH source语义独立复核实际资产，只启动固定工具并返回receipt；Stage 6优先原样复用receipt，能直接消费时生产代码为0。该接口不预建Stage5/6，也不使Stage4实现自动获权。

### 4.11 Stage 5规划边界与T1-T12冻结

Stage 5的唯一产品目标是：真实腾讯WorkBuddy作为唯一运行中的Agent，通过一个且仅一个显式入口接收用户业务请求和素材；保持literal `user_message`原样；将技术控制、授权、当前Release的`PackageToolDefinitionV1`、Provider环境和完整Stage 3原始事实分离承载；按“显式入口 -> Stage 2 Locator -> Registration/PackageRoot/Manifest/Lock/Guide/完整必带工具链验证 -> 已验证Guide -> 当前Release工具定义 -> Stage 4一次固定工具调用”的顺序执行；由WorkBuddy/OpenMontage承担生产决策；把事实和结果转交给Stage 6。Shell不成为第二Agent、Director/FSM/Supervisor、Pipeline/Stage/Artifact/Checkpoint执行器、Provider/渲染器选择器、CLI/MCP控制面、自动重试/重放器或后台调度器。

```text
Stage 4 accepted contract -> Stage 5 one WorkBuddy entry -> Stage 6 direct fact/receipt relay
                                      |
                                      +-> WorkBuddy/OpenMontage owns Guide, Pipeline, Provider, media and creative decisions
```

`[HISTORICAL_PRE_CLOSEOUT_T1_STATE]` 本段记录 closeout 前的规划状态`stage_5_planning=IN_PROGRESS / T1_FIXED_CLI_BRIDGE_FROZEN_FOR_PLANNING`；不得把“CLI/MCP/命令/argv/Shell直调未被腾讯官方定义”解释为 CLI 一概禁止。T1 固定边界仍是：WorkBuddy 唯一 Agent 通过一个真实 Skill 入口，固定 CLI 仅可作为该 Skill 内部的单消费者 transport adapter；第二用户入口、并行控制面、第二 Agent、失败兜底、任意命令/argv/Shell 生成和自动重试/重放仍禁止。固定 CLI 的 release-specific identity、固定模板、单一 JSON envelope、Stage4 API 调用和 `LauncherReceiptV1` 映射已冻结为本项目 `FROZEN_FOR_PLANNING` 内部合同；本 closeout 候选的 `PASS_ACCEPTED` 规划状态和实施交接字段已接管当前 live 候选，不再以本段的 IN_PROGRESS/NOT_GRANTED 镜像作当前状态。原 `T1_EVIDENCE_INCOMPLETE` 和旧的“零 CLI”条件均保留为历史证据候选，已由本轮机制确认和内部合同冻结 supersede；不得把 CLI 存在本身判为架构不可用。现有两个Golden Key Skill是V1双入口/旧CLI形态，不能复用；不得以假Skill、CLI、MCP或第二Skill填补仍未证明的真实合同。Stage 5真实WorkBuddy、Provider/媒体、Stage 6、最终Package和生产Registration均继续`NOT_GRANTED`或未证明。

T1-T12的详细执行合同以`TASK-REGISTER.md`同名章节为唯一任务级权威；本章程冻结其产品裁决如下：

| 任务 | 产品裁决 | 物理承载/实施边界 | 通过或停止 |
|---|---|---|---|
| T1 入口身份 | 证明唯一真实Skill的包、安装归属、调用主体、固定内部CLI桥梁和消费者 | 一个 WorkBuddy-managed Skill catalog 入口；物理路径保持opaque；固定 CLI 必须是该入口内部单消费者 transport adapter | 官方资料和既有客户端确认 WorkBuddy 外部 Skill/CLI 机制；本候选已冻结固定 interpreter/module/argv/schema/环境/receipt 合同，release-specific hash 由 Installer/Skill 资产写入并验证；当前为`T1_INTERNAL_FIXED_CLI_BRIDGE_CONTRACT_FROZEN_FOR_PLANNING`，不编造物理路径 |
| T2 输入合同 | 原话、素材、controls、工具定义、Provider环境、完整Stage3事实、取消/继续分离 | 只进入唯一入口和受控调用域，不落平行服务 | 跨域/摘要重包装即停止 |
| T3 验证顺序 | Locator及全部身份成功后才读Guide和取得工具定义 | 不扫盘、不猜路径、不复制Guide | 身份/Guide/必带工具链失败则spawn 0 |
| T4 Stage4适配 | 只消费固定`launch_session_tool(...)`与`LauncherReceiptV1`；可由T1冻结的固定CLI内部桥梁承载 | 不拼接任意命令、argv、Shell，不建立第二Launcher；固定 CLI envelope 必须原样传递输入并逐字段返回receipt | 违反一次固定调用、动态命令、摘要替代、重试/重放或第二入口即停止 |
| T5 授权继续 | 能力、服务、网络/费用独立授权；拒绝/暂缓可走基础；不支持继续时提示“继续刚才的任务” | 不保存重放请求、不建授权数据库 | 失效授权/自动重放即停止 |
| T6 结果映射 | Stage3五结果与Stage4九outcome闭集映射 | 直接呈现receipt/事实，不解释Artifact | 失败不得改成功，优先级不重排 |
| T7 凭据隐私 | secret只进定义allowlist child env；Key不等于可用/授权/成功 | 无Provider目录、日志仓或独立服务 | 任意非授权传播即fail closed |
| T8 失败闭集 | 15类失败逐项给出Locator/Stage4/spawn/用户结果/基础继续/终止 | 复用Stage4 11级优先级 | 未分类、残留、泄密或无最终exit即停止 |
| T9 Package Gate | 规划可用受控fixture；真实生产前必须最终Package/安装/Registration/Activation/新进程Locator | 最终Package由后续Installer承载，入口不物化 | 缺具体Release定义实例真实调用阻断 |
| T10 证据分层 | 静态、测试、Stage2/3/4集成、WorkBuddy入口/原话/授权继续、生产身份、Provider/媒体、业务效果各自裁决 | 不用前层PASS冒充后层 | 缺证据保持`NOT_PROVED/INCOMPLETE` |
| T11 Stage6交接 | 先直接复用`LauncherReceiptV1`；无字段缺口则生产代码0 | 本阶段不预建Stage6 | 只有真实缺口才另行授权 |
| T12 实施任务包 | Builder=`V2-S5-WORKBUDDY-ENTRY-BUILDER1`；入口1、生产模块≤1、直接测试1 | 精确白名单已冻结为`workbuddy-skill/golden-key-openmontage/SKILL.md`、`golden_key_openmontage_workbuddy/workbuddy_entry_cli.py`、`tests/workbuddy/test_workbuddy_entry_cli.py`，并最小同步`tests/workbuddy/test_repository_hygiene.py`、`.github/workflows/ci.yml`；tracked`37 -> 40`；固定direct/hygiene/full命令见任务账本；第N+1路径停止 | 用户已明确“启动阶段五实施”；本候选正式推广后才可由最新formal Builder接管，独立APPROVE和普通FF仍必须 |

本候选只能修改六份 authority 文档：`AGENT_GUIDE.md`、`PROJECT-STATE.md`、`docs/workbuddy/v2/TASK-REGISTER.md`、`docs/workbuddy/v2/PROJECT-CHARTER.md`、`docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`、`docs/workbuddy/v2/DRIFT-GUARD.md`；不改代码、测试、CI、Package或外部对象，不运行WorkBuddy/Launcher/Provider/媒体/WSL。候选经独立 Reviewer `APPROVE/P0=0/P1=0/P2=0`并普通 FF 后，Stage5 planning 才成为`PASS_ACCEPTED`；随后`current_task=NONE`、下一任务为`V2-S5-WORKBUDDY-ENTRY-BUILDER1`。用户实施授权已记录，但 Builder 必须从届时最新formal精确对象接管，不能由本候选冒充实施完成；真实客户端、最终Package/Registration、Provider/媒体和Stage6仍未证明或未授权。

#### T1官方证据候选的固化边界（历史候选，已被当前Skill+CLI重新评估取代）

Evidence1 只使用腾讯/WorkBuddy官方公开资料和仓库已有静态证据，访问日期为 `2026-08-21`；受控真实客户端在该历史任务中固定为 `NOT_AUTHORIZED_IN_THIS_TASK`。官方资料能确认 WorkBuddy 有 Skill 导入/安装、对话选择和自动调用能力，也确认存在脚本/外部程序权限控制；连接器资料另明确公开 `Skill + CLI（内置脚本）`形态。官方页面没有给出本项目固定 CLI 的身份、envelope、唯一消费者或 `LauncherReceiptV1` 映射；这属于本项目内部桥梁合同缺口，不是 CLI 一概禁止的证据。

`[HISTORICAL_PRE_CLOSEOUT_T1_REASSESSMENT_CONTEXT]` 任务级来源、精确 URL、页面更新时间、claim/gap 和 closeout 前裁决曾以 `TASK-REGISTER.md` 的 T1 Skill+CLI 章节为唯一权威；旧 Evidence1 五项表和“零 CLI”条件仅作历史记录。当前不可漂移规则仍是：官方资料和既有客户端证明 WorkBuddy 的外部 Skill/CLI 机制，项目文档冻结的是一个 Skill 内固定 CLI 的单入口/单消费者/固定 envelope 边界；物理安装路径保持 opaque，不从 CodeBuddy 页面推断 WorkBuddy 路径。固定 CLI identity、内部调用映射和唯一消费者已由前置 T1 合同冻结为 `FROZEN_FOR_PLANNING`；当前 Stage5 planning 状态和实施交接以本章程下方 closeout 候选及顶部 live 字段为准。不得从相邻腾讯产品、旧V1 Skill或自然语言/脚本能力填造本项目接口，也不得把 CLI 本身当成架构不可用。

后续另行授权的受控客户端任务已在 WorkBuddy `5.3.13` 执行：D盘隔离根中的唯一无副作用 candidate Skill 通过客户端默认安全检测导入；客户端可见合同确认文件夹或ZIP包含`SKILL.md`，Markdown YAML含name/description；新任务的`/`入口显式加载 exact Skill，并在明确选择`Hy3`后返回`T1_CONTROLLED_NOOP_OK`。第一次Auto结果只作为探测历史，不计入HY3验收。该证据把显式调用提升为`PROVED_CLIENT_FOR_5.3.13_SESSION`，但完整schema、物理安装位置与完整归属、全局唯一消费者，以及固定 CLI identity/envelope 与 Stage4 `launch_session_tool(...)`/`LauncherReceiptV1` 绑定仍未证明。因此历史总结果保持`T1_CLIENT_EVIDENCE_INCOMPLETE`，不得将其改写成 CLI 禁止或 CLI 可用；不得运行Provider、媒体、最终Package或Stage4真实spawn，也不得启动Stage5实现。

#### T1 Skill+CLI合同重新评估（当前候选）

本节是当前 T1 裁决，优先于本章前述历史 Evidence1/客户端候选文字。最初产品目标回读为`PASS`：WorkBuddy 是唯一运行中的 Agent 和唯一用户入口；它读取已验证 Package Guide 后承担 OpenMontage 逻辑生产角色。官方资料确认 Skill 可以封装脚本/工作流，且官方连接器技术形态包含 `Skill + CLI（内置脚本）`；因此固定 CLI 不因其为 CLI 而被排除。

当前项目合同只允许以下单链：

```text
WorkBuddy conversation
  -> one WorkBuddy-managed Skill catalog entry
  -> one fixed internal CLI bridge (not a user-facing second entry)
  -> accepted Stage 4 launch_session_tool(...)
  -> one immutable LauncherReceiptV1
```

固定 CLI 必须有可验证的 release-specific identity/owner/hash（或等效身份）、固定单一 input/output envelope；它原样承载 `literal user_message`、非秘密 closed controls、`PackageToolDefinitionV1`、完整 approved capability definition 与 original Stage 3 fact、cancel 事实，并逐字段回传 `LauncherReceiptV1`。Provider secret value 不进入 envelope：CLI 只按 `provider_environment_names` 从自身进程环境读取并重建 Stage4 `executor_controls.provider_environment`，再由 Stage4 依据 allowlist 注入固定 child 环境。不得把用户原话拼成任意 command/argv/Shell，不得使用 MCP/第二Skill/全局意图截获作旁路，不得自动重试或重放。WorkBuddy-managed Skill catalog 是可冻结的逻辑归属，官方未披露的物理路径保持 opaque；CodeBuddy Skills 页面及 `.codebuddy/skills` 不能作为 WorkBuddy 路径合同。

`[HISTORICAL_PRE_CLOSEOUT_T1_CONTRACT_STATE]` 本轮官方能力形态和既有 HY3 exact Skill 命中已足以判定“唯一 Skill 内部固定 CLI”是可用的外部机制；本 T1 候选把固定 CLI identity、固定 argv、单一 JSON envelope、secret-safe controls、全局唯一消费者、一次 `launch_session_tool(...)` 和真实 `LauncherReceiptV1` wire mapping 冻结为 `FROZEN_FOR_PLANNING`。固定命令严格为 `LOCATOR_PACKAGE_PYTHON -I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli`，无 console-script/子命令/动态 argv；pre-Stage4 错误无 stdout receipt，Stage4 返回的任何真实 receipt 才是运输成功。该 T1 状态已被实施结果和本文末当前入口收口 mirror 接管；不要把本段的 `stage_5_planning=IN_PROGRESS / T1_FIXED_CLI_BRIDGE_FROZEN_FOR_PLANNING`、`stage_5_implementation_authorization=NOT_GRANTED` 或旧下一任务当作当前 live 值。真实客户端/Stage4执行仍未证明；实施结果、收口候选和独立推广条件见本文末新节。

### T1固定桥梁的最小可实现字段与出口

逻辑安装归属固定为一个 WorkBuddy-managed Skill catalog entry，物理路径保持 `opaque`。Installer/Skill release asset 必须写入并可验证 `skill_identity/release_identity/authority_owner/bridge_contract_id/interpreter_binding/absolute_package_private_interpreter_identity+path/module_name/module_sha256/request_schema_id+hash/result_schema_id+hash/fixed_argv+hash/bridge_environment_names`；缺失或漂移即停止，不从客户端目录或 CodeBuddy 页面猜路径。固定执行模板只有 `LOCATOR_PACKAGE_PYTHON -I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli`，CLI 是无子命令、无路由、无业务决策的 transport adapter。T4 禁止调用者、用户消息或 controls 动态生成/追加 argv；Installer/Skill release asset 预冻结的固定字面量模板及其 hash 不属于动态生成，模板漂移即 fail closed。

单一 stdin 是 versioned canonical JSON envelope：`schema_version/bridge_contract_id/data_root/user_message/executor_controls/package_tool_definition/local_capability_evidence/cancel_requested/continuation`。canonical 只约束 UTF-8 wire encoding、key order、数字形式和单个末尾 LF，不对 literal `user_message` 做 NFC/NFD、trim 或换行转换；桥接层只验证 Stage4 既有的 NFC/合法字符串前置，非 NFC、surrogate、非法 UTF-8/JSON 或其他 closed Stage4 string contract 违例直接按 exit `64` fail closed，已满足前置的 Unicode code-point sequence 原样传给 Stage4。`executor_controls` 只含 schema、session/request、timeout、termination grace、result root、固定 process-env source 和 `provider_environment_names`；不含 `provider_environment` secret values。完整 `PackageToolDefinitionV1`、完整批准 capability definition 和未改写 Stage3 原始 fact 均逐字段承载，禁止摘要/改写。CLI 只在自身进程环境名称集合与固定 bridge names 加声明 names 完全匹配、且 names 是定义 allowlist 子集时读取值；缺失、额外或禁用名称 pre-Stage4 fail closed。值不进入 JSON、argv、stdout、stderr、hash、长度、log、异常或 receipt，只经 Stage4 `provider_environment` 到 allowlisted child env。

stdout 只允许一个 `golden-key-workbuddy-launcher-receipt-v1` JSON mapping，逐字段对应 immutable `LauncherReceiptV1`；stderr 只允许固定脱敏诊断 token。transport exit code 闭集只为 `0/64/70/78`：`0`=Stage4 恰好一次且完整 receipt 已缓冲、验证、序列化并输出（真实失败 outcome 也为 `0`）；`64`=input/schema/identity/cancel/continuation 或 Stage4 `user_message` NFC/UTF-8 前置无效；`78`=固定 asset/process-env/provider-name 配置或 secret provenance 无效；`70`=bridge internal 或 Stage4 后完整 receipt 序列化/输出前验证失败。stdout 必须先完整缓冲验证，任一非 `0` 错误时为空且不得伪造 receipt。`cancel_requested` 只在入口创建并设置本地 `threading.Event` 后传入一次 Stage4；运行中取消/Host终止不发明后台 IPC。continuation 只能是用户明确确认的新 request/envelope，禁止 replay。该固定桥梁合同已被本 closeout 候选消费；其 PASS_ACCEPTED 规划结果、未来白名单和下一 Builder 条件见下节。

### [历史 / 已被 V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1 取代] Stage 5规划收口与实施交接候选

本节记录前一轮 `V2-S5-PLANNING-CLOSEOUT-IMPLEMENTATION-HANDOFF-ASSESSMENT1` 的历史 handoff 条件；后续 Builder 已消费其白名单并完成正式实施结果。当前 Stage5 状态和入口收口以本文末新的六文档 mirror 为准。

未来 Builder 只允许五条实现/验收路径：

1. `workbuddy-skill/golden-key-openmontage/SKILL.md`：唯一仓库 Skill 源资产；root `SKILL.md`、name/description YAML 是既有客户端最小导入事实。客户端物理安装路径保持 opaque，最终 Installer/Package gate 必须按 release identity、owner、固定 module/schema/argv/environment hash 承载，placeholder/漂移 fail closed。
2. `golden_key_openmontage_workbuddy/workbuddy_entry_cli.py`：唯一 package-private `-I -m` transport adapter，不加入公共导出。
3. `tests/workbuddy/test_workbuddy_entry_cli.py`：唯一直接测试。
4. `tests/workbuddy/test_repository_hygiene.py`：只同步 tracked/source inventory、唯一 Skill 和 CLI module 断言。
5. `.github/workflows/ci.yml`：只把新直接测试加入现有单一 pytest 命令，不改触发器。

目标 tracked 为 `37 -> 40`；不改 `__init__.py`、`pyproject.toml`、`MODULE-DISPOSITION.md`。D盘 task-private venv 固定为 `D:\BlazingCD\Personal\Temp\workbuddy-v2-s5-entry-builder1\.venv`。direct、hygiene、full/CI 命令分别为：

```text
python -m pytest -p no:cacheprovider tests/workbuddy/test_workbuddy_entry_cli.py -q
python -m pytest -p no:cacheprovider tests/workbuddy/test_repository_hygiene.py -q
python -m pytest -p no:cacheprovider tests/workbuddy/test_package_registration.py tests/workbuddy/test_runtime_prepare.py tests/workbuddy/test_session_launcher.py tests/workbuddy/test_workbuddy_entry_cli.py tests/workbuddy/test_repository_hygiene.py -q
```

这只是实施 handoff，不是实施完成或真实生产 PASS；真实 WorkBuddy、最终 Package/Registration、Provider、媒体和 Stage6 仍需独立证据与门禁。

## 5. 消息与授权边界

`user_message`只包含用户真实会说的业务请求、素材、事实、授权和期望结果。执行包/Shell身份、路径、Python、cwd、测试编号、重试预算、停止条件以及证据采集只属于独立的`executor_controls`，两者禁止拼接。

下载、安装、网络、Provider、费用和重要降级分别授权；一个授权不得推导另一个授权。Shell只向WorkBuddy当前受控会话及其固定工具进程传递最小必要凭据；Provider value只能进入固定child环境，不得复制或派生进argv、stdin、动态receipt、日志或异常。协议常量偶然相同不等于凭据传播，但不可信child输出没有该例外。

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

## 10. [HISTORICAL / SUPERSEDED_BY_V2-S5-R00-REMAINDER-PLAN-STATE-CORRECTION1] Stage 5实施结果与入口收口候选（2026-08-21）

Stage 5 planning 当前为 `PASS_ACCEPTED`，不是 candidate。`V2-S5-WORKBUDDY-ENTRY-BUILDER1` 已 `CONSUMED_COMPLETE`，其实施结果为 `0e7a0be65877b03fb386e1c6c6bc258c0b27db6c`（tree `85c266edb7349c940e8cd45870cc0538c95726c0`，parent `aa70c2cf9b6b4a29517d7354f0239ea0cdc9a5d3`），精确五路径、tracked `37 -> 40`，独立 Reviewer `APPROVE / P0=0 / P1=0 / P2=0`。Windows 最终证据为 direct `19 passed`、hygiene `11 passed`、full `377 passed`，均 final exit 0；正式 CI 为 run `32489111184`、completed/success、headSha 同上、Ubuntu/Python 3.14.7、`376 passed / 1 skipped`。

本轮 `V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1` 只做六文档 `DOCS_ONLY / EXACT_6_PATHS / ZERO_PRODUCT_STATE_CHANGE` 镜像。候选在独立 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 与 ordinary fast-forward 进入 formal 前不能自称已交付；只有该推广后 `stage_5_implementation=PASS_ACCEPTED`。收口后 `current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE`，不自动授权真实 WorkBuddy production acceptance、最终 Installer-stamped Skill、最终 Package materialization/Registration、Provider/media 或 Stage 6。

唯一入口合同保持一个 WorkBuddy-managed Skill -> package-private fixed `-I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli` -> 恰好一次 `launch_session_tool(...)` -> immutable `LauncherReceiptV1`。禁止 console script、subcommands、router、MCP、第二 Agent、retry/replay、动态 command/argv/Shell；literal message、closed JSON、provider-secret、fixed identity、cancel/continuation 与 receipt 边界保持不变。静态、direct、hygiene、CI 证据与真实 WorkBuddy/业务/E2E 证据严格分层。

精确五个实施路径为：`.github/workflows/ci.yml`、`workbuddy-skill/golden-key-openmontage/SKILL.md`、`golden_key_openmontage_workbuddy/workbuddy_entry_cli.py`、`tests/workbuddy/test_workbuddy_entry_cli.py`、`tests/workbuddy/test_repository_hygiene.py`。物理 Skill 安装路径保持 opaque；最终 Installer/Package/Registration、真实客户端、Provider、媒体和 Stage 6 均须另行授权与验证。

## 11. [HISTORICAL / CONSUMED_BY_V2-S5-R01] Stage 5剩余计划（R00纠偏）

Stage 5整体状态固定为 `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`。WorkBuddy仍是唯一运行中的Agent和唯一用户入口；Shell仍只负责六模块，不成为Director/FSM/第二Agent/媒体控制面。已交付的入口代码、固定CLI、一次Stage4调用、Reviewer和CI只能证明entry-code子项，不等于整体PASS。

整体 `PASS_ACCEPTED` 必须同时有五类证据：持久 final Package Release+PackageRoot；production Registration+Activation+new-process Locator；无placeholder且唯一的最终安装Skill；HY3真实WorkBuddy成功取得真实`LauncherReceiptV1`；独立Review、正式Git/CI和无歧义live authority。Provider、媒体/视频、Remotion/HyperFrames下载安装、Stage6转换代码和完整业务E2E不属于Stage5完成前置；optional缺失/decline/defer不阻断base。Stage5完成后Stage6先判断能否直接复用receipt（可直用则优先零代码），完整业务E2E另行授权，不称为Stage7。

当时的 R00 任务已正式推广并消费；其 `current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE` 只表示 R00 收口后的历史交接状态。R01 已由 2026-08-22 单独授权并执行，当前结果由本文末的 R01 镜像统一定义。

## 12. [ORIGINAL R01 / FORMALLY CLOSED / PRESERVED] 当前 Stage 5 R01 受控执行合同证据结果

Stage 5 仍为 `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`，不是整体 PASS。产品目标回读和范围扩张审计均为 `PASS`：WorkBuddy 仍是唯一运行中的 Agent/用户入口，Shell 仍只负责六模块；固定 CLI 只作为唯一 Skill 内部桥梁，不构成任意 CLI 旁路。R01 最终结果为 `BLOCKED_EXTERNAL_CONTRACT`，独立审查已批准并正式 fast-forward；因此严格依赖链在 R01 停止，R02-R08 为 `NOT_STARTED / NOT_AUTHORIZED_BY_CHAIN`。

```text
task_id: V2-S5-R01-WORKBUDDY-EXECUTION-CONTRACT-EVIDENCE1
task_kind: CONTROLLED_CLIENT_EVIDENCE + DOCS_ONLY_CLOSEOUT / ZERO_PRODUCT_STATE_CHANGE
user_authorization: 2026-08-22 / Stage5继续执行、每个子任务独立审核、边界审计和产品目标回读
base_commit: d0a055689e9fc928a31edb24f3740e9408e123ef
base_tree: 50197a1eb103ffad42ac3e2952dcd3f9761a9512
base_parent: 2207c9083ceabcf6539936e47b0935a4eaa77c46
tracked_files_at_base: 40
official_sources: 134432 WorkBuddy Skills; 134391 local AI workbench task bar; 134324 update notes; 134516 CodeBuddy PRODUCT_MISMATCH_NOT_CONTRACT_PROOF
workbuddy_version_observed: 5.3.14
baseline_installed_skills: 2 / agent-browser; find-skills
temporary_probe_zip: r01-controlled-probe.zip / sha256 C55C90B7E86E9399F04EF13B8D78DF9228A8D72F7149B5B2A11B4362320F102D / DELETED_AFTER_REVIEW
temporary_probe_skill_sha256: D1BE59EF9221BA739482555744385244C86B771F5604DB738F5E0952CCC1E1E1 / HASH_ONLY_SOURCE_DELETED_AFTER_REVIEW
temporary_probe_script_sha256: 52B1F6283FF376F99DE49AE87EF24781042DC12F679AAAF7F976F58F19307064 / HASH_ONLY_SOURCE_DELETED_AFTER_REVIEW
client_safety_scan: NOT_SKIPPED / AUTO_INSTALL_ACCEPTED / installed count 3 / exact probe identity
controlled_task_model: HY3 / NEVER_AUTO
native_bundled_script_invocation_event: ABSENT / client exposed Bash/PowerShell only
coordinator_stop: BEFORE_ANY_SHELL_OR_TERMINAL_EXECUTION
probe_script_execution: NOT_RUN / stdout_stderr_exit_cwd_timeout_evidence=NONE
nonzero_case: NOT_RUN
timeout_case: NOT_RUN
r01_result: BLOCKED_EXTERNAL_CONTRACT / native event is mandatory and cannot be replaced by model text, marker, JSON, or inference
r01_result_review: APPROVE / P0=0 / P1=0 / P2=0 / FORMALLY_FAST_FORWARDED_TO_ORIGIN_CODEX_WORKBUDDY_SHELL_V2 / COMMIT=9eefe8600d9bed0c8ea6024880e4b2d2ef4e3bfc
r02_r08_status: NOT_STARTED / NOT_AUTHORIZED_BY_CHAIN
temporary_skill_cleanup: COMPLETE / USER_UNINSTALLED_TEMPORARY_SKILL / WORKBUDDY_INSTALLED_SKILLS_2 / TASK_HISTORY_RETAINED / BASELINE_SKILLS_2_UNTOUCHED
baseline_skill_cleanup: NOT_TOUCHED / TWO_RETAINED_SKILLS
temporary_probe_cleanup: COMPLETE / EXACT_ISOLATED_WORKTREE_FOLDER_AND_ZIP_DELETED / GIT_STATUS_CLEAN
candidate_test: NOT_RUN_DOCS_ONLY
```

官方资料只证明脚本/工作流打包、上传、选择和自动调用的公开形态，未证明精确 native command/cwd/env/stdin/stdout/stderr/exit/timeout 合同。R01 的三个 case 不得继续运行；本结果不创建或推广 Package、Registration、Installer、最终 Skill、Stage4 spawn、Provider、媒体或 Stage6。

## 13. Current Stage 5 R01 Sandbox Refresh1 governance mirror (2026-08-22)

This is an independent refresh of the original R01 closeout; the original record remains preserved. Product-goal recheck and anti-expansion audit are `PASS`: WorkBuddy remains the sole Agent/user entry, and the fixed CLI remains eligible only as the internal bridge of that one Skill. Official 134420 establishes only that enterprise Skill scripts execute in the client sandbox. Controlled WorkBuddy observation records PowerShell as an `ELIGIBLE_CANDIDATE_SURFACE`, not an official exact execution contract; 134432 establishes Skill script/workflow packaging and upload/invocation shape; 134516 is CodeBuddy `PRODUCT_MISMATCH_NOT_CONTRACT_PROOF`. The unresolved contract is Skill-root cwd/bundled-relative resource resolution plus exact stdin/stdout/stderr/final-exit/timeout semantics.

```text
refresh1_task: V2-S5-R01-WORKBUDDY-SANDBOX-REFRESH1 / RESULT_CANDIDATE / PENDING_INDEPENDENT_DOCS_REVIEW
formal_base: 932bcabc5baf90d0190101b1039e4ccf087b2b08 / tree 2ed2cd0e67dd8628b7f0b1acf84df0a7d8b0d0fd / tracked 40
workbuddy: 5.3.14 / baseline=agent-browser,find-skills / HY3_ONLY / NEVER_AUTO
source_root: ISOLATED_D_DRIVE_TEMP_ROOT / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / RETAINED_PENDING_USER_CLEANUP
hashes: SKILL=A369E89912B51C1627C972A7DE8F82111E55E2909622CB2E0E3276B45331FFF9 / SCRIPT=8A1D38A65945CC99C4B7F8EE95FDF4FF744D105303BC9904E5915E630DF58359 / ZIP=2284E6D6FE8FFD38689A357DD0A6653CEB23B923F0C531BF9EAC376178E9A28A
install_and_identity: SAFETY_SCAN_NOT_SKIPPED / NO_NON_HIGH_RISK_AUTO_INSTALL_SELECTED / INSTALLED_COUNT_3 / client_id=workbuddy-skill-1787379691395 / SKILL_MD_NO_METADATA_NAME / BODY_FIRST_LINE_MATCHED_PROBE
native_read: SKILL_MD_AND_scripts\\r01_contract_probe.py_READ / PHYSICAL_INSTALL_PATH_EXPOSED_CONTRACT_DEVIATION_SENSITIVE_MINIMIZATION_FAILURE / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
execution: SESSION_WORKSPACE_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / frozen_relative=.\\scripts\\r01_contract_probe.py / NO_CD_NO_ABSOLUTE_PATH_NO_GUESSING_NO_COMMAND_MUTATION / SKILL_ROOT_CWD_NOT_EXPOSED / BUNDLE_RELATIVE_NOT_EXPOSED / POWERSHELL_NOT_STARTED
result: BLOCKED_EXTERNAL_CONTRACT / MISSING_SKILL_ROOT_CWD_AND_BUNDLE_RELATIVE_RESOLUTION / NOT_BECAUSE_POWERSHELL_IS_NON_NATIVE
evidence: USER_CANCELLED / NO_SCRIPT_STDOUT_STDERR_FINAL_EXIT_CWD_CLASSIFICATION_TIMEOUT / nonzero=NOT_RUN / timeout=NOT_RUN
review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_REVIEWER
reviewer_independent_observation: WORKBUDDY_5.3.14 / HY3 / USER_CANCELLED / NO_SUCCESS_STDOUT_STDERR_EXIT_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
chain: R02-R08_NOT_STARTED_NOT_AUTHORIZED_BY_CHAIN / Stage5=IN_PROGRESS_ENTRY_CODE_COMPLETE_REAL_INTEGRATION_INCOMPLETE
cleanup: TEMP_SKILL_STILL_INSTALLED / USER_ACTION_REQUIRED / TASK_HISTORY_RETAINED / BASELINE_SKILLS_UNTOUCHED
computer_use_transparency: LOW_IMPACT_OPERATIONAL_ANOMALY / EXPLORER_MISTAKEN_FOR_FILE_PICKER / ALT+N_MAY_OPEN_TAB_OR_WINDOW / NO_PATH_INPUT_NO_FILE_SELECTION_NO_WRITE_DELETE / STOPPED_AND_RECOVERED
```

The refresh1 candidate does not authorize or create Package, Registration, Installer, final Skill, Stage 4 spawn, Provider, media, Stage 6, or production flow. It also does not elevate Stage 5 to `PASS_ACCEPTED`; user confirmation is still required to uninstall the temporary Skill.
