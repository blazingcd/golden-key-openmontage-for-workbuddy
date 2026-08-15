# Project State

更新时间：2026-08-15

## 2026-08-15 WorkBuddy Shell V2 统筹文档基线

- Shell V2统筹已经从聊天记忆迁移到版本化文档，权威入口为`docs/workbuddy/v2/README.md`。
- 项目章程、防漂移停止规则、八阶段任务账本、阶段1执行计划和验收矩阵已经固化。
- 当前状态为`GOVERNANCE_DOCS=DONE / STAGE_1=READY_NOT_STARTED`。
- 阶段1启动授权在本套文档审阅后仍为`NO`；当前没有创建`codex/workbuddy-shell-v2`分支或独立worktree，没有修改生产代码、Skill、安装器、测试或Core。
- 已批准的V2代码基线仍为`2a2bf09832d558388dc2816c54b32a2dce4aa607`。后续阶段1从该固定提交建立worktree，再选择性带入本次治理文档，不merge/rebase推进中的`main`或旧长期分支。
- 最高职责原则已冻结：WorkBuddy是唯一对话Agent，OpenMontage Core是唯一生产决策与执行权威，Shell只负责安装、对象锁定、环境绑定、会话入口以及状态和结果转交；Shell不得成为第二个Director或生产状态机。
- 长期工作区既有未跟踪`.codex/config.toml`与`docs/workbuddy/WORKBUDDY-SHELL-V2-REFACTOR-HANDOFF-2026-08-15.md`继续原样保护，不属于本次权威文档提交。

## 当前里程碑

`WB-OFFICIAL-SUCCESS-CLOSEOUT1 COMPLETE / OFFICIAL OPENMONTAGE RUNNABILITY PASS / STRICT MANIFEST CONFORMANCE PARTIAL / W0 DONE / W1 DONE / W2 DONE / W3 PASS / WB-UX1 ROUTING PENDING / W4.1 PORTABLE-PYTHON VALIDATION PASS`

新的 W0 只审计 `golden-key-v0.3.21` WorkBuddy Callable Core Release 导出包、公开
`origin/main` lineage 和 WorkBuddy 自有增量。技术 Gate 已通过；用户在看到完整报告和目标提交后
明确授权推送，首个 `Pre-Alpha` 公开基线已发布到 `origin/main`。

## 2026-08-14 官方 OpenMontage 成功证据收口

### 当前权威结论

- 官方 OpenMontage 固定提交 `4eab34c5cfcccaa4f1970554928feccce73ee930` 已在真实 WorkBuddy 中跑通并生成用户基本认可的本地成片：`PASS`。
- `REAL_WORKBUDDY`、`CAPABILITY_REAL`、`LOCAL_RENDER_E2E`、`BUSINESS_EFFECTIVE`：`PASS`。
- HY3 确实从原始门店素材重新选材、调色、剪辑、配字幕/BGM并完成本地成片；Kimi 首次展示复用旧片，`v2` 是同一 15 段方案重新编码，`fresh` 才是重新审阅 29 段原始素材、选择 14 段并重新剪辑的新版本。
- `STRICT_MANIFEST_CONFORMANCE`：`PARTIAL`。checkpoint 缺失、canonical/fresh 并列、报告/发布指针不一致等属于稳定化、可恢复性和治理问题，不否定官方原包已经跑通。
- 外部平台发布、Provider/cloud/SaaS E2E：本阶段 `OUT OF SCOPE`，不是失败或阻断项。
- 一次受控 preflight 在 WorkBuddy 内置 Python 路径因缺少 `requests` 失败，只证明该次解释器/命令路径失败，不能推翻显式项目 `.venv` 和本地 FFmpeg 已完成的成功链路。
- 下一 Gate 尚未执行，不得提前宣称通过；后续顺序由统筹另行裁决。

### 成功证据与环境收口

- D 盘证据归档：`D:\WorkBuddyData\Evidence\openmontage-official-success-closeout-20260814`。
- 归档包含两条成功 WorkBuddy JSONL、公开链接和归因说明、关键项目 artifacts、三份成片哈希清单、两份源码区脚本原始副本及 quarantine、副本完整的用户级 FFmpeg Skill、画像当前版和可证明的任务前版本、运行路径差异与 `RESTORE-MANIFEST.md`。
- 官方目录两份未跟踪脚本 `scripts\prepare_fresh_edit.py`、`scripts\render_portrait.py` 已在复制和逐文件 SHA-256 校验后移入归档 quarantine；官方 HEAD 仍精确为 `4eab34c5...`，tracked diff=0、staged=0、普通 `git status` 干净。
- `projects\toutouxiang-store-intro` 和三份成片保持原位，收口前后哈希不变；未触碰 tracked 源码、`.venv`、`node_modules`、缓存或其他 ignored 文件。
- 初次收口时因 WorkBuddy 仍有活动进程，没有竞争性移动全局 Skill 或回写画像。用户随后确认客户端完全退出；执行前、中、后相关进程均为 0，剩余环境隔离现已 `COMPLETE`。
- 活动 `openmontage-ffmpeg-portrait-render` Skill 已在移动前再次复制并逐文件核验，随后可恢复地移动到归档 `quarantine\workbuddy-skill-openmontage-ffmpeg-portrait-render-20260814T161526+0800\`；活动路径不再存在，两个文件 SHA 与既有归档一致。
- 覆盖前的 `IDENTITY.md`、`SOUL.md`、`USER.md` 已再次快照到 `profiles\pre-restore-current-20260814T161526+0800\`。活动画像已使用 `profiles\pre-store-tasks\` 的可证明完整版本恢复，SHA-256 分别为 `EA88682EFDE077F73D6D7625B03915455C87FEC5B4D5ADD6CA7C5842D8BB92E0`、`09E4782B1CE17312C22050947B3D5C699C3B51D391669A1BFB66A5CD36971EF4`、`5ABB73720FABC14F3C602CD0C0FFE6AC8D798BEB29278B3C12910617522ED06E`。
- `.mcp.json` 与其他无法归因配置未修改；已恢复启用的 `golden-key-video-agent` 仅做只读状态记录，未触碰。

### 运行路径差异

- 失败基线的 agent shell 裸 `python/python3` 默认落到 WorkBuddy 内置 Python；该解释器缺 `requests`，`registry.discover()` 在导入 ComfyUI client 时失败。
- HY3 对依赖重的 registry preflight 和 `init_project()` 显式使用官方项目 `.venv\Scripts\python.exe`；后续项目级 `render_full.py` 使用标准库、`subprocess` 和 FFmpeg，即使在内置 Python 上也完成成片。
- Kimi fresh 的 `prepare_fresh_edit.py`、`render_portrait.py` 明确使用官方项目 `.venv\Scripts\python.exe`。
- 因此 Host 解释器不是已证明的全局主阻断，而是与具体 Agent 命令路径和依赖集合相关的偶发可靠性风险；后续应按步骤锁定解释器。
- HY3 原始成片早于 Kimi 两份源码脚本和用户级 Skill 创建，故不依赖它们；Kimi `v2/fresh` 直接依赖源码脚本，但成功命令没有把用户级 Skill 作为必经执行入口。

### 中文 fork 身份

- 正确中文 fork：`https://github.com/noah-1106/openmontage-zh-mcp`，不是 `OpenMontage-golden-key`。
- 本专项采用的已确认只读值为远端 `main/HEAD=1aa30636325bb1dab60e81d1bf76d6df2dd662ca`；本任务没有下载或验证该 fork，后续实际使用前仍须按运行时重新锁定。

### Git 集成状态

- 收口文档源提交形成于独立任务分支 `codex/wb-official-success-closeout1`。
- 初始收口提交 `3ca7dfb` 与后续环境隔离完成提交按顺序选择性 cherry-pick 到主协调长期分支 `codex/w4.1-portable-python`；未 merge、未 rebase、未从 `main` 同步。
- 主协调工作区未跟踪 `.codex/config.toml` 全程保持原样、未暂存，SHA-256 仍为 `E5D533440B4EF6587293B3596DDA46DD8525F9A39107108B75C67B6F2E49AAFC`。

### 零边界

本收口零 Provider 调用、零费用、零新 WorkBuddy 会话/运行、零 preflight/测试/W0/repair、零媒体生成、零中文 fork 下载、零 v0.3.23 验证。

## 当前权威基线

| 项目 | 当前值 |
|---|---|
| Release | `golden-key-v0.3.21` |
| Source commit（仅provenance） | `757ea3822e5f2eef7f341389983119021e827c8d` |
| ZIP SHA-256 | `DC21792B6F9D773B1559B1687DEE0CC78FCBFC442400D71A735F7EE375426599` |
| Contract ID | `golden-key-workbuddy-callable-core-v1` |
| Authority | `direct_agent` / nested Agent Host forbidden |
| Managed files | `1566`，目标清单和每文件hash/mode完全匹配 |
| Public base | `origin/main` / `4eab34c5cfcccaa4f1970554928feccce73ee930` |
| Private ancestry | 不属于发布候选；source commit不是当前`main`祖先 |
| Public baseline | `e4f7577bad99e93e0a35217940d8c17f7a6d81cb`，已推送到`origin/main` |

## DONE

- Release ZIP、GitHub asset digest、外部 SHA sidecar、外部/内嵌 lock 完整核验。
- managed scope 精确镜像；公开基线首次导入改写 96 个文件，第二次同步 0 改动。
- 六个 `consumer_remove_paths` 均不存在；`requirements.txt`、`setup.py`、README、配置、同步脚本和文档均保留。
- 同步器对 forbidden path、hash/mode、缺失、额外、scope 漂移、六路径漂移和幂等风险建立负测。
- 四个 Golden Key Pipeline、44 个 Pipeline Skill、Reviewer/Checkpoint、Schema、Tool Registry 和 10 个变更合同测试通过完整性核验。
- 回归：contracts `716 passed, 7 skipped`；tools `284 passed, 1 subtest passed`；WorkBuddy `15 passed`。
- 公开性扫描、direct-agent静态隔离和公开Git lineage Gate通过；未扫描或引入Golden Key私有历史。
- 旧`v0.3.18`整仓发布W0报告保留并脱敏，明确标记为历史且已被取代。
- 首个完整`Pre-Alpha`公开基线已发布；远端`origin/main`核验为`e4f7577bad99e93e0a35217940d8c17f7a6d81cb`。
- W1新增`sync-release`维护者命令：缓存缺失时只下载三个固定Release资产，验证后原子发布缓存；缓存命中时完整复核并复用。
- 真实v0.3.21 D盘缓存回归：1566个文件验证通过，0改动、0删除；当前WorkBuddy专项`18 passed`。
- W0 Pipeline比较基线已固定为配置中的`upstream_base_commit`，不再因首次推送后`origin/main`前移而误报0个合同变化。
- W1建立独立Python发行`golden-key-openmontage-workbuddy==0.1.0a0`和`golden-key-workbuddy`命令。
- `doctor`可验证v0.3.21合同、direct-agent authority、四Pipeline、Python/Node/FFmpeg并建立D盘目录。
- `gate`持续拒绝六个禁入路径、嵌套Agent Host导入和W2裁决前的活动`.workbuddy/mcp.json`。
- WorkBuddy Skill与`.workbuddy`骨架已建立；当前明确为Skill-first，MCP裁决为`optional`，CLI为权威回退。
- 维护者环境已完成固定Release `sync-release`幂等复核；公开CI不依赖私有Core凭据，执行W1 Gate和完整测试。
- 本轮真实D盘验证：1566文件、0改动、0删除；Skill校验通过；contracts `716 passed, 7 skipped`；
  tools `284 passed, 1 subtest passed`；WorkBuddy `27 passed`；W1增量公开审计=`PASS`。
- W2第一段直接调用基线已建立：`context`、`pipelines`、`project create/status`、`stage inspect`、
  `artifact validate`和`checkpoint submit`。
- WorkBuddy仍是唯一Pipeline选择者；CLI只读取已绑定Pipeline和当前Stage合同，不推荐、排序或重选。
- 项目目录限制在`<data-root>/Projects/<project-id>`；Artifact/Checkpoint输入限制在项目`artifacts/`内；
  项目ID穿越、Pipeline重绑定、缺少Manifest产物和未批准完成均fail-closed。
- W2离线生命周期测试封锁socket后通过，Provider调用和嵌套Agent调用均为0。
- W2受限Tool切片已建立：`tool list`只返回当前Stage Manifest allowlist、输入Schema和Layer 3 Skill；
  `tool execute`要求项目内请求/路径和Skill确认，只允许本地、零网络、零估算成本工具。
- API/Hybrid及声明需要网络的工具在状态探测和`execute()`前fail-closed；`video_selector`负测在socket封锁下
  网络尝试、Tool调用和Provider调用均为0。
- 原生`scene_detect`已在项目内真实执行：Tool调用1次、Provider调用0次、成本0，输出场景JSON通过路径复核。
- 当前回归：WorkBuddy `51 passed`；contracts `716 passed, 7 skipped`；tools `284 passed, 1 subtest passed`；
  完整套件`1111 passed, 10 skipped, 1 subtest passed`；W1 `python -S` Gate=`PASS`；Skill格式校验=`Skill is valid!`。
- W2 Tool增量公开审计=`PASS`：1566个Core文件匹配，候选12个文件，公开性/lineage/运行时/回归全通过；
  private Core历史未扫描且不在候选中；最终候选摘要保存在D盘审计证据目录并在发布报告中给出。
- 用户提供的CI `31077036248`属于提交`facc548`的历史失败；顶层W2依赖问题已由`e227660`修复，
  后续CI `31077374841`在同一`main`上完整通过。
- W1～W4明确只修改消费方层；v0.3.21 managed Core快照保持只读，Core变更只能通过新Release合同迁移。
- W2模型配置分层已建立：`config inspect`明确WorkBuddy主对话模型由WorkBuddy Host管理，生产Provider由
  Golden Key Tool Registry管理；Adapter不保存或代理主模型凭据，不允许嵌套Agent Host。
- 国内生态生产能力只报告Registry已核验的6组Provider：DashScope、豆包、火山即梦、可灵官方为厂商直连；
  Seedance、MiniMax当前实现明确标为第三方网关，不把模型品牌误报为国内直连。
- `config template`在`D:/WorkBuddyData/Config`生成只含环境变量名称的消费方模板；密钥值不读取到输出、
  不落盘，重复生成幂等，用户修改后的文件拒绝覆盖。专项`51 passed`，socket封锁下网络/Provider调用均为0。
- 本增量W0公开性审计=`PASS`：Release/Pipeline/运行时/公开lineage/候选风险/回归全部通过，候选12个文件，
  snapshot SHA=`d4e9c91ae51035e453fc0f2141d749e8bc29f361a43beea6e32463dca3911204`；证据位于
  `D:/WorkBuddyData/Temp/w2-model-provider-config-publication-audit`，private Core历史未扫描且不在候选中。
- W2本地Tool持久任务入口已建立：`task submit/status/run/cancel/recover`将状态保存在D盘`Jobs`目录；
  输入hash和任务身份防篡改，稳定task ID、重复提交和成功终态重放可防止重复执行。
- 当前取消合同已如实冻结：queued任务可取消；Core blocking Tool开始运行后没有通用安全取消协议，CLI明确拒绝
  运行中取消，不伪称成功、不杀进程；中断任务只恢复为failed且禁止自动重试，避免局部文件副作用重复发生。
- 本地Tool执行新增socket-denial边界；误声明为local的Tool即使尝试联网也会在真实socket调用前失败。
  Hybrid/API仍在状态探测和任务落盘前拒绝。任务/Skill专项`13 passed`，完整WorkBuddy专项`61 passed`。
- 本增量W0公开性审计=`PASS`：1566个Core文件精确匹配，15个候选文件与managed Core重叠为0；
  Release、四Pipeline/44 Skill、运行时隔离、公开lineage、风险扫描和回归全部通过，private Core历史未扫描且不在候选中。
- 真实WorkBuddy 5.3.8离线对照已通过：本地Skill安装并启用；Skill+CLI读取Guide并运行`doctor/context`，
  两条命令退出码0；Skill+stdio MCP首轮16/16工具绿色在线，`context/pipelines`均`pass`；最终等价面补齐
  `golden_key_tool_execute`后固定为17个Schema工具。
- MCP失败路径只调用一次非法task status，未重试，业务`status=fail`且Tool/Provider/网络调用均为0；
  WorkBuddy模型侧未稳定呈现MCP传输层`isError`，因此业务`status/errors`继续作为强制错误合同。
- W2 MCP Gate=`PASS / optional`：CLI是必选和权威回退；stdio MCP只作为本地结构化Schema/工具发现增强，
  不复制业务逻辑，不是远端服务或第二个Agent。完整W4安装/普通用户验收仍未通过。
- 本增量专项=`66 passed`，完整回归=`1126 passed, 10 skipped, 1 subtest passed`；最终W0公开性审计=`PASS`，
  1566个Core文件精确匹配、17个候选文件、snapshot SHA=
  `5b1bd5dbb401dad6cf1e313a071c6f3dd481b85af449fd4217ce20fd1a9a4064`，private Core历史未扫描且不在候选中。
- W2跨任务执行合同已建立：同一D盘数据根使用原子执行槽把跨项目并发固定为1；竞争任务保持queued、
  attempt_count不增加、Tool调用为0且不自动重试。中断恢复只释放与该任务身份匹配且进程已死亡的遗留执行槽。
- `task run`默认记录3600秒可观测截止时间并允许显式设置大于0且不超过86400秒；超过截止时间时
  `task status`报告`timeout_exceeded=true`，但因Core无通用协作式取消而不会强杀、伪称取消或自动重试。
- 本轮任务/MCP专项=`19 passed`；完整WorkBuddy专项=`70 passed`；完整回归=
  `1130 passed, 10 skipped, 1 subtest passed`；W1 `python -S` Gate和Skill格式校验均通过。
- 本轮最终W0公开性审计=`PASS`：1566个managed Core文件精确匹配，四Pipeline/44 Skill、运行时隔离、
  公开lineage、风险扫描和回归全部通过；private Core历史未扫描且不在候选中。证据位于
  `D:/WorkBuddyData/Temp/w2-concurrency-timeout-publication-audit-20260806-final`。
- W3把本地Tool网络边界继承到其Python/Node子进程：真实loopback监听器负测确认连接未建立；
  Python通过`sitecustomize`、Node通过`NODE_OPTIONS --require`加载消费方离线guard，执行结束后环境恢复。
- W3统一脱敏runtime、CLI、MCP和任务原子JSON：Tool异常、Schema错误、Bearer文本、环境密钥和明确敏感字段
  均替换为`[REDACTED]`，CLI/MCP语义负测和任务落盘负测通过。
- SaaS/private Core仓库路径指向不存在目录、测试进程从仓库外启动时，direct-agent context和离线项目创建仍通过；
  证明当前WorkBuddy运行时不依赖Golden Key SaaS仓库。
- W3专项=`6 passed`；WorkBuddy专项=`76 passed`；完整回归=`1136 passed, 10 skipped, 1 subtest passed`；
  W1 `python -S` Gate、22个消费方Python源码内存编译和`git diff --check`通过，Provider调用0。
- W3离线可靠性Gate=`PASS`，证据见`docs/workbuddy/W3-OFFLINE-RELIABILITY-REPORT-2026-08-06.md`；
  该裁决不等于W4安装/普通用户验收，也不允许声明`OFFLINE ADAPTER READY`。
- `WB-UX1`已作为独立消费方任务从W2/W4拆出：新增`golden-key-openmontage-onboarding` Skill，
  只处理不知道如何开始、询问能力或模糊视频意愿；读取本机真实能力后用中文业务结果和少量示例引导。
- 新手引导在用户形成具体请求后立即交给`golden-key-openmontage`生产Skill；不盘点SaaS素材库、不复制Core
  生产需求澄清、不创建生产项目、不调用真实/付费Provider，也不修改1566个managed Core文件。
- `WB-UX1`已补齐消费端素材交接对话：根据用户情况引导附加相关现有素材、提供参考内容，或在无素材时
  先说明真实对象和观众行动；每轮最多问一个相关问题，不要求盘点整个素材库，不硬编码盘符或伪报已导入。
- `WB-UX1`与生产Skill已补齐API Key配置引导：`config guide`只报告能力、Provider和Key名称/存在状态；
  不返回Key值、不联网。用户通过包内`配置API密钥.cmd`隐藏录入，凭据使用Windows当前用户DPAPI保存到
  独立DataRoot，launcher仅向当前进程解密注入；`present_unverified`只表示“已录入但未验证”。
- 保存Key不授权联网、连通性测试、余额检查或真实/付费生成；这些动作仍需单次独立授权。
- API Key引导已进一步改为目标优先：用户先选择生成图片、生成视频、中文配音、数字人或内容分析；报告和本地
  向导用中文显示推荐Provider、直连/网关属性、官方申请入口、友好凭据名称、账户权限与费用提醒。只有用户明确
  选择现在配置后，WorkBuddy才可用`Start-Process`打开可见本地窗口；Key仍不进入进程参数或聊天。
- launcher固定启用Python UTF-8输出，避免中文Provider/能力信息经过PowerShell和WorkBuddy时乱码。
- 目标优先API引导候选r25位于
  `D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-goal-first-api-guide-20260808-r25`；ZIP大小`72,817,257`字节，
  SHA-256=`d572aaff91e4863886e694a08af3f8148000e083d18978578d23fb9677cea725`。隔离安装中选择“生成视频”后，
  仅火山即梦和可灵官方标为推荐，普通Provider列表不显示环境变量名；取消不创建凭据，网络/Provider调用0。
- 独立前向测试首次发现依赖缺失时误导用户重装ZIP；Skill已改为先给出`runtime plan`并等待明确下载同意，依赖
  准备前仍可提供API配置建议。第二次安装态复测正确推荐可灵官方+豆包语音，并区分运行时下载和API配置两次授权。
- 当前WorkBuddy专项=`109 passed`，两个Skill格式校验和PowerShell解析通过；r25隔离安装已卸载，程序与两个Skill
  均不存在，默认WorkBuddy安装根仍不存在，WorkBuddy进程为0。
- 本增量最终W0=`PASS`：Release合同、1566个Core文件、四Pipeline/44个阶段Skill、Schema/Tool/Checkpoint合同、
  direct-agent边界、公开lineage、风险扫描和回归全部通过；private Core历史不在候选中。证据目录为
  `D:/WorkBuddyData/Temp/w4-goal-first-api-guide-publication-audit-20260808-r25-final`。
- `WB-UX1`验证：Skill Creator格式=`Skill is valid!`；WorkBuddy专项=`78 passed`；消费方Gate=`PASS`，
  静态隔离违规0、活动MCP配置不存在、Provider调用0。
- `WB-UX1`真实客户端验收尚未完成：当前Windows应用控制只能读取到WorkBuddy空壳控件树，无法可靠识别
  Skill导入和聊天区域，因此没有盲点或伪报成功；该验收仍属于`WB-UX1`，不并入W4安装包。
- W4已冻结首包为`portable ZIP + PowerShell注册脚本`，不是Setup.exe/MSI。ZIP可解压到任意目录；注册脚本
  复制到稳定用户级目录、建立数据目录、注册生产/新手两个Skill，并写入`WORKBUDDY-RUNTIME.json`定位launcher。
- 普通用户默认路径已纠正为`%LOCALAPPDATA%\GoldenKeyOpenMontageForWorkBuddy`，允许显式覆盖到D盘；
  `D:\WorkBuddyData`只保留为当前维护者开发、构建和烟测策略。
- 首个完整候选包基于v0.3.21的1566个managed文件构建成功，最新ZIP大小`72,795,687`字节，SHA-256=
  `45aec88d6ae339c5ef83cd7d46978663f95a14473ad1bc3e1c9dfecb374317f1`；包内明确声明
  `temporary_first_package_build_baseline_not_final_core`，不把v0.3.21误称最终Core。
- D盘隔离安装烟测通过：两个Skill注册、MCP默认关闭、Core/authority/四Pipeline核验通过；系统Python扫描发现
  `dotenv/google.genai/jsonschema/openai`缺失并返回`degraded`；切换到已准备依赖的Python后
  `doctor/context/pipelines/config inspect`全部退出码0，网络/Provider调用均为0。
- WorkBuddy调用桥已改为注册Skill读取runtime locator并通过稳定launcher先运行`doctor`；`doctor`新增九项Python
  模块只读发现，`config inspect`继续独立检查安全Provider引用。首包现已具备经同意后的依赖准备能力，但尚未完成
  普通用户完整requirements下载和全新Windows验收，不能声明完整可用。
- 首包新增根目录中文双击入口`安装到WorkBuddy.cmd`；注册完成后立即运行一次离线`doctor`，结果与退出码写入
  `WORKBUDDY-INSTALL.json`，WorkBuddy首次调用继续复核。安装链固定使用系统Windows PowerShell，并以.NET SHA-256
  校验文件，降低PATH和PowerShell模块差异风险。
- `setup.py`的官方历史来源已复核，但当前内容是WorkBuddy消费层自有包元数据，Core导出合同禁止覆盖；开发仓库继续
  保留，普通用户ZIP明确排除，用户不需要执行它。
- 根README已改为面向公开用户的差异化介绍：突出WorkBuddy专用direct-agent适配、四条中文商业短视频业务
  Pipeline、中文新手引导与素材/参考内容交接、国内模型生态配置识别、持久任务与轻量ZIP；用户介绍区不再展示
  仓库同步历史、首次推送流程或其他维护者内部信息，并继续明确Pre-Alpha与未验收边界。
- W4运行时准备已扩展为`complete_video_production`标准环境：`runtime plan`只读列出Python、FFmpeg、Node、
  Remotion、HyperFrames和托管浏览器；只有用户接受下载、存储和许可提示后，`runtime prepare --confirm-download`
  才写入所选`<data_root>/Runtime`与`<data_root>/Caches`。不修改系统Python/PATH，不调用Provider。
- 新增`WORKBUDDY-PRODUCTION-RUNTIME.lock.json`，固定Node/FFmpeg发行资产和SHA、Remotion/HyperFrames npm lock
  hash、HyperFrames版本与浏览器版本；组件按所有权记录幂等复用，浏览器可执行文件按记录hash复核。
- 注册launcher只在当前进程优先使用托管Python/FFmpeg/Node/浏览器。生产Skill必须先展示计划并获得一次明确同意；
  安装阶段不要求用户选择Remotion或HyperFrames，具体方案仍按Core规则说明可选路径并等待批准。
- r27已完成真实D盘隔离准备：Runtime=`1,504,426,322`字节（1.401GiB），Caches=`500,145,944`字节
  （0.466GiB）；二次prepare=`created=false/reused=true/network_calls=0`。r28安装复用该DataRoot后
  `doctor=pass`，托管Python/FFmpeg 8.1.2/Node 22.23.2/Remotion 4.0.484/HyperFrames 0.7.101均通过可执行探测。
- 首次浏览器准备真实发现Puppeteer下载器`ECONNRESET`；浏览器现与FFmpeg/Node同样锁定外部URL、大小和
  SHA-256=`ec7d7cfbc9d97093c9269d6a26de78a3244a49f3112ff9616e2ccb5ac3afeb24`，先校验缓存再在staging解压。
  托管Chrome实际运行返回`Google Chrome for Testing 152.0.7928.2`。
- Core `VideoCompose.get_info()`在隔离已安装包报告`ffmpeg=true/remotion=true/hyperframes=true`；这证明本地
  合成能力已被发现，但不等于真实WorkBuddy自然语言路由、Human Checkpoint或Provider成片验收完成。
- r29最终轻量ZIP大小=`72,849,518`字节，SHA-256=
  `abb350f5c004e19f390e56e0fe4b02ab8abe4f4a1581838f55de1c518485b2a2`，位于
  `D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-complete-runtime-20260808-r29`。r29安装器在复用ready DataRoot时
  无网络修复Remotion junction，安装后`doctor=pass`。
- 本增量W0初次最终审计=`PASS`：1566个managed Core文件、四Pipeline合同、direct-agent边界、公开lineage、
  风险扫描与回归全部通过；contracts=`716 passed, 7 skipped`、tools=`284 passed, 1 subtest passed`、
  WorkBuddy=`111 passed`。证据目录为
  `D:/WorkBuddyData/Temp/w4-complete-runtime-publication-audit-20260808-r29-final-r3`。
- W4.1新增`WORKBUDDY-BOOTSTRAP-RUNTIME.lock.json`，固定官方Windows便携Python 3.13.15和pip 26.1.2 wheel；
  launcher优先使用包内Python，普通用户不再需要预装Python，依赖安装到DataRoot私有`site-packages`。
- 真实包探针先发现pip wheel未进入嵌入式`._pth`，修复后`python -m pip`、包导入、无系统PATH启动、四Pipeline发现
  和Manifest更新后hash全部通过。完整运行时准备耗时约10分32秒，网络调用6次、Provider调用0次。
- W4.1真实fresh install -> runtime prepare -> repair矩阵最终`doctor=pass`；Python 3.13.15、FFmpeg 9.0、
  Node 22.23.2、Remotion 4.0.484、HyperFrames 0.7.101和Chrome 152均来自隔离安装/DataRoot。
- Remotion首次冷启动真实超过20秒，doctor探针超时已提高到60秒并补回归；HyperFrames doctor确认受管
  Node/FFmpeg/FFprobe/Chrome，Whisper/Kokoro/MusicGen/Docker daemon仅为可选能力。
- validation-only ZIP为`85,860,139`字节，SHA-256=
  `2b54a4f5cbf8f8c53716a9d1a89684aae759149a3ffedceda56f58c0b3bfa423`，继续明确v0.3.21只是首包临时Core。
  真实自卸载已移除程序和两个Skill；随后整个隔离DataRoot和构建探针均已删除，不影响纯新人工验收起点。
- 当前WorkBuddy全量专项=`119 passed, 1 skipped`；W4.1最终W0=`PASS`：contracts=`716 passed, 7 skipped`、
  tools=`284 passed, 1 subtest passed`、WorkBuddy=`119 passed, 1 skipped`，证据目录为
  `D:/WorkBuddyData/Temp/w41-publication-audit-20260808-final`。
- 最新真实包候选位于`D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-first-bundle-20260807-r5`，ZIP大小
  `72,799,449`字节，SHA-256=`ff7af11546b3e4e0e72fb9f9822375825d7d8dc84476b38528195126d5c0bfb3`。
  D盘真实注册后`runtime plan=needs_confirmation`；未确认prepare退出码1且没有创建Runtime目录。
- 当前WorkBuddy专项=`88 passed`，完整回归=`1148 passed, 10 skipped, 1 subtest passed`；托管环境夹具覆盖
  计划、拒绝、创建、launcher切换和幂等。真实完整依赖下载
  仍需一次明确授权后的普通用户路径验收，本轮没有调用Provider。
- GitHub Actions已恢复；跨平台安装测试修正提交`b33a512`的公开CI `31147633115`=`success`。
- 本增量最终W0=`PASS`：Release、四Pipeline合同、direct-agent运行时边界、公开lineage、风险扫描和回归均通过；
  1566个managed Core文件精确匹配，候选17个文件。private Core历史未扫描且不在候选中；
  证据位于`D:/WorkBuddyData/Temp/w4-runtime-prepare-publication-audit-20260807-final-r2`。
- W4重复注册修复切片已实现：覆盖解压目录中的额外旧文件只记入安装记录，不进入正式程序目录；同版本重复运行
  可替换具有有效所有权记录的程序和两个Skill，程序目录或其中一个Skill被手动删除后可从同一或不同解压目录恢复。
- 数据目录保持独立，修复不删除用户项目、Artifact、配置、模型、缓存或输出；同名外来Skill、无效安装记录或
  无效Skill所有权记录均fail closed并保留原内容；当时跨版本替换先拒绝，随后已由下述正式向前升级合同取代。
- 新真实候选r7位于`D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-tolerant-install-20260807-r7`；ZIP大小
  `72,800,975`字节，SHA-256=`ebf95cd067dce94bdf25f979740484e453df9dcd91b0a3dadde5c08eb6e1589a`。
  D盘隔离矩阵验证覆盖残留忽略、同版本重复、换解压目录、程序/Skill误删修复、数据保留和外来Skill冲突；
  network/Provider调用均为0。即使程序目录已删除，遗留Skill版本与当前包不一致也拒绝静默降级。
  portable bundle专项=`10 passed`，WorkBuddy专项=`95 passed`，完整回归=
  `1155 passed, 10 skipped, 1 subtest passed`。
- 本切片W0公开性审计=`PASS`：1566个managed Core文件精确匹配，Release、四Pipeline合同、direct-agent运行时边界、
  公开lineage、风险扫描和回归全部通过；private Core历史未扫描且不在候选中。证据目录为
  `D:/WorkBuddyData/Temp/w4-tolerant-install-publication-audit-20260807-r7-final`。
- W4跨版本切片已实现：Manifest版本动态决定默认程序目录；严格更高版本可以升级，相同版本继续修复，旧包降级拒绝。
  新版本先替换到活动位置并运行离线doctor，只有pass/degraded才提交；失败会删除新版本并恢复旧程序和两个旧Skill。
- 新增包内`从WorkBuddy卸载.cmd`和`uninstall-workbuddy.ps1`。卸载只移除所有权匹配的程序与Skill，默认保留
  DataRoot、项目、Artifact、配置、模型、缓存、托管Python和输出；外来或标记不匹配的Skill列为protected并保留。
- 最终真实候选r10位于`D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-upgrade-uninstall-20260807-r10`；ZIP大小
  `72,805,580`字节，SHA-256=`e0fd2ea1ee6831ee5652b32e13c42d92afca77773babdb341bc606e61bac46e4`。
- r10 D盘完整矩阵=`PASS`：错误DataRoot在写入前拒绝、v1向前升级v2、坏v3 doctor失败并恢复v2、已安装目录
  中文CMD自卸载、两个自有Skill移除、原DataRoot数据哨兵保留；network/Provider调用均为0。
  portable bundle=`16 passed`，WorkBuddy专项=`101 passed`，完整回归=`1161 passed, 10 skipped, 1 subtest passed`。
- 本切片W1消费方Gate=`PASS`；最终W0公开性审计=`PASS`：1566个managed Core文件精确匹配，Release、四Pipeline、
  direct-agent运行时、公开lineage、风险扫描和回归全部通过，private Core历史未扫描且不在候选中。最终证据目录为
  `D:/WorkBuddyData/Temp/w4-upgrade-uninstall-publication-audit-20260807-r10-final`。
- r11在真实Windows默认路径完成安装、WorkBuddy Skill发现和中文CMD自卸载。安装launcher即使从开发仓库cwd启动，
  也固定以已安装runtime为导入根，不再被调用者目录中的同名Python包遮蔽；自卸载CMD先切换到`%TEMP%`，延迟清理
  最多重试30秒，真实程序目录和两个项目Skill均最终消失。
- r11默认路径`doctor=degraded`只因为本轮没有获得完整Python依赖下载授权；安装合同、Core、authority和四Pipeline
  没有错误，网络/Provider调用均为0。WorkBuddy“我的技能”能发现两个Golden Key Skill，但自然语言
  `我不知道怎么开始做视频`被WorkBuddy通用视频流程接管，未命中新手引导Skill；因此`WB-UX1`真实路由验收=`FAIL/PENDING`。
- r11用于上述真实默认路径验收；提交前的最终交付候选为r18，另补统一原生stderr错误出口，确保WorkBuddy/CI重定向
  启动时所有安装拒绝原因仍可见。r18 ZIP位于
  `D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-final-clean-baseline-20260807-r18`，大小`72,806,177`字节，
  SHA-256=`310050115DA8EAD14B1131C9AC51C95B9A67CC478CA2B829C13C15E366429BF3`。
- portable bundle=`17 passed`，WorkBuddy专项=`102 passed`；此前扩展完整回归=
  `1162 passed, 10 skipped, 1 subtest passed`。最终W0自带回归为contracts `716 passed, 7 skipped`、tools
  `284 passed, 1 subtest passed`、WorkBuddy `102 passed`。
- 最终W0公开性审计=`PASS`：1566个managed Core文件精确匹配，Release、四Pipeline合同、direct-agent运行时、
  公开lineage、风险扫描和回归全部通过；候选9个文件，snapshot SHA=
  `bb47187cad702320da29dc7c3aa21bbde92bb3f2d9c0b269ede45477d849ad2c`，证据目录为
  `D:/WorkBuddyData/Temp/w4-clean-client-final-publication-audit-20260807-r17`。
- 已按用户要求清理本次真实客户端验收：默认程序根、两个Golden Key Skill和MCP注册均不存在，WorkBuddy后台进程为0；
  三条Golden Key验收会话已标记删除，相关会话/trace文件移出WorkBuddy用户目录到D盘隔离区。清理后重启一次
  WorkBuddy，未出现新的Golden Key MCP连接记录，删除状态未被恢复。该清理不等于清空用户账号或其他项目。
- API Key引导候选r23位于
  `D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-api-key-guide-20260807-r23`；ZIP大小`72,812,987`字节，
  SHA-256=`ca71961edfd76c87cb91fb7b8f8857e599c748cea0b486ecc38baa1beeb8eb38`。隔离安装后即使缺少
  `jsonschema`，`config guide=pass`并以`deferred_missing_python_dependency`诚实标记Registry核验待依赖准备，
  仍可显示6类Provider选择；Key值返回0，网络/Provider调用0，本地配置向导可打开并取消且不创建凭据文件。
- DPAPI合同测试验证加密凭据只能由当前Windows用户解密，并由已安装launcher仅注入当前子进程；测试输出不含
  假Key。WorkBuddy专项=`108 passed`，两个Skill格式校验通过；r23隔离安装已卸载，程序与两个Skill均不存在。
- 本增量最终W0=`PASS`：Release合同、1566个Core文件、四Pipeline/44个阶段Skill、Schema/Tool/Checkpoint合同、
  direct-agent边界、公开lineage、公开风险扫描和回归全部通过；private Core历史不在候选中。证据目录为
  `D:/WorkBuddyData/Temp/w4-api-key-guide-publication-audit-20260807-r23-final`。

## 历史记录（不再是当前Gate）

- `golden-key-v0.3.18`整仓/private ancestry方案的W0裁决为`FAIL`。
- 该结论只约束已废弃旧方案，不否定或阻断v0.3.21 Release导出候选。
- 旧本地分支保留为`legacy/core-sync-v0.3.18`和`legacy/private-ancestry-v0.3.18`，不得推送。

## 下一步

1. 查明并修复WorkBuddy真实客户端没有把模糊视频请求路由到`golden-key-openmontage-onboarding`的原因；不得用文档宣称代替真实触发。
2. 按`MCP=optional`生成用户可选择、可禁用、可卸载的配置；不得覆盖用户已有WorkBuddy MCP配置。
3. 创建W4.1本地提交；本轮不制作正式安装包、不推送，也不把validation-only ZIP发布为Release。
4. 在真实WorkBuddy中继续完成自然语言新手/生产Skill触发、长任务/恢复和Human Checkpoint验收后，才重新裁决
   `OFFLINE ADAPTER READY`。
5. 等v0.3.23准备好后，在用户新开的对话中按新的不可变Release/ZIP/SHA/lock完成Core集成，不从Core main同步。
6. 真实/付费Provider执行仍需单独明确授权；未授权不阻止先推进W4离线打包与安装Gate。

## 当前允许声明

- v0.3.21 WorkBuddy Callable Core已同步并通过本地W0和回归。
- 首个公开基线已发布，状态为`Pre-Alpha`/“WorkBuddy Adapter开发中”。
- W2 Skill-first项目/Artifact/Checkpoint、受限本地Tool和持久长任务基线已通过专项测试。
- W2跨项目并发1、可观测超时和中断执行槽释放合同已通过专项测试。
- 真实WorkBuddy 5.3.8中的离线Skill+CLI与Skill+stdio MCP对照已通过，MCP裁决为`optional`。
- W3离线可靠性与安全Gate已通过；Python/Node子进程网络继承、SaaS不可用和统一脱敏矩阵已验证。

当前不允许声明：

- 已形成可供普通用户下载的正式安装发布；
- W1 Skill骨架已经是完整可用的WorkBuddy生产Skill；
- 真实或付费Provider生产执行闭环已经完成；
- 可选MCP或完整发行版已经达到普通用户安装可用；
- `OFFLINE ADAPTER READY`；
- 真实Provider成片通过。

## 权威文件

- `docs/workbuddy/ARCHITECTURE.md`
- `docs/workbuddy/CORE-SYNC-POLICY.md`
- `docs/workbuddy/LOCAL-STORAGE-POLICY.md`
- `docs/workbuddy/FIRST-PUBLIC-PUSH-POLICY.md`
- `docs/workbuddy/W2-MCP-DECISION-2026-08-06.md`
- `docs/workbuddy/W3-OFFLINE-RELIABILITY-REPORT-2026-08-06.md`
- `docs/workbuddy/audits/W0-PUBLICATION-AUDIT-REPORT-v0.3.21-2026-08-05.md`
- `NEXT-CONVERSATION-PROMPT-2026-08-06-W4.md`
