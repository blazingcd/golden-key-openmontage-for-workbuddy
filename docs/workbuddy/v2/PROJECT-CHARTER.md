# WorkBuddy Shell V2 项目章程

状态：`FROZEN_FOR_STAGE_1_PLANNING`

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
| WorkBuddy | 与用户对话、读取Core指令、按Core合同执行 | 把Shell逻辑伪装为Core决策 |
| WorkBuddy Skill | 显式产品入口、Locator调用、授权提示、结果呈现 | Pipeline选择、生产编排、创意决策 |
| Core Registration | 精确记录并验证Core对象和活动指针 | 扫盘猜测、根据文件名推断正式身份 |
| Launcher | 确定性绑定环境、启动受控Core入口、返回退出和结果 | Agent、Director、任意Shell、业务状态机 |
| OpenMontage Core | Pipeline、Stage、Director、Reviewer、Checkpoint、Artifact、Tool和媒体生产 | 安装器与WorkBuddy产品入口 |

最高原则：

> WorkBuddy负责对话，OpenMontage负责生产决策与执行，WorkBuddy壳只负责安装、对象锁定、运行环境绑定、会话入口以及状态和结果转交。壳不重新实现OpenMontage，也不成为第二个导演。

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

## 5. Launcher合同边界

V2可规划`inspect / prepare / session / exec / status`五类能力，但它们只表达Shell能力：

- `inspect`：只读报告登记对象和环境；
- `prepare`：只准备经授权且当前方案需要的组件；
- `session`：生成不可混淆的会话绑定回执；
- `exec`：在锁定环境中调用受控Core入口，不接受任意Shell文本；
- `status`：转交进程、Core结果和错误，不发明Pipeline Stage状态。

Launcher不得解析用户意图、选择Pipeline、创建Artifact、推进Checkpoint或进行媒体判断。

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
