# 金钥匙 WorkBuddy Shell V2

WorkBuddy Shell V2负责把腾讯WorkBuddy可靠连接到经过身份验证、版本化的金钥匙版OpenMontage执行包。WorkBuddy是唯一运行中的Agent；它读取执行包Guide后承担OpenMontage生产角色。Shell只负责六个模块：安装与生命周期、执行包登记与定位、Runtime按需准备、会话Launcher、WorkBuddy入口、状态与结果转交。

当前状态：

- 阶段1：`PASS_ACCEPTED`
- 阶段2 Registration/Locator实现：`PASS_ACCEPTED`
- 阶段2真实临时Package验证：`PASS_ACCEPTED`；最终Release保留：`NOT_MATERIALIZED`；生产Package登记：`NOT_CREATED`
- 仓库卫生：`PASS_ACCEPTED`；历史Wave C对象`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`为33文件，当前正式树tracked精确40
- 阶段3规划与实现：`PASS_ACCEPTED`
- 阶段4规划与实现：`PASS_ACCEPTED`
- 阶段5整体：`IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`
- 阶段6状态结果转交：`NOT_GRANTED`
- 最终Package/PackageRoot/生产Registration/Activation/最终安装Skill：`NOT_MATERIALIZED / NOT_CREATED`
- 真实WorkBuddy `LauncherReceiptV1`：`NOT_PROVED`

实时状态、精确Git对象和任务授权只以[`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md)为准。R00已经正式推广并消费。R01已于2026-08-22取得单独授权并执行；HY3路径没有暴露独立原生bundled-script invocation/tool event，因此最终裁决仍为`BLOCKED_EXTERNAL_CONTRACT`，其文档收口已由独立审查批准并在`9eefe8600d9bed0c8ea6024880e4b2d2ef4e3bfc`正式fast-forward；R02-R08因链式阻断均未启动、未授权。

阶段2 Registration/Locator、阶段3 Runtime按需准备和阶段4会话Launcher实现均已接受。阶段2还证明过一次包含Python、FFmpeg、Node的真实临时Package，但临时Package随后已删除；这不能证明最终Release已经保留、生产PackageRoot已经安装登记，也不能证明Installer或最终分发。阶段2合同边界见[`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md)。

本仓库不得运行或指挥视频Pipeline、Provider或媒体生产；这些能力由WorkBuddy依据已验证执行包合同执行，不存在第二个OpenMontage Agent进程。

金钥匙版交付包必须自带并登记完整的私有必带工具链：可用Python 3.10+环境及锁定核心依赖、FFmpeg/ffprobe、Node.js及npm/npx。Node必须满足当前Package内最高要求；因为当前HyperFrames要求Node 22+，不能只锁官方通用README的18+下限。精确`gyan.dev` FFmpeg资产归Package组装供应链候选，接受来源、hash、许可和分发审查，不作为阶段3面向终端用户的下载项。

阶段3已接受的唯一公共入口为`prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`，结果闭集精确为`DETECTION_REPORT / CONSENT_REQUIRED / INTEGRATED / SKIPPED / BLOCKED`。它只对可选Remotion和HyperFrames做有界探测，为缺失或不兼容项生成零下载计划，并只集成用户明确批准的单项能力。阶段3不选择渲染器，不发现、下载或替换Python/FFmpeg/Node，不扫描盘符，也不运行视频；可选下载只使用批准的中国大陆镜像，不得自动海外回退。

阶段4已接受的唯一公共入口为`launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`。它只接受批准Package定义/最终交付Installer owner提供的release-specific immutable `PackageToolDefinitionV1`，恰好启动一个固定Package工具，并返回九值闭集、递归不可改写的`LauncherReceiptV1`。阶段4对Provider和Runtime保持opaque，不选择Remotion、HyperFrames或任何其他Provider/Runtime。

阶段5尚未完成：入口代码已交付，但真实集成仍不完整。完整PASS必须同时有五类证据：持久final Release/PackageRoot；生产Registration+Activation及新进程Locator；无placeholder且唯一的最终安装Skill；HY3真实WorkBuddy取得真实`LauncherReceiptV1`；独立审查、正式Git/CI和无歧义live authority。Provider、媒体/视频、Remotion/HyperFrames下载安装、Stage6转换代码和完整业务E2E不属于阶段5完成前置。阶段5之后先判断能否直接复用回执；整个项目业务E2E另行处理，不称为阶段7。

历史证据可以保留旧阶段3签名、Package绑定能力模型或阶段4实施前Gate，但这些内容只代表historical记录，不覆盖上述当前已接受接口与状态。
