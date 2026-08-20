# WorkBuddy Shell V2 防漂移与Git生命周期

状态：`ACTIVE / FAIL_CLOSED`

## 立即停止

出现以下任一情况时停止并报告`INCOMPLETE`或明确的范围冲突，不得顺手修复：

- 当前HEAD、实时正式远端、任务起点、允许路径、tracked计数或锁定blob不一致；
- 需要修改任务未授权路径，或与其他任务/用户改动重叠；
- 需要Shell选择或运行Pipeline、Stage、Provider、模型、媒体或创意；
- 需要实现未授权的Runtime、Launcher、WorkBuddy入口、状态结果转交或其他阶段；
- 需要扫描磁盘、猜测“最新”执行包、读取未验证Package Guide或修改外部执行包；正常PATH命令解析不等于扫盘，但只能产生待核验候选；
- 把阶段2的Registration/Locator实现和一次真实临时Package验证误报为“最终Release已保留”“生产Package已安装/登记”，或接受缺少Python私有环境、FFmpeg/ffprobe、Node/npm/npx任一必带项的最终Package；
- 需要把PackageRoot、Python、cwd、测试编号、重试或证据控制拼入literal `user_message`；
- 命令超时、输出截断、没有最终退出、证据缺失，或文档与任务账本冲突；
- 需要reset、stash、merge、rebase或改写已审对象。

以下范围扩张直接报告`STOPPED_SCOPE_EXPANSION`，不得以“预留”“通用化”或“后续复用”为理由继续：

- 没有已验证上游输入或直接下游消费者仍新增生产代码；
- 阶段3发现、下载、替换或回退到系统Python/FFmpeg/Node，借此补偿阶段2必带工具链不完整；
- 阶段3自动安装Remotion或HyperFrames、替WorkBuddy/OpenMontage选择渲染器，或准备用户未逐项批准的浏览器/附属资产；
- 把Remotion或HyperFrames写成必带Runtime，或因能力缺失、用户拒绝/暂缓集成而阻塞Package、项目、最终交付或其他已有/基础能力；
- 阶段3从默认Git/GitHub、Google、npmjs或其他未批准海外源下载，在批准大陆镜像失败后静默回退；
- 阶段3把PATH命中直接判为可用而不核验版本、路径、能力和登记身份，扫描盘符，或覆盖未知/外来目录；
- 把历史阶段3前置Gate重新激活，或否认已正式推广的Stage3实现/closeout；重新增加Package、Registration、Package绑定能力元数据、task-only登记验证或Stage 5输入Gate；
- 阶段3接受能力定义外的任意URL、命令或目标，或把批准OpenMontage能力定义扩张成通用包管理框架；
- 阶段3实现已标记`SUPERSEDED`的旧`prepare_runtime_on_demand(...)`签名、旧全闭集Runtime Lock或旧任务包，或恢复`host_tools.py`、通用下载器、CLI/MCP、服务、数据库等第二入口；
- 阶段3把可选能力写入Package、系统目录或必带工具链目录，修改系统PATH/注册表，要求管理员权限，或在失败后遗留staging/cache临时对象；
- 阶段3准备前为了发现或互斥而创建Runtime、缓存、锁文件或staging，或在没有该能力最终`PRESENT`或`INTEGRATED`证据时让阶段4把完整或不完整的已发布对象视为可执行能力；
- 阶段4接受任意Shell/命令、改写literal `user_message`、解析意图、读取未验证Package Guide、启动多个Agent、安装Runtime、选择渲染器、自动重试/重放、建立队列/调度/常驻服务/数据库、执行媒体生产、创建Artifact、推进Checkpoint或进入Agent业务内部；
- 阶段4基础固定工具调用未绑定有效Registration和必带工具链，或执行Remotion/HyperFrames时没有Stage 3对该能力给出的`PRESENT`或`INTEGRATED`证据；
- 阶段5并存多套生产入口、全局截获用户意图或成为第二聊天Agent；
- 阶段6在Runtime计划/准备事实或Launcher回执可直接消费时仍建立独立服务、数据库、轮询/流式平台，或自行安装Runtime、解释Artifact业务语义；
- 把建设顺序`阶段3 -> 阶段4 -> 阶段5 -> 阶段6`误写成最终用户调用顺序，或在阶段3准备后自动重试原生产请求；
- 改写已接受Stage3的一个公共入口、一个新增生产模块、`__init__.py`导出、一个直接测试及两项验收基础设施闭集；其他阶段超过其未来任务包明示的最小文件范围且没有单独的新授权与消费者证据。

## 产品边界

腾讯WorkBuddy是唯一运行中的Agent，读取已验证Package Guide后承担OpenMontage生产角色；不存在由Shell另行启动的OpenMontage Agent进程。Shell只负责六模块。仓库Agent不得运行视频Pipeline、Provider或媒体生产。SaaS Core不是Package Registration对象，也不在Shell V2当前实现范围。

金钥匙版交付包必须自带Manifest/Lock锁定的完整必带私有工具链：可用Python 3.10+环境及核心依赖、FFmpeg/ffprobe、Node/npm/npx；Node满足当前Package最高要求，当前不得低于HyperFrames所需的22。阶段2已经接受Registration/Locator实现，并以一次随后清理的真实临时Package完成组装、register、task-only activate和new-process locate验证；清理不重开、不重做阶段2，但也不等于最终Release、已安装生产PackageRoot或生产Registration已经存在。最终Package的持久组装、安装与生产登记仍是强制交付要求，但只属于后续最终交付或Installer收口任务，最迟在阶段5真实WorkBuddy生产验收前完成，绝不是阶段3或阶段4编码/规划前置。FFmpeg `gyan.dev`候选只属于Package组装供应链、hash、许可和分发审查，不再是阶段3面向终端用户的下载例外。

阶段3只对Remotion和HyperFrames执行有界探测、事实报告、零下载计划和用户逐能力批准后的受管集成。探测仅允许受管DataRoot、明确登记/配置候选路径和正常命令解析；禁止遍历盘符、系统软件清单、全局npm状态或猜目录。结果闭集为`DETECTION_REPORT/CONSENT_REQUIRED/INTEGRATED/SKIPPED/BLOCKED`，能力事实为`PRESENT/MISSING/INCOMPATIBLE/NOT_INTEGRATED`。缺失、拒绝或暂缓不是失败；Shell不选择渲染器，OpenMontage从实际可用能力中决定生产使用。唯一入口为`prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`。实现`a3f8959682d296301dc573c2835f8c705a52e8b2`和closeout `7c15aae4e77c579309312b21c79076f930970214`已正式推广，Stage3现为`PASS_ACCEPTED`；证据层为55 direct、10 hygiene、199 full，全部退出0且无skip，不包含真实下载、生产DataRoot、WorkBuddy、Stage4、Provider或媒体/视频E2E。

阶段3已接受Builder只编辑三个产品路径及`tests/workbuddy/test_repository_hygiene.py`、`.github/workflows/ci.yml`两项验收基础设施，当时正式树tracked精确35；Stage4随后严格按其五路径新增一个生产模块和一个直接测试并同步两项验收基础设施，当前正式树tracked精确37。这不改变每阶段“一个生产模块、一个公共入口”的产品边界。

Stage4规划已`PASS_ACCEPTED`，`PackageToolDefinitionV1`固定工具身份合同及唯一`launch_session_tool(...)`和九值递归不可改写`LauncherReceiptV1`合同均已冻结。Stage4实现结果`fa9adb8470ab94b88ec9900ede03cb26f7de0ebd`经第八轮独立零写审查`APPROVE / P0=0 / P1=0 / P2=0`，严格在既定五路径内将tracked从35迁移到37并普通fast-forward；首个正式CI run `32367792637`仅暴露测试夹具错误假定GitHub `setup-python`包含`pyvenv.cfg`，不是生产Launcher finding。单测试路径修复`13a3227b0c55bbe9039b46d7e92eba822b48f57e`也经独立`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward，正式Ubuntu CI run `32369588814`为`357 passed / 1 skipped / exit 0`；Windows最终证据为158 direct、11 hygiene、358 combined，全部exit 0且无skip。当前只允许`V2-S4-IMPLEMENTATION-CLOSEOUT-REVIEW1`零写审查本六权威closeout候选；只有审查`APPROVE / P0=0 / P1=0 / P2=0`且候选普通fast-forward后，Stage4实现才有效记为`PASS_ACCEPTED`，随后`next_authorized_task=NONE`。当前Locator仍只重验Registration、PackageRoot、必带工具链、Guide、Manifest和Lock；Stage4从批准Package定义及最终交付/Installer owner提供的release-specific定义取得工具身份，不得猜Guide、重开Stage2、选择Provider/Runtime或扩大路径。缺具体Release定义实例时必须fail closed且spawn 0。WSL只用于临时Linux等价验证并已清理关闭，不是运行依赖。真实生产WorkBuddy/Launcher会话、Stage5、Stage6、Provider/媒体执行及final Package物化/生产登记仍为`NOT_GRANTED`或未证明。

外部Package Guide只有在Registration身份完整验证、Locator返回已验证身份后，才可由对应下游消费者读取。本仓库根`AGENT_GUIDE.md`只治理Shell V2，不能替代或预先信任外部Guide。

`user_message`只包含用户真实会说的业务请求、素材、事实、授权和期望结果。包身份、路径、Python、cwd、命令、测试、停止条件和证据采集只进入独立的`executor_controls`。

## Git任务生命周期

- Builder分支是单任务临时隔离；不得发展为长期分支。
- Reviewer独立只读，不建立长期审阅分支，不修改结果制造APPROVE。
- 用户接受或Reviewer批准不等于已交付。
- 任务或阶段只有在已审结果进入`origin/codex/workbuddy-shell-v2`后才算仓库完成。
- 正式主线只允许fast-forward到已审集成结果；不得merge/rebase推进中的`main`或旧长期分支。
- 推广后，所有已完全合入且无未合入commit的临时远端分支必须删除。
- 本地分支仅在对应worktree关闭后安全删除；不得清理其他任务的worktree、branch、stash、tracked、untracked或ignored现场。
- 下一阶段接管只能使用正式主线最新精确commit，不能使用任务分支。

只精确暂存授权路径，禁止`git add .`。正式状态只以`TASK-REGISTER.md`为准；Git历史保存旧Prompt、计划、报告和证据，但不恢复其活动授权。

## 证据边界

静态检查、单元测试、Package Registration成功、ZIP、Guide读取或旧运行历史都不能证明真实Installer、Runtime、Launcher、WorkBuddy、OpenMontage生产、Provider、媒体、SaaS或业务效果。任何Gate对象不一致或无最终退出一律不是PASS。
