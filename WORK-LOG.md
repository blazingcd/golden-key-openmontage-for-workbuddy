# Work Log

## 2026-08-17：V2-S2-S3-RUNTIME-CORRECTION-DOCS1

### 用户裁决与历史证据

- 用户明确裁决：金钥匙版OpenMontage for WorkBuddy交付包必须自带私有Python，避免普通用户首次运行前缺少解释器；其他运行组件先发现，缺失时再安装；终端用户下载必须使用中国大陆镜像，不得使用默认Git等海外位置。
- Git历史`347272c`已实现包内便携Python引导；`899592d`已实现锁定Python依赖、FFmpeg、Node、Remotion、HyperFrames和浏览器，并记录阿里云/清华PyPI、npmmirror npm/Node/Chrome源；`639978d`已实现`managed`、`registered_host`、`PATH_host`、`missing`分类和missing-only准备。
- 旧FFmpeg锁仍使用gyan.dev，不符合本轮“终端用户下载只用批准大陆镜像”的更严格裁决；新版Runtime Lock没有批准且可校验的大陆FFmpeg源前必须fail closed，不能静默回退海外源。

### 文档固化边界

- 纠正Agent身份：腾讯WorkBuddy是唯一运行中的Agent；“OpenMontage Agent”只表示WorkBuddy读取已验证Package Guide后承担的逻辑生产角色，不是第二Agent进程。
- 阶段2重新打开：旧实现与集成只保留为旧Package历史证据；新版官方输入必须重新组装为带锁定私有Python的金钥匙版Package，并完成重新登记、独立审阅和推广。
- 阶段3固定闭集为Python私有依赖、FFmpeg、Node、Remotion、HyperFrames和锁定浏览器。包内Python不发现、不下载；其余组件只查受管路径、明确登记宿主工具和PATH命令候选，不扫描盘符。
- discover/plan必须零写入；只有完整missing-only计划展示组件、版本、hash、大小、目标和许可并取得用户明确同意后，才能从Runtime Lock批准的中国大陆镜像准备缺失项。无批准镜像返回`BLOCKED_SOURCE_UNAPPROVED`。
- 本任务只修改现有文档，不新增生产代码、测试或Runtime资产，不运行下载、安装、WorkBuddy、Provider或媒体生产。结果最多为`REVIEW_READY`，独立Reviewer批准并fast-forward到正式分支前不算交付。
- 静态一致性检查=`PASS`：13个变化路径全部在本任务白名单内，tracked仍精确33，生产代码/测试/CI变化0，`git diff --check`通过；项目`.venv`不存在，未混用全局Python，pytest保持`NOT_RUN_PROJECT_VENV_MISSING`。

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
