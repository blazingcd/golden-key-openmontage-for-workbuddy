# WorkBuddy Shell V2 项目章程

状态：`STAGE_1_REVIEW_READY / NOT_PASS_ACCEPTED`

阶段1架构决策对象：`V2-S1-BUILDER1@codex/v2-s1-builder1`

## 1. 最终目标

普通用户在真实WorkBuddy中明确调用“金钥匙短视频智能体”，只提供业务需求、素材和授权信息，不需要知道Core目录、Python、虚拟环境、CLI、Pipeline、Stage、Schema、Artifact或Checkpoint。

项目要把已被真实WorkBuddy证明可行的“WorkBuddy直接驱动OpenMontage”路径，固化为可安装、可定位、可恢复、可审计的稳定入口。目标不是制造一个更复杂的壳。

## 2. 唯一职责模型

```text
普通用户
  -> WorkBuddy（唯一对话Agent）
     -> 显式调用金钥匙短视频智能体Skill
        -> Core Registration（锁定已安装对象）
           -> Launcher（绑定CoreRoot/Python/DataRoot/cwd/env）
              -> WorkBuddy读取该Core自己的AGENT_GUIDE.md
                 -> OpenMontage原生Pipeline/Director/Reviewer/Checkpoint/Tool
                    -> 原生Artifact、进度和最终结果
```

| 组件 | 唯一职责 | 明确不得承担 |
|---|---|---|
| WorkBuddy | 唯一对话Agent；保留用户原话，读取锁定Core自己的Guide，按Core合同执行并向用户呈现 | 把Shell逻辑伪装为Core决策；自行成为媒体生产器 |
| WorkBuddy Skill | 显式产品入口、Locator调用、授权提示、literal用户消息转交、结果呈现 | Pipeline/Stage/Provider/模型选择、生产编排、创意决策 |
| Core Registration | 精确记录并验证Core Release/commit、Manifest/Lock/SHA、CoreRoot、Python、Guide、活动指针 | 扫盘猜测、根据文件名/时间推断正式身份、执行生产 |
| Installer | 安装/修复/升级/回滚/卸载Shell与Core对象，原子更新Registration并保护数据 | 运行Pipeline、修改Core业务代码、静默下载或删除用户数据 |
| Runtime准备层 | 按已授权且当前会话实际需要的层准备Python、FFmpeg、动态合成或其他组件 | 一次全装、选择生产方案、把Provider配置当调用授权 |
| Launcher | 确定性绑定Shell/Core/Python/DataRoot/ProjectsRoot/cwd/env，启动受控Core入口，返回退出、结果和残留 | Agent、Director、任意Shell、业务状态机、Artifact/Checkpoint写入 |
| OpenMontage Core | Pipeline、Stage、Director、Reviewer、Checkpoint、Artifact、Tool、Provider/模型/媒体选择和媒体生产 | 安装器、WorkBuddy产品入口、Shell对象登记 |
| Tool / Provider | 只在Core原生合同与用户授权内执行具体能力并返回可审计结果 | 绕开Core或把可配置状态冒充真实执行 |

最高原则：

> WorkBuddy负责对话，OpenMontage负责生产决策与执行，WorkBuddy壳只负责安装、对象锁定、运行环境绑定、会话入口以及状态和结果转交。壳不重新实现OpenMontage，也不成为第二个导演。

## 2.1 控制权、信任边界与最小数据流

```text
literal user_message
  -> WorkBuddy（唯一对话上下文）
  -> 显式生产Skill
  -> Locator只读活动Core Registration
  -> Launcher生成Session Binding Receipt
  -> 锁定Core自己的公开入口与AGENT_GUIDE.md
  -> Core原生生产链
  -> Core退出码 + 原生结果指针 + 进程/残留事实
  -> Launcher原样转交
  -> WorkBuddy向用户呈现

executor_controls
  -> 仅进入Locator/Launcher/测试卡
  -> 永不拼接进literal user_message
```

信任规则：

- WorkBuddy只信任经Registration锁定且通过Manifest/Lock/SHA核验的Core，不信任目录名、“最新”时间或磁盘搜索结果；
- Launcher只调用受控Core公开入口，不导入`lib.checkpoint`、`lib.pipeline_loader`、Artifact Schema、Tool Registry或其他Core业务内部实现；
- Shell只报告绑定、进程、退出和结果指针事实，不解析Artifact业务语义，不把Core状态翻译成第二套Stage状态；
- Core拥有全部生产状态、Artifact、Checkpoint、Reviewer结论和恢复语义；Shell自己的安装/会话状态不得与它们同名混用；
- Provider、网络、下载、费用、模型切换和重要降级各自需要明确授权，任一授权不得由普通视频请求推导。

## 2.2 `user_message`与`executor_controls`

`user_message`必须保持用户真实会说的业务请求、素材位置、事实、授权和期望结果；其字面值是验收证据，不得被Shell追加技术尾巴。

以下只属于`executor_controls`：Shell/Core/包身份、CoreRoot、Python、DataRoot、cwd、Guide读取方式、测试编号、模型/重试预算、停止条件、下载/Provider/费用控制、证据采集和残留要求。二者必须在测试卡、日志和Launcher参数中分字段保存，禁止字符串拼接。

## 3. Shell V2第一版必须具备

- Shell、Core、Runtime、DataRoot、Projects相互分离；
- 安装、同版本修复、向前升级、失败回滚和默认保留数据的卸载；
- Core Release、commit、Manifest、Lock、SHA、CoreRoot、Core Python和Guide身份；
- 显式触发，不全局截获所有视频请求；
- literal `user_message`与`executor_controls`分离；
- 每次会话绑定精确CoreRoot、Python、DataRoot、cwd和最小环境；
- 基础Python、FFmpeg、动态合成、Provider和大型模型分层准备；
- 下载、安装、Provider、网络、费用和重要降级分别授权；
- 路径边界、所有权、凭据保护、日志脱敏和单真实执行锁；
- 实际解释器、Core身份、退出码、结果路径、进程和残留可审计。

## 4. Shell V2第一版明确不做

- 不选择、推荐或排序Pipeline；
- 不编写Brief、Script、Scene Plan、Asset Manifest或Edit Decisions；
- 不实现Reviewer或决定Checkpoint；
- 不选择或替换Provider；
- 不判断rotation、画幅、剪辑、配乐或成片质量；
- 不导入Core Pipeline Loader、Checkpoint、Artifact Schema或Tool Registry建立第二套流程；
- 不启动嵌套模型、Supervisor、Director或Agent Host；
- 不把17个MCP工具作为第一版关键路径；
- 不验证或依赖中文fork；
- 不修复Core横竖屏和安全删除语义；
- 不新增Web UI、SaaS、多租户、计费后台或外部平台发布；
- 不要求首次使用前准备所有大型运行时。

上述非目标只能通过第9节的范围变更程序改变，不能由后续Builder、Reviewer、测试通过或聊天中的临时说法静默扩大。

## 5. Launcher合同边界

V2可规划`inspect / prepare / session / exec / status`五类能力，但它们只表达Shell能力：

- `inspect`：只读报告登记对象和环境；
- `prepare`：只准备经授权且当前方案需要的组件；
- `session`：生成不可混淆的会话绑定回执；
- `exec`：在锁定环境中调用受控Core入口，不接受任意Shell文本；
- `status`：转交进程、Core结果和错误，不发明Pipeline Stage状态。

Launcher不得解析用户意图、选择Pipeline、创建Artifact、推进Checkpoint或进行媒体判断。

### 5.1 会话绑定回执

每次`session/exec`至少锁定并回报：

```text
shell_commit / shell_package_version
core_release / core_commit / core_manifest_sha256 / core_lock_sha256
core_root / core_python / core_guide
data_root / projects_root / cwd
session_id / process_id / started_at
literal_user_message_hash / executor_controls_hash
exit_code / core_result_pointer / residual_processes
```

回执只证明对象与环境绑定。没有Core最终退出、结果指针或进程收口时必须为`INCOMPLETE`，不得用“已启动”代替成功。

## 6. Core与Shell问题分界

必须留给Core项目：

- rotation和有效显示方向识别；
- 目标画幅和素材规范化；
- 避免重复旋转；
- 最终成片规格复核；
- Core Tool安全删除语义；
- 原生Artifact、Reviewer、Checkpoint和生产恢复合同。

必须由Shell解决：

- 精确对象定位；
- Core项目Python和工作目录绑定；
- 安装、运行时、升级、回滚和卸载；
- 显式Skill入口；
- 用户授权和技术细节隐藏；
- 状态、错误、结果和残留转交。

## 7. Git与存储边界

- V2代码基线固定为`2a2bf09832d558388dc2816c54b32a2dce4aa607`。
- V2建立后不merge/rebase推进中的`main`或旧长期分支。
- 后续只允许带来源commit、文件清单和消费者证据的选择性迁移。
- 不新建第二个Git仓库，不复制无历史项目副本。
- 开发、测试、缓存、构建和临时文件优先放D盘。
- 普通用户系统级应用可使用标准用户应用目录；DataRoot必须可配置且不能扫描盘符猜测。
- 升级和卸载默认不删除用户Projects、素材、配置、模型和输出。

## 8. 角色与交付责任

- 统筹任务：维护章程、账本、任务Prompt、依赖和Gate，不直接实现代码。
- 执行任务：只在允许路径实现单个有界目标，提供精确commit、测试和非证明项。
- 独立Reviewer：检查精确对象和diff，不替执行任务修代码。
- 真实WorkBuddy Operator：仅在单独授权的Gate中运行一个新会话和新项目。
- Core负责人：提供不可变Core Release及Core层修复证据。
- 用户：批准范围变化、真实运行、下载、Provider、费用和产品Gate。

## 9. 范围变更程序

若后续发现本章程无法满足真实使用场景：

1. 当前任务停止在安全点并记录精确对象、新事实和受影响Gate；
2. 明确问题归属Shell、Core、Host、Tool、Provider或产品范围；
3. 同时给出“不处理”“调整当前阶段”“新增后续任务”的影响；
4. 由用户批准后先更新`PROJECT-CHARTER.md`、`TASK-REGISTER.md`和对应执行计划并提交；
5. 只有版本化文档生效后才能恢复执行。

阶段1`PASS_ACCEPTED`之前不得细化或启动阶段2；本Builder的`REVIEW_READY`不是用户Gate结论。
