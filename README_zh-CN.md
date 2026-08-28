# 金钥匙 WorkBuddy Shell V2

WorkBuddy Shell V2把腾讯 WorkBuddy 连接到经过验证的金钥匙版 OpenMontage
执行包。WorkBuddy 是唯一 Agent、对话主体和生产决策者；Shell 只是机械支持层，
不是第二控制面。

## 当前四个产品结果

1. **可安装 Shell 成品：COMPLETE。** 正式 commit
   `869358810ee41a0a61d10cec10c1b3b93c2c3450`，tree
   `3a623cb1eab9fee0d90854c0df271450f9779b9a`，Release SHA256
   `7e5585298e50a5c5713ecd8fc4df57cfb6e88381b39453364cec62fdea1c6280`。
   安装、Registration、Activation、卸载、重装和用户数据保护已通过。
2. **WorkBuddy 自然语言结果：COMPLETE。** WorkBuddy `5.3.14` / Hy3 已用
   `用金钥匙智能体给我做新店开业视频` 实际调用唯一
   `golden-key-openmontage` Skill 和 Shell，返回具体业务回复及可核对
   LauncherReceipt。Skill ZIP SHA256：
   `c96ec03522b744e8771eb16f22f5521102c4007af50ccb27d895efb82b1fe3a6`。
3. **真实可播放金钥匙视频：COMPLETE。** WorkBuddy `5.3.14` / `Hy3 0.00x`
   已显示并播放真实 46.6 秒 H.264/AAC MP4，独立评审为
   `P0/P1/P2=0/0/0`。
4. **正式收口：COMPLETE。** 已审查的收口提交通过 ordinary fast-forward
   到达历史正式分支；R4 没有再次运行 WorkBuddy 或生成视频。

Result 2 回执中的 `INCOMPLETE / RESULT_POINTER_INVALID` 只表示当次没有生成
视频文件。视频文件/result pointer 属于 Result 3，不否定 Result 2。

## 下一阶段规划

已完成的历史基线是 `codex/workbuddy-shell-v2` 分支上的
`aa9cabfa0d4f75d93e22317466709b6bad3bc3b4`。后续规划在
`codex/workbuddy-capability-onboarding` 分支进行，当前未授权实现。

FFmpeg 是最低生产基线。首次使用时，WorkBuddy 将盘点与当前目标有关的可选
增强能力，明确基础制作仍可直接进行，并允许用户选择继续，或者配置 Remotion、
HyperFrames、外部生视频、TTS 等当前可用能力。之后，用户可用包含
`金钥匙智能体` 的自然语言再次进入检查、配置、更换或重测流程。Shell 不选择
Provider、模型或渲染器。

## 产品边界

用户只需在 WorkBuddy 输入包含 `金钥匙智能体` 的自然语言请求；其余业务描述和
素材路径都是开放输入。WorkBuddy 是 harness Agent：相同输入的内部思考、工具
路径、步骤、表达和中间结论可以变化。Skill 和提示词不得强制预设脚本。只要过程
没有导致产品结果失败、增加普通用户技术负担、形成第二控制面或产生虚假结果，
这种变化就不是失败。

Shell 只负责安装/生命周期、Registration/Locator、Runtime 准备、固定机械调用、
WorkBuddy 入口和状态/回执传递；不选择生产内容、Pipeline/Stage、Provider、渲染器、
恢复方式或媒体策略。外部 Package 的 `AGENT_GUIDE.md` 只能在 Registration/Locator
返回已验证 PackageRoot 后由 WorkBuddy 读取。

## 权威文档与约束

实时状态在 [`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md)。
其余权威文档为 [`AGENT_GUIDE.md`](AGENT_GUIDE.md)、[`PROJECT-STATE.md`](PROJECT-STATE.md)、
[`docs/workbuddy/v2/PROJECT-CHARTER.md`](docs/workbuddy/v2/PROJECT-CHARTER.md)、
[`docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`](docs/workbuddy/v2/ACCEPTANCE-MATRIX.md) 和
[`docs/workbuddy/v2/DRIFT-GUARD.md`](docs/workbuddy/v2/DRIFT-GUARD.md)。

项目 Python 只能使用
`D:\BlazingCD\Personal\.venvs\golden-key-openmontage-workbuddy-w0\Scripts\python.exe`。
临时文件只放 D 盘，清理时不得删除用户数据。可选增强能力的安装或使用可以延期，
不阻塞 FFmpeg 已就绪的基础生产。历史 Git 基线保留在
`refs/heads/codex/workbuddy-shell-v2`；当前规划分支为
`refs/heads/codex/workbuddy-capability-onboarding`。
