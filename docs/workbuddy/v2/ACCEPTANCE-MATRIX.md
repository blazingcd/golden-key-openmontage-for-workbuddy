# WorkBuddy Shell V2 验收矩阵

状态：`STAGE_3_PASS_ACCEPTED / STAGE_4_PLANNING_PASS_ACCEPTED / STAGE_4_IMPLEMENTATION_PASS_ACCEPTED / STAGE_5_IN_PROGRESS_ENTRY_CODE_COMPLETE_REAL_INTEGRATION_INCOMPLETE / SIX_MODULE_MVP`

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

Stage5的消费者合同只需提供literal message、closed controls、approved PackageToolDefinition、经单独授权的Provider环境，并在定义声明时原样传递完整approved capability definition与未改写original Stage3 fact；不得重包装摘要。Stage4按原始managed/explicit/PATH source语义独立验证实际资产；Stage6优先直接使用同一receipt，格式无缺口时必须`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`且生产代码0。Stage5整体仍为`IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`；真实生产WorkBuddy/Launcher会话、Stage5最终集成、Stage6、Provider/媒体执行及final Package物化/生产登记仍为`NOT_GRANTED`或未证明，不得用Stage4单元测试冒充。

### 3.6 [历史 / 已被 V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1 取代] 阶段5规划验收与实施启动前置

本节记录前一轮 Stage 5 planning closeout 候选及其实施启动前置条件；后续 Builder 已完成正式实施结果。当前 Stage5 状态和入口收口以本文末新的六文档 mirror 为准。

```text
stage_5_planning: PASS_ACCEPTED_CANDIDATE / HISTORICAL_PRE_ENTRY_IMPLEMENTATION_CLOSEOUT
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

#### [HISTORICAL / SUPERSEDED_BY_2026-08-24_REBASELINE] T1 Skill+CLI合同重新评估

本节 supersede 上述历史候选中“零 CLI 才能成立”的解释。最初产品目标回读为`PASS`：腾讯 WorkBuddy 是唯一运行中的 Agent 和唯一用户入口；读取已验证 Package Guide 后承担 OpenMontage 逻辑生产角色。CLI 只有在一个 WorkBuddy Skill 内作为固定、内部、单消费者 transport adapter 时才可进入候选；它不是用户第二入口、并行控制面或失败兜底。

本节曾把官方支持层与项目内部 fixed-CLI 合同层分开裁决；该区分本身可作历史事实，但具体 fixed-CLI/fixed-child 产品合同已被 2026-08-24 重基线取代。当前接口裁决以 `TASK-REGISTER.md` 末尾的重基线矩阵为准。

当前冻结边界如下：

- `one WorkBuddy Skill -> one fixed internal CLI bridge -> accepted Stage4 consumer` 是唯一允许的候选形态；WorkBuddy 仍是唯一 Agent，Skill/CLI 不得创建第二 Agent。
- 固定 CLI 必须绑定 release-specific identity/owner/hash（或同等可验证身份）、固定单一 envelope，并原样承载 `literal user_message`、非秘密 closed controls、`PackageToolDefinitionV1`、完整 approved capability definition 与 original Stage 3 fact、cancel 事实；provider secret value 只从固定 CLI 进程环境按 allowlist names 读取并重建 Stage4 controls；输出必须是字段保持的 `LauncherReceiptV1`。
- 不得从用户原话拼接任意 command/argv/Shell，不得启用 MCP 旁路、第二 Skill、全局意图截获、自动重试或自动重放；Stage4 的一次固定 Package-tool spawn 上限不变。
- WorkBuddy-managed installed Skill catalog 是可冻结的逻辑安装归属；官方未披露的物理路径保持 `opaque`，不得借 CodeBuddy 页面或路径推断 WorkBuddy 目录。

本轮官方能力证据和既有 HY3 exact Skill 命中已足以确认该 WorkBuddy 外部机制可用；本段保留已冻结的固定 CLI identity、固定 argv、secret-safe envelope、唯一消费者和 Stage4 字段映射合同。其 `T1_INTERNAL_FIXED_CLI_BRIDGE_CONTRACT_FROZEN_FOR_PLANNING / IN_PROGRESS` 状态属于实施前历史；实施结果和本文末当前入口收口 mirror 已接管 live 状态，不得把旧状态或“CLI存在即架构不可用”作为当前裁决。

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
| 实施边界 | 前一轮 handoff 仅 docs-only；实施已由 `V2-S5-WORKBUDDY-ENTRY-BUILDER1` 消费并形成正式五路径结果；本轮只做六文档 closeout。该 closeout 候选仅在独立 APPROVE 和 ordinary FF 后使 `stage_5_implementation=PASS_ACCEPTED`，候选不得自称已交付 | 任何本候选代码/测试/CI执行、真实客户端、Python/Stage4 spawn、Provider、媒体、Package、Registration、Stage6 或未审候选冒充生产 `PASS_ACCEPTED` |

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

## 10. [HISTORICAL / SUPERSEDED_BY_V2-S5-R00-REMAINDER-PLAN-STATE-CORRECTION1] Stage 5实施结果与入口收口机械出口

Stage 5 planning 当前为 `PASS_ACCEPTED`（不是 candidate）。实施任务 `V2-S5-WORKBUDDY-ENTRY-BUILDER1` 为 `CONSUMED_COMPLETE`，正式结果为 `0e7a0be65877b03fb386e1c6c6bc258c0b27db6c`、tree `85c266edb7349c940e8cd45870cc0538c95726c0`、parent `aa70c2cf9b6b4a29517d7354f0239ea0cdc9a5d3`，精确五路径、tracked `37 -> 40`。独立实施 Reviewer 为 `APPROVE / P0=0 / P1=0 / P2=0`；Windows direct/hygiene/full 为 `19/11/377 passed`、final exit 0；正式 CI run `32489111184` 为 completed/success、headSha 同上、Ubuntu/Python 3.14.7、`376 passed / 1 skipped`。

本轮 `V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1` 是 `DOCS_ONLY / EXACT_6_PATHS / ZERO_PRODUCT_STATE_CHANGE`。候选必须经过独立 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 并 ordinary fast-forward 进入 formal；在此之前 `stage_5_implementation` 只能记为 closeout-pending，候选不得自称已交付。推广后 `current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE`，且不自动授权真实 WorkBuddy production acceptance、最终 Installer-stamped Skill、最终 Package materialization/Registration、Provider/media 或 Stage 6。

入口验收合同不变：一个 WorkBuddy-managed Skill 是唯一 Agent/用户入口；Skill 内只调用 package-private fixed `-I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli` transport adapter，并在 bridge preflight 通过后恰好一次调用 `launch_session_tool(...)`，输出完整 immutable `LauncherReceiptV1`。无 console script、subcommands、router、MCP、第二 Agent、retry/replay、动态 command/argv/Shell；literal user message、closed JSON、provider secret、fixed identity、cancel/continuation 和 receipt 边界保持 fail-closed。

精确五个实施路径为：`.github/workflows/ci.yml`、`workbuddy-skill/golden-key-openmontage/SKILL.md`、`golden_key_openmontage_workbuddy/workbuddy_entry_cli.py`、`tests/workbuddy/test_workbuddy_entry_cli.py`、`tests/workbuddy/test_repository_hygiene.py`。静态/direct/hygiene/CI 证据只证明实现与运输合同，不证明真实 WorkBuddy、业务效果或 E2E；最终 Installer/Package/Registration、Provider、媒体和 Stage 6 仍须独立授权与证据。

## 11. [HISTORICAL / CONSUMED_BY_V2-S5-R01] Stage 5当前R00纠偏与整体验收门

当前Stage5不是PASS，而是 `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`。入口代码及其正式Review/CI是已接受子项；旧的 closeout candidate 只作 `HISTORICAL`，不得作为当前整体状态。

整体PASS的五个必要验收对象如下，缺一即不得 `PASS_ACCEPTED`：

| 必要证据 | 必须成立的事实 | 不能替代 |
|---|---|---|
| Final Release | retained final Package Release 与 PackageRoot 在清理后仍存在 | task-only临时Package、ZIP或旧运行历史 |
| Production registration | production Registration+Activation，new-process Locator 返回一致Package/工具链/Guide身份 | 单次register、task-only DataRoot或静态Registration |
| Final Skill | Installer-stamped、零placeholder、已安装且全局唯一的`golden-key-openmontage` Skill | 源目录、测试Skill、旧V1、一次导入成功 |
| Real WorkBuddy | HY3真实新会话成功取得真实`LauncherReceiptV1`，呈现字段可比对 | mock、静态CLI、Codex、客户端no-op标记 |
| Governance | 独立Review、正式Git/CI、无歧义live authority | 候选分支、聊天确认、历史PASS或未推广closeout |

R00 已正式推广并消费；其推广后 `current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE` 是历史交接状态。R01 入口面已接受，R02 已完成 docs-only 核验但因缺少 safe fixed tool 与 release-specific `PackageToolDefinitionV1`/Manifest/Lock binding 阻断；当前结果由本文末最新 R02 镜像定义。

## 12. [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / ORIGINAL R01 / FORMALLY CLOSED / PRESERVED] 当前 Stage 5 R01 受控执行合同证据验收结果

产品目标回读和范围扩张审计均为 `PASS`。Stage 5 仍为 `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`。R01 的验收要求每个 case 均有独立、可观察、由 WorkBuddy 原生提供的 bundled-script invocation/tool event；event 必须证明真实相对脚本调用并原生捕获 stdout、stderr、最终 exit、cwd 和 timeout。模型文字、自报、重复 JSON、marker 匹配或推断不能替代。

```text
task_id: V2-S5-R01-WORKBUDDY-EXECUTION-CONTRACT-EVIDENCE1
task_kind: CONTROLLED_CLIENT_EVIDENCE + DOCS_ONLY_CLOSEOUT / ZERO_PRODUCT_STATE_CHANGE
user_authorization: 2026-08-22 / Stage5继续执行、每个子任务独立审核、边界审计和产品目标回读
base_commit: d0a055689e9fc928a31edb24f3740e9408e123ef
base_tree: 50197a1eb103ffad42ac3e2952dcd3f9761a9512
base_parent: 2207c9083ceabcf6539936e47b0935a4eaa77c46
tracked_files_at_base: 40
initial_product_goal_recheck: PASS
scope_expansion_audit: PASS
official_sources: 134432 WorkBuddy Skills; 134391 local AI workbench task bar; 134324 update notes; 134516 CodeBuddy PRODUCT_MISMATCH_NOT_CONTRACT_PROOF
workbuddy_version_observed: 5.3.14
baseline_installed_skills: 2 / agent-browser; find-skills
temporary_probe_zip: r01-controlled-probe.zip / sha256 C55C90B7E86E9399F04EF13B8D78DF9228A8D72F7149B5B2A11B4362320F102D / DELETED_AFTER_REVIEW
temporary_probe_skill_sha256: D1BE59EF9221BA739482555744385244C86B771F5604DB738F5E0952CCC1E1E1 / HASH_ONLY_SOURCE_DELETED_AFTER_REVIEW
temporary_probe_script_sha256: 52B1F6283FF376F99DE49AE87EF24781042DC12F679AAAF7F976F58F19307064 / HASH_ONLY_SOURCE_DELETED_AFTER_REVIEW
client_safety_scan: NOT_SKIPPED / AUTO_INSTALL_ACCEPTED / installed count 3 / exact probe identity
controlled_task_model: HY3 / NEVER_AUTO
native_bundled_script_invocation_event: ABSENT / Bash-PowerShell-only path exposed
coordinator_stop: BEFORE_ANY_SHELL_OR_TERMINAL_EXECUTION
probe_script_execution: NOT_RUN
stdout_stderr_exit_cwd_timeout_evidence: NONE
nonzero_case: NOT_RUN
timeout_case: NOT_RUN
r01_result: BLOCKED_EXTERNAL_CONTRACT
r01_result_review: APPROVE / P0=0 / P1=0 / P2=0 / FORMALLY_FAST_FORWARDED_TO_ORIGIN_CODEX_WORKBUDDY_SHELL_V2 / COMMIT=9eefe8600d9bed0c8ea6024880e4b2d2ef4e3bfc
r02_r08_status: NOT_STARTED / NOT_AUTHORIZED_BY_CHAIN
temporary_skill_cleanup: COMPLETE / USER_UNINSTALLED_TEMPORARY_SKILL / WORKBUDDY_INSTALLED_SKILLS_2 / TASK_HISTORY_RETAINED / BASELINE_SKILLS_2_UNTOUCHED
baseline_skill_cleanup: NOT_TOUCHED / TWO_RETAINED_SKILLS
temporary_probe_cleanup: COMPLETE / EXACT_ISOLATED_WORKTREE_FOLDER_AND_ZIP_DELETED / GIT_STATUS_CLEAN
candidate_test: NOT_RUN_DOCS_ONLY
```

R01 的阻断不改变五类 Stage5 总体验收门，也不构成 Stage5 PASS。独立 Reviewer 已 `APPROVE / P0=0 / P1=0 / P2=0`，该结果已正式 fast-forward；用户已卸载临时 Skill，WorkBuddy 显示安装技能数为 `2`，任务历史保留，probe folder/ZIP 已删除。R02-R08 严格停止；不运行 nonzero/timeout，不把上传/安装、旧客户端历史或模型输出当作真实脚本、Launcher 或 receipt 证据。Provider、媒体、最终 Package、Stage4 spawn 和 Stage6 均未运行。

## 13. [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT] 当前 Stage 5 R01 Sandbox Refresh1 受控客户端正式结果镜像（2026-08-22）

本节独立于原始 R01 已关闭记录；旧记录不改写。官方 134420 明示 enterprise Skill scripts 在客户端沙箱执行。受控 WorkBuddy 客户端观察将 PowerShell 记录为 `ELIGIBLE_CANDIDATE_SURFACE`，不是官方精确执行合同；不能再以“PowerShell 非原生/只暴露 shell”阻断。134432 证明脚本/工作流封装、上传和调用形态；134516 为 CodeBuddy `PRODUCT_MISMATCH_NOT_CONTRACT_PROOF`。剩余合同缺口是 bundled-relative resource resolution、Skill-root cwd，以及 stdin/stdout/stderr/final-exit/timeout 精确语义。

```text
task_id: V2-S5-R01-WORKBUDDY-SANDBOX-REFRESH1
candidate_branch: codex/v2-s5-r01-sandbox-refresh1-closeout
base: 932bcabc5baf90d0190101b1039e4ccf087b2b08 / tree 2ed2cd0e67dd8628b7f0b1acf84df0a7d8b0d0fd / tracked 40
goal_and_scope: product_goal_recheck=PASS / scope_expansion_audit=PASS / WorkBuddy唯一Agent-user入口 / fixed CLI仅唯一Skill内部桥梁
client: WorkBuddy 5.3.14 / baseline=agent-browser,find-skills / HY3 / NEVER_AUTO
probe: ISOLATED_D_DRIVE_TEMP_ROOT / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / CLEANUP_COMPLETE / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
hashes: SKILL=A369E89912B51C1627C972A7DE8F82111E55E2909622CB2E0E3276B45331FFF9 / SCRIPT=8A1D38A65945CC99C4B7F8EE95FDF4FF744D105303BC9904E5915E630DF58359 / ZIP=2284E6D6FE8FFD38689A357DD0A6653CEB23B923F0C531BF9EAC376178E9A28A
install: SAFETY_SCAN_NOT_SKIPPED / NO_NON_HIGH_RISK_AUTO_INSTALL_SELECTED / INSTALLED_COUNT_3 / client_id=workbuddy-skill-1787379691395 / SKILL_MD_NO_METADATA_NAME / BODY_FIRST_LINE_MATCHED_PROBE
native_read: PRESENT / SKILL_MD_AND_scripts\\r01_contract_probe.py_READ / PHYSICAL_INSTALL_PATH_EXPOSED_CONTRACT_DEVIATION_SENSITIVE_MINIMIZATION_FAILURE / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
frozen_success: relative=.\\scripts\\r01_contract_probe.py / SESSION_WORKSPACE_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / NO_CD_NO_ABSOLUTE_PATH_NO_GUESSING_NO_COMMAND_MUTATION / Skill-root-cwd=NOT_EXPOSED / bundle-relative=NOT_EXPOSED
execution: POWERSHELL_NOT_STARTED / USER_CANCELLED / no script, stdout, stderr, final exit, cwd classification or timeout evidence
result: BLOCKED_EXTERNAL_CONTRACT / MISSING_SKILL_ROOT_CWD_AND_BUNDLE_RELATIVE_RESOLUTION / NOT_BECAUSE_POWERSHELL_IS_NON_NATIVE
review: APPROVE / P0=0 / P1=0 / P2=0 / independent Reviewer
reviewer_independent_observation: WORKBUDDY_5.3.14 / HY3 / USER_CANCELLED / NO_SUCCESS_STDOUT_STDERR_EXIT_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
nonzero_timeout: NOT_RUN / R02-R08_NOT_STARTED_NOT_AUTHORIZED_BY_CHAIN
temporary_skill: UNINSTALLED / USER_UNINSTALLED_TEMPORARY_SKILL / TEMP_SKILL_ID=workbuddy-skill-1787379691395_NOT_IN_INSTALLED_LIST / WORKBUDDY_MY_INSTALLED_SKILLS_2=agent-browser,find-skills / TASK_HISTORY_RETAINED / BASELINE_SKILLS_UNTOUCHED / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
computer_use: LOW_IMPACT_OPERATIONAL_ANOMALY / EXPLORER_MISTAKEN_FOR_FILE_PICKER / ALT+N_MAY_OPEN_TAB_OR_WINDOW / NO_PATH_INPUT_NO_FILE_SELECTION_NO_WRITE_DELETE / STOPPED_AND_RECOVERED
accepted_result: 6c20371f1c72ee9d55147e1ad7feb8ede201858f / tree 9eb4643f09d03cc9f39b0b46906773e5bcc9125d / docs_review=APPROVE_P0_0_P1_0_P2_0
candidate_state: current_task=NONE / NO_ACTIVE_TASK / R01_REFRESH1_ACCEPTED_BLOCKED_EXTERNAL_CONTRACT / next_authorized_task=NONE / R01_REMAINS_BLOCKED / ONLY_SEPARATE_R01_REOPEN_AUTHORIZATION_PLUS_ACCEPTED_SUCCESS_CONTRACT_EVIDENCE_CAN_UNLOCK_R02_R08
test_and_scope: NOT_RUN_DOCS_ONLY / product_code=0 / tests=0 / ci=0 / Provider-media-Package-Stage4-Stage6=0
```

该候选继续保持 Stage5 `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`，不形成 Stage5 PASS；不运行 nonzero/timeout，不启动 R02-R08，不创建或运行 Provider、媒体、Package、Stage4、Stage6 或生产流程。

## 14. [HISTORICAL / CONSUMED_BY_V2-S5-R02] 当前 Stage 5 R01 验收契约纠正（2026-08-22）

原始 R01、Sandbox Refresh1 和 Expert Entry Feasibility 记录均为 `HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT`；其旧 `BLOCKED_EXTERNAL_CONTRACT`/`INCOMPLETE` 事实与裁决保留。本节是用户基于最初产品目标作出的项目验收归属纠正，不是新官方证据，也不宣称脚本或 Launcher 已执行。

| R01层 | 当前裁决 | 证据边界 |
|---|---|---|
| 入口面 | `ENTRY_SURFACE_ACCEPTED` | 只接受 Skill 包装、上传、安装、身份出现、选择命中、客户端 sandbox scripts 与 PowerShell `ELIGIBLE_CANDIDATE_SURFACE` |
| 执行面 | `EXECUTION_PROOF_DEFERRED_TO_R03_R07` | Skill-root cwd、bundle-relative、stdin/stdout/stderr/final-exit/timeout 不再是 R01 硬门，但仍未证明；实现链 `Locator -> fixed PowerShell/private CLI -> LauncherReceipt` 归 R03/R07 |
| 真实结果 | `NOT_PROVED` | 不伪造脚本执行、stdout/stderr/exit/cwd/timeout、LauncherReceipt 或 Stage5 PASS |

```text
task_id: V2-S5-R01-ACCEPTANCE-CONTRACT-CORRECTION1
task_kind: DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE / USER_AUTHORIZED_ACCEPTANCE_CORRECTION
hy3_policy: CURRENT_TEST_MODEL_ONLY / COST_AVOIDANCE / PRODUCT_MODEL_NEUTRAL / USER_SELECTED_MODEL / NOT_A_SKILL_OR_EXPERT_OR_SYSTEM_DEPENDENCY
client_test_policy: AUTHORIZED_CLIENT_TESTS_FOLLOW_USER_HY3_AND_NEVER_AUTO / PRODUCT_MODEL_NOT_LOCKED
preserved_boundaries: ONE_WORKBUDDY_SKILL_AND_ONE_USER_ENTRY / FIXED_CLI_INTERNAL_BRIDGE_ONLY / NO_ARBITRARY_CLI / NO_PATH_GUESSING / NO_SCAN / NO_PATH_FALLBACK / NO_MCP / NO_SECOND_SKILL / NO_SECOND_AGENT / NO_ROUTER / NO_RETRY / NO_REPLAY / FINAL_SKILL_INSTALLER_STAMPED_LOCATOR
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
current_task: HISTORICAL / NONE / NO_ACTIVE_TASK / R01_CORRECTED_ACCEPTED_ENTRY_SURFACE
next_authorized_task: HISTORICAL / V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1 / R02_AUTHORIZED_ONLY / R03-R08_NOT_AUTHORIZED_BY_CHAIN
```

## 15. 当前 Stage 5 R02 Package Release/Tool Definition Binding1 收口（2026-08-22）

R02 的 published candidate 身份已核验匹配，但不能作为 bindable final Release：远程递归树 `truncated=false`、`2614` entries，绑定相关路径为 `0`；本地同树不可变审计为 `2155` blobs。`GOLDEN_KEY_OPENMONTAGE_RELEASE.json` 仅有 `release_version=0.3.24`、`console_script_entrypoint=null`、`python_load_probe=lib.pipeline_loader:load_pipeline`、`authority_entry=README.md`；lock 没有 `PackageToolDefinitionV1`、`workbuddy_entry_cli`、`package_tool_definition`、`launcher`、`fixed_tool` 或相应顶级字段。不得从媒体工具中随意挑选，不造 fixture/definition，不改外部 Package。

```text
task_id: V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1
published_candidate: blazingcd/golden-key-openmontage / codex/golden-key-openmontage-v0.3.24 / published_commit=ef5f5b58fa1c2b494b0154989cf0e4e36615a701 / published_root_tree=0464861c5985c7c9072e789b94889d29cf9a937a / approved_source_commit=8395e578165e802990d53fef5a166f8b4cf0461a / approved_source_commit_tree=4624394238802a9577690248e43b8f0dff391a2b / approved_source_package_subtree=0464861c5985c7c9072e789b94889d29cf9a937a
r02_result: BLOCKED_PACKAGE_RELEASE / PUBLISHED_CANDIDATE_IDENTITY_VERIFIED / MISSING_SAFE_FIXED_TOOL_AND_RELEASE_SPECIFIC_DEFINITION
current_task: NONE / NO_ACTIVE_TASK / R02_CLOSED_BLOCKED_PACKAGE_RELEASE
next_authorized_task: NONE / PACKAGE_OWNER_RELEASE_BINDING_REAUTHORIZATION_REQUIRED / R03-R08_NOT_AUTHORIZED_BY_CHAIN
unblock_condition: SEPARATE_PACKAGE_OWNER_APPROVAL_AND_INDEPENDENT_SAFE_FIXED_TOOL_DEFINITION_MANIFEST_LOCK_VERIFICATION / THEN_REAUTHORIZE_R02
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
product_goal_anti_expansion: PASS / WorkBuddy_ONLY_AGENT_USER_ENTRY / FIXED_CLI_ONLY_SOLE_SKILL_INTERNAL_BRIDGE / NO_ARBITRARY_MEDIA_TOOL_SELECTION_OR_FIXTURE_OR_DEFINITION_OR_EXTERNAL_PACKAGE_MODIFICATION
```

## 项目级架构纠偏审计 Phase A 验收镜像（A7 docs-only 已正式推广，2026-08-22）

本节是 A0-A6 独立审查批准后的当前验收边界。A7 docs-only 结果已正式推广；它不把审计完成写成产品纠偏完成，不覆盖历史证据，也不改变 R02 live 状态。

```text
task_id: V2-PROJECT-ARCHITECTURE-RECOVERY-PHASE-A1
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_baseline_parent: f338d9d50cad2cccf1398438ad4a8c8d45127a21 / tree 5ef5e8e524412f6220ad31f2cc38448c6b1dac8b
phase_a_audit_commit: 4727c5efda6ae53194ff2c16dd224c67178e8d8d
phase_a_audit_tree: ac6206950b36f71663eddfb89b7e311aa85b53e6
phase_a_status: A0-A6_APPROVED / A7_DOCS_FORMALLY_PROMOTED
scope: EXACT_SIX_EXISTING_AUTHORITY_FILES / DOCS_ONLY
effect: ZERO_PRODUCT_STATE_CHANGE
review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_ZERO_WRITE
formal_promotion: ORDINARY_FAST_FORWARD / FORMALLY_PROMOTED / commit=4727c5efda6ae53194ff2c16dd224c67178e8d8d / tree=ac6206950b36f71663eddfb89b7e311aa85b53e6 / ci_run=32615371879 / completed=success / headSha=4727c5efda6ae53194ff2c16dd224c67178e8d8d
task_artifacts_cleanup: ORIGINAL_PHASE_A_WORKTREE_LOCAL_AND_REMOTE_TASK_BRANCH_CLEANED
state_closeout: THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR
verification: GIT_DIFF_CHECK_ONLY / NOT_RUN_DOCS_ONLY
phase_b: NOT_AUTHORIZED / A7_HISTORICAL_SNAPSHOT
```

### 历史证据与当前架构处置必须分栏

| Stage | 历史合同/证据字段 | 当前架构验收字段 | 处置 |
|---|---|---|---|
| Stage 1 | 六模块、唯一 Agent 边界历史接受 | 与目标一致 | `KEEP` |
| Stage 2 | Registration/Locator 与临时 assembled-Package proof 接受 | 不等于 final Package/production Registration | `KEEP_WITH_NARROWING` |
| Stage 3 | bounded optional capability preparation 接受 | 不拥有必带 Python/FFmpeg/Node，也不选 Renderer/Provider | `KEEP_WITH_NARROWING` |
| Stage 4 | `PackageToolDefinitionV1`、固定 spawn、Receipt、测试/CI 历史通过 | 仅机械合同通过，真实产品架构与 WorkBuddy 未证明 | `HISTORICAL_PASS_ONLY` |
| Stage 5 | entry-code/static layer delivered | final PackageRoot、Installer、Guide-read、真实 receipt/E2E 缺失 | `REWORK` |
| Stage 6 | later relay boundary design only | 直接复用 Receipt 的前提不足 | `INSUFFICIENT_EVIDENCE` |

### 目标与需求分类验收

```text
unique_WorkBuddy_Agent_and_six_module_Shell: FULFILLED_AND_RETAIN
ordinary_natural_language_user_entry: FULFILLED_BUT_NARROW / REAL_CLIENT_NOT_PROVED
OpenMontage_Guide_drives_WorkBuddy_production_decisions: UNPROVED / REWORK_REQUIRED
Stage2_registration_locator: FULFILLED_BUT_NARROW
Stage3_optional_capabilities: FULFILLED_BUT_NARROW
final_PackageRoot_Installer_private_toolchain: DEFERRED_WITH_VALID_OWNER / UNPROVED
Stage4_mechanical_contract: FULFILLED_BUT_NARROW / HISTORICAL_PASS_ONLY
Stage5_real_WorkBuddy_Artifact_and_business_E2E: PARTIAL / UNPROVED
Stage6_receipt_relay: INSUFFICIENT_EVIDENCE
R02_attribution: MISASSIGNED_TO_WRONG_LAYER
old_Stage2_branch_and_old_R03_R05: SUPERSEDED_WITH_VALID_REASON
```

### 真实集成验收顺序

```text
Registration_identity_validation
 -> Locator_verified_PackageRoot_and_Guide_identity_hash
 -> WorkBuddy_reads_Guide_Manifest_Pipeline_Stage_Skills
 -> WorkBuddy_makes_production_decisions
 -> one_fixed_internal_CLI_transport
 -> one_deterministic_fixed_child_tool
 -> immutable_LauncherReceipt_mechanical_facts
 -> WorkBuddy_presents_Artifact_result
```

必需证据是独立可见的 WorkBuddy/client Guide-read event 或同等权威客户端记录、匹配的 Guide identity/hash、固定 child source/hash/argv/cwd/stdin/stdout/stderr、`spawn=1`、`retry=0`、真实 receipt/Artifact，以及独立 Reviewer 对 exact commit/tree、Git 和 CI headSha 的核验。模型自报、child 自报、普通日志、静态代码、单元测试、CI、Skill 被识别、CLI 能启动或生成 receipt 均不能单独证明真实 WorkBuddy 生产。

最终 Package 必带 Node.js `22+`、npm、npx 和其他必需 private toolchain；Stage 3 不探测、下载或替换 Node/npm/npx。Optional Remotion/HyperFrames 仍是显式授权能力，不改变 Shell 六模块边界。

### R02 binding 验收归属

```text
r02_live_status: R02_CLOSED_BLOCKED_PACKAGE_RELEASE
recommended_reclassification: SHELL_INSTALLER_ADAPTER_BINDING_REQUIRED + REAL_FIXED_CHILD_UNVERIFIED
recommended_reclassification_state: NOT_YET_EFFECTIVE
binding_delivery_owner: V2 Final-delivery Installer / Release Assembly Owner
binding_carrier: FINAL_WORKBUDDY_PACKAGEROOT / INDEPENDENT_SHELL_ADAPTER_SUBTREE
shell_owns: BINDING_SCHEMA_AND_CONSUMER
0_3_25: IMMUTABLE / NO_WORKBUDDY_ADAPTER_EMBEDDING
```

本历史 A7 方案正确保留了“不能修改共享 Package、0.3.24 只作历史证据”的边界，但其 adapter/fixed-child 验收合同已被 2026-08-24 重基线取代；当前接口和装配验收以 TASK-REGISTER 末尾为准。

### [HISTORICAL / SUPERSEDED_BY_2026-08-24_REBASELINE] B01-B07 纠偏任务验收门

下表只保存 A7 当时的 B01-B07 验收门，已无执行效力；当前验收任务为本文件末尾及 TASK-REGISTER 末尾的 C01-C07。

| Gate | 必须证明 | 不能证明/失败处置 |
|---|---|---|
| B01 | binding owner/carrier、Guide-read 顺序、可观察证据、第二控制面禁止条件 | 缺字段或职责冲突则 `BLOCKED`，不改代码 |
| B02 | 一个 Skill、一个固定 transport、一个 deterministic child、无第二 Agent/Router/MCP/retry/replay | 任何并行入口、用户技术参数或导演逻辑则 `FAIL_CLOSED` |
| B03 | final PackageRoot、private toolchain（含 Node 22+ npm/npx）、adapter、fixed child、Manifest/Lock/hash、生命周期与生产 Registration/Activation | 只有临时 Package、源码 checkout、静态 lock 或无 owner 则 `INCOMPLETE` |
| B04 | fresh install/register/activate、新进程 Locator、Guide-read event、官方 fixed control 的真实 receipt/Artifact | 模型/child 自报或复用旧状态不算证据 |
| B05 | 同一 Shell 路径在固定 0.3.25 上复现 B04 证据 | 同时改 Shell 与 Package、复用 Registration/PackageRoot 或改 0.3.25 则 `BLOCKED` |
| B06 | 五类 Stage 5 证据齐全且独立审查通过 | 只允许 `HANDOFF_TO_B07_ONLY`，不得推广/清理/启动 Stage 6 |
| B07 | 普通自然语言 portrait 业务 Artifact 与独立业务验收 | Core/业务 gate 未过则不推广；Shell 不补媒体逻辑 |

旧 Stage 2 分支 `codex/v2-s2-official-package-alignment-b1`（HEAD `86a7902465d8e215e0830b9640e7222d7c7f5188`）和两个 dirty detached worktree（均 `4d74d6576773dc9d383efec091bdc8d42f0d480c`）只登记、物理保留，不合并、不复制、不删除。本 Phase A 状态镜像保持 docs-only 六文件范围与 `NOT_RUN_DOCS_ONLY`；审计结果已正式推广，上方 `NOT_AUTHORIZED` 与下方 B01-only 都只作历史，当前权威是 2026-08-24 重基线的 `PAUSED_BY_OWNER`。

## [HISTORICAL / SUPERSEDED_BY_2026-08-24_REBASELINE] Phase B 执行镜像：B01 已授权（2026-08-23）

本节只保存 2026-08-23 当时的 B01-only 授权和 package 输入，已被 2026-08-24 重基线取代，不提供当前执行授权。

```text
phase_b_authorization: USER_AUTHORIZED_2026-08-23 / B01_ONLY
current_task: B01 / CURRENT_DOCS_ONLY_CONTRACT_FREEZE
b01_scope: FREEZE_BINDING_GUIDE_READ_CONTRACT + PACKAGE_INPUT_MIGRATION + AUTHORIZATION_MIRROR
b01_effect: ZERO_PRODUCT_STATE_CHANGE / DOCS_ONLY
b01_not_do: NO_PRODUCT_CODE_EXECUTION_OR_B02_B03_B04_B05_B06_B07_EXECUTION / NO_PACKAGE_OR_EXTERNAL_REPO_CHANGE / NO_CLIENT_SKILL_REGISTRATION_ACTIVATION_PROVIDER_MEDIA_DATAROOT
b01_tests: NOT_RUN_DOCS_ONLY
official_current_input: checkout=D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-main-cd9f3c1f / commit=cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / tree=6cd1961d552dd9d2bcfba990b80ac06edfe4b061 / state=DETACHED_CLEAN
golden_key_current_input: release=0.3.25 / checkout=D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673 / commit=73cab67322451601a824875c0e426067d736dd44 / tree=29231e0464fa4bc7533c1928415849e9b3a48e7c / parents=ef5f5b58fa1c2b494b0154989cf0e4e36615a701+cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / state=DETACHED_CLEAN
historical_only_inputs: official_old=4eab34c5cfcccaa4f1970554928feccce73ee930,95e1c3d0ab93482159818560f6a8c8e866b9139f / Golden_Key_0.3.24=ef5f5b58fa1c2b494b0154989cf0e4e36615a701 / provenance_only / NEVER_FUTURE_CALL_OR_VERIFY
b01_result: THIS_COMMIT
b01_review_gate: INDEPENDENT_ZERO_WRITE_APPROVE_REQUIRED / NO_RESULT_PREWRITTEN
b01_repository_delivery_resolution: INDEPENDENT_ZERO_WRITE_APPROVE + LIVE_FORMAL_REF_CONTAINS_THIS_COMMIT + EXACT_HEAD_CI_SUCCESS
next: B02_ONLY_IF_B01_DELIVERED
b02_b07: BLOCKED_BY_CHAIN
builder_boundary: NO_FORMAL_PROMOTION
```

## [HISTORICAL / SUPERSEDED_WHEN_D_ROUTE_CANDIDATE_IS_FORMALLY_PROMOTED] 重基线验收矩阵（2026-08-24）

| 对象 | 历史事实 | 当前裁决 | 可复用边界 |
|---|---|---|---|
| Phase A A0 | exact formal base、独立分支/worktree 与残留对象被记录 | `KEEP_PROCEDURAL_FACTS / REVIEW_EVIDENCE_GAP` | 保留 Git 身份；不能推导 A1-A6 正确 |
| Phase A A1 | 唯一 WorkBuddy Agent、六模块 Shell、自然语言目标重建正确；原 formal 缺完整矩阵，本重基线已在 TASK-REGISTER 补齐 | `KEEP_TARGET / ORIGINAL_INCOMPLETE_CLOSED_BY_REBASELINE` | 后续必须按新矩阵逐项验收，不得恢复旧 fixed-child 计划 |
| Phase A A2 | Stage 1/2 薄 Shell 与临时 Package 证据缩小正确 | `PARTIAL_KEEP` | 遗留 Git-checkout 分支整体不合入；其中 stable-handle/reparse 思路仅列独立 hardening 候选，不进入本纠偏主链 |
| Phase A A3 | Optional Remotion/HyperFrames 不由 Shell 选型的边界正确 | `KEEP_WITH_NARROWING / AUDIT_GAP_CLOSED_NOW` | 两个 dirty worktree 是旧 Stage3 计划迭代，已被正式 Stage3 实现/合同取代；继续只读保留 |
| Phase A A4 | 区分机械合同 PASS 与产品架构 PASS 是对的 | `HISTORICAL_PASS_ONLY / CORE_QUESTION_UNRESOLVED` | `launch_session_tool` 最多保留为一次工具调用原语；不得把一次 spawn 当作完整用户请求 |
| Phase A A5 | 识别 Stage5 真实集成缺口、R02 错层和 Stage6 前提不足 | `PARTIAL_KEEP / INHERITED_UNRESOLVED_ASSUMPTION` | 撤销 fixed-child 整体主链 |
| Phase A A6 | 找到了职责和证据分层，但首次把未证假设写成 B 计划 | `EARLIEST_EXPLICIT_WRONG_PLAN / SUPERSEDED` | 旧 B01-B07 不再授权执行 |
| Phase A A7 | 六份文档已审查、推广 | `PROMOTION_VALID / CONTENT_SUPERSEDED` | 保留 Git/审查事实，不再执行旧 B01-B07 计划 |
| B01 | docs-only 合同提交存在 | `HISTORICAL / SUPERSEDED` | 仅保留 exact package identity 与禁止第二控制面 |
| B02 | Bridge/Skill 单测与机械 schema 存在 | `NOT_PRODUCT_ACCEPTED` | 可读作实现证据；不得作为后续基线直接补丁式修复 |
| B03 | assembly、toolchain、Registration/Activation、Locator、lifecycle 可重复证据存在 | `KEEP_WITH_NARROWING` | 复用装配基础设施；最终 Skill/Bridge binding 与 placeholder gate 重做 |
| B04 | 三次真实 WorkBuddy 尝试均未产生有效 Shell receipt/Artifact | `INCOMPLETE` | 作为失败机制证据；直接策划文件仅为 WorkBuddy fallback |

未来验收必须同时满足：

| Gate | 必须可独立观察 | 失败条件 |
|---|---|---|
| 产品入口 | 普通自然语言、一个 Skill、无技术路由提示 | 用户/模型需提供 Python、路径、hash、schema、JSON 或脚本 |
| Agent-first | WorkBuddy 读取 exact Guide、manifest、Stage Skills，并据此逐阶段决策 | 只读 Skill、只启动 Bridge、只产生 receipt，或固定 child 替代原生流程 |
| Shell 边界 | 同一 verified session 提供定位、运行时、工具调用和机械结果 | Shell 选择 Pipeline/Stage/Provider/Renderer，或出现第二控制面 |
| WorkBuddy 兼容 | 宿主可保留自己的沙箱环境；child 环境由 Shell 收敛 | 因宿主额外环境变量直接拒绝，或要求绕过 WorkBuddy 安全逻辑 |
| 真实结果 | OpenMontage tool/Artifact/Checkpoint/Reviewer 链与最终业务产物可关联 | WorkBuddy 直接 fallback、mock、self-report 或无 provenance 的文件 |
| 证据与推广 | 每步目标回归审计、独立零写审查、exact Git/package/client evidence | 缺项、状态台账滞后、越界修补或未授权推广 |

当前验收状态固定为 `PAUSED_BY_OWNER / REBASELINE_DOCS_ONLY / NO_PRODUCT_PASS`。

## 新任纠偏 D01-D08 候选验收矩阵（2026-08-24）

本候选正式推广后，本文件更早的 C01-C07 `current/next/only` 验收口径立即降为历史；未推广前本节不具 authority。无论哪种状态，任何 Gate 都未被执行或证明。

| Gate | 必须独立证明 | 明确不能证明 | 硬失败/归属 |
|---|---|---|---|
| D01 native surface | 两个 fresh 普通语言 probe session；exact Skill/fixture；固定无害 operation；完整可观察结果；清理状态 | Shell、Package、产品成功 | guessed path、model helper、security bypass 或证据不全即 `BLOCKED_WORKBUDDY_SURFACE` |
| D02 contract | D01 支持的 exact surface；Package-agnostic Skill；hidden binding；WorkBuddy-owned loop；per-operation Shell | 正确代码或 client E2E | 未证接口、whole-request child、model-visible technical binding 即 `REJECT_ARCHITECTURE` |
| D03 implementation | 最小 allowlist；语义 inputs；resource/stage/tool validation；closed child；focused/full/CI | Installer、real WorkBuddy、完整视频 | Shell 作生产决策、技术 JSON、host-env exact-set、fallback 即 `REJECT_PRODUCT_CODE` |
| D04 Installer | Installer 为仓库版本化产品；确定性装配/迁移/回滚/卸载；private toolchain；不可变 Package | fresh final assembly 或 client success | 只存在临时脚本、修改 Package、Skill 被 stamp 即 `REJECT_INSTALLER` |
| D05 assemblies | fresh official/GK roots、Lock/hash、Registration lifecycle；同一 Package-agnostic Skill ZIP；零 Package 写入 | WorkBuddy/视频成功 | 旧状态复用、Skill 字节不同、binding 暴露给模型即 `REJECT_ASSEMBLY` |
| D06 official control | exact `cd9f3c1f`；两次普通提示；用户 Pipeline；完整 Guide/Stage/tool/review/checkpoint/video lineage；playable local video | GK 或真实门店质量 | `framework-smoke`、首个 Artifact 止步、direct fallback、验收期修复即 `INCOMPLETE_OFFICIAL` |
| D07 GK comparison | exact `73cab673`；D06 非 Package 输入逐字节不变；只换 immutable Package-owned authority 与 derived binding；每个 Package 下由 WorkBuddy 按其 Guide 选择正确用户 Pipeline；两次完整成片 | 业务质量或规模 | 任一非 Package 第二变量、强制 Pipeline ID 相同、0.3.24、Package mutation、证据复用即 `INCOMPLETE_GK` |
| D08 business/closeout | 普通门店请求、正确 GK Pipeline、distinct human/provider/cost gates、portrait 视频、业务验收、六文档 closeout 与 exact cleanup manifest | 正式推广或全场景规模 | 技术提示、Shell 媒体修补、未授权花费、假 PASS、推广/删除即 `REJECT_CLOSEOUT` |

每个 Gate 还必须同时满足对应 21 字段与逐任务补充合同，并在实际执行后逐题通过十问 `EXECUTION_GATE`。未来 commit/tree、client build 或 evidence manifest 不能预先伪造，必须标为 `NOT_PROVED_FUTURE_INPUT` 并在接管时解析为完整 identity，否则任务不启动。规划中的未知事实只能作为当前任务的 fail-closed 输出，不能预写为 PASS；执行中的任何所需事实为 `NOT_PROVED` 都阻断当前 Gate 和下游。Worker 与 Reviewer 必须不同，Reviewer 零写；失败回到 named owner，下一任务不是修复窗口。

当前候选状态是 `PLAN_CANDIDATE_ONLY / NOT_RUN_DOCS_ONLY / NO_PRODUCT_PASS / NO_EXECUTION_AUTHORITY`。Reviewer 通过只能证明上述验收设计未发现 P0/P1，不证明任何 D Gate 已完成。
