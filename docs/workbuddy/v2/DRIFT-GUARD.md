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
- 阶段3同时安装Remotion与HyperFrames、替WorkBuddy/OpenMontage选择渲染器，或准备所选能力锁未声明的浏览器/附属资产；
- 把Remotion或HyperFrames写成所有Package Release必带Runtime，要求未声明支持的能力也必须有Lock，或因未声明能力缺Lock而阻塞最终Package；
- 阶段3从默认Git/GitHub、Google、npmjs或其他未批准海外源下载，在批准大陆镜像失败后静默回退；
- 阶段3把PATH命中直接判为可用而不核验版本、路径、能力和登记身份，扫描盘符，或覆盖未知/外来目录；
- 阶段3在最终Release未保留、生产Package未登记、Locator未在新进程重验、Release可选能力声明未冻结、声明支持的能力缺少Package自有Lock、最小结果到WorkBuddy动作接口不完整或正式Git对象漂移时提前编码；
- 阶段3在Shell仓库复制、维护或猜测可选能力Lock，而不是核验当前Registration所绑定Package内的能力Lock；
- 阶段3实现已标记`SUPERSEDED`的旧`prepare_runtime_on_demand(...)`签名、旧全闭集Runtime Lock或旧任务包，或恢复`host_tools.py`、通用下载器、CLI/MCP、服务、数据库等第二入口；
- 阶段3把可选能力写入Package、系统目录或必带工具链目录，修改系统PATH/注册表，要求管理员权限，或在失败后遗留staging/cache临时对象；
- 阶段4接受任意Shell、启动多个Agent、自动重试、建立队列/调度/常驻服务或进入Agent业务内部；
- 阶段4基础固定工具调用未绑定有效Registration和必带工具链，或可选Remotion/HyperFrames执行在没有同一Registration、同一Package能力Lock的阶段3就绪回执时仍继续；
- 阶段5并存多套生产入口、全局截获用户意图或成为第二聊天Agent；
- 阶段6在Runtime计划/准备事实或Launcher回执可直接消费时仍建立独立服务、数据库、轮询/流式平台，或自行安装Runtime、解释Artifact业务语义；
- 把建设顺序`阶段3 -> 阶段4 -> 阶段5 -> 阶段6`误写成最终用户调用顺序，或在阶段3准备后自动重试原生产请求；
- 阶段3超过一个公共入口、一个新增生产模块、对`__init__.py`的导出式修改和一个直接测试文件，或其他阶段超过其任务包明示的最小文件范围，且没有单独的新授权与消费者证据。

## 产品边界

腾讯WorkBuddy是唯一运行中的Agent，读取已验证Package Guide后承担OpenMontage生产角色；不存在由Shell另行启动的OpenMontage Agent进程。Shell只负责六模块。仓库Agent不得运行视频Pipeline、Provider或媒体生产。SaaS Core不是Package Registration对象，也不在Shell V2当前实现范围。

金钥匙版交付包必须自带Manifest/Lock锁定的完整必带私有工具链：可用Python 3.10+环境及核心依赖、FFmpeg/ffprobe、Node/npm/npx；Node满足当前Package最高要求，当前不得低于HyperFrames所需的22。阶段2已经接受Registration/Locator实现，并以一次随后清理的真实临时Package验证这些字节；这不等于最终Release、已安装生产PackageRoot或生产Registration已经存在。最终Package的持久组装、安装与生产登记必须在阶段3实现前单独过Gate。FFmpeg `gyan.dev`候选只属于Package组装供应链、hash、许可和分发审查，不再是阶段3面向终端用户的下载例外。

阶段3只准备经验证WorkBuddy/OpenMontage决定且当前Package Release声明支持的一个可选能力，允许目录当前为Remotion或HyperFrames，以及该能力Package自有Lock明确声明的附属资产。每个Release可声明零个、一个或两个；未声明能力不需要Lock且不是安装目标。普通用户只确认精确missing-only计划，不选择技术组件；终端用户可选下载必须使用批准的中国大陆镜像且不得自动海外回退。阶段3建议唯一入口为`prepare_optional_capability(data_root, capability_request, authorization_receipt=None)`，最大代码面为一个新增生产模块、一次仅导出修改和一个直接测试文件。旧阶段3条件授权、入口签名、全闭集Lock和执行包均已暂停并标记`SUPERSEDED`；只有最终Package、生产登记、Release声明及对应Locks、最小结果到WorkBuddy动作接口和精确任务包全部满足Start Gate，`TASK-REGISTER.md`再明确写为`GRANTED`，Builder才可开始。真实WorkBuddy新会话和继续验证属于阶段5验收，不得反向阻塞阶段3。

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
