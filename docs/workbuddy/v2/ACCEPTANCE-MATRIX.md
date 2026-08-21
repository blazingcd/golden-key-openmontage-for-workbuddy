# WorkBuddy Shell V2 验收矩阵

状态：`STAGE_3_PASS_ACCEPTED / STAGE_4_PLANNING_PASS_ACCEPTED / STAGE_4_IMPLEMENTATION_PASS_ACCEPTED / STAGE_5_PLANNING_PASS_ACCEPTED_CANDIDATE / STAGE_5_IMPLEMENTATION_AUTHORIZED_PENDING_BUILDER / SIX_MODULE_MVP`

```text
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_head_resolution: LIVE_REMOTE_REF_REQUIRED
formal_tree_resolution: LIVE_REMOTE_REF_TREE_REQUIRED
mirror_result: THIS_COMMIT
mirror_effect: ZERO_PRODUCT_STATE_CHANGE
mirror_repository_delivery_resolution: zero-write APPROVE exists AND LIVE_REMOTE_REF contains THIS_COMMIT
```

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

### 3.4 Stage 3完成证据与Stage 4正式实现结果

Stage 3已接受证据为：direct 55 passed、repository hygiene 10 passed、CI-equivalent full 199 passed，全部最终退出0且无skip；独立Reviewer只读核验精确对象、代码、测试定义和Builder原始输出，没有重跑测试。该证据不证明真实第三方/大陆镜像下载、生产DataRoot集成、WorkBuddy、Stage4、Provider或媒体/视频E2E，也不需要这些后续证据来维持Stage3 `PASS_ACCEPTED`。

Stage4规划已经独立审查、普通fast-forward并记为`PASS_ACCEPTED`。已接受的release-specific immutable `PackageToolDefinitionV1`闭合当前Locator不提供固定工具入口身份的问题，并冻结`launch_session_tool(...)`及`LauncherReceiptV1`精确字段。既定实施授权已消费完成；最终Package物化和真实WorkBuddy都不是编码前置，具体Release缺工具定义实例时，真实调用必须preflight阻断。

实现严格覆盖既定五路径和35到37的固定树迁移。最终实现对象`fa9adb8470ab94b88ec9900ede03cb26f7de0ebd`、tree `0809d1c4cccc9838180a016c75320b0d9fbce28a`经第八轮独立零写审查`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward。首个正式CI run `32367792637`只因测试夹具错误假定GitHub `setup-python`环境有`pyvenv.cfg`而失败，没有生产Launcher finding；单测试路径修复`13a3227b0c55bbe9039b46d7e92eba822b48f57e`、tree `d3ac89ec89b66789cabe92d94c3e827f9c2cc22f`也经独立审查`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward。修复后官方Ubuntu 24.04 / Python 3.11.16 CI run `32369588814`为`357 passed / 1 skipped / exit 0`；Windows最终证据为158 direct、11 hygiene、358 combined，全部exit 0且无skip。

secret nondisclosure合同澄清已经独立`APPROVE / P0=0 / P1=0 / P2=0`并进入formal，实现候选也已经据此修订和重新独立验收。Stage4 closeout固定历史锚点`b63d8c2bc2214bc39f18378dbe47057ef538301e`、tree `02814c6a4a483913e7b1abe3e9ee6d025236c951`已经`V2-S4-IMPLEMENTATION-CLOSEOUT-REVIEW1`独立`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward；closeout CI run `32371507874`在Ubuntu 24.04 / Python 3.11.16上`357 passed / 1 skipped`。Stage4实现已是`PASS_ACCEPTED`；其中`current_task=NONE / current_task_status=NO_ACTIVE_TASK / next_authorized_task=NONE`是`HISTORICAL_STAGE4_CLOSEOUT_CONTEXT`，不覆盖当前Stage5 authority。`mirror_result/mirror_effect/mirror_repository_delivery_resolution`只自解析镜像仓库交付，不形成当前任务、不重新门禁既有Stage4产品状态。

### 3.5 Stage 4已实现合同与验收边界

已接受规划已把两个已知缺口闭合为可实现合同，仓库实现及修复也已正式集成；这些证据仍不授权真实生产Launcher运行。固定工具身份不等于编造上游入口：`PackageToolDefinitionV1`冻结authority、closed schema、release绑定和缺实例fail-closed规则，具体Release实例由批准Golden Key Package定义/最终交付Installer owner提供。

已实现合同的Gate继续按以下顺序裁决：

1. **输入PASS**：唯一入口精确为`launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`；inputs closed，user message字节不变，返回递归冻结。所有非空Provider value在入口先保守标记为secret source，唯一授权sink为child环境；pre-cancel在Locator 0/spawn 0前完成动态hints保护。
2. **身份PASS**：同次Locator的Registration/Manifest/Lock身份由preflight外部绑定并进入receipt；定义只绑定稳定Release/commit、定义文件、工具、解释器、argv/env/local requirements，不含Registration/Manifest/Lock hash。定义文件本身和工具文件均在当前Manifest与Lock中唯一覆盖，传入定义字节与Package内文件相同，authority owner及工具relative path/hash/size/owner一致；定义、工具和解释器每个路径组件无link/reparse且在PackageRoot内；spawn前复核不漂移。真实fixture必须完成含定义+工具Package的`register -> locate -> validate`往返。
3. **opaque capability PASS**：代码中无Provider、renderer或runtime catalog；环境变量名只来自定义allowlist，Provider-secret source只进入子进程环境；只有定义声明时才接受完整approved capability definition、其canonical SHA、未改写original Stage3 fact及其canonical SHA。Stage4独立验证closed definition/fact hash，并按fact source重验：managed必须是DataRoot受管安全root、全部定义assets及closed-tree；explicit必须是定义候选安全绝对root、全部定义assets，允许且保留额外外来文件；PATH必须`runtime_root == verified_entrypoint`且为安全绝对regular command，只核对entrypoint asset。未知source fail closed；`INTEGRATED`必须managed并保留plan identity。原始fact仅作审计，version_evidence不受信。Provider缺失不触发Stage3。
4. **进程PASS**：`cwd`为verified PackageRoot，环境为固定最小基线加allowlisted provider环境，stdin为单一closed JSON envelope且Provider value为0，`shell=False`，spawn恰好一次，retry恒为0；timeout/cancel终止自有进程树并检测残留。不可信stdout/stderr对每个完整secret UTF-8 bytes做跨chunk检测，任一命中都无常量例外地裁决`SECRET_DISCLOSURE_DETECTED`。
5. **回执PASS**：任何输入/preflight/spawn/运行结果都返回`golden-key-workbuddy-launcher-receipt-v1`全部固定字段，outcome只取9值、reason只取23值。固定secret-independent协议常量及`TASK-REGISTER.md`精确字段闭集内、可从Package/PackageToolDefinition/Manifest+Lock/实际工具与解释器字节独立重建的权威字段与secret偶然相同不误报；caller/child动态域在freeze前做provenance-aware non-propagation检查。`original_stage3_fact`及其`plan_sha256/original_stage3_fact_sha256/status/source/reused/runtime_root/verified_entrypoint/version_evidence`都是动态域；local identity因混合fact-derived字段而整体不得套authority例外，任一item受污染必须清空整个`local_capability_evidence_identities` tuple。其他受污染值只用现有类型允许的`None`、空tuple、固定安全文本或安全流摘要替换，不删除字段、不向`tuple[str]`插入`None`。任何Provider value复制/派生进动态receipt、日志或异常为0。
6. **结果PASS**：精确优先级仍为11级：invalid cancel/input、pre-cancel、preflight、spawn fail、residual、secret disclosure、timeout/cancel首次monotonic观察、nonzero、invalid output/result、child FAILED、success。入口已取消且secret等于session/request时仍为`CANCELLED/CANCELLED_BEFORE_SPAWN`、Locator 0、spawn 0，相关hints为`None`；exit 0+child `FAILED`为`CHILD_REPORTED_FAILURE/CHILD_REPORTED_FAILURE`；只有exit 0、单个有效`SUCCEEDED` envelope、受控result root内hash/size匹配指针、无泄密且无残留可为`EXITED_SUCCESS`。

以下任一项为实现`FAIL`：从Guide/registry/目录/调用者推断工具；修改Stage2 Registration；任意shell/argv/env注入；硬编码Remotion/HyperFrames或Provider；把Provider配置缺失当Stage3证据缺失；Provider value被复制/派生进argv、canonical stdin、动态receipt、log、异常或回传原文；对child输出遗漏单chunk/跨chunk完整secret；把固定协议常量偶然碰撞误判到无法返回合法schema；多次spawn/retry；工具/解释器替换后继续；结果路径逃逸或reparse；残留未报告；第二Agent、服务、数据库、调度、媒体、Artifact或Checkpoint逻辑存在。

以下为`PRELAUNCH_BLOCKED`而非实现失败：没有活动Registration；Release尚未提供具体`PackageToolDefinitionV1`实例；定义文件/工具未被当前Manifest与Lock正确覆盖，或定义的Release/commit与Locator不同；定义声明的本地能力证据缺失/漂移；环境变量名不在allowlist。最终Package物化与真实WorkBuddy都不是规划或编码前置，但是真实生产启动必须具备其当前Release实例。

直接测试最低矩阵精确覆盖：Registration/Package/tool/interpreter全部漂移；定义closed schema/self-hash/authority/Manifest+Lock覆盖及定义不含Registration/Manifest/Lock hash；含定义+工具的真实Stage2 fixture完成`register -> locate -> validate`；路径逃逸、ADS、alias、symlink/junction/reparse；命令/argv/env注入；user message不变与controls分离；本地能力声明/不声明、完整定义+原始fact、摘要重包装拒绝、version_evidence不受信；managed/explicit/PATH三种合法PRESENT；managed额外文件/目录拒绝；explicit定义资产漂移拒绝且额外文件零改写；PATH命令替换、非regular或不安全拒绝；合法managed INTEGRATED保留plan identity，非managed INTEGRATED与未知source拒绝；动态Provider名不硬编码、任意env名拒绝、Provider缺失不错误要求Stage3；Python-script/direct-executable两种成功；总是返回receipt、invalid input nullable字段、pre-cancel spawn0、spawn失败；优先级全部竞争分支；child FAILED；spawn一次/no retry；非零/timeout/cancel/残留；输出上限；结果envelope和pointer全部失败分支；递归不可修改receipt。secret专项必须另覆盖：value=`-`/`I`只撞固定token时schema可表示；value等于pre-cancel session/request时取消结果不变且hints安全；value传播进user_message/session/request/result root/pointer/error时阻断并安全替换；stdout/stderr单chunk与跨chunk完整bytes检测；JSON escape后动态重建检测；独立authority name/identity偶撞不误报；`None`/空tuple/固定文本/安全流摘要不破坏类型；argv/stdin/dynamic receipt/log/exception最终来源传播为0。

上述secret专项中“独立authority name/identity”只指`TASK-REGISTER.md`字段级闭集，不包括任何local capability identity item。必须另有otherwise-valid managed `INTEGRATED`和`PRESENT`反例：其`plan_sha256/original_stage3_fact_sha256/status/source/reused/runtime_root/verified_entrypoint/version_evidence`或同一identity其他字段复制/派生Provider value时，精确为preflight fail closed、spawn 0、receipt原文0，并以空tuple清空整个`local_capability_evidence_identities`；不得保留混合identity的独立子字段。

正式实现路径精确为：

```text
golden_key_openmontage_workbuddy/session_launcher.py
golden_key_openmontage_workbuddy/__init__.py
tests/workbuddy/test_session_launcher.py
tests/workbuddy/test_repository_hygiene.py
.github/workflows/ci.yml
```

新增一个生产模块和一个直接测试后，固定tracked树已从35精确变为37。hygiene显式更新37文件等值、4个Python源文件和API闭集；CI在现有唯一pytest命令中显式加入Stage4直接测试，没有用glob或动态计数放宽。`package_registration.py`、`runtime_prepare.py`、`pyproject.toml`及任何第6路径均未进入实现差异。

Builder最终给出Stage4 direct 158、repository hygiene 11、full suite 358的未截断Windows输出，全部exit 0且无skip，并报告精确base/candidate/tree/5路径/37 tracked/clean/untracked0/stash0。Reviewer独立零写比较精确base..candidate，核对公共合同最小性、fail-closed反例、secret边界和无Scope扩张，最终为`APPROVE / P0=0 / P1=0 / P2=0`；单文件CI夹具修复也独立`APPROVE / P0=0 / P1=0 / P2=0`。WSL只作临时Linux等价验证，已清理关闭，不是运行依赖。普通fast-forward正式推广后仍不得自动启动Stage5/6。

Stage5的消费者合同只需提供literal message、closed controls、approved PackageToolDefinition、经单独授权的Provider环境，并在定义声明时原样传递完整approved capability definition与未改写original Stage3 fact；不得重包装摘要。Stage4按原始managed/explicit/PATH source语义独立验证实际资产；Stage6优先直接使用同一receipt，格式无缺口时必须`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`且生产代码0。真实生产WorkBuddy/Launcher会话、Stage5、Stage6、Provider/媒体执行及final Package物化/生产登记仍为`NOT_GRANTED`或未证明，不得用Stage4单元测试冒充。

### 3.6 阶段5规划验收与实施启动前置

本节裁决Stage 5规划候选，不裁决Stage 5产品实现或真实客户端PASS。当前必须保持：

```text
stage_5_planning: PASS_ACCEPTED_CANDIDATE / EFFECTIVE_ONLY_AFTER_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
stage_5_implementation_authorization: EXPLICIT_USER_AUTHORIZED / PENDING_FORMAL_CLOSEOUT_AND_BUILDER_TAKEOVER
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
final_package_gate: NOT_GRANTED / final_package_artifact=NOT_MATERIALIZED / production_registration=NOT_CREATED
next_authorized_task: V2-S5-WORKBUDDY-ENTRY-BUILDER1 / EFFECTIVE_ONLY_AFTER_THIS_CLOSEOUT_CANDIDATE_IS_INDEPENDENTLY_APPROVED_AND_ORDINARY_FAST_FORWARD_TO_FORMAL
test: NOT_RUN_DOCS_ONLY / CLOSEOUT_DOCS_ONLY
```

Stage 5唯一目标是“WorkBuddy唯一Agent + 一个真实显式入口 + 原话不变 + Locator/Guide/PackageToolDefinition顺序 + 一次已接受Stage 4调用 + 原始事实转交”。固定链路为：

```text
Stage 4 accepted API
  -> one real WorkBuddy entry
  -> locate_active_package(data_root)
  -> Registration/PackageRoot/Manifest/Lock/Guide/required-toolchain validation
  -> verified Guide read
  -> current-release PackageToolDefinitionV1
  -> launch_session_tool(...), Stage4 fixed tool spawn <= 1
  -> WorkBuddy/OpenMontage production decisions
  -> Stage6 direct LauncherReceiptV1/fact relay
```

此前 Stage 5 T1 固定桥梁候选四路径规则仅属于历史 docs-only 合同候选；当前规划收口候选允许六份 authority 文档同步，未来实施另有五路径白名单。当前候选不等同于实现完成，也不冒充真实生产 PASS。任一任务超出各自明确白名单即`STOPPED_SCOPE_EXPANSION`。本候选不运行代码、测试、CI、真实WorkBuddy、Launcher、Provider、媒体、WSL，不物化最终Package或创建生产Registration。

#### T1-T12规划验收表

| 任务 | 验收对象/权威输入 | 必须动作与输出 | 未来物理承载 | 失败裁决与下游 |
|---|---|---|---|---|
| T1 真实唯一入口 | 腾讯/WorkBuddy官方资料、WorkBuddy 5.3.13既有受控客户端证据、本仓库入口边界；旧V1 Skill仅历史证据 | 入口冻结为一个 WorkBuddy-managed Skill catalog 资产；官方资料确认 Skill 可封装脚本/工作流并支持 `Skill + CLI` 形态，固定 CLI 只能作为该 Skill 内部桥梁；既有 HY3 exact Skill 证据证明会话命中。内部桥梁已冻结为单消费者、固定身份、固定 envelope，并绑定已接受 Stage4 `launch_session_tool(...)`/`LauncherReceiptV1` | 物理安装路径保持 opaque（不得编造磁盘目录）；禁止第二用户入口、第二Agent、MCP/CLI并行控制面、兜底、任意命令/argv/Shell生成和自动重试/重放 | 外部 WorkBuddy 机制已确认；T1 内部桥梁为`FROZEN_FOR_PLANNING`，当前规划为`STAGE5_PLANNING_PASS_ACCEPTED_CANDIDATE`，仅待独立 APPROVE/ordinary FF 生效；release-specific Installer/Skill asset 与真实实现仍待后续 handoff/验收；不因CLI存在判架构不可用 |
| T2 输入合同 | Stage2/3/4正式合同与用户授权 | 冻结literal `user_message`、素材、closed controls、PackageToolDefinitionV1、Provider env、完整approved definition+original Stage3 fact、cancel/continuation | 唯一入口和受控调用域；不进入日志/平行库 | 跨域、非法字段、摘要重包装即fail closed；下游T3/T4 |
| T3 验证顺序 | Registration/Locator合同 | 显式入口后先Locator，验证Registration/PackageRoot/Manifest/Lock/Guide/必带工具链，成功后读Guide并取得当前定义 | 复用Stage2 Locator；不复制Guide/Package | 扫盘/猜路径/未验证Guide/漂移即spawn 0；下游T4 |
| T4 Stage4适配 | 固定`launch_session_tool(...)`与LauncherReceiptV1；本项目T1内部桥梁合同 | 原样传message；只传完整定义/原始事实；Skill 内部桥梁只消费已冻结固定 CLI envelope，Stage5不拼接任意命令/argv/Shell、不改写摘要；Stage4固定工具最多spawn一次 | 最多一个入口适配生产模块；固定 CLI 的 release-specific identity/template/envelope 已`FROZEN_FOR_PLANNING`，实际资产与实现仍待后续授权 | 任何第二入口、动态命令、重试/重放、字段丢失或receipt改写即停止；下游T5/T6 |
| T5 授权继续 | Stage3逐能力授权、Package Guide、WorkBuddy会话 | 能力/外部服务/费用独立授权，绑定definition+plan+session；失效即重问；拒绝/暂缓走基础/其他路径；不支持继续时提示“继续刚才的任务” | 当前会话，不建重放库/授权数据库 | 自动重试/重放、授权混用即停止；下游T6/T10 |
| T6 结果映射 | Stage3五结果、Stage4九outcome和11级优先级 | 建立展示事实、展示计划、继续基础、准备完成、阻断、取消/超时/失败/泄密/残留、结果指针的闭集映射 | 入口确定性呈现或直接receipt；不建结果服务 | 失败不改成功、不解释Artifact、不改优先级；下游T11 |
| T7 凭据隐私 | Stage4 secret合同和定义allowlist | secret只入allowlisted child env；不进入chat/message/argv/stdin非授权域/log/receipt/error；Key不等于可用/费用授权；不推荐/排序/回退Provider | child环境短生命周期，不建Provider目录/密钥库 | 任意传播/未授权环境/泄密即fail closed；下游真实安全验收 |
| T8 失败闭集 | Stage2 Locator、Stage4 9值+11级优先级 | 每类固定Locator?、Stage4?、spawn次数、用户结果、基础能力继续、是否终止；覆盖15类：无Registration、Package/工具链漂移、Guide未验证、定义缺失/不匹配、非法输入、能力证据缺失/漂移、Provider未授权、拒绝/暂缓、入口前取消、启动失败、child失败、timeout、secret disclosure、非法result pointer、残留进程 | 只在入口/receipt呈现边界，不建重试器/数据库 | 未分类、无最终exit、优先级被覆盖即`INCOMPLETE`；下游T10/T12 |
| T9 Package Gate | Package Registration合同、Project State、Stage4定义合同 | 规划不要求最终Package；受控fixture可证明合同；真实生产前必须Final Package物化/安装/Production Registration+Activation/新进程Locator；缺具体Release定义实例真实调用阻断 | 最终Package由后续Installer承载，入口不写PackageRoot | 临时ZIP/旧Skill/单测冒充生产即停止；下游真实Gate |
| T10 证据分层 | 本矩阵状态定义和真实测试卡 | 独立报告10层：静态合同、单元负面、Stage2/3/4集成、WorkBuddy新会话、唯一入口、原话不变、授权/继续、生产Package身份、Provider/媒体、业务效果 | 各自证据对象，不在代码伪造 | 前层PASS不得替代后层；缺证据`NOT_PROVED/INCOMPLETE` |
| T11 Stage6交接 | Stage4 LauncherReceiptV1、Stage3 facts、真实Stage5消费者（尚未证明） | 先直接复用；无真实字段缺口则`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`、生产代码0；有缺口才另行授权 | 当前零Stage6文件/模块 | 无消费者/无缺口不预建；下游独立Stage6授权 |
| T12 实施任务包 | T1-T11、届时latest formal、用户明确“启动阶段五实施” | 固定Builder `V2-S5-WORKBUDDY-ENTRY-BUILDER1`；入口1、生产模块≤1、直接测试1；Reviewer、P0/P1/P2、普通FF、清理和N+1停止规则 | 精确五路径已冻结：`workbuddy-skill/golden-key-openmontage/SKILL.md`、`golden_key_openmontage_workbuddy/workbuddy_entry_cli.py`、`tests/workbuddy/test_workbuddy_entry_cli.py`、`tests/workbuddy/test_repository_hygiene.py`、`.github/workflows/ci.yml`；tracked`37 -> 40`；direct/hygiene/full命令固定；第N+1路径停止 | 无T1/授权/对象一致性/独立APPROVE不得实施或推广 |

#### T1 Evidence1 官方证据门禁（历史候选，已被本轮T1 Skill+CLI重新评估取代）

Evidence1 的正式候选基线是 `44d89625c1fd71d07d1173e18681e64e7459cec2`、tree `10c8c4187299564fc83cef38a3f9ac65f4f9790a`、tracked 37；候选分支为 `codex/v2-s5-t1-official-contract-evidence1`，最大白名单为 `PROJECT-STATE.md`、`docs/workbuddy/v2/TASK-REGISTER.md`、`docs/workbuddy/v2/PROJECT-CHARTER.md`、`docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`。证据只来自腾讯/WorkBuddy官方公开页面和仓库既有静态记录，访问日期为 `2026-08-21`；真实客户端固定为`NOT_AUTHORIZED_IN_THIS_TASK`；测试固定为`NOT_RUN_DOCS_ONLY`。

官方页面已证明的是高层产品事实：WorkBuddy可导入/安装 Skill，在对话框选择已安装 Skill 后自动调用对应能力；官方连接器资料还明确列出`Skill + CLI（内置脚本）`形态，权限资料确认WorkBuddy可在用户授权边界内执行脚本、命令或外部程序。页面没有证明本项目固定 CLI 的名称、身份、单一输入输出 envelope、唯一消费者或与`launch_session_tool(...)`/`LauncherReceiptV1`的具体映射。旧 Evidence1 把“官方未证明零 CLI 直调”误写成“CLI不得存在”的必要条件，该解释已被本轮纠偏取代。完整 URL、标题、页面更新时间、精确 claim/gap和逐项状态以`TASK-REGISTER.md`本轮T1章节为任务级权威。

五项逐项状态必须按以下闭集裁决：

| T1 项目 | Evidence1候选状态 | 通过条件 |
|---|---|---|
| Skill 包结构/必需文件/schema | `UNPROVED_OFFICIAL` | 官方资料或另行授权受控客户端给出可复核的完整包树、必需文件和schema |
| 安装/导入归属与物理位置 | `PARTIALLY_PROVED_OFFICIAL` | 必须证明导入后的物理位置、所有权及用户级/workspace级语义，不能由项目级功能名推断 |
| 显式调用主体/入口/触发 | `PARTIALLY_PROVED_OFFICIAL` | 必须证明当前固定入口名、选择绑定、dispatch和会话边界 |
| 唯一消费者/WorkBuddy唯一Agent边界 | `PARTIALLY_PROVED_OFFICIAL` | 必须证明唯一消费者且无第二Agent/CLI/MCP/并行入口 |
| Stage4消费/内部桥梁协议 | `UNPROVED_PROJECT_BRIDGE` | 腾讯官方无需定义本仓库Python API；项目必须冻结一个固定 CLI identity、单一 envelope、原样承载`user_message`/`executor_controls`/完整定义与原始事实、一次调用和逐字段`LauncherReceiptV1`映射。不得生成任意命令/argv/Shell |

因旧Evidence1的五项未全部闭合，其`T1_EVIDENCE_INCOMPLETE`只作为历史候选保留；当前总裁决由本轮T1章节给出，不得继续使用“CLI存在即架构不可用”。无论本轮是否闭合，Stage5实现授权、最终Package、生产Registration、Provider、媒体和Stage6仍保持未授权/未证明。

#### T1受控客户端证据门禁（候选）

受控客户端候选使用 WorkBuddy `5.3.13`、D盘隔离根和唯一无副作用 `golden-key-s5-t1-noop-evidence`。客户端默认安全检测完成后，“我安装的”从0变1；上传页明确文件夹或ZIP包含`SKILL.md`，Markdown YAML含name/description；新任务输入框明确“`/` 调用技能与指令”。在模型明确由Auto切换为`Hy3`后，第二次 exact Skill 调用8秒完成并精确返回`T1_CONTROLLED_NOOP_OK`，响应底部标注`Hy3`。第一次`Auto (GLM-5.2)`结果排除出最终模型证据。未出现额外权限提示，Provider、媒体、最终Package、production Registration、Python、CLI/MCP和Stage4真实spawn均未运行。

| T1 项目 | 受控客户端候选状态 | 当前通过范围 | 仍需闭合 |
|---|---|---|---|
| Skill 包结构/必需文件/schema | `PARTIALLY_PROVED_CLIENT` | root `SKILL.md` ZIP、name/description YAML最小导入合同 | 完整schema和可选目录树 |
| 安装/导入归属与物理位置 | `PARTIALLY_PROVED_CLIENT` | 当前客户端“我安装的”集合及exact身份 | 物理落点、账号/设备/workspace/project完整归属 |
| 显式调用主体/入口/触发 | `PROVED_CLIENT_FOR_5.3.13_SESSION` | WorkBuddy新任务slash入口加载exact Skill，HY3返回exact marker | 不外推其他版本/账号；生产Stage4入口未实现/运行 |
| 唯一消费者/WorkBuddy唯一Agent边界 | `PARTIALLY_PROVED_CLIENT` | 干净UI起点只有该临时Skill，调用与响应均由同一WorkBuddy UI呈现 | 全局唯一消费者、无第二Agent及无其他dispatch未由UI证明 |
| Stage4消费/内部桥梁协议 | `UNPROVED_CLIENT_BRIDGE` | 无 | 固定 CLI identity、单一 envelope、与`launch_session_tool(...)`调用及`LauncherReceiptV1`逐字段回传尚未由客户端运行证明；依授权不得真实spawn |

客户端候选五项未全部闭合，故历史客户端结果仍为`T1_CLIENT_EVIDENCE_INCOMPLETE`；它不能裁决固定 CLI 桥梁可用或不可用。临时Skill已由用户手动卸载，客户端核验已安装技能为0；精确D盘隔离根已移入Windows回收站且源路径不存在。该候选不是产品PASS或实现授权；独立Reviewer批准并普通fast-forward前，也不是正式仓库交付。

#### T1 Skill+CLI合同重新评估（当前候选）

本节 supersede 上述历史候选中“零 CLI 才能成立”的解释。最初产品目标回读为`PASS`：腾讯 WorkBuddy 是唯一运行中的 Agent 和唯一用户入口；读取已验证 Package Guide 后承担 OpenMontage 逻辑生产角色。CLI 只有在一个 WorkBuddy Skill 内作为固定、内部、单消费者 transport adapter 时才可进入候选；它不是用户第二入口、并行控制面或失败兜底。

官方支持层与本项目合同层分开裁决：腾讯官方资料只需证明 WorkBuddy 的 Skill/脚本/CLI 能力形态；固定 CLI 的名称、身份、输入输出 envelope、Stage4 API 调用和 receipt 映射属于本项目自己的内部桥梁合同，不要求腾讯页面定义本仓库 Python API。官方资料、精确 URL、标题和缺口以 `TASK-REGISTER.md` 的当前 T1 评估矩阵为准。

当前冻结边界如下：

- `one WorkBuddy Skill -> one fixed internal CLI bridge -> accepted Stage4 consumer` 是唯一允许的候选形态；WorkBuddy 仍是唯一 Agent，Skill/CLI 不得创建第二 Agent。
- 固定 CLI 必须绑定 release-specific identity/owner/hash（或同等可验证身份）、固定单一 envelope，并原样承载 `literal user_message`、非秘密 closed controls、`PackageToolDefinitionV1`、完整 approved capability definition 与 original Stage 3 fact、cancel 事实；provider secret value 只从固定 CLI 进程环境按 allowlist names 读取并重建 Stage4 controls；输出必须是字段保持的 `LauncherReceiptV1`。
- 不得从用户原话拼接任意 command/argv/Shell，不得启用 MCP 旁路、第二 Skill、全局意图截获、自动重试或自动重放；Stage4 的一次固定 Package-tool spawn 上限不变。
- WorkBuddy-managed installed Skill catalog 是可冻结的逻辑安装归属；官方未披露的物理路径保持 `opaque`，不得借 CodeBuddy 页面或路径推断 WorkBuddy 目录。

本轮官方能力证据和既有 HY3 exact Skill 命中已足以确认该 WorkBuddy 外部机制可用；本节保留已冻结的固定 CLI identity、固定 argv、secret-safe envelope、唯一消费者和 Stage4 字段映射合同。其 closeout 前状态为 `T1_INTERNAL_FIXED_CLI_BRIDGE_CONTRACT_FROZEN_FOR_PLANNING` / `IN_PROGRESS`；当前 planning closeout 候选已接管 live 状态，规划为 `STAGE5_PLANNING_PASS_ACCEPTED_CANDIDATE`，仅待独立 APPROVE/ordinary FF 生效，下一 Builder 见本文件当前 closeout 段，不得把旧状态或“CLI存在即架构不可用”作为当前裁决。

#### 当前 T1 固定 CLI 桥梁验收合同（`FROZEN_FOR_PLANNING`）

| 验收面 | 当前冻结的最小合同 | 立即拒绝/停止条件 |
|---|---|---|
| 唯一入口与身份 | 一个 WorkBuddy-managed installed Skill catalog entry；Skill 是唯一用户入口，物理安装路径 `opaque`；Installer/Skill release asset 可验证 skill/release/owner、绝对 package-private interpreter identity/path、module、schema、argv、environment 与 hash 身份 | 第二用户入口、第二 Skill、第二 Agent、MCP/并行控制面、猜测物理路径或复用旧 V1 Skill |
| 固定调用形状 | `LOCATOR_PACKAGE_PYTHON -I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli`；`shell=false`；无 console-script、子命令、业务路由或动态 argv；解释器来自同次 Locator 的 package-private Python | 从 `user_message`/controls 生成 command、argv、Shell、子命令或解释器；调用者追加参数；retry/replay。T4 禁止调用者/用户动态生成或追加 argv；Installer/Skill release asset 预冻结的固定字面量模板不属于动态生成 |
| 输入 transport | stdin 恰好一个 `golden-key-workbuddy-skill-cli-request-v1` canonical JSON 对象；canonical 只约束 UTF-8 wire encoding、key order、数字形式和单个末尾 LF，不对 literal `user_message` 做 NFC/NFD、trim 或换行转换；桥接层只验证 Stage4 既有 NFC 前置，非 NFC/非法 UTF-8/JSON 直接 exit `64`，已合法 code-point sequence 原样传递。closed fields 为 `schema_version/bridge_contract_id/data_root/user_message/executor_controls/package_tool_definition/local_capability_evidence/cancel_requested/continuation`；完整 PackageToolDefinitionV1 与完整 approved definition+original Stage3 fact 逐字段传递 | 多对象/多行协议、未知或缺字段、摘要/摘要hash替代完整对象、改写 literal message、技术控制拼入 user message |
| controls 与 secret | `executor_controls` 只含 session/request/timeout/termination grace/result root、固定 process-env source 和 `provider_environment_names`；secret value 不进 stdin。CLI 仅按 names 从自身进程 env 读取并重建 Stage4 `provider_environment`，Stage4 再按定义 allowlist 注入固定 child env | `provider_environment` value 进入 JSON/argv/stdout/stderr/hash/长度/log/异常/receipt；name 缺失、额外、重复或不在 allowlist；整份宿主环境继承 |
| 一次 Stage4 调用 | 仅当 bridge preflight 已通过并进入 Stage4 的有效请求，CLI 才必须恰好一次调用 `launch_session_tool(...)`，传原话、重建 controls、完整 definition、完整 local evidence 和本地 cancel Event；Stage4 保持 Locator/preflight/spawn/receipt 唯一控制面 | bridge preflight 通过后 0 次或 2 次调用、并行、后台服务/IPC、Provider选择、Stage4字段重排或新控制面；pre-Stage4 input/identity/env/asset fail-closed 的合法结果是 Stage4 调用0次、无 receipt |
| 输出与 exit | stdout 只允许一个 `golden-key-workbuddy-launcher-receipt-v1` 完整 JSON mapping，逐字段对应 immutable LauncherReceiptV1；stderr 只允许固定脱敏诊断 token。闭集为 `0`=Stage4 恰好一次且完整 receipt 缓冲/验证/序列化/输出（含失败 outcome），`64`=输入/schema/identity/cancel/continuation 无效，`78`=固定 asset/process-env/provider-name 配置或 secret provenance 无效，`70`=bridge internal 或 Stage4 后 receipt 完整序列化/输出前验证失败；stdout 先完整缓冲验证，错误时为空 | stdout 摘要/包装/多对象/日志、receipt 改写或丢字段；使用非 `0/64/70/78`、伪造 receipt、错误时输出部分 stdout；stderr含secret/路径/异常/动态值 |
| 取消与继续 | `cancel_requested` 只在入口创建本地 `threading.Event`，true 先 set 后一次调用；运行中取消/Host终止留给 T5/实现，不造后台 IPC。`USER_CONFIRMED_NEW_REQUEST` 必须是新 request/envelope，`prior_request_id` 仅审计关联 | 自动重放旧 message、把 continuation 当 retry、伪造运行中取消 receipt |
| 实施边界 | 本 closeout 候选仅 docs-only；规划 `PASS_ACCEPTED` 仅在独立 APPROVE 和 ordinary FF 后生效；未来五路径实现白名单、D盘 task-private venv、direct/hygiene/full 命令和`37 -> 40`已冻结；用户“启动阶段五实施”已记录，但 Builder 必须从最新formal接管 | 任何候选代码/测试/CI执行、真实客户端、Python/Stage4 spawn、Provider、媒体、Package、Registration、Stage6 或实施完成/真实生产 `PASS_ACCEPTED` 宣称 |

transport exit 语义必须保持闭集且只允许 `0/64/70/78`：`0` 表示 Stage4 恰好调用一次且完整 receipt 已先缓冲、验证、序列化并输出，Stage4 返回任何真实 receipt（包括非成功 outcome）均为 `0`；`64` 表示 input/schema/identity/cancel/continuation 或已验证的 Stage4 `user_message` NFC/UTF-8 前置无效；`78` 表示固定 release asset、process-environment、provider-name 配置或 secret provenance 无效；`70` 表示 bridge internal failure，或 Stage4 调用后完整 receipt 序列化/输出前验证失败。所有非 `0` 结果 stdout 为空且不得伪造 receipt；Stage4 原有九值 outcome、23 reason、11级优先级、`spawn_count<=1` 和 `retry_count=0` 不由 CLI 改写。

#### T8失败矩阵的机械要求

对于15类失败，候选文档必须同时给出：是否调用Locator、是否调用Stage4、`spawn_count`、用户可见状态、是否允许基础能力继续、是否终止当前请求。入口前非法输入和入口前取消可在Locator前阻断；Package/Guide/定义/能力身份失败必须保持spawn 0；Stage4启动失败为spawn 0；child失败、timeout、secret disclosure、非法pointer、残留均为spawn 1并保留真实事实。拒绝/暂缓与Provider未授权可以在WorkBuddy明确选择下继续基础能力，但不得自动回放；所有竞争结果服从Stage4既定11级优先级，Stage5不覆盖。

#### T9/T10生产边界

规划、fixture、Stage 2/3/4接口集成和真实WorkBuddy生产是不同证据层。当前最终Package仍`NOT_MATERIALIZED`，生产Registration仍`NOT_CREATED`；真实WorkBuddy生产验收前必须完成最终物化、安装、生产登记/激活和新进程Locator。真实Provider、媒体、成片和业务效果均不能由Stage 5单测宣称完成。

#### 历史规划候选治理验收（`V2-S5-PLAN-BUILDER1`，仅历史）

本段只记录旧候选的治理规则，不是当前 T1 候选的 live 基线或路径约束：旧基线为`042686039386a63866eba2f964f1fa9674bbec4b`、tree `6d6f3f0352eeb75c57170f2fe9e854c79564416c`、tracked 37，旧候选只允许三条文档路径。该旧规则的`git diff --check`、tracked 37、无代码/测试/CI/Package/外部对象变化、`NOT_RUN_DOCS_ONLY`、独立零写Reviewer及 P0/P1/P2 分级要求均保留为历史审计依据；它不得否定当前四路径 T1 reassessment，也不得把当前外部机制重新标为阻断。

#### 历史 T1 reassessment 候选治理出口（已被固定桥梁候选 supersede）

该段只记录前一轮 T1 reassessment 候选：基线`24418c7cf5cc003c106a8282158adb3125bb0606`、tree `d61a4a455a0e4f5202a2b4907476beb97a655201`、tracked 37 和四路径规则。它已被当前 `V2-S5-T1-FIXED-CLI-BRIDGE-CONTRACT-PLAN1` 的新 base/合同/治理出口 supersede，不再是当前候选的 live base、状态或下一任务。

#### 当前固定 CLI 桥梁候选治理出口

当前候选基线固定为`3eed285da6ae48e502d5be1f8ca726906d36b7cd`、tree `c0b03c4e7d858d5f15c7ce328cf5e2b60b57978b`、tracked 37；候选精确允许且只允许以下四条路径：`PROJECT-STATE.md`、`docs/workbuddy/v2/TASK-REGISTER.md`、`docs/workbuddy/v2/PROJECT-CHARTER.md`、`docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`。必须通过`git diff --check`，tracked 仍为37，不得出现第五路径、代码/测试/CI/客户端/生产/Provider/媒体/Package/Registration/Stage6变化；测试状态固定为`NOT_RUN_DOCS_ONLY`。独立零写 Reviewer 只审固定模板、closed envelope、secret non-disclosure、一次 Stage4 调用、receipt/exit 语义、唯一入口和范围；P0 为安全/架构/授权/身份绕过或泄密，P1 为可执行合同/映射/证据缺口，P2 为非合同性文档问题。只有`APPROVE / P0=0 / P1=0 / P2=0`才可对该候选普通非force fast-forward；Reviewer不能把规划变成产品PASS。通过后仅条件化进入`V2-S5-PLANNING-CLOSEOUT-IMPLEMENTATION-HANDOFF-ASSESSMENT1`，仍不授予实现、客户端或生产授权，且不推送远端。

用户已于 2026-08-21 明确“启动阶段五实施”，因此该用户授权条件已满足；但实现仍须等待本 closeout 候选的独立 APPROVE/P0=0/P1=0/P2=0、ordinary fast-forward，并由 Builder 从届时最新 formal 接管。T1合同闭合、实时formal对象等值、精确白名单冻结、直接测试/CI命令冻结仍是实施门禁。Builder必须使用D盘独立worktree和项目私有`.venv`，REQUEST_CHANGES只能回原Builder；审核通过后普通非force fast-forward，关闭并清理临时worktree/branch。任何第N+1路径、假设路径/命令、formal前移、无最终exit或真实入口证据缺失均停止。

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
