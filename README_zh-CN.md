# 金钥匙 WorkBuddy Shell V2

WorkBuddy Shell V2负责把腾讯WorkBuddy可靠连接到经过身份验证、版本化的金钥匙版OpenMontage执行包。WorkBuddy是唯一运行中的Agent；它读取执行包Guide后承担OpenMontage生产角色。Shell只负责六个模块：安装与生命周期、执行包登记与定位、Runtime按需准备、会话Launcher、WorkBuddy入口、状态与结果转交。

当前状态：

- 阶段1：`PASS_ACCEPTED`
- 阶段2 Registration/Locator实现：`PASS_ACCEPTED`
- 阶段2真实临时Package验证：`PASS_ACCEPTED`；最终Release保留：`NOT_MATERIALIZED`；生产Package登记：`NOT_CREATED`
- 仓库卫生：`PASS_ACCEPTED`，正式对象`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`，精确33文件
- 阶段3规划：`PASS_ACCEPTED`
- 阶段3实现：`NOT_GRANTED`
- 阶段4 Launcher：`NOT_GRANTED`
- 阶段5 WorkBuddy入口：`NOT_GRANTED`
- 阶段6状态结果转交：`NOT_GRANTED`
- 阶段3接管前规划文档：独立审查并正式fast-forward后`PASS_ACCEPTED`

当前任务只把缩减后的阶段3接管前规划统一到现有权威中，不构成实现授权。实时状态和精确Git对象只以[`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md)为准。

当前唯一生产实现是阶段2 Registration与Locator。该实现和一次包含Python、FFmpeg、Node的真实临时Package验证已经接受，但临时Package随后已删除；这不能证明最终Release已经保留、生产PackageRoot已经安装登记，也不能证明Installer或最终分发。合同边界见[`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md)。

本仓库不得运行或指挥视频Pipeline、Provider或媒体生产；这些能力由WorkBuddy依据已验证执行包合同执行，不存在第二个OpenMontage Agent进程。

金钥匙版交付包必须自带并登记完整的私有必带工具链：可用Python 3.10+环境及锁定核心依赖、FFmpeg/ffprobe、Node.js及npm/npx。Node必须满足当前Package内最高要求；因为当前HyperFrames要求Node 22+，不能只锁官方通用README的18+下限。精确`gyan.dev` FFmpeg资产归Package组装供应链候选，接受来源、hash、许可和分发审查，不作为阶段3面向终端用户的下载项。

阶段3只负责WorkBuddy/OpenMontage已经选择并锁定的一个可选能力：无需可选能力、Remotion或HyperFrames，以及Package自有能力Lock明确声明的附属资产。建议唯一入口为`prepare_optional_capability(data_root, capability_request, authorization_receipt=None)`；未来最大代码面为一个新增模块、一次仅导出修改和一个直接测试文件。阶段3不选择渲染器，不预装两种渲染器，不发现、下载或替换Python/FFmpeg/Node，不扫描盘符，也不运行视频。终端用户可选下载必须先形成精确missing-only计划、取得明确同意并使用批准的中国大陆镜像，不得自动海外回退。

最终用户从阶段5进入：阶段5先通过阶段2重验生产Package；阶段4可以使用必带工具链发起基础固定工具调用，只有可选Remotion/HyperFrames执行才额外需要绑定同一Registration和能力Lock的阶段3回执。暂停、同意与继续由WorkBuddy负责，阶段6只转交事实，Shell不得自动重放原业务请求。

旧阶段3任务包、公共入口签名和Shell自有全组件Runtime Lock均已标记`SUPERSEDED`。只有最终Release已保留并完成安装和生产登记、Locator在新进程验证成功、Package自有能力Lock与真实WorkBuddy暂停/同意/继续合同已经冻结、精确Builder任务包获得明确授权后，阶段3才能启动；当前仍为`NOT_GRANTED`。
