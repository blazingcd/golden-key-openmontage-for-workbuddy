# WorkBuddy Shell V2 验收矩阵

状态：`STAGE_3_PASS_ACCEPTED / STAGE_4_PLANNING_PASS_ACCEPTED / STAGE_4_IMPLEMENTATION_BUILDER_AUTHORIZED / SIX_MODULE_MVP`

## 1. 状态必须独立报告

| 状态 | 含义 | 不能由什么代替 |
|---|---|---|
| `SHELL_INSTALLED` | Shell和Skill进入受支持安装位置 | ZIP构建成功 |
| `OBJECT_IDENTITY_VERIFIED` | Shell/OpenMontage 执行包/Release/Manifest/Lock/SHA/安装实例一致 | 文件名、目录名、最新时间 |
| `FINAL_PACKAGE_MATERIALIZED` | 最终Release、SHA sidecar和生产PackageRoot在任务清理后仍持久存在 | 一次临时Package组装成功 |
| `PRODUCTION_PACKAGE_REGISTERED` | 生产DataRoot有活动Registration，且新进程Locator返回同一Package和完整工具链 | task-only DataRoot中的临时登记 |
| `RUNTIME_BOUND` | 实际PackageRoot、完整必带工具链、cwd、DataRoot以及当前已选可选能力（如有）的来源/路径被锁定 | 单个Python包存在、系统PATH命中或doctor文字说明 |
| `REAL_WORKBUDDY` | 真实WorkBuddy客户端在新会话执行 | Codex、CLI、fixture或历史会话 |
| `PROCESS_CORRECT` | WorkBuddy依据已验证Package执行原生Pipeline/Skill/Artifact/Reviewer/Checkpoint合同 | 产生项目目录或MP4 |
| `CAPABILITY_REAL` | 真实工具或能力执行 | mock、静态registry、旧产物 |
| `LOCAL_RENDER_E2E` | 本次运行产生有效本地成片 | 旧成片、单个中间媒体 |
| `BUSINESS_EFFECTIVE` | 用户实际观看并认可业务结果 | ffprobe或自动评分 |
| `REAL_E2E` | 当前定义的完整本地产品链闭环 | 任一局部PASS |
| `STRICT_MANIFEST_CONFORMANCE` | 原生合同严格一致 | 业务效果认可 |
| `PROVIDER_E2E` | 经授权真实调用指定Provider | Key存在、静态配置、费用估算 |
| `PUBLISH_E2E` | 外部发布能力 | 当前项目不适用，记`NOT_APPLICABLE` |

## 2. 通用裁决

- `BLOCKED`：只用于执行前依赖、精确输入或授权未满足；
- `PASS`：精确对象、规定动作、证据和最终退出全部满足；
- `FAIL`：在正确对象和有效执行中证明合同或结果不满足；
- `INCOMPLETE`：执行一旦开始后对象不一致、命令无最终退出、证据缺失、环境干扰或任务被用户停止；
- `NOT_TESTED`：没有执行；
- `NOT_APPLICABLE`：功能不在当前范围；
- `PARTIAL`：只用于明确允许的非二元治理维度，不得替代关键Gate的PASS。

## 3. 六模块 MVP 验收

| 模块 | 最小 PASS 条件 | 越界失败条件 |
|---|---|---|
| 安装与生命周期 | 锁定对象可安装/修复/升级/回滚/卸载，所有权正确且用户数据保留 | 运行生产、覆盖外来对象、静默下载/降级或删除用户数据 |
| OpenMontage 执行包登记与定位 | 唯一活动Package Registration同时锁定Package、可用私有Python环境及核心依赖、FFmpeg/ffprobe、Node/npm/npx的身份、hash、版本、能力和规范化路径 | 只登记Python；依赖系统Python/FFmpeg/Node；扫盘猜测对象、身份漂移仍继续、修改执行包或执行生产；登记/实现SaaS Core |
| Runtime按需准备 | 有界探测Remotion和HyperFrames并逐项报告`PRESENT/MISSING/INCOMPATIBLE`；对缺失/不兼容项零下载展示批准OpenMontage能力定义中的来源、版本、大小、许可证和目标；用户逐能力同意后只集成批准项并验证；拒绝/暂缓返回`SKIPPED/NOT_INTEGRATED`，其他已有/基础能力继续可用 | 扫盘、枚举系统软件或猜目录；把Remotion/HyperFrames当必带Runtime；发现/下载/替换Python/FFmpeg/Node；Shell选择渲染器；未授权、全局或全部自动安装；自动海外回退；修改PATH/注册表；把能力缺失或用户拒绝当Package/项目失败 |
| 会话Launcher | 一次WorkBuddy拥有的会话先调用`locate_active_package(data_root)`；验证release-specific不可变`PackageToolDefinitionV1`及Manifest/Lock覆盖；仅在定义声明时接收完整approved capability definition与未改写original Stage3 fact，并按managed/explicit/PATH来源语义独立重验实际资产；`shell=False`恰好一次启动固定工具，并返回绑定全部身份、真实退出、结果指针、错误、泄密与残留事实的递归不可改写receipt | 改写literal `user_message`；读取未验证Guide；硬编码或选择Provider/Runtime；查询registry routing；绕过source-aware就绪检查；启动第二Agent；接受任意Shell/命令/调用者argv；安装Runtime；多进程调度/队列/服务/数据库；自动重试/重放；媒体生产；创建Artifact或推进Checkpoint |
| WorkBuddy入口 | 真实新会话显式命中唯一入口，literal用户消息不变，并绑定活动执行包与Runtime | 多套生产入口；全局截获；第二聊天Agent；技术控制词进入用户消息或Shell作生产选择 |
| 状态与结果转交 | 直接转交Runtime计划/准备事实与Launcher回执并零代码退出，或只做一次有消费者证明的确定性格式转换；事实可追溯且不改写WorkBuddy语义 | 无格式缺口仍造模块；安装Runtime；建立数据库/轮询/流式平台或Stage/FSM；解释Artifact；自动重试或伪造成功 |

### 3.1 阶段3至阶段6缩减Gate

阶段编号是建设与验收顺序`3 -> 4 -> 5 -> 6`，不是最终用户运行顺序。阶段4可依据阶段2必带工具链事实启动基础固定工具；阶段3独立有界探测Remotion和HyperFrames，能力存在则复用，缺失/不兼容则询问用户是否集成。OpenMontage只从实际可用能力中决定生产选择。

阶段3结果闭集为`DETECTION_REPORT`、`CONSENT_REQUIRED`、`INTEGRATED`、`SKIPPED`和`BLOCKED`。每项能力事实只取`PRESENT/MISSING/INCOMPATIBLE/NOT_INTEGRATED`。缺失、拒绝或暂缓不阻塞Package、项目、最终交付或其他能力；只有无效定义、越界目标或已授权集成失败才可`BLOCKED`。

Python核心依赖、FFmpeg/ffprobe、Node/npm/npx都属于Package必带工具链。阶段2缺少任何一项时是`FAIL`，阶段3不得以宿主PATH、下载或受管目录补救。Node虽然官方Quick Start最低为18+，但当前HyperFrames要求22+，Package锁定值必须满足最高当前要求。

阶段4 `PASS`要求在启动时消费阶段2必带工具链就绪事实，并只在固定工具定义的`required_local_capabilities`声明要求时消费同一opaque capability+definition的通用本地证据。定义未声明时不得硬编码要求Remotion/HyperFrames；Provider API key、外部服务配置或动态registry状态不得被误作Stage3证据。缺少定义所需事实必须preflight阻断且spawn 0；任何第二Agent、Provider/Runtime选择、registry routing、自动重试、队列、调度、常驻服务、多Agent或Package业务内部导入均为越界`FAIL`。

阶段5是用户实际运行起点。`PASS`要求唯一Skill在真实WorkBuddy新会话命中，按已冻结映射消费阶段3五种结果，literal `user_message`不变，授权与`executor_controls`分离，并验证用户同意后的同任务继续；若不能自动继续，必须验证固定“继续刚才的任务”提示。入口格式未确认时应记`BLOCKED`，不得同时实现CLI/MCP/多个Skill兜底。

阶段6先验证WorkBuddy能否直接消费Runtime计划/准备事实和Launcher回执：能则记录`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`且生产代码变化为0；不能则必须有精确字段差异和真实消费者证据，只允许一次确定性转换。非零退出、超时、缺少结果指针和残留进程必须保持原事实；阶段6不得安装、解释或重试。

### 3.2 阶段3重新规划Gate

旧Package绑定能力元数据、Registration绑定及零能力零代码模型全部`SUPERSEDED`。Stage 3实现`a3f8959682d296301dc573c2835f8c705a52e8b2`和closeout `7c15aae4e77c579309312b21c79076f930970214`已正式推广，现行状态为`PASS_ACCEPTED`。`FINAL_PACKAGE_MATERIALIZED`和`PRODUCTION_PACKAGE_REGISTERED`仍是后续最终交付/Installer要求，最迟在Stage5真实WorkBuddy生产验收前完成；不是Stage3或Stage4编码/规划前置。

新阶段3最多一个公共入口`prepare_optional_capabilities(...)`、一个新生产模块、一个导出编辑和一个直接测试文件；不得新增通用Runtime框架。直接验收必须覆盖：

1. 同次有界探测Remotion和HyperFrames，并分别产生`PRESENT/MISSING/INCOMPATIBLE`事实；
2. 探测只使用受管DataRoot、明确登记/配置候选路径和正常命令解析，盘符/软件清单/全局npm枚举为零；
3. 已存在且兼容的能力复用并报告，零下载/零写入；
4. 缺失/不兼容项只返回绑定定义、版本、来源、hash、大小、许可证、目标和`plan_sha256`的计划，零下载；
5. `decline/defer`返回`SKIPPED/NOT_INTEGRATED`，不是失败；
6. 定义、计划或探测事实变化使旧批准失效；
7. 只使用批准大陆来源，禁止自动海外回退和全局安装；
8. 外来目标保留，hash/大小/许可/来源/探针失败全部回滚并清理；
9. 未批准能力、必带Python/FFmpeg/Node、Package和用户消息零修改；
10. Shell选择渲染器、自动重放业务请求和生产执行均为零。

证据必须分层：阶段3单元/负面测试、本地真实准备、大陆镜像网络验证、阶段5真实WorkBuddy消费和视频E2E分别报告；前一层PASS不能替代后一层，阶段5证据不得反向作为阶段3实现前置。

### 3.3 阶段3交付闭集和不断档验收

阶段3仓库交付只有一个公共入口、五种结果、一套数据驱动的两能力探测/集成事务和阶段4可验证的能力证据。产品实现文件固定为`runtime_prepare.py`、`__init__.py`导出编辑和`test_runtime_prepare.py`，并已同步更新`test_repository_hygiene.py`和`.github/workflows/ci.yml`两项验收基础设施；正式树tracked精确35。

最小交付成果必须同时满足：

1. `prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`是唯一公共入口；
2. 能力定义和用户决定拒绝未知/缺失字段，调用方不能注入任意URL、任意命令或安装目标；
3. 五种结果及WorkBuddy动作保持闭集，能力证据不能跨能力或定义复用；
4. 只读阶段不创建受管目录、缓存、准备锁、staging或临时文件；
5. 缺失/不兼容计划规范排序并绑定能力、定义、精确资产、来源、许可、目标和总量；
6. 仅有效批准后的第二次调用可以产生网络和受管写入，且必须先重新执行只读Gate；
7. 只使用批准OpenMontage能力定义中的大陆来源和阶段2必带Node/npm/npx，无自动海外回退；
8. 同卷staging中的所有对象通过来源、大小、SHA-256、许可和能力探针后才可发布；失败清理任务临时对象并保留外来对象；
9. 最终探针从发布目标重新取证，`PRESENT`或`INTEGRATED`证据绑定同一能力和定义；
10. PackageRoot、Registration、Activation、Python、FFmpeg、Node、未批准能力和literal用户消息全程零修改；
11. 阶段4可以只凭阶段3能力证据判断该可选能力是否可执行，不需要理解阶段3集成内部；
12. 阶段5只按五结果映射展示、询问或继续，阶段6可原样转交，不要求补建平行状态服务。

阶段3直接测试至少闭合以下20类反例和成功路径，并分别断言结果、网络次数、最终文件树、外来对象、mtime/hash和任务临时残留：

1. 两能力均存在；2. 一项存在一项缺失；3. 不兼容版本；4. 显式登记/配置候选；5. 正常命令候选；6. 禁止盘符扫描；7. 禁止系统软件/全局npm枚举；8. 缺失只返回计划；9. 拒绝；10. 暂缓；11. 授权缺失；12. 旧定义或旧plan授权；13. 非大陆来源；14. 大陆来源失败且海外回退为零；15. 来源/大小/hash/许可不完整；16. 空间/权限/网络失败；17. 外来目标；18. 重复或并发调用无半成品；19. 失败清理且必带工具链零修改；20. 能力证据不能跨能力或定义消费。

阶段3直接测试和完整仓库测试都必须有未截断输出和最终退出0。真实大陆镜像下载证据、真实WorkBuddy继续、阶段4真实执行和视频E2E仍是后续独立证据层，不能塞入阶段3直接测试或用mock冒充。

### 3.4 Stage 3完成证据与Stage 4已接受规划

Stage 3已接受证据为：direct 55 passed、repository hygiene 10 passed、CI-equivalent full 199 passed，全部最终退出0且无skip；独立Reviewer只读核验精确对象、代码、测试定义和Builder原始输出，没有重跑测试。该证据不证明真实第三方/大陆镜像下载、生产DataRoot集成、WorkBuddy、Stage4、Provider或媒体/视频E2E，也不需要这些后续证据来维持Stage3 `PASS_ACCEPTED`。

Stage4规划已经独立审查、普通fast-forward并记为`PASS_ACCEPTED`。已接受的release-specific immutable `PackageToolDefinitionV1`闭合当前Locator不提供固定工具入口身份的问题，并冻结`launch_session_tool(...)`及`LauncherReceiptV1`精确字段。用户已授权`V2-S4-IMPLEMENTATION-BUILDER1`执行既定仓库实现与测试；最终Package物化和真实WorkBuddy都不是编码前置，具体Release缺工具定义实例时，真实调用必须preflight阻断。

规划合同已经`V2-S4-PLAN-REVIEW1`独立零写APPROVE、规划closeout审查并普通fast-forward，现已生效。live task为`V2-S4-IMPLEMENTATION-BUILDER1`，必须从本权威同步推广后的最新formal精确SHA/tree接管；授权只覆盖既定五路径和35到37的固定树迁移，不授权真实生产Launcher运行、Stage5、Stage6或最终Package。

本次secret nondisclosure合同澄清不是实现PASS证据，也不自动修复现有code candidate。只有`V2-S4-SECRET-NONDISCLOSURE-CONTRACT-CLARIFICATION-REVIEW1`独立`APPROVE / P0=0 / P1=0 / P2=0`且澄清commit普通fast-forward为formal head后，下列secret验收语义才成为implementation authority；此前code candidate不得推广，之后须回原Implementation Builder修订并重新独立验收。

### 3.5 Stage 4规划完成合同与未来实现验收

已接受规划已把两个已知缺口闭合为可实现合同；仓库实现授权只授予`V2-S4-IMPLEMENTATION-BUILDER1`，并不授权真实生产Launcher运行。固定工具身份不等于编造上游入口：`PackageToolDefinitionV1`冻结authority、closed schema、release绑定和缺实例fail-closed规则，具体Release实例由批准Golden Key Package定义/最终交付Installer owner提供。

未来实现的Gate按以下顺序裁决：

1. **输入PASS**：唯一入口精确为`launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`；inputs closed，user message字节不变，返回递归冻结。所有非空Provider value在入口先保守标记为secret source，唯一授权sink为child环境；pre-cancel在Locator 0/spawn 0前完成动态hints保护。
2. **身份PASS**：同次Locator的Registration/Manifest/Lock身份由preflight外部绑定并进入receipt；定义只绑定稳定Release/commit、定义文件、工具、解释器、argv/env/local requirements，不含Registration/Manifest/Lock hash。定义文件本身和工具文件均在当前Manifest与Lock中唯一覆盖，传入定义字节与Package内文件相同，authority owner及工具relative path/hash/size/owner一致；定义、工具和解释器每个路径组件无link/reparse且在PackageRoot内；spawn前复核不漂移。真实fixture必须完成含定义+工具Package的`register -> locate -> validate`往返。
3. **opaque capability PASS**：代码中无Provider、renderer或runtime catalog；环境变量名只来自定义allowlist，Provider-secret source只进入子进程环境；只有定义声明时才接受完整approved capability definition、其canonical SHA、未改写original Stage3 fact及其canonical SHA。Stage4独立验证closed definition/fact hash，并按fact source重验：managed必须是DataRoot受管安全root、全部定义assets及closed-tree；explicit必须是定义候选安全绝对root、全部定义assets，允许且保留额外外来文件；PATH必须`runtime_root == verified_entrypoint`且为安全绝对regular command，只核对entrypoint asset。未知source fail closed；`INTEGRATED`必须managed并保留plan identity。原始fact仅作审计，version_evidence不受信。Provider缺失不触发Stage3。
4. **进程PASS**：`cwd`为verified PackageRoot，环境为固定最小基线加allowlisted provider环境，stdin为单一closed JSON envelope且Provider value为0，`shell=False`，spawn恰好一次，retry恒为0；timeout/cancel终止自有进程树并检测残留。不可信stdout/stderr对每个完整secret UTF-8 bytes做跨chunk检测，任一命中都无常量例外地裁决`SECRET_DISCLOSURE_DETECTED`。
5. **回执PASS**：任何输入/preflight/spawn/运行结果都返回`golden-key-workbuddy-launcher-receipt-v1`全部固定字段，outcome只取9值、reason只取23值。固定secret-independent协议常量及可证明来自独立Package/definition authority的身份与secret偶然相同不误报；caller/child动态域在freeze前做provenance-aware non-propagation检查，受污染值只用现有类型允许的`None`、空tuple、固定安全文本或安全流摘要替换，不删除字段、不向`tuple[str]`插入`None`。任何Provider value复制/派生进动态receipt、日志或异常为0。
6. **结果PASS**：精确优先级仍为11级：invalid cancel/input、pre-cancel、preflight、spawn fail、residual、secret disclosure、timeout/cancel首次monotonic观察、nonzero、invalid output/result、child FAILED、success。入口已取消且secret等于session/request时仍为`CANCELLED/CANCELLED_BEFORE_SPAWN`、Locator 0、spawn 0，相关hints为`None`；exit 0+child `FAILED`为`CHILD_REPORTED_FAILURE/CHILD_REPORTED_FAILURE`；只有exit 0、单个有效`SUCCEEDED` envelope、受控result root内hash/size匹配指针、无泄密且无残留可为`EXITED_SUCCESS`。

以下任一项为实现`FAIL`：从Guide/registry/目录/调用者推断工具；修改Stage2 Registration；任意shell/argv/env注入；硬编码Remotion/HyperFrames或Provider；把Provider配置缺失当Stage3证据缺失；Provider value被复制/派生进argv、canonical stdin、动态receipt、log、异常或回传原文；对child输出遗漏单chunk/跨chunk完整secret；把固定协议常量偶然碰撞误判到无法返回合法schema；多次spawn/retry；工具/解释器替换后继续；结果路径逃逸或reparse；残留未报告；第二Agent、服务、数据库、调度、媒体、Artifact或Checkpoint逻辑存在。

以下为`PRELAUNCH_BLOCKED`而非实现失败：没有活动Registration；Release尚未提供具体`PackageToolDefinitionV1`实例；定义文件/工具未被当前Manifest与Lock正确覆盖，或定义的Release/commit与Locator不同；定义声明的本地能力证据缺失/漂移；环境变量名不在allowlist。最终Package物化与真实WorkBuddy都不是规划或编码前置，但是真实生产启动必须具备其当前Release实例。

直接测试最低矩阵精确覆盖：Registration/Package/tool/interpreter全部漂移；定义closed schema/self-hash/authority/Manifest+Lock覆盖及定义不含Registration/Manifest/Lock hash；含定义+工具的真实Stage2 fixture完成`register -> locate -> validate`；路径逃逸、ADS、alias、symlink/junction/reparse；命令/argv/env注入；user message不变与controls分离；本地能力声明/不声明、完整定义+原始fact、摘要重包装拒绝、version_evidence不受信；managed/explicit/PATH三种合法PRESENT；managed额外文件/目录拒绝；explicit定义资产漂移拒绝且额外文件零改写；PATH命令替换、非regular或不安全拒绝；合法managed INTEGRATED保留plan identity，非managed INTEGRATED与未知source拒绝；动态Provider名不硬编码、任意env名拒绝、Provider缺失不错误要求Stage3；Python-script/direct-executable两种成功；总是返回receipt、invalid input nullable字段、pre-cancel spawn0、spawn失败；优先级全部竞争分支；child FAILED；spawn一次/no retry；非零/timeout/cancel/残留；输出上限；结果envelope和pointer全部失败分支；递归不可修改receipt。secret专项必须另覆盖：value=`-`/`I`只撞固定token时schema可表示；value等于pre-cancel session/request时取消结果不变且hints安全；value传播进user_message/session/request/result root/pointer/error时阻断并安全替换；stdout/stderr单chunk与跨chunk完整bytes检测；JSON escape后动态重建检测；独立authority name/identity偶撞不误报；`None`/空tuple/固定文本/安全流摘要不破坏类型；argv/stdin/dynamic receipt/log/exception最终来源传播为0。

未来实现路径只允许：

```text
golden_key_openmontage_workbuddy/session_launcher.py
golden_key_openmontage_workbuddy/__init__.py
tests/workbuddy/test_session_launcher.py
tests/workbuddy/test_repository_hygiene.py
.github/workflows/ci.yml
```

新增一个生产模块和一个直接测试后，固定tracked树从35精确变为37。hygiene必须显式更新37文件等值、4个Python源文件和API闭集；CI必须在现有唯一pytest命令中显式加入Stage4直接测试；不得用glob或动态计数放宽。`package_registration.py`、`runtime_prepare.py`、`pyproject.toml`及任何第6路径默认禁止。

Builder证据必须分别给出Stage4 direct、repository hygiene、full suite的未截断输出和最终exit 0，以及base/candidate/tree/5路径/37 tracked/clean/untracked0/stash0。Reviewer独立零写比较精确base..candidate，除了绿测还必须核对公共合同最小性、fail-closed反例、secret边界和无Scope扩张；`REQUEST_CHANGES`只回原Builder。普通fast-forward正式推广后也不得自动启动Stage5/6。

Stage5的消费者合同只需提供literal message、closed controls、approved PackageToolDefinition、经单独授权的Provider环境，并在定义声明时原样传递完整approved capability definition与未改写original Stage3 fact；不得重包装摘要。Stage4按原始managed/explicit/PATH source语义独立验证实际资产；Stage6优先直接使用同一receipt，格式无缺口时必须`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`且生产代码0。真实WorkBuddy、Provider和媒体E2E仍分别验收，不得用Stage4单元测试冒充。

## 4. Gate A：对象与环境

入口：阶段7安装候选通过离线测试并锁定安装对象。

要求：

- literal用户消息不含PackageRoot、Python或`.venv`；
- 显式Skill正确命中；
- Locator只读取登记对象，不扫盘；
- Launcher绑定精确PackageRoot、阶段2登记的完整必带工具链、cwd和DataRoot；若本次执行需要已选可选能力，还绑定对应阶段3就绪事实；
- 正确环境中的最小WorkBuddy/Package工具preflight成功；
- 实际解释器和执行包身份进入会话回执；
- Provider调用0、费用0；
- 新增进程和窗口残留为0；临时、测试、重复或旧版本Skill残留为0；正式受支持且身份锁定的目标Skill必须保留，不得误删。

Gate A不证明Pipeline、成片或业务效果。

## 5. Gate B：原生生产入口

入口：Gate A `PASS_ACCEPTED`。

要求：

- WorkBuddy读取活动执行包自己的Guide；
- WorkBuddy依据Package Guide自主选择Pipeline；
- Shell没有推荐、覆盖或预填Pipeline；
- 产生WorkBuddy依据Package合同创建的原生第一阶段Artifact；
- 产生原生Checkpoint或按Manifest进入相应Gate；
- `user_message`与`executor_controls`证据分离。

Gate B不证明最终渲染或业务效果。

## 6. Gate C：本地短成片

入口：Gate B `PASS_ACCEPTED`。

要求：

- 使用无rotation争议的短素材；
- 使用新WorkBuddy会话和新项目；
- WorkBuddy依据Package合同调用原生工具真实执行；
- Artifact、Checkpoint、Final Review和结果指针一致；
- Tool正常返回；
- MP4有效；
- Provider调用0、费用0；
- 新增浏览器和进程残留为0；临时、测试、重复或旧版本Skill残留为0；正式受支持且身份锁定的目标Skill必须保留。

Gate C不证明门店竖屏问题已修复。

## 7. Gate D：OpenMontage修复后的门店业务验收

入口：

- Gate C `PASS_ACCEPTED`；
- OpenMontage发布项目提供包含方向闭环的新不可变执行包Release、ZIP/SHA/Lock和独立证据；
- Shell通过原子活动执行包指针登记并切换到该新Package Registration。

要求：

- 普通用户消息不包含PackageRoot、Python、9:16或技术补丁；
- 自动识别素材实际显示方向；
- 不使用Shell transpose、临时预转码Skill或项目级救火脚本；
- 输出正确9:16成片；
- 用户实际观看并确认业务效果；
- `PROCESS_CORRECT`、`LOCAL_RENDER_E2E`和`BUSINESS_EFFECTIVE`分别报告；
- 默认Provider调用=`0`、费用=`0`；
- 若未来确需Provider，必须引用独立、显式的Provider授权和费用授权，并把调用、实际费用、对象和退出状态单独报告；该调用不得使Gate D自动获得`PROVIDER_E2E`，也不得替代Gate E。

## 8. Gate E：可选Provider扩展

Gate E不是Shell V2本地版完成前置，且与Gate D保持独立裁决。

只有用户单独授权后才验证：

- Provider配置和身份；
- 费用披露与预算；
- 网络和真实生成调用；
- Provider返回资产进入WorkBuddy依据Package合同维护的原生Artifact链；
- 完整成片及费用对账。

Key存在、`present_unverified`、静态registry和Provider菜单均不能证明`PROVIDER_E2E`。

## 9. 真实WorkBuddy测试卡最低身份

首次真实V2验证前必须锁定：

```text
shell_commit
shell_package_version
openmontage_release
openmontage_commit
package_manifest_sha256
package_lock_sha256
install_root
data_root
package_root
package_python
package_ffmpeg
package_ffprobe
package_node
package_npm
package_npx
selected_optional_capability
skill_hashes
literal_user_message
executor_controls
workbuddy_version
model
global_skill_interference
new_session_id
new_project_id
provider_authorization
cost_authorization
```

任何字段缺失时，真实验收不得开始。
