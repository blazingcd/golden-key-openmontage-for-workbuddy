# Project State

更新时间：2026-08-07 12:10 +08:00

## 当前里程碑

`W0 DONE / v0.3.21 PRE-ALPHA BASELINE PUBLISHED / W1 DONE / W2 DONE / W3 PASS / WB-UX1 IMPLEMENTED / W4 LIGHT-ZIP SLICE IN PROGRESS`

新的 W0 只审计 `golden-key-v0.3.21` WorkBuddy Callable Core Release 导出包、公开
`origin/main` lineage 和 WorkBuddy 自有增量。技术 Gate 已通过；用户在看到完整报告和目标提交后
明确授权推送，首个 `Pre-Alpha` 公开基线已发布到 `origin/main`。

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
- W4缺失Python依赖准备切片已实现：`runtime plan`只读给出目标和下载提示；只有显式
  `runtime prepare --confirm-download`才在所选`<data_root>/Runtime/Python`创建隔离环境并使用
  `<data_root>/Caches/pip`，不修改系统Python。hash一致重复执行直接复用，目标漂移拒绝覆盖。
- 注册launcher会在有效托管环境记录存在时优先使用它；WorkBuddy生产Skill必须先展示计划并获得用户明确同意，
  不得把原始视频请求当作下载授权。Python为必需，FFmpeg为合成/本地媒体必需，Node仅在选择Remotion或
  HyperFrames时需要。
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
  无效Skill所有权记录均fail closed并保留原内容；跨版本替换在正式升级合同完成前同样拒绝。
- 新真实候选r7位于`D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-tolerant-install-20260807-r7`；ZIP大小
  `72,800,975`字节，SHA-256=`ebf95cd067dce94bdf25f979740484e453df9dcd91b0a3dadde5c08eb6e1589a`。
  D盘隔离矩阵验证覆盖残留忽略、同版本重复、换解压目录、程序/Skill误删修复、数据保留和外来Skill冲突；
  network/Provider调用均为0。即使程序目录已删除，遗留Skill版本与当前包不一致也拒绝静默降级。
  portable bundle专项=`10 passed`，WorkBuddy专项=`95 passed`，完整回归=
  `1155 passed, 10 skipped, 1 subtest passed`。
- 本切片W0公开性审计=`PASS`：1566个managed Core文件精确匹配，Release、四Pipeline合同、direct-agent运行时边界、
  公开lineage、风险扫描和回归全部通过；private Core历史未扫描且不在候选中。证据目录为
  `D:/WorkBuddyData/Temp/w4-tolerant-install-publication-audit-20260807-r7-final`。

## 历史记录（不再是当前Gate）

- `golden-key-v0.3.18`整仓/private ancestry方案的W0裁决为`FAIL`。
- 该结论只约束已废弃旧方案，不否定或阻断v0.3.21 Release导出候选。
- 旧本地分支保留为`legacy/core-sync-v0.3.18`和`legacy/private-ancestry-v0.3.18`，不得推送。

## 下一步

1. W4下一片在已完成的同版本重复注册修复之上实现跨版本升级/降级、完整卸载和事务回滚；用户项目、Artifact、
   配置、模型和输出默认保留。
2. 按`MCP=optional`生成用户可选择、可禁用、可卸载的配置；不得覆盖用户已有WorkBuddy MCP配置。
3. 在获得明确同意后，用真实首包requirements完成一次数据目录托管Python下载/准备和launcher复核。
4. 在普通用户默认路径、D盘覆盖路径和真实WorkBuddy中完成自然语言触发、长任务/恢复验收后，才重新裁决
   `OFFLINE ADAPTER READY`。
5. 在真实WorkBuddy中对`WB-UX1`做首次对话体验验收；它独立留痕但可复用W4注册后的Skill。
6. 真实/付费Provider执行仍需单独明确授权；未授权不阻止先推进W4离线打包与安装Gate。

## 当前允许声明

- v0.3.21 WorkBuddy Callable Core已同步并通过本地W0和回归。
- 首个公开基线已发布，状态为`Pre-Alpha`/“WorkBuddy Adapter开发中”。
- W2 Skill-first项目/Artifact/Checkpoint、受限本地Tool和持久长任务基线已通过专项测试。
- W2跨项目并发1、可观测超时和中断执行槽释放合同已通过专项测试。
- 真实WorkBuddy 5.3.8中的离线Skill+CLI与Skill+stdio MCP对照已通过，MCP裁决为`optional`。
- W3离线可靠性与安全Gate已通过；Python/Node子进程网络继承、SaaS不可用和统一脱敏矩阵已验证。

当前不允许声明：

- 已经可以安装；
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
