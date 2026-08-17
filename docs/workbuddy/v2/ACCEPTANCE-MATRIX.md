# WorkBuddy Shell V2 验收矩阵

状态：`STAGE_1_PASS_ACCEPTED / SIX_MODULE_MVP`

## 1. 状态必须独立报告

| 状态 | 含义 | 不能由什么代替 |
|---|---|---|
| `SHELL_INSTALLED` | Shell和Skill进入受支持安装位置 | ZIP构建成功 |
| `OBJECT_IDENTITY_VERIFIED` | Shell/OpenMontage 执行包/Release/Manifest/Lock/SHA/安装实例一致 | 文件名、目录名、最新时间 |
| `RUNTIME_BOUND` | 实际PackageRoot、包内私有Python、cwd、DataRoot和闭集组件来源/路径被锁定 | Python包存在、系统PATH命中或doctor文字说明 |
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
| OpenMontage 执行包登记与定位 | 唯一活动Package Registration的身份、hash和规范化路径与实际执行包一致 | 扫盘猜测对象、身份漂移仍继续、修改执行包或执行生产；登记/实现SaaS Core |
| Runtime按需准备 | 包内私有Python身份有效；闭集组件按`managed`/`registered_host`/`PATH_host`/`missing`分类；discover/plan零写入；用户确认后从批准大陆镜像或唯一已验证FFmpeg临时例外准备锁定缺失项；二次调用零下载复用 | 扫盘；扫描或下载Python；首次盲目全装；通用下载/包管理/repair；自动海外源回退；未验证即使用FFmpeg例外；修改系统Python/PATH；Shell选择渲染引擎、版本或生产方案 |
| 会话Launcher | 绑定精确环境，只为WorkBuddy会话调用一次固定工具入口，并返回真实退出码、结果指针和残留事实 | 启动第二Agent；接受任意Shell；多进程调度；自动重试；进入Package生产业务；创建Artifact或推进Checkpoint |
| WorkBuddy入口 | 真实新会话显式命中唯一入口，literal用户消息不变，并绑定活动执行包与Runtime | 多套生产入口；全局截获；第二聊天Agent；技术控制词进入用户消息或Shell作生产选择 |
| 状态与结果转交 | 直接复用Launcher回执并零代码退出，或只做一次有消费者证明的确定性格式转换；事实可追溯且不改写WorkBuddy语义 | 无格式缺口仍造模块；建立数据库/轮询/流式平台或Stage/FSM；解释Artifact；自动重试或伪造成功 |

### 3.1 阶段3至阶段6缩减Gate

阶段3只有两条合法PASS路径：

1. 已验证Package和真实下游合同证明没有额外Runtime缺口，记录`STAGE_3_NO_ADDITIONAL_RUNTIME_REQUIRED`，生产代码变化为0；
2. 对固定闭集执行只读发现，形成只包含缺失/不兼容项的锁定计划；计划完整列出组件、版本、hash、大小、批准源、许可证和目标，用户明确同意后，只实现该计划的prepare、同目录staging、互斥、原子发布与幂等。

固定闭集为Python私有依赖、FFmpeg、Node、Remotion、HyperFrames和锁定浏览器。包内私有Python由阶段2登记，阶段3不得扫描、替换或下载它。发现只允许受管路径、明确登记且重新核验的宿主工具和正常PATH命令解析，不允许盘符扫描。除精确锁定的FFmpeg 9.0 `gyan.dev`临时例外外，Runtime Lock没有批准大陆镜像、精确hash或许可证时必须返回`BLOCKED_SOURCE_UNAPPROVED`；FFmpeg例外直连验证前返回`BLOCKED_SOURCE_ACCESS_UNVERIFIED`，失败返回`BLOCKED_SOURCE_UNREACHABLE`。任何自动海外源回退为`FAIL`。

阶段3不让普通用户在Remotion、HyperFrames或FFmpeg之间作技术安装选择；确认的是一份包含全部真实缺失/不兼容闭集组件的missing-only计划。组件就绪后，WorkBuddy才依据已验证Package生产合同在具体视频方案中选择渲染能力。下载授权不得推导Provider、费用或生产授权。

阶段4 `PASS`要求一次Locator重验、一次精确环境绑定、一次固定工具进程调用和一个最终回执。任何第二Agent启动、自动重试、队列、调度、常驻服务、多Agent或Package业务内部导入均为越界`FAIL`。

阶段5 `PASS`要求真实WorkBuddy合同确认的一种显式入口、新会话命中、literal `user_message`不变、授权与`executor_controls`分离。入口格式未确认时应记`BLOCKED`，不得同时实现CLI/MCP/多个Skill兜底。

阶段6先验证WorkBuddy能否直接消费Launcher回执：能则记录`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`且生产代码变化为0；不能则必须有精确字段差异和真实消费者证据，只允许一次确定性转换。非零退出、超时、缺少结果指针和残留进程必须保持原事实。

## 4. Gate A：对象与环境

入口：阶段7安装候选通过离线测试并锁定安装对象。

要求：

- literal用户消息不含PackageRoot、Python或`.venv`；
- 显式Skill正确命中；
- Locator只读取登记对象，不扫盘；
- Launcher绑定精确PackageRoot、包内私有Python、闭集Runtime、cwd和DataRoot；
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
