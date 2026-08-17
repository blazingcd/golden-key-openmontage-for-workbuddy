# 金钥匙 WorkBuddy Shell V2

WorkBuddy Shell V2负责把腾讯WorkBuddy可靠连接到经过身份验证、版本化的金钥匙版OpenMontage执行包。WorkBuddy是唯一运行中的Agent；它读取执行包Guide后承担OpenMontage生产角色。Shell只负责六个模块：安装与生命周期、执行包登记与定位、Runtime按需准备、会话Launcher、WorkBuddy入口、状态与结果转交。

当前状态：

- 阶段1：`PASS_ACCEPTED`
- 阶段2：`REOPENED_REQUIRED_TOOLCHAIN_PACKAGE_REFRESH`（只登记Python的旧Package为`PASS_ACCEPTED_HISTORICAL`）
- 仓库卫生：`PASS_ACCEPTED`，正式对象`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`，精确33文件
- 阶段3规划：`REOPENED_OPTIONAL_CAPABILITY_RECLASSIFICATION_REQUIRED`
- 阶段3实现：`NOT_GRANTED`
- 阶段4 Launcher：`NOT_GRANTED`
- 阶段5 WorkBuddy入口：`NOT_GRANTED`
- 阶段6状态结果转交：`NOT_GRANTED`
- 必带工具链纠偏文档：`REVIEW_READY`

当前任务只把阶段2重新登记前置条件、阶段3 Runtime范围及WorkBuddy唯一Agent结论统一到现有权威中，不构成实现授权。实时状态和精确Git对象只以[`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md)为准。

当前唯一生产实现是旧Package的Registration与Locator；它是历史已接受证据，不是新版Package验收。重新登记裁决见[`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md)。

本仓库不得运行或指挥视频Pipeline、Provider或媒体生产；这些能力由WorkBuddy依据已验证执行包合同执行，不存在第二个OpenMontage Agent进程。

金钥匙版交付包必须自带并登记完整的私有必带工具链：可用Python 3.10+环境及锁定核心依赖、FFmpeg/ffprobe、Node.js及npm/npx。Node必须满足当前Package内最高要求；因为当前HyperFrames要求Node 22+，不能只锁官方通用README的18+下限。只登记Python的旧阶段2结果仅是历史证据，不是本次交付验收。精确`gyan.dev` FFmpeg资产改归Package组装供应链候选，接受来源、hash、许可和分发审查，不再作为阶段3面向终端用户的下载项。

阶段3只负责WorkBuddy/OpenMontage已经选择并锁定的一个可选能力：Remotion或HyperFrames，以及该能力Lock明确声明的附属资产。阶段3不选择渲染器，不预装两种渲染器，也不发现、下载或替换Python、FFmpeg、Node。终端用户可选下载必须先形成精确missing-only计划、取得明确同意并使用批准的中国大陆镜像，不得自动海外回退。阶段3与阶段4在真实会话中的暂停/继续合同必须来自真实WorkBuddy消费者，Shell不得预先猜测。

旧阶段3任务包、公共入口签名和全组件Runtime Lock均已标记`SUPERSEDED`，原条件授权暂停。只有阶段2登记完整必带工具链，并从真实WorkBuddy/OpenMontage消费者冻结新的可选能力输入合同和精确任务包后，阶段3才可能获得实现授权；当前仍为`NOT_GRANTED`。
