# WorkBuddy Shell V2 验收矩阵

状态：`STAGE_1_PASS_ACCEPTED / SIX_MODULE_MVP`

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
| 会话Launcher | 用阶段2必带工具链事实启动固定入口；所选可选能力执行前另有对应阶段3就绪事实；返回真实退出码、结果指针和残留事实 | 绕过相应就绪检查；启动第二Agent；接受任意Shell；多进程调度；自动重试；进入Package生产业务；创建Artifact或推进Checkpoint |
| WorkBuddy入口 | 真实新会话显式命中唯一入口，literal用户消息不变，并绑定活动执行包与Runtime | 多套生产入口；全局截获；第二聊天Agent；技术控制词进入用户消息或Shell作生产选择 |
| 状态与结果转交 | 直接转交Runtime计划/准备事实与Launcher回执并零代码退出，或只做一次有消费者证明的确定性格式转换；事实可追溯且不改写WorkBuddy语义 | 无格式缺口仍造模块；安装Runtime；建立数据库/轮询/流式平台或Stage/FSM；解释Artifact；自动重试或伪造成功 |

### 3.1 阶段3至阶段6缩减Gate

阶段编号是建设与验收顺序`3 -> 4 -> 5 -> 6`，不是最终用户运行顺序。阶段4可依据阶段2必带工具链事实启动基础固定工具；阶段3独立有界探测Remotion和HyperFrames，能力存在则复用，缺失/不兼容则询问用户是否集成。OpenMontage只从实际可用能力中决定生产选择。

阶段3结果闭集为`DETECTION_REPORT`、`CONSENT_REQUIRED`、`INTEGRATED`、`SKIPPED`和`BLOCKED`。每项能力事实只取`PRESENT/MISSING/INCOMPATIBLE/NOT_INTEGRATED`。缺失、拒绝或暂缓不阻塞Package、项目、最终交付或其他能力；只有无效定义、越界目标或已授权集成失败才可`BLOCKED`。

Python核心依赖、FFmpeg/ffprobe、Node/npm/npx都属于Package必带工具链。阶段2缺少任何一项时是`FAIL`，阶段3不得以宿主PATH、下载或受管目录补救。Node虽然官方Quick Start最低为18+，但当前HyperFrames要求22+，Package锁定值必须满足最高当前要求。

阶段4 `PASS`要求在启动时消费阶段2必带工具链就绪事实，并在执行已选可选能力前消费对应阶段3就绪事实。缺少相应事实必须返回`RUNTIME_NOT_READY`；任何第二Agent启动、自动重试、队列、调度、常驻服务、多Agent或Package业务内部导入均为越界`FAIL`。

阶段5是用户实际运行起点。`PASS`要求唯一Skill在真实WorkBuddy新会话命中，按已冻结映射消费阶段3五种结果，literal `user_message`不变，授权与`executor_controls`分离，并验证用户同意后的同任务继续；若不能自动继续，必须验证固定“继续刚才的任务”提示。入口格式未确认时应记`BLOCKED`，不得同时实现CLI/MCP/多个Skill兜底。

阶段6先验证WorkBuddy能否直接消费Runtime计划/准备事实和Launcher回执：能则记录`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`且生产代码变化为0；不能则必须有精确字段差异和真实消费者证据，只允许一次确定性转换。非零退出、超时、缺少结果指针和残留进程必须保持原事实；阶段6不得安装、解释或重试。

### 3.2 阶段3重新规划Gate

旧Package绑定能力元数据、Registration绑定及零能力零代码模型全部`SUPERSEDED`。当前Stage 3编码启动只需本五文档纠偏完成独立审阅/正式推广，并由live authority授予最新正式Git对象、精确五路径和Reviewer范围；不得增加Package、Registration、Package绑定能力元数据或Stage 5输入Gate。`FINAL_PACKAGE_MATERIALIZED`和`PRODUCTION_PACKAGE_REGISTERED`仍是后续最终交付要求，但不是Stage 3编码前置。

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

阶段3仓库交付只有一个公共入口、五种结果、一套数据驱动的两能力探测/集成事务和阶段4可验证的能力证据。实现不得增加第二个公共入口、独立下载器或后台状态模块。产品实现文件固定为`runtime_prepare.py`、`__init__.py`导出编辑和`test_runtime_prepare.py`；未来同一个已授权Builder必须同步更新现有`test_repository_hygiene.py`和`.github/workflows/ci.yml`，使最终tracked白名单、公共导出断言和唯一CI pytest命令覆盖Stage 3。这两项是验收基础设施，不增加产品模块或产品行为。

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
