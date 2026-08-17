# Work Log

## 2026-08-18：V2必带工具链重新分类纠偏

### 最新用户裁决

- 官方OpenMontage基础Prerequisites为Python 3.10+、FFmpeg和Node.js 18+；金钥匙版面向普通用户，三项都必须随Package交付，不能只打包Python。
- 当前HyperFrames要求Node.js 22+，所以金钥匙Package的Node锁必须满足Package内最高要求，当前按22+，不能只取通用README的18+下限。
- Remotion、HyperFrames及其各自明确需要的浏览器/附属资产属于可选能力；由WorkBuddy/OpenMontage形成技术选择并锁定，普通用户只确认精确下载计划。

### 对阶段2和阶段3的影响

- 阶段2再次重新打开：Package组装、Manifest/Lock、Registration、Locator和测试必须覆盖可用私有Python环境及核心依赖、FFmpeg/ffprobe、Node/npm/npx。此前只显式登记Python的实现保留为历史证据，不得标为当前PASS。
- 阶段3不再发现、下载、替换或回退到系统Python/FFmpeg/Node；只处理已选定的一个Remotion或HyperFrames可选能力和该能力Lock声明的附属资产。未选择能力时允许零代码/零下载。
- 终端用户可选能力下载继续要求精确missing-only计划、明确同意、批准的中国大陆镜像和禁止自动海外回退。精确`gyan.dev` FFmpeg资产改归Package组装供应链候选，接受来源、hash、许可和分发审查，不再属于阶段3下载流程。
- 旧阶段3入口`prepare_runtime_on_demand(...)`、全组件Runtime Lock、精确文件范围、八步路径和条件授权全部`SUPERSEDED`或暂停。必须等待完整阶段2输出和真实WorkBuddy/OpenMontage可选能力消费者合同后重新冻结，不得把旧包交给Builder。
- 本任务仍只修改现有文档，不新增生产代码、测试或Runtime资产，不运行下载、安装、WorkBuddy、Provider或媒体生产。结果最多为`REVIEW_READY`；独立Reviewer批准并fast-forward到正式分支前不算仓库交付。
- 静态范围复核：13个变化路径全部在任务白名单内，tracked仍精确33，未跟踪文件0，生产代码/测试/CI变化0，`git diff --check`通过。项目测试仍不运行；本轮只验证文档合同一致性。

## 2026-08-17：V2-S2-S3-RUNTIME-CORRECTION-DOCS1（已被2026-08-18纠偏取代）

- 当日先将Python设为Package必带项，并把Python核心依赖、FFmpeg、Node、Remotion、HyperFrames和浏览器划入阶段3闭集；这项Required/Optional分类已被上方最新裁决取代，不能作为活动执行依据。
- 当日为FFmpeg阶段3下载设置的`gyan.dev`直连阻断已退出阶段3；该资产现在只可能作为Package组装供应链候选。
- 当日冻结的阶段3单一入口、全组件Runtime Lock、八步执行路径和`GRANTED_AFTER_ALL_START_GATES_PASS`已全部`SUPERSEDED`或暂停。当前阶段3仍为`NOT_GRANTED`，新任务包尚未冻结。
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
