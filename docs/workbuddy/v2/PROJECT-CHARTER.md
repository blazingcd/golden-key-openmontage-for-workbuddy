# WorkBuddy Shell V2 项目章程

状态：`STAGE_3_PASS_ACCEPTED / STAGE_4_PLANNING_ELIGIBLE_AFTER_DOCS_PROMOTION / SIX_MODULE_MVP`

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
| 会话Launcher | 对一次WorkBuddy拥有的会话先调用`locate_active_package(data_root)`重验活动Package和完整必带工具链；只在明确执行某可选能力时核对同一capability+definition的阶段3`PRESENT`或`INTEGRATED`证据；随后调用一个固定Package工具入口并返回一次不可改写真实进程回执 | 输入：DataRoot、分离的literal `user_message`与`executor_controls`、固定工具请求，以及可选能力调用时的对应阶段3证据；输出：绑定Registration和工具身份的一次真实退出、结果指针及残留事实 | 改写用户原话；读取未验证Package Guide；启动第二Agent；解析意图；接受任意Shell/命令；安装Runtime；选择渲染器；自动重试/重放；队列/服务/数据库/多进程调度；媒体生产；创建Artifact或推进Checkpoint |
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
- 阶段4基础固定工具调用继续接受阶段2必带工具链事实；执行Remotion或HyperFrames前只需阶段3对该能力给出的`PRESENT`或`INTEGRATED`证据。缺少能力时OpenMontage可以使用其他已有/基础能力；阶段4不得自行安装。
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

该证据不是布尔值，不能跨能力或跨定义复用。阶段4必须重新比对能力、入口和版本；缺失或不匹配时不得自行安装，OpenMontage可选择其他已有/基础能力。

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

### 4.9 Stage 4规划接管边界与已知缺口

本九文档同步经审阅并正式推广后，Stage 4只获得`planning_eligible`，实现授权仍为`NOT_GRANTED`，下一授权任务仍为`NONE`。规划目标仅是冻结一次WorkBuddy拥有会话中的固定Package工具调用和不可改写真实进程回执；不得创建Stage5/6 Task Packet或预建Launcher实现。

当前Stage 2 `locate_active_package(data_root)`已权威返回并重验Registration SHA、PackageRoot、Python/FFmpeg/ffprobe/Node/npm/npx、Guide、Manifest和Lock身份，但没有返回固定Package工具入口身份。现有权威也没有唯一确定Stage4公共入口签名及回执字段。后续单独授权的Stage4规划必须精确闭合：

1. 由批准OpenMontage Package定义及后续最终交付/Installer所有者提供可验证的固定工具身份来源、Package内相对路径、hash/owner和固定argv形状；不得重开Stage2，也不得把最终Package物化变成规划前置。
2. 由Stage4规划所有者冻结唯一公共入口，以及至少绑定Registration、Package/tool identity、进程启动事实、真实退出码、结果指针、错误和残留事实的不可改写回执精确字段。
3. 基础固定工具调用只依赖阶段2必带工具链；可选能力证据仅在本次明确执行该能力时适用，且必须匹配同一capability+definition。

真实WorkBuddy新会话、唯一入口、literal `user_message`不变、逐能力询问和同任务继续归Stage5实现/验收。Stage6只在Stage4回执和Stage5真实消费者存在后判断；直接消费必须走`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`且生产代码变化为0。

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
