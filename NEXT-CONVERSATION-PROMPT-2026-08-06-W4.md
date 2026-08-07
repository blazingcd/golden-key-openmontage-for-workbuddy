# Golden Key OpenMontage for WorkBuddy：W4继续开发Prompt

请在`<WORKBUDDY_REPO_ROOT>`继续工作。先完整读取`AGENT_GUIDE.md`，然后读取：

1. `PROJECT-STATE.md`
2. `docs/workbuddy/ARCHITECTURE.md`
3. `docs/workbuddy/ROADMAP.md`
4. `docs/workbuddy/W3-OFFLINE-RELIABILITY-REPORT-2026-08-06.md`
5. `docs/workbuddy/W2-MCP-DECISION-2026-08-06.md`
6. `docs/workbuddy/LOCAL-STORAGE-POLICY.md`
7. `docs/workbuddy/CORE-SYNC-POLICY.md`
8. `WORK-LOG.md`最后一条记录

## 当前权威基线

- Core=`golden-key-v0.3.21`；contract ID=`golden-key-workbuddy-callable-core-v1`；1566个managed文件只读。
  该Core只用于第一个轻量安装包的构建与调用链验证，不是最终Core版本；Golden Key Core正在进行较大调整。
- authority=`direct_agent`；WorkBuddy是唯一Agent；nested Agent Host forbidden。
- 四个Golden Key业务Pipeline、44个Pipeline Skill、Schema/Reviewer/Checkpoint/Tool Registry合同完整。
- W0首个`Pre-Alpha`公开基线已发布；W1同步/包/doctor/gate/Skill/CI完成；W2调用、任务和
  `MCP=optional`裁决完成；W3离线可靠性Gate=`PASS`。
- W3验证Python/Node子进程网络继承、SaaS/private Core仓库不可用、CLI/MCP/任务统一脱敏；
  WorkBuddy专项=`76 passed`，完整回归=`1136 passed, 10 skipped, 1 subtest passed`。
- CLI是权威回退；MCP仅是本地stdio结构化工具增强，活动配置尚未进入仓库发行面。
- 当前仍为`Pre-Alpha`，尚未通过W4全新Windows安装和普通用户WorkBuddy验收，不得声明
  “已经可以安装”或`OFFLINE ADAPTER READY`。
- W4已经完成经用户确认的Python依赖准备纵向切片：`runtime plan`零写入，
  `runtime prepare --confirm-download`只写入所选数据目录并由launcher优先使用；Python必需、FFmpeg在合成/媒体
  处理时必需、Node仅在Remotion/HyperFrames路径需要。完整真实requirements下载仍需单次明确同意后验收。
- W4已经完成同版本重复注册修复切片：覆盖解压目录只按Manifest白名单进入正式安装；程序目录或项目自有Skill
  被手动删除后可从同一或不同解压目录修复；用户数据独立保留；同名外来Skill和无效所有权记录fail closed。
- W4已经实现严格向前的跨版本升级、doctor失败自动恢复旧程序/Skill，以及默认保留DataRoot的中文卸载入口；
  旧包降级拒绝，升级DataRoot漂移在写入前拒绝，外来或所有权不匹配的Skill不删除。
- r11已在真实Windows默认路径完成安装、两个Skill发现和中文CMD自卸载，并修复“开发仓库cwd遮蔽已安装包”和
  “自卸载后程序目录残留”两个真实缺陷。portable bundle=`17 passed`，WorkBuddy专项=`102 passed`，完整回归=
  `1162 passed, 10 skipped, 1 subtest passed`，W0=`PASS`。
- 提交前最终候选为r18：安装器增加统一原生stderr失败出口；ZIP SHA-256=
  `310050115DA8EAD14B1131C9AC51C95B9A67CC478CA2B829C13C15E366429BF3`，大小`72,806,177`字节。最终W0候选9个文件，
  snapshot SHA=`bb47187cad702320da29dc7c3aa21bbde92bb3f2d9c0b269ede45477d849ad2c`，证据在
  `D:/WorkBuddyData/Temp/w4-clean-client-final-publication-audit-20260807-r17`。
- r11真实客户端自然语言路由没有通过：`我不知道怎么开始做视频`进入WorkBuddy通用视频流程，没有进入
  `golden-key-openmontage-onboarding`。该项是当前明确阻断，不能因为Skill已发现而标记完成。
- WorkBuddy消费层已增加生产工具API Key引导和本地配置入口：用户不在聊天中发送Key；
  `配置API密钥.cmd`隐藏录入并用Windows当前用户DPAPI保存到DataRoot，launcher只向当前进程解密注入。
  `config guide`只报告`present_unverified/partial/not_configured`和Key名称，不返回Key值、不联网。
- Key录入不等于账号、余额、网络或模型可用性已验证，也不授权真实/付费Provider调用。r18不包含该增量，已过期；
  必须以最新源码重建候选并重新给出ZIP SHA和W0证据。
- 本次验收已卸载并清理到纯新起点：默认程序根、两个Golden Key Skill和MCP注册均不存在，WorkBuddy进程为0；
  本项目验收会话已从客户端可见状态删除。没有清空用户账号、其他项目或全局WorkBuddy数据。

## W4目标

1. 当前`PKG-001`已冻结首包为`portable ZIP + PowerShell注册脚本`，不是Setup.exe/MSI。保持已完成的
   Python托管依赖合同和Python/Node/FFmpeg矩阵，不盲目携带全部运行时。
2. 以TDD查明并修复真实WorkBuddy的Skill自然路由/优先级问题；必须在真实客户端证明模糊请求进入新手引导、具体请求
   交给生产Skill。不得通过改写提示词文档伪装真实触发成功。
3. 打包两个可导入WorkBuddy Skill和完整v0.3.21 Callable Core；清楚标记它只是首包验证基线，普通用户不得
   另外下载Golden Key私有Core。Core后续只能通过新不可变Release合同更新。
4. 按`MCP=optional`提供明确选择：默认CLI可用；启用MCP时只生成用户级stdio配置和首次信任指引，
   不覆盖已有配置，并提供禁用/卸载路径。
5. 编写中文快速开始、自然语言示例和故障排查；所有状态继续明确`Pre-Alpha`，不声称Provider生产验收。
   API Key配置必须使用本地隐藏输入和当前用户加密存储，不得要求用户把Key发送到WorkBuddy聊天。
6. 默认目录首装与自卸载已通过；下一步继续验证真实跨版本升级、自然语言触发、Pipeline选择、Stage Skill、本地Tool、
   长任务状态/恢复和Human Checkpoint。真实Provider成片保持独立授权Gate。
7. 每个安全可验证增量更新`PROJECT-STATE.md`、追加`WORK-LOG.md`、重跑W0并持续提交推送。

## 发布红线

- 不修改v0.3.21 managed Core；Core改动只能通过新的不可变Release合同迁移。
- 不修改Golden Key SaaS/private Core仓库，不直接同步官方OpenMontage或private Git ancestry。
- 不调用真实/付费Provider，除非用户针对该次验证另行明确授权。
- 不覆盖或删除用户已有WorkBuddy配置、项目、Artifact、模型、缓存或凭据。
- W4全新安装和真实WorkBuddy普通用户验收通过前，不声明`OFFLINE ADAPTER READY`。
