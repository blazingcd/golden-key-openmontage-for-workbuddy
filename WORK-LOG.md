# Work Log

## 2026-08-18：V2-S3-OPTIONAL-CAPABILITY-AND-CONSUMER-CONTRACT-CORRECTION1

- 用户确认Remotion与HyperFrames始终是可选能力。本次撤销“两份Lock一律阻塞最终Package”的过度前置：每个不可变Package Release可声明支持零个、一个或两个，只为声明支持者携带Manifest覆盖的能力Lock；未声明能力不需要Lock、不是安装目标，也不阻塞最终Package。
- 阶段3前只冻结五种结果到WorkBuddy动作的最小接口：直接继续、复用继续、展示计划并询问且零下载、准备后继续、报告阻断并停止。用户同意绑定Registration、能力Lock与计划身份。
- 真实WorkBuddy新会话、用户确认和同任务继续证据改回阶段5验收，不再反向阻塞阶段3。若真实客户端不能自动继续，WorkBuddy固定提示用户回复“继续刚才的任务”；Shell不保存或自动重放原业务请求。
- 本任务只更新现有文档，不新增文件，不修改生产代码、测试或CI，不生成最终Package，不安装可选能力，不实现阶段3至阶段6。
- 本节是2026-08-18早先“Remotion/HyperFrames两份Lock + 真实WorkBuddy合同先于最终Package/阶段3”结论的活动纠偏；早先记录只保留历史，不得作为当前执行依据。
- 静态范围与全文旧结论检查通过，tracked仍为33；使用D盘任务独立`.venv`执行全量测试`144 passed in 26.33s`、最终退出0，随后已清理该任务临时目录。候选仍须独立只读Reviewer批准并普通fast-forward后才生效。
- 候选`7ba6ad64270c7ccdd7500e2a59b05cf55c73d7ed`经独立只读Reviewer批准：`APPROVE / P0=0 / P1=0 / P2=0`，随后普通fast-forward进入`origin/codex/workbuddy-shell-v2`。本状态收口只有三份既有文档，仍须独立只读审查并进入正式分支后才激活完成状态。

## 2026-08-18：V2-S3-PRETAKEOVER-REPLAN-CLOSEOUT1

- 规划累计对象`95eeeff175060f06ca2f549737e724160edc9e14..72719c758f092868fc6446e44a803d13eeae44a6`经独立只读Reviewer三轮审查；前两轮发现并关闭双路线、FFmpeg资产、旧模块状态和结果集歧义，最终结论`APPROVE / P0=0 / P1=0 / P2=0`。
- 已审规划结果以普通fast-forward进入`origin/codex/workbuddy-shell-v2=72719c758f092868fc6446e44a803d13eeae44a6`；已完全合入的远端临时规划分支随后删除。
- 本Closeout只把现有入口的阶段3规划状态收口为条件式`PASS_ACCEPTED`并记录审查/推广证据，生产代码、测试和CI变化保持0。Closeout自身仍须独立只读审查和正式fast-forward；否则状态条件不成立。
- 下一执行项仍是`V2-FINAL-PACKAGE-MATERIALIZATION-AND-PRODUCTION-REGISTRATION-GATE1`，且未被本Closeout授权；阶段3实现继续`NOT_GRANTED`。

## 2026-08-18：V2-S3-PRETAKEOVER-REPLAN-DOCS1

### 重新规划结论

- 阶段2已经接受Registration/Locator实现和一次包含Python、FFmpeg、Node完整必带工具链的真实临时Package验证；临时Package随后已清理，最终Release、已安装生产PackageRoot和生产Registration仍不存在。
- 阶段3只准备WorkBuddy/OpenMontage已选定的`none`、Remotion或HyperFrames之一，以及Package自有能力Lock明确声明的附属资产。它不负责最终组包、生产登记、三项必带工具链、渲染器决策、扫盘或视频执行。
- 建议唯一入口为`prepare_optional_capability(data_root, capability_request, authorization_receipt=None)`，结果闭集为`NO_OPTIONAL_CAPABILITY_REQUIRED`、`READY_REUSED`、`CONSENT_REQUIRED`、`READY_PREPARED`、`BLOCKED`。
- 未来最大代码面收敛为一个新增`runtime_prepare.py`、一次`__init__.py`仅导出修改、一个直接`test_runtime_prepare.py`；能力Lock归已验证Package所有，Shell不复制第二份Lock。

### 执行路径与衔接

- 八步路径固定为：Locator重验生产Registration；核验选择和Package能力Lock；只读有限发现；无可选或已就绪直接返回；缺失时生成精确missing-only计划；取得绑定Registration/Lock/plan的授权后用必带Node工具准备；同卷staging、hash/license核验、原子发布与失败清理；复探测并返回身份绑定回执。
- 阶段5是最终用户入口，先调用阶段2；阶段4基础固定工具调用可直接使用必带工具链，只有可选Remotion/HyperFrames执行才额外要求阶段3回执；阶段6只转交事实。WorkBuddy负责暂停、同意和继续，Shell不自动重放业务请求。
- 当时记录的Start Gate要求真实WorkBuddy消费者合同先行；该前置已被本文件最上方当前纠偏取代，不得继续执行。活动Gate只要求Release声明及声明能力Locks、最小结果到动作接口和精确Builder任务包；真实WorkBuddy证据属于阶段5。
- 本文档任务推广后的下一执行项固定为独立的`V2-FINAL-PACKAGE-MATERIALIZATION-AND-PRODUCTION-REGISTRATION-GATE1`，不是阶段3Builder；它不得被阶段3吸收，本任务也没有自动授予其实现权限。

### 本文档任务边界

- 只更新现有权威和入口文档，不新增规划文档，不修改生产代码、测试或CI，不运行安装、下载、WorkBuddy、Provider或媒体生产。
- 当前结果等待静态检查、独立只读Reviewer和正式分支fast-forward；完成这些步骤前，不得把本节当作阶段3实现授权。

### Reviewer1修正

- Reviewer1在`85eb55c75a5988baded734a0c9a135df477b8026`发现`P0=0 / P1=2 / P2=1`，结论`REQUEST_CHANGES`：已有可选能力是否仍经阶段3核验存在双路线；FFmpeg旧ZIP字样与`.7z / 9.0.1-essentials_build`证据冲突；旧模块处置仍写等待重规划。
- 修正后统一为：选择Remotion/HyperFrames后必经阶段3核验；已有能力返回`READY_REUSED`，只有缺失项下载/准备需要同意；FFmpeg精确资产只引用任务账本和Registration合同；旧模块处置改为“已重规划、实现未授权”。
- Reviewer1复审确认上述三项关闭后，又发现`INCOMPLETE_STAGE_3_INPUT`和`BLOCKED_BEFORE_PUBLISH`可能被误读为第六/第七种公共结果。现统一为：前者在实现授权前是任务治理裁决；未来运行期两者都只能作为`BLOCKED(reason_code=...)`原因码，公共结果仍精确为五种。

## 2026-08-18：V2必带工具链重新分类纠偏

### 最新用户裁决

- 官方OpenMontage基础Prerequisites为Python 3.10+、FFmpeg和Node.js 18+；金钥匙版面向普通用户，三项都必须随Package交付，不能只打包Python。
- 当前HyperFrames要求Node.js 22+，所以金钥匙Package的Node锁必须满足Package内最高要求，当前按22+，不能只取通用README的18+下限。
- Remotion、HyperFrames及其各自明确需要的浏览器/附属资产属于可选能力；由WorkBuddy/OpenMontage形成技术选择并锁定，普通用户只确认精确下载计划。

### 对阶段2和阶段3的影响

- 当时曾把阶段2重新打开；后续阶段2已完成Registration/Locator实现和一次真实临时Package验证。该历史判断不能覆盖上方最新结论，也不能把临时验证误报为最终Release或生产登记。
- 阶段3不再发现、下载、替换或回退到系统Python/FFmpeg/Node；只处理已选定的一个Remotion或HyperFrames可选能力和该能力Lock声明的附属资产。未选择能力时允许零代码/零下载。
- 终端用户可选能力下载继续要求精确missing-only计划、明确同意、批准的中国大陆镜像和禁止自动海外回退。精确`gyan.dev` FFmpeg资产改归Package组装供应链候选，接受来源、hash、许可和分发审查，不再属于阶段3下载流程。
- 当时的旧阶段3入口`prepare_runtime_on_demand(...)`、全组件Runtime Lock、精确文件范围、八步路径和条件授权全部`SUPERSEDED`或暂停；后来只重新冻结了上方接管前规划，仍未授权Builder实现。
- 本任务仍只修改现有文档，不新增生产代码、测试或Runtime资产，不运行下载、安装、WorkBuddy、Provider或媒体生产。结果最多为`REVIEW_READY`；独立Reviewer批准并fast-forward到正式分支前不算仓库交付。
- 静态范围复核：13个变化路径全部在任务白名单内，tracked仍精确33，未跟踪文件0，生产代码/测试/CI变化0，`git diff --check`通过。项目测试仍不运行；本轮只验证文档合同一致性。

## 2026-08-17：V2-S2-S3-RUNTIME-CORRECTION-DOCS1（已被2026-08-18纠偏取代）

- 当日先将Python设为Package必带项，并把Python核心依赖、FFmpeg、Node、Remotion、HyperFrames和浏览器划入阶段3闭集；这项Required/Optional分类已被上方最新裁决取代，不能作为活动执行依据。
- 当日为FFmpeg阶段3下载设置的`gyan.dev`直连阻断已退出阶段3；该资产现在只可能作为Package组装供应链候选。
- 当日冻结的阶段3单一入口、全组件Runtime Lock、八步执行路径和`GRANTED_AFTER_ALL_START_GATES_PASS`已全部`SUPERSEDED`或暂停。该日的新任务包尚未冻结；后续仅形成上方接管前规划，阶段3实现仍为`NOT_GRANTED`。
- WorkBuddy唯一Agent、Shell不成为生产控制面、不得扫描盘符、可选下载必须missing-only且不得自动海外回退等未受本次纠偏影响的边界继续有效。

## 2026-08-17：V2-S3-S6-SCOPE-DOCS1

### 对象与授权

- 起点、本地正式分支、origin tracking和实时正式远端均为`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`；起始工作树clean，tracked精确33。
- 用户明确要求把阶段3至阶段6缩减结论更新到相关旧文档，消除前后矛盾。
- 本任务只改现有的项目入口与权威文档，不新增文档，不修改生产代码或测试，不构成阶段3至阶段6实现授权。

### 收口结果

- `TASK-REGISTER.md`与`PROJECT-STATE.md`不再把Wave A或卫生序列写成当前任务；Git历史继续保存Wave A/B/C过程。
- `PROJECT-CHARTER.md`冻结每阶段单入口、单生产模块、单直接测试文件，以及阶段3和阶段6的零代码出口。
- `MODULE-DISPOSITION.md`禁止恢复V1通用Runtime、CLI/MCP生产入口、任务FSM和多套WorkBuddy入口。
- `ACCEPTANCE-MATRIX.md`把“无真实缺口时零代码”和“Launcher回执可直用时零代码”列为合法PASS路径。
- `DRIFT-GUARD.md`把预建通用框架、没有消费者仍写代码、多入口和阶段越级列为`STOPPED_SCOPE_EXPANSION`。

### 当前边界

- Git diff whitespace、11路径白名单、固定33文件等值、零未跟踪文件、零生产代码/测试变化、阶段3至阶段6授权字段和零代码出口静态一致性检查均为`PASS`。
- 项目`.venv`不存在；遵守项目Python隔离规则，未使用全局Python，pytest记为`NOT_RUN_PROJECT_VENV_MISSING`。
- 结果最多为`REVIEW_READY`。下一步只能由独立Reviewer只读比较`20ddab75825c1b6e7de5a51603afe8b6fd82eceb..THIS_COMMIT`；未经APPROVE和正式分支fast-forward，不得把本次文档结果当作已交付权威，也不得启动任何实现。

## 2026-08-16：V2-REPO-HYGIENE-WAVE-A-BUILDER1

### 对象与范围

- 起点与实时正式主线：`ca6e93b7da108732f2034239da340a986ba3da3a`。
- 计划审计：`01a00621-f896-7ce1-865d-7bd581bfef7e`，`CLEANABLE`。
- 计划Reviewer2：`01a00617-e037-72a3-b1e5-d88b3d0be19f`，`APPROVE / P0=0 / P1=0 / P2=0`。
- 临时Builder分支：`codex/v2-repo-hygiene-wave-a1`。

### 结果

- 机械展开A/B/C/D删除集合为`6 + 4 + 36 + 11 = 57`，两两交叉为0。
- 删除57个活动树历史Prompt、旧任务文档和旧docs证据；没有建立archive、legacy或quarantine副本。
- 新增`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`，只提取已接受的稳定登记合同，不保留执行历史。
- 最小重写Shell V2 Agent治理、README、状态、账本与Git生命周期入口；Stage1/2保持`PASS_ACCEPTED`，Stage3仅规划`GRANTED`、实现`NOT_GRANTED`。
- `package_registration.py`与`test_package_registration.py`相对起点blob不变；生产代码变化0、测试变化0。
- 结果提交语义为`THIS_COMMIT`，状态最多`REVIEW_READY`，下一任务仅为`V2-REPO-HYGIENE-WAVE-A-REVIEW1`。

### 零执行边界

未运行pytest、安装器、WorkBuddy、Provider、网络、媒体或下载。正式主线未推广；只有独立Reviewer批准后才能进入后续集成决策。
