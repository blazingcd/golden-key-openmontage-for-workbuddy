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
| Runtime按需准备 | 只消费绑定生产Registration和Package-owned Lock的已选Remotion或HyperFrames要求；discover/plan零写入；用户确认后从批准大陆镜像只准备该能力及其锁声明附属资产；二次调用零下载复用；向阶段4返回身份绑定回执 | 最终Package/生产Registration不存在仍实现；扫盘；Shell-owned重复Lock；发现/下载/替换必带Python/FFmpeg/Node；同时安装全部可选能力；通用下载/包管理/repair；自动海外源回退；修改系统PATH/注册表；Shell或普通用户替OpenMontage选择渲染器 |
| 会话Launcher | 用阶段2必带工具链事实启动固定入口；所选可选能力执行前另有对应阶段3就绪事实；返回真实退出码、结果指针和残留事实 | 绕过相应就绪检查；启动第二Agent；接受任意Shell；多进程调度；自动重试；进入Package生产业务；创建Artifact或推进Checkpoint |
| WorkBuddy入口 | 真实新会话显式命中唯一入口，literal用户消息不变，并绑定活动执行包与Runtime | 多套生产入口；全局截获；第二聊天Agent；技术控制词进入用户消息或Shell作生产选择 |
| 状态与结果转交 | 直接转交Runtime计划/准备事实与Launcher回执并零代码退出，或只做一次有消费者证明的确定性格式转换；事实可追溯且不改写WorkBuddy语义 | 无格式缺口仍造模块；安装Runtime；建立数据库/轮询/流式平台或Stage/FSM；解释Artifact；自动重试或伪造成功 |

### 3.1 阶段3至阶段6缩减Gate

阶段编号是建设与验收顺序`3 -> 4 -> 5 -> 6`，不是最终用户运行顺序。旧“阶段3先检查所有Runtime再进入阶段4”的链路已失效：阶段4可依据阶段2必带工具链事实启动固定工具；WorkBuddy/OpenMontage锁定可选渲染能力后，只有该能力缺失时才调用阶段3。

阶段3结果闭集为`NO_OPTIONAL_CAPABILITY_REQUIRED`、`READY_REUSED`、`CONSENT_REQUIRED`、`READY_PREPARED`和`BLOCKED`。没有可选能力要求或所选能力已就绪时零下载；所选Remotion或HyperFrames缺失时形成只针对该能力及Package-owned Lock声明附属资产的计划，用户确认后按锁准备。不得把另一渲染器或未声明浏览器顺带安装。

Python核心依赖、FFmpeg/ffprobe、Node/npm/npx都属于Package必带工具链。阶段2缺少任何一项时是`FAIL`，阶段3不得以宿主PATH、下载或受管目录补救。Node虽然官方Quick Start最低为18+，但当前HyperFrames要求22+，Package锁定值必须满足最高当前要求。

阶段4 `PASS`要求在启动时消费阶段2必带工具链就绪事实，并在执行已选可选能力前消费对应阶段3就绪事实。缺少相应事实必须返回`RUNTIME_NOT_READY`；任何第二Agent启动、自动重试、队列、调度、常驻服务、多Agent或Package业务内部导入均为越界`FAIL`。

阶段5是用户实际运行起点。`PASS`要求真实WorkBuddy合同确认的一种显式入口、新会话命中、literal `user_message`不变、授权与`executor_controls`分离。入口格式未确认时应记`BLOCKED`，不得同时实现CLI/MCP/多个Skill兜底。

阶段6先验证WorkBuddy能否直接消费Runtime计划/准备事实和Launcher回执：能则记录`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`且生产代码变化为0；不能则必须有精确字段差异和真实消费者证据，只允许一次确定性转换。非零退出、超时、缺少结果指针和残留进程必须保持原事实；阶段6不得安装、解释或重试。

### 3.2 阶段3重新规划Gate

上一版阶段3入口、Shell-owned全闭集Runtime Lock、实现文件白名单和直接验收矩阵均为`SUPERSEDED`。新实现Gate必须同时证明：`FINAL_PACKAGE_MATERIALIZED`、`PRODUCTION_PACKAGE_REGISTERED`、新进程Locator成功、Package-owned能力Lock被Manifest覆盖、真实WorkBuddy消费者合同已冻结、最新正式Git对象和精确Builder白名单获授权。缺一项必须以`INCOMPLETE_STAGE_3_INPUT`零代码退出。

新阶段3最多一个公共入口`prepare_optional_capability(...)`、一个新生产模块、一个导出编辑和一个直接测试文件；不得新增Shell Runtime Lock。直接验收必须覆盖：

1. 无能力要求返回`NO_OPTIONAL_CAPABILITY_REQUIRED`，零下载/零写入；
2. 只检查已选能力，另一渲染器零触碰；
3. Lock未声明浏览器时浏览器零触碰；
4. 无确认只返回绑定版本、镜像、hash、大小、许可证、目标和`plan_sha256`的`CONSENT_REQUIRED`，零写入；
5. Registration、Lock或计划身份变化使旧确认失效；
6. 只使用批准大陆镜像，禁止自动海外回退；
7. 外来目标保留，hash/大小/许可/来源/能力失败全部回滚并清理；
8. 二次调用返回`READY_REUSED`且零下载；
9. 必带Package工具链、Manifest、Registration和另一能力零修改；
10. `READY_PREPARED`回执精确绑定Registration、能力Lock、runtime root、入口和版本证据；
11. 阶段4拒绝过期、跨Package或能力不匹配回执；
12. Shell选择渲染器、自动重放业务请求、扫描盘符、全局npm修改均为零。

证据必须分层：单元/负面测试、本地真实准备、大陆镜像网络验证、真实WorkBuddy消费和视频E2E分别报告；前一层PASS不能替代后一层。

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
