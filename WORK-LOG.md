# Work Log

本文件只追加，不改写既有记录。每次可验证工作完成后记录：范围、动作、结果、证据、提交和下一步。

## 2026-08-05：项目架构与本地基线建立

### 范围

- 固化独立WorkBuddy项目边界。
- 固化Golden Key核心拉取式同步策略。
- 记录运行环境打包待决策项。
- 建立本地完整核心Git基线和持续留痕机制。

### 动作

- 读取项目交接文件、现有README、Golden Key核心Guide和相关仓库状态。
- 核对SaaS `config/openmontage.lock.json`。
- 核对Golden Key核心正式tag和远端提交。
- 从private核心的正式tag fetch完整Git对象，没有复制核心工作目录。
- 建立`core-sync`和`main`分支。
- 将原项目README和交接文件作为WorkBuddy增量保留在`main`。
- 编写架构、同步、路线、打包待决策和状态文档。

### 结果

- `DONE`：`core-sync`精确指向`golden-key-v0.3.18` / `381a08e8dbdea025367c4970174ae0cd29980337`。
- `DONE`：SaaS lock当前指向同一tag/commit。
- `DONE`：项目完整包含OpenMontage/Golden Key核心代码，不是Adapter空壳。
- `DONE`：运行环境问题记录为`PKG-001`，未提前决定方案。
- `TODO`：完成W0公开审计后才能推送Golden Key派生内容到公开fork。

### 下一步

1. 创建官方OpenMontage公开fork并记录URL。
2. 不推送当前本地`main`，直到W0公开审计通过。
3. 完成W0差异、秘密、素材和许可证审计。

## 2026-08-05：GitHub公开fork建立

### 范围

- 建立项目正式GitHub入口。
- 验证它是官方OpenMontage的公开fork。
- 保持W0审计前的发布隔离。

### 动作

- 从`calesthio/OpenMontage`创建`blazingcd/golden-key-openmontage-for-workbuddy`。
- 设置项目描述和`openmontage`、`workbuddy`、`mcp`、`video-production`主题。
- 将公开fork配置为本地`origin`，将Golden Key核心配置为`golden-key-core`。
- 比对公开远端`main`与本地`main`。

### 结果

- `DONE`：公开仓库已建立，GitHub确认`isFork=true`、`isPrivate=false`，parent为`calesthio/OpenMontage`。
- `DONE`：公开远端`main`仍精确指向官方提交`4eab34c5cfcccaa4f1970554928feccce73ee930`。
- `DONE`：本地完整核心、架构文档和WorkBuddy增量尚未推送；W0审计门禁有效。
- `TODO`：完成W0公开性审计并形成明确裁决。
- `TODO`：只有审计Gate允许后，才把审计通过的完整快照发布到公开fork。

### 证据

- GitHub：`https://github.com/blazingcd/golden-key-openmontage-for-workbuddy`
- 本地架构文档提交：`f94f63e`
- Golden Key核心基线：`golden-key-v0.3.18` / `381a08e8dbdea025367c4970174ae0cd29980337`

### 下一步

1. 对Golden Key核心相对官方OpenMontage的差异和Git历史做公开性审计。
2. 审核秘密、内部地址、素材、许可证、测试样例和Provider示例。
3. 将审计结果及证据追加到本日志，并同步更新`PROJECT-STATE.md`。

## 2026-08-05：README合并与W0执行交接

### 范围

- 将WorkBuddy项目说明和官方OpenMontage README合并为一个根README。
- 为下一对话建立可直接执行的W0启动Prompt。

### 动作

- 保留当前WorkBuddy README全部内容及其未提交的场景文案调整。
- 在WorkBuddy说明后加入明确标题、分隔线和机器可识别标记。
- 将`core-sync:README.md`完整追加为下半部分，并逐行核对官方区内容。
- 新建`NEXT-CONVERSATION-PROMPT-2026-08-05-W0.md`，写明权威文件、冻结边界、执行任务、Gate和禁止事项。

### 结果

- `DONE`：根README上半部分为WorkBuddy项目说明，下半部分为当前锁定核心中的官方OpenMontage README。
- `DONE`：官方README区与`core-sync:README.md`内容一致，仅在其前方增加区隔说明和同步标记。
- `DONE`：下一对话Prompt要求直接执行W0，不把重新规划当成完成。
- `DONE`：主要内容已形成本地提交`7666680`。
- `TODO`：在新对话中完成W0公开性、架构和接口审计。
- `TODO`：W0 Gate通过且用户明确授权前，继续禁止向公开`origin`推送Golden Key派生内容。

### 下一步

1. 新对话读取`NEXT-CONVERSATION-PROMPT-2026-08-05-W0.md`并执行W0。
2. 形成公开审计报告、运行时隔离方案和明确Gate裁决。

## 2026-08-05：纠正本地同步与公开发布状态混淆

### 范围

- 重新核对Golden Key核心是否真正同步到本地WorkBuddy仓库。
- 修正W0交接Prompt，防止把公开空fork误判为本地核心缺失。

### 证据与结果

- `DONE`：实时fetch后，`golden-key-core/main`与本地`core-sync`均为`golden-key-v0.3.18` / `381a08e8dbdea025367c4970174ae0cd29980337`，全仓差异为空。
- `DONE`：本地`main`完整包含四个Golden Key业务Pipeline，其manifest blob与Golden Key远端逐一相同。
- `DONE`：本地`main`相对`core-sync`在Pipeline、Skill、Schema、Tool和核心合同测试等受保护路径上无漂移。
- `DONE`：Golden Key相对官方新增4个业务Pipeline manifest、44个对应Pipeline Skill和11个合同测试；Pipeline复用通用Schema和Tool Registry。
- `DONE`：公开`origin/main`仍为官方提交`4eab34c5cfcccaa4f1970554928feccce73ee930`，没有四个Golden Key Pipeline。
- `DONE`：更新W0 Prompt，要求分别核验Golden Key远端、本地`core-sync`、本地`main`和公开`origin/main`。
- `DONE`：Prompt及状态纠正已形成本地提交`c737521`。
- `TODO`：W0审计通过并获得用户明确授权后，把完整Golden Key核心加WorkBuddy增量发布到公开fork。

### 下一步

1. 在新对话按更新后的Prompt执行W0。
2. 形成首次公开发布文件清单和Gate裁决。

## 2026-08-05：W0公开性、架构和接口审计

### 范围

- 分别核验Golden Key远端、本地`core-sync`、本地`main`和公开`origin/main`。
- 核验四个Golden Key业务Pipeline、44个Pipeline Skill、Reviewer/Checkpoint、通用Schema、Tool Registry和合同测试。
- 审计Golden Key相对官方的完整差异、提交历史、秘密/路径/客户数据、素材/字体/品牌/第三方代码和许可证风险。
- 固化WorkBuddy运行时隔离验证方案并形成首次公开发布Gate。

### 动作与命令证据

- 实时fetch `golden-key-core`与`origin`，核对tag、commit、祖先关系、tree差异和受保护路径差异。
- 只读核对SaaS `config/openmontage.lock.json`，与同步清单一致。
- 新增并运行`scripts/workbuddy/w0_audit.py`，生成Git、Pipeline、发布清单、脱敏风险和隔离证据。
- 在独立D盘venv运行`python -m pytest tests\contracts -q --disable-warnings --maxfail=1`。
- 运行6个Golden Key差异相关工具测试文件。
- 使用腾讯云官方文档核对测试中的TokenHub地址为公开接口地址。
- 运行Codex Security标准扫描预检；工作台因worker能力未决和Windows仓库路径清单错误未形成sealed report，已明确记录覆盖缺口。

### 结果

- `DONE`：四位置Git身份重新验证；远端核心与`core-sync`差异0，`main`受保护路径漂移0，公开`origin/main`仍只有官方基线。
- `DONE`：4 manifests、44 Pipeline Skills、Reviewer/Checkpoint、通用Schema和22个Tool Registry引用完整一致。
- `DONE`：11个新增合同测试文件完整一致；合同测试`743 passed, 7 skipped`，相关工具测试`70 passed`。
- `DONE`：完整差异/历史/首次发布清单与脱敏风险证据已保存到`docs/workbuddy/audits/evidence-2026-08-05/`。
- `DONE`：当前WorkBuddy交接文件中的本机绝对路径已脱敏；README增加预发布状态警示。
- `DONE`：运行时隔离测试方案已冻结；当前无Adapter入口，动态隔离为`NOT YET APPLICABLE`。
- `FAIL`：首次公开发布Gate。核心包含private-fork/真实客户命名案例和具体业务信号；现行ancestry还会公开commit邮箱及历史路径。

### 责任与下一步

1. 用户/仓库所有者决定：明确授权现有历史公开，或批准净化公开导出历史方案。
2. Golden Key核心责任方确认/匿名化private-fork、真实客户和命名fixture内容；WorkBuddy不直接修改核心拥有路径。
3. 对最终拟公开commit/history重跑W0审计和测试；新Gate通过前继续禁止公开推送。
4. 本轮审计内容先形成安全本地提交；提交hash在后续追加日志中记录。

## 2026-08-05：W0审计提交记录

- 审计报告、证据、脚本、测试、状态更新和安全修正提交：`dfe4c4d948786419b02a8d682f325523f2fa6c02`。
- 提交前确认未暂存或修改Golden Key核心受保护路径。
- 本轮未推送`origin`或`golden-key-core`，未调用真实/付费Provider，未修改Golden Key SaaS仓库。
- 公开发布Gate保持`FAIL`；本条日志收尾提交仅记录证据，不改变Gate。

## 2026-08-05：首次公开推送时机规则冻结

### 范围

- 消除“首次公开推送必须等待 W1～W4”与“W0 PASS 会自动触发推送”两种误解。
- 固化首次完整公开基线、对外状态声明和后续持续发布节奏。

### 动作

- 新建`docs/workbuddy/FIRST-PUBLIC-PUSH-POLICY.md`作为权威政策。
- 同步更新README、架构边界、核心同步策略、W0-W4路线和`PROJECT-STATE.md`。
- 明确首次推送必须同时满足：目标版本W0明确`PASS`，以及用户看到报告后的再次明确授权。
- 明确首次完整基线不等待W1～W4；首次基线后采用持续开发、留痕、提交和推送。

### 结果

- `DONE`：规则已固化到项目权威文档。
- `DONE`：首次基线最低内容包括锁定完整核心`golden-key-v0.3.18` / `381a08e8dbdea025367c4970174ae0cd29980337`、四个业务Pipeline及合同面、安全可公开的WorkBuddy增量和治理文档。
- `DONE`：首次基线只能声明`Pre-Alpha`或“WorkBuddy Adapter开发中”。
- `BLOCKED`：当前W0仍为`FAIL`，所以不得推送；本次规则补充不是推送授权。
- 本轮未推送任何远端，未调用真实/付费Provider，未修改Golden Key SaaS仓库或Golden Key核心拥有路径。

### 下一步

1. 完成当前W0报告列明的安全、可逆、范围内修正，并列出外部阻断项。
2. 对最终拟公开commit/history重跑W0；只有明确`PASS`才能进入授权等待状态。
3. 向用户报告Gate、风险、待发布文件清单、测试证据和目标提交；等待明确推送授权。

### 提交证据

- 首次公开推送政策及关联文档提交：`37124106fc91e4a9e5363fcbc97e3d67d0571a8f`。
- 本条提交证据只记录本地Git边界，不改变W0=`FAIL`，也不构成公开推送授权。

## 2026-08-05：v0.3.21两层导出基线纠偏、同步与W0重审

### 范围

- 废弃“整仓同步Golden Key private ancestry”方案。
- 采用`golden-key-v0.3.21` WorkBuddy Callable Core Release导出合同。
- 实现fail-closed同步器、同步干净公开lineage、回归四Pipeline合同并重做W0。

### Release与同步证据

- GitHub Release实时核验：tag=`golden-key-v0.3.21`，source commit=`757ea3822e5f2eef7f341389983119021e827c8d`。
- ZIP固定SHA-256：`DC21792B6F9D773B1559B1687DEE0CC78FCBFC442400D71A735F7EE375426599`，与GitHub asset digest和sidecar一致。
- 外部lock与ZIP内嵌lock一致；contract ID=`golden-key-workbuddy-callable-core-v1`；bundle digest验证通过。
- 1566个managed文件逐项通过path、hash、size和Git mode验证。
- 在旧本地工作树首次纠偏时，12个文件改写、214个受管旧/缓存文件清理，六个历史Agent Host代码/测试路径被移除；消费方文件哈希保持不变。
- 在公开`origin/main`干净lineage建立候选时，Release导入改写96个文件、删除0个；六路径原本不存在且持续不存在。
- 两次场景的第二次同步均为0改动，幂等成立。

### 实现与测试

- 新增`scripts/core_sync/sync_workbuddy_core.py`，验证外部ZIP SHA、内外lock、bundle digest、managed scope、required/forbidden、逐文件hash/mode和目标清单。
- 新增同步专项负测：精确镜像、消费方文件保留、六路径固定集合、forbidden/hash/mode/缺失/额外拒绝、外部SHA拒绝、只读漂移核验和幂等。
- 四Pipeline：4 manifests / 44 Pipeline Skills / 10个相对官方变更合同测试（8新增、2修改），Reviewer/Checkpoint、Schema和Tool Registry引用完整。
- 回归结果：contracts=`716 passed, 7 skipped`；tools=`284 passed, 1 subtest passed`；WorkBuddy=`15 passed`。
- 全程未调用真实/付费Provider，未修改Golden Key SaaS仓库。

### Git与W0结果

- 旧private ancestry本地保留为`legacy/private-ancestry-v0.3.18`；旧`core-sync`改名为`legacy/core-sync-v0.3.18`，两者均禁止发布。
- 当前`main`重新从公开`origin/main`建立；Golden Key source commit只记录Release provenance，不是`main`祖先。
- 旧v0.3.18 W0 `FAIL`报告保留、脱敏并标记为已取代的历史结论。
- 新v0.3.21候选W0：Release合同、Pipeline合同、direct-agent边界、公开lineage、公开性扫描、回归全部`PASS`。
- 公开`origin/main`仍为`4eab34c5cfcccaa4f1970554928feccce73ee930`；本交接不是推送授权。

### 下一步

1. 形成干净本地目标提交并完成提交后只读复核。
2. 报告Gate、风险、待发布文件、测试证据和目标提交。
3. 等待用户再次明确允许推送后，才建立首个`Pre-Alpha`公开基线。

## 2026-08-05：首个Pre-Alpha公开基线发布

### 授权与范围

- 用户在看到v0.3.21 W0 `PASS`报告、风险、文件清单、测试证据和目标提交后，明确要求该推送即推送并继续项目。
- 发布范围严格限定为已审计的本地`main`目标提交`e4f7577bad99e93e0a35217940d8c17f7a6d81cb`。
- 未推送`legacy/core-sync-v0.3.18`或`legacy/private-ancestry-v0.3.18`，未创建额外Release或标签。

### 发布前门禁

- 重新获取公开`origin/main`，仍为`4eab34c5cfcccaa4f1970554928feccce73ee930`。
- 工作树干净；候选仍为143个路径；W0证据Gate仍为`PASS`。
- 当前`main`以公开`origin/main`为祖先，Golden Key source commit不在发布历史中。

### 结果

- `DONE`：`main`已推送到公开`origin/main`。
- 远端核验：`refs/heads/main`=`e4f7577bad99e93e0a35217940d8c17f7a6d81cb`。
- 对外状态保持`Pre-Alpha`/“WorkBuddy Adapter开发中”；没有声明可安装、真实WorkBuddy验收通过或`OFFLINE ADAPTER READY`。
- 未调用真实/付费Provider，未修改Golden Key SaaS仓库。

### 下一步

1. 进入W1，先完成可重复Release同步维护命令和常规Gate集成。
2. 建立WorkBuddy包、Skill/测试/示例配置骨架及D盘环境`doctor`。
3. W1～W4采用持续开发、持续留痕、持续提交和持续推送方式推进。

## 2026-08-05：W1 Release同步维护命令

### 范围

- 将手工准备ZIP/lock的同步流程升级为可重复执行的`sync-release`维护者命令。
- 保持Release-only、direct-agent、消费方所有权和fail-closed边界不变。

### TDD与实现

- 红灯1：证明现有同步器未校验SHA sidecar；新增固定SHA和ZIP文件名双重校验。
- 红灯2：证明现有CLI不支持一条命令执行Release同步；新增`sync-release --asset-dir ...`公共接口。
- 红灯3：证明缓存缺失没有下载路径；新增GitHub CLI三资产限定下载、同盘隔离暂存、完整验证后原子发布。
- 真实缓存检查发现`extracted/`子目录导致误拒绝；新增回归测试，允许不参与同步的子目录，但继续拒绝同级额外文件。
- 缓存命中仍完整验证sidecar、ZIP、lock、bundle和逐文件合同；不会调用GitHub CLI。

### 回归与发现

- 同步专项：`15 passed`。
- 完整WorkBuddy专项：`18 passed`。
- 真实v0.3.21 D盘缓存执行`sync-release`：1566个文件通过，`changed_file_count=0`、`deleted_file_count=0`。
- 首次公开推送后，动态`origin/main`导致W0合同变化数误报为0；已将Pipeline/合同比较基线固定为配置锁定的`upstream_base_commit`，保持4 Pipeline / 44 Skill / 10个合同变化证据稳定。
- 测试依赖安装于D盘隔离临时环境；未调用真实/付费Provider。

### 下一步

1. 提交并持续推送本增量。
2. 把`sync-release`接入常规Gate/CI入口。
3. 建立WorkBuddy包、Skill/示例配置骨架和D盘环境`doctor`。

## 2026-08-06：W1 WorkBuddy基础入口、Skill骨架与持续门禁

### 范围

- 完成W1剩余的消费方包、Skill/配置骨架、D盘`doctor`和常规CI门禁。
- 将架构从“MCP预先必选”纠正为“Skill-first，真实WorkBuddy对比后裁决MCP”。
- 保持v0.3.21 Release-only、direct-agent、无嵌套Agent Host和无真实Provider边界。

### TDD与实现

- 新增独立发行`golden-key-openmontage-workbuddy==0.1.0a0`和控制台命令`golden-key-workbuddy`。
- `doctor`报告锁定Core身份、authority、四Pipeline、本地Python/Node/FFmpeg、D盘目录和禁止声明状态；
  `--create-dirs`建立`Projects/Caches/Models/Temp/Logs/Jobs`。
- `gate`复用doctor并fail-closed检查Skill、六个禁入路径、WorkBuddy运行时代码AST导入和活动MCP配置。
- 新建`workbuddy-skill/golden-key-openmontage/SKILL.md`，冻结WorkBuddy唯一Agent、Rule Zero、四Pipeline、
  Stage Skill/Schema/Reviewer/Checkpoint和Provider授权规则。
- 新建`.workbuddy/README.md`，明确W1不发布活动`mcp.json`；W2进行CLI与stdio MCP真实对比。
- CI新增W1 Gate和完整回归；固定Release`sync-release`与1566文件目标复核保留为已授权维护者环境Gate。
- 新建`docs/workbuddy/LOCAL-STORAGE-POLICY.md`，将项目数据、缓存、模型、临时文件和开发venv固定到D盘策略。

### 验证

- D盘开发环境：`D:\WorkBuddyData\Dev\venvs\golden-key-workbuddy-w1`，包可编辑安装成功。
- 真实`doctor --create-dirs`=`PASS`：Python 3.11.9、Node v24.16.0、FFmpeg 8.1.1，Provider调用0。
- 真实W1 `gate`=`PASS`：四Pipeline齐全、六路径不存在、AST隔离0命中、活动MCP配置不存在。
- Skill Creator `quick_validate.py`：`Skill is valid!`。
- 真实v0.3.21 `sync-release`：1566文件通过，改写0、删除0，Release资产下载到D盘缓存。
- 回归：contracts=`716 passed, 7 skipped`；tools=`284 passed, 1 subtest passed`；WorkBuddy=`27 passed`。
- W1最终候选：Release合同、Pipeline合同、运行时边界、公开lineage、公开性扫描和回归全部`PASS`；
  未扫描或引入Golden Key私有历史。
- 公开CI首次实跑发现消费者仓库`GITHUB_TOKEN`不能读取私有Core Release；按最小权限原则移除该跨仓库依赖，
  公开CI只验证已发布快照，且不得持有私有Core读取令牌。
- 公开CI第二次实跑完成1086项后，唯一失败为默认浅克隆缺少固定公开比较基线；checkout改为完整公开历史，
  不获取或合并Golden Key私有历史。

### 结果与边界

- `DONE`：W1完成；下一阶段为W2 Skill-first生产调用闭环和MCP决策Gate。
- 当前仍为`Pre-Alpha`；Skill只是W1安全骨架，不得声明完整生产可用、真实WorkBuddy验收或
  `OFFLINE ADAPTER READY`。
- 未调用真实/付费Provider，未修改Golden Key SaaS仓库，Core同步结果为0改动。

## 2026-08-06：W2第一段Skill-first直接调用基线

### 范围

- 只开发WorkBuddy消费方调用层；锁定v0.3.21 managed Core快照只读。
- 建立从权威上下文到项目、当前Stage、Artifact和Checkpoint的首段确定性闭环。
- 不启用MCP，不执行生产Tool，不调用真实/付费Provider。

### TDD与实现

- 新增`context`和`pipelines`：读取Guide与四Pipeline合同，明确`selected_pipeline=null`且不排序/选择。
- 新增`project create/status`：Pipeline必须由WorkBuddy显式传入；同一项目禁止重新绑定Pipeline。
- 新增`stage inspect`：从原生Checkpoint顺序解析下一Stage，返回Stage Skill、产物、允许工具和Human Gate。
- 新增`artifact validate`：只读取项目`artifacts/`内JSON并调用原生Artifact Schema。
- 新增`checkpoint submit`：要求Manifest声明的完整产物集合，再调用原生`write_checkpoint`执行Schema、前置Stage和Human Gate。
- 项目ID、Artifact/Checkpoint路径、Pipeline重绑定、缺产物和未批准完成均fail-closed。
- WorkBuddy Skill更新为上述CLI生命周期；MCP仍为`decision_pending`。

### 当前验证与边界

- W2新专项：`13 passed`；完整WorkBuddy专项：`41 passed`；Skill格式校验=`Skill is valid!`。
- Core回归：contracts=`716 passed, 7 skipped`；tools=`284 passed, 1 subtest passed`。
- W2增量公开审计=`PASS`：1566个Core文件匹配，候选11个文件，公开性/lineage/运行时/回归全部通过。
- 离线测试封锁socket后，context/Pipeline/项目生命周期仍通过；Provider调用数为0。
- 公开CI首次实跑发现W2/Core依赖被CLI顶层提前加载，破坏W1轻量Gate；改为命令级懒加载，并新增`python -S`
  回归，保证缺少W2运行依赖时`doctor/gate`仍可启动。
- 当前尚未开放生产Tool执行，尚未进行真实WorkBuddy与stdio MCP对比，因此W2仍为`IN PROGRESS`。

## 2026-08-06：W2受限Tool Registry发现与纯本地执行

### CI纠偏

- 用户提供的Actions run `31077036248`对应历史提交`facc548`，失败点为W2运行时在CLI顶层导入，
  使W1 Gate在依赖安装差异下报`ModuleNotFoundError: jsonschema`。
- 当前`main`的`e227660`已经采用命令级懒加载；后续run `31077374841`在同一主线通过W1 Gate、lint和完整测试。
- 本轮再次以`python -S`执行W1 Gate，结果=`PASS`，确认W2 Tool入口没有重新引入该回归。

### TDD与实现

- 新增`golden-key-workbuddy tool list`：只读取项目已绑定Pipeline的当前Stage，按Manifest顺序返回允许工具、
  Tool Registry输入Schema、运行时、网络声明、Layer 3 Skill和本地执行策略；不选择Pipeline或Provider。
- 新增`golden-key-workbuddy tool execute`：请求JSON必须位于项目`artifacts/`内，Schema声明的所有路径必须
  位于项目目录，必须用`--ack-agent-skill`确认已读取全部Layer 3 Skill。
- 仅允许`runtime=local|local_gpu`、`network_required=false`、可用且估算成本为0的当前Stage工具；
  API、Hybrid、需网络、未列入Stage、Skill未确认、Schema错误和路径穿越均在`execute()`前拒绝。
- 发现Hybrid selector的状态探测本身可能访问本机`localhost:8188`；Adapter不再对被阻断的API/Hybrid执行
  `get_status()/get_info()`，从而把授权门禁前移到任何状态探测和网络访问之前。
- 原生`scene_detect`在测试项目内真实调用FFmpeg并写出场景JSON；没有修改v0.3.21 managed Core文件。
- WorkBuddy Skill同步加入Tool发现、Layer 3 Skill读取确认、项目路径和API/Hybrid拒绝流程；MCP仍为`decision_pending`。

### 验证与边界

- WorkBuddy专项=`47 passed`；Skill格式=`Skill is valid!`。
- Core contracts=`716 passed, 7 skipped`；Core tools=`284 passed, 1 subtest passed`。
- 完整套件=`1107 passed, 10 skipped, 1 subtest passed`。
- 本地Tool纵向验证：Tool调用1、Provider调用0、成本0；socket封锁下网络尝试0。
- Hybrid selector负测：Tool调用0、Provider调用0、网络尝试0；未调用真实/付费Provider。
- W2 Tool增量公开审计=`PASS`：1566个Core文件匹配，候选12个文件，公开性/lineage/运行时/回归全通过；
  `private_core_history_scanned=false`且`private_core_history_in_candidate=false`；最终候选摘要保存在D盘审计证据目录。
- W2仍为`IN PROGRESS`：真实Provider授权路径、主对话模型/视频Provider配置分层、长任务可靠性和
  真实WorkBuddy的CLI/MCP对比尚未完成，不能声明安装可用或`OFFLINE ADAPTER READY`。

## 2026-08-06：W2主对话模型与生产Provider配置分层

### TDD与实现

- 先新增CLI/Skill公共合同负测，确认`config inspect/template`原本不存在，再实现消费方模块；未修改v0.3.21 managed Core。
- `config inspect`明确WorkBuddy conversation model由WorkBuddy Host配置，Adapter不定义或代理该模型、
  不读取其凭据，也不允许nested Agent Host；Golden Key生产Provider继续由Tool Registry管理。
- 国内生态生产能力只列出Registry实际存在且合同匹配的工具：DashScope、豆包、火山即梦、可灵官方标为
  `direct_vendor_api`；Seedance和MiniMax当前Registry实现标为`third_party_gateway`。
- Registry核验只读取工具类的provider/runtime/network/capability合同，不执行`get_status()`、`execute()`或Provider调用。
- `config template`只在`D:/WorkBuddyData/Config/golden-key-production-providers.json`写环境变量名称引用；
  不写密钥值，同内容重复执行幂等，已被用户修改的文件fail-closed且不覆盖。
- WorkBuddy Skill、项目README、架构、Roadmap、状态和下一轮Prompt同步更新；MCP仍为`decision_pending`。

### 当前验证与边界

- 新模型/Provider配置与Skill专项=`7 passed`；完整WorkBuddy专项=`51 passed`。
- socket封锁和伪密钥负测证明输出不泄漏密钥值，网络尝试0、Provider调用0。
- 完整套件=`1111 passed, 10 skipped, 1 subtest passed`；W1 `python -S` Gate=`PASS`；
  Skill Creator校验=`Skill is valid!`，Python编译检查通过。
- W0增量公开性审计=`PASS`：1566个Core文件匹配，候选12个文件，Release/Pipeline/运行时/公开lineage/
  秘密扫描/回归全部通过；snapshot SHA=`d4e9c91ae51035e453fc0f2141d749e8bc29f361a43beea6e32463dca3911204`。
- 审计证据：`D:/WorkBuddyData/Temp/w2-model-provider-config-publication-audit`；
  `private_core_history_scanned=false`且`private_core_history_in_candidate=false`。
- 尚未配置或调用任何真实/付费Provider；尚未声称WorkBuddy支持某个具体主模型兼容端点。
- W2仍为`IN PROGRESS`；下一增量是本地Tool长任务状态、幂等、取消语义和更完整网络/嵌套模型拦截。

## 2026-08-06：W2本地Tool持久任务与明确取消/恢复合同

### TDD与实现

- 只修改WorkBuddy消费方包、Skill、测试和文档；v0.3.21 managed Core保持只读。
- 新增`task submit/status/run/cancel/recover`公共CLI。任务JSON持久化到
  `D:/WorkBuddyData/Jobs/<project-id>`，输入正文仍留在项目`artifacts`，任务只记录路径和SHA-256。
- `submit`在落盘前复用当前Stage、Tool Registry、本地运行时、网络声明、Layer 3 Skill、Schema、路径和
  零成本门禁；稳定身份摘要使同一请求重复提交返回同一task ID，不执行Tool。
- `run`使用单任务独占锁，运行前复核输入hash，终态结果原子写回；成功任务重复运行只返回持久结果，
  不再次调用Tool。持久任务身份被改写或输入文件提交后变化均fail-closed。
- 取消语义按当前Core能力冻结：queued任务可取消且幂等；blocking Tool开始后没有通用协作式取消合同，
  因此running任务明确返回“not safely cancelable”，不伪称已取消、不粗暴终止进程。
- 进程中断后`status`返回`recovery_required`；`recover`只把任务标记为failed并移除陈旧锁，禁止自动重试，
  避免未知的局部文件副作用重复发生。
- 本地Tool执行增加socket-denial运行时边界，覆盖DNS、连接和数据报入口；误声明local但尝试联网的Tool
  在真实socket调用前失败。API/Hybrid仍在状态探测、任务落盘和网络前拒绝。
- WorkBuddy Skill、项目README、架构、路线图、D盘存储、隔离测试计划、项目状态和下一轮Prompt同步更新；
  MCP仍为`decision_pending`，没有创建活动`.workbuddy/mcp.json`。

### 当前验证与边界

- 任务与Skill专项=`13 passed`；完整WorkBuddy专项=`61 passed`。
- 完整套件=`1121 passed, 10 skipped, 1 subtest passed`；四Pipeline、44个Pipeline Skill、Schema、
  Reviewer/Checkpoint、Tool Registry合同均保持通过。
- W1 `python -S` Gate=`PASS`；Skill Creator校验=`Skill is valid!`；Python编译和`git diff --check`通过。
- W0增量公开性审计=`PASS`：1566个Core文件精确匹配，15个候选文件；Release/Pipeline/运行时隔离、
  公开lineage、风险扫描和回归均通过，private Core历史未扫描且不在候选中。证据写入
  `D:/WorkBuddyData/Temp/w2-durable-task-publication-audit-20260806-retry`。
- 未调用真实/付费Provider，未修改Golden Key SaaS或Golden Key私有Core仓库。
- 仍未完成真实WorkBuddy的Skill+CLI/Skill+stdio MCP对比；Node/子进程网络继承、跨任务并发和超时属于
  后续W2/W3 Gate，因此不能声明安装可用、MCP已裁决或`OFFLINE ADAPTER READY`。

## 2026-08-06：真实WorkBuddy CLI/MCP对照与`MCP=optional`裁决

### 实机CLI基线

- 核验官方WorkBuddy `5.3.8`已安装、登录，任务使用项目仓库工作区和默认权限。
- 生成只含`SKILL.md`的本地导入ZIP，SHA-256=
  `4B40A3A614388E32F9FAA3525A1C94E3E7E72BE993F75FC39FC7BD665619EAA3`；Skill成功安装、启用。
- WorkBuddy自身Skill安全检测超过界面预计时间未返回；在包内容和哈希已独立核验后手动继续安装，未开启
  “非高风险自动安装”。
- 真实任务加载`golden-key-openmontage` Skill、读取`AGENT_GUIDE.md`，运行本地`doctor/context`；
  两条命令退出码均为0，authority=`direct_agent`、nested Host=`false`、四Pipeline完整，Provider调用0。
- WorkBuddy Host为首次实质任务自动写入未跟踪`.workbuddy/memory`；该客户端副作用已清理，没有进入发布候选。

### stdio MCP候选与真实对照

- 新增无第三方MCP依赖的消费方stdio服务器与`golden-key-workbuddy-mcp`入口；首轮把现有16个确定性消费方
  函数暴露为JSON Schema工具，不复制Pipeline选择、Reviewer、Checkpoint、任务状态或重试逻辑。
- 协议专项覆盖握手、工具发现、结构化context、参数拒绝和任务失败不重试，首轮`5 passed`。
- WorkBuddy用户级配置成功启动D盘虚拟环境中的stdio服务器；首次信任后界面绿色在线，显示`1启用`、
  `16/16个工具已启用`。仓库没有创建活动`.workbuddy/mcp.json`。
- 对照输出暴露Skill提及但首轮MCP遗漏的直接`tool_execute`包装；随后补齐同一消费方函数，最终MCP合同为
  17个Schema工具，长任务仍优先使用持久`task`入口。
- 第二个真实任务先读取Guide和Skill，不运行Shell，直接发现并调用`golden_key_context/pipelines`；两项均
  `status=pass`，四Pipeline完整，authority合同正确，Provider调用0，且未写workspace memory。
- 失败路径只调用一次`golden_key_task_status`；非法ID在校验阶段返回`status=fail`，Tool/Provider/网络调用0，
  WorkBuddy未重试。服务器本地确认`isError=true`，但WorkBuddy 5.3.8模型侧未稳定暴露该传输层字段；
  因此业务`status/errors`继续作为强制错误合同。

### Gate裁决与边界

- W2真实对照Gate=`PASS`，MCP裁决=`optional`。
- CLI继续作为必选入口和权威回退；MCP只增加结构化Schema发现、语义工具选择和免Shell参数拼接。
- MCP不是远端服务或第二个Agent；它与CLI共用相同Core、任务、网络、成本、Artifact和Checkpoint门禁。
- W4打包前不发布活动仓库配置；安装器后续必须支持用户不启用、首次信任、禁用和卸载。
- 本轮未调用真实/付费Provider，未修改v0.3.21 managed Core、Golden Key SaaS或私有Core仓库。
- 这不是完整安装/普通用户验收或`OFFLINE ADAPTER READY`；下一步为跨任务并发/超时和W3离线矩阵。

### 最终回归与公开Gate

- WorkBuddy专项=`66 passed`；完整套件=`1126 passed, 10 skipped, 1 subtest passed`。
- `python -S` Gate=`PASS`，Skill格式=`Skill is valid!`，Python编译与`git diff --check`通过。
- W0第一次按fail-closed拒绝pytest/compileall生成在managed scope中的`__pycache__`额外文件；只清理精确列出的
  可重建缓存后，以相同ZIP、lock和候选重跑。
- 最终W0公开性审计=`PASS`：Release/Pipeline/运行时/公开lineage/风险扫描/回归全部通过，1566个Core文件
  精确匹配、17个候选文件，snapshot SHA=
  `5b1bd5dbb401dad6cf1e313a071c6f3dd481b85af449fd4217ce20fd1a9a4064`。
- 审计证据目录：`D:/WorkBuddyData/Temp/w2-mcp-optional-publication-audit-20260806-retry`；
  `private_core_history_scanned=false`且`private_core_history_in_candidate=false`。

## 2026-08-06：W2跨任务并发与可观测超时合同

### TDD与实现

- 继续只修改WorkBuddy消费方包、Skill、测试和文档；v0.3.21 managed Core保持只读，未调用真实/付费Provider。
- 先以CLI公共边界新增跨项目并发负测，确认原实现会同时执行两个任务；随后新增数据根级原子执行槽，
  把并发上限固定为1。竞争任务保持`queued`、`attempt_count=0`、Tool调用0，不自动重试。
- 先新增运行时截止时间负测，再为CLI和可选MCP的同一`task run`函数加入`timeout_seconds`，默认3600秒，
  允许大于0且不超过86400秒。截止时间只做可观测报警；running阻塞Tool不被强杀、不伪称取消。
- 新增中断恢复负测：只有任务身份匹配且owner进程已死亡时，`task recover`才释放遗留全局执行槽；
  仍只把任务标记failed，不重放未知局部副作用。
- Skill、README、架构、路线图、D盘存储、隔离方案、项目状态和下一轮Prompt同步更新；MCP仍为可选，
  工具总数保持17，没有发布活动`.workbuddy/mcp.json`。

### 验证与当前边界

- 任务/MCP专项=`19 passed`；完整WorkBuddy专项=`70 passed`。
- 完整套件=`1130 passed, 10 skipped, 1 subtest passed`；四Pipeline、44个Pipeline Skill、Schema、
  Reviewer/Checkpoint和Tool Registry合同保持通过。
- W1 `python -S` Gate=`PASS`；Skill Creator校验=`Skill is valid!`；Python编译和`git diff --check`通过。
- W0首轮按fail-closed拒绝测试生成在managed scope内的21个`__pycache__`目录；只删除精确核验的可重建缓存，
  源文件未动，并设置`PYTHONDONTWRITEBYTECODE=1`重跑。
- 更新状态和日志后的最终W0公开性审计=`PASS`：1566个Core文件精确匹配，四Pipeline/44 Skill、运行时、
  公开lineage、风险扫描和回归全部通过；private Core历史未扫描且不在候选中。最终证据目录为
  `D:/WorkBuddyData/Temp/w2-concurrency-timeout-publication-audit-20260806-final`。
- 真实/付费Provider、Golden Key SaaS和私有Core仓库均未调用或修改。W4安装/普通用户验收与
  `OFFLINE ADAPTER READY`仍未通过；下一步进入W3离线可靠性矩阵。

## 2026-08-06：W3离线可靠性、安全与回归Gate

### TDD与实现

- 继续只修改WorkBuddy消费方运行时、测试、打包元数据、Skill和文档；v0.3.21的1566个managed Core文件保持只读。
- 先用真实loopback监听器建立Python子进程联网红灯，再通过消费方`sitecustomize.py`和临时`PYTHONPATH`
  把当前runtime的离线socket拒绝继承到Python子进程；连接在到达监听器前失败。
- 再用Node `net.createConnection`建立独立红灯，通过`NODE_OPTIONS --require`加载消费方CommonJS guard，
  拒绝`net/tls/http/https/dns/dgram/fetch`；执行上下文结束后恢复原环境变量。
- 先建立Tool异常泄漏到CLI/任务JSON、Schema错误泄漏输入值和MCP嵌套ToolResult泄漏三组红灯；随后增加
  统一脱敏模块，在runtime、CLI、MCP和任务原子写入边界替换环境密钥、常见Bearer/API key文本及明确敏感字段。
- 增加SaaS隔离验证：从仓库外目录启动，把SaaS/private Core根指向不存在目录，direct-agent context和
  `golden-key-product-marketing`离线项目创建仍成功，Provider调用0。
- 更新README、架构、路线图、隔离矩阵、WorkBuddy Skill、项目状态和W4交接Prompt；新增W3 Gate报告。

### 验证与边界

- W3专项=`6 passed`；完整WorkBuddy专项=`76 passed`。
- 完整套件=`1136 passed, 10 skipped, 1 subtest passed`；四Pipeline、44个Pipeline Skill、Schema、
  Reviewer/Checkpoint、Tool Registry和既有Core合同保持通过。
- W1 `python -S` Gate=`PASS`：六个禁入路径不存在、静态隔离违规0、活动MCP配置不存在、Provider调用0。
- 消费方Python源码内存编译22个文件通过，`git diff --check`通过。
- W3离线可靠性Gate=`PASS`，但这不是W4打包/全新Windows安装/普通用户WorkBuddy验收，仍不得声明
  “已经可以安装”或`OFFLINE ADAPTER READY`。
- 本轮未调用真实/付费Provider，未修改Golden Key SaaS/private Core仓库；MCP保持`optional`且未发布活动配置。

## 2026-08-06：WB-UX1 WorkBuddy新手引导独立任务

### 边界纠偏与实现

- 将新手引导从W2生产调用和W4安装包中拆出，建立独立任务`WB-UX1`；v0.3.21 managed Core保持只读。
- 新增独立消费方Skill `workbuddy-skill/golden-key-openmontage-onboarding`。它只在用户询问能力、如何开始或
  仅表达模糊视频意愿时触发，读取本机`doctor/context/pipelines/config inspect`后用中文业务结果引导。
- 引导只呈现产品/服务、品牌/公司、获客转化、主体/IP四类结果和少量真实可用示例；用户形成具体请求后
  立即交接给`golden-key-openmontage`生产Skill，不重复已知信息。
- 职责明确冻结：新手引导不属于Core，不盘点或管理Golden Key SaaS素材库，不复制Core的生产需求澄清，
  不属于安装器流程，不创建生产项目，也不调用真实/付费Provider。

### 验证与边界

- 新增WorkBuddy合同测试，覆盖独立触发、真实能力读取、生产Skill交接以及素材库/Core/安装职责隔离。
- Skill Creator格式校验=`Skill is valid!`；专项Skill合同=`5 passed`；完整WorkBuddy专项=`78 passed`。
- 消费方Gate=`PASS`：六个禁入路径不存在、静态隔离违规0、活动MCP配置不存在、Provider调用0；
  `git diff --check`通过。
- 更新`.workbuddy`说明、ROADMAP任务列表和`PROJECT-STATE.md`；真实WorkBuddy首次对话体验验收保留为
  独立客户端验收项，不与W4安装包实现捆绑。
- 已确认本机WorkBuddy进程和窗口存在；Windows应用控制仅返回空壳控件树，无法可靠识别Skill导入或聊天区域，
  因而停止盲点操作并保留客户端验收为`PENDING`，没有伪称触发和交接已经通过。
- 根据用户复核补齐素材引导边界：WorkBuddy消费端可以按需说明如何附加相关本地源素材、提供参考内容，
  或在暂时无素材时先从真实对象和观众行动开始；每轮最多问一个素材交接问题，不要求盘点整个SaaS素材库。
- 素材引导不硬编码C盘/D盘，不移动原文件，不伪称文件已导入、索引或理解；素材事实充分度和后续生产判断
  仍由Core Pipeline合同负责。
- 本轮没有修改Golden Key SaaS/private Core仓库或1566个managed Core文件，没有调用真实/付费Provider。

## 2026-08-06：W4首个轻量ZIP与WorkBuddy调用桥纵向切片

### 产品决策与TDD

- 根据用户纠偏，将首个交付物冻结为`portable ZIP + PowerShell注册脚本`，不是Setup.exe/MSI或独立桌面软件。
  ZIP可解压到任意目录，但WorkBuddy稳定调用必须先注册：复制到用户级安装目录、注册两个Skill并写入runtime locator。
- 明确v0.3.21只用于构建和验证第一个安装/调用包。Golden Key Core正在大调整，本包不把v0.3.21声明为最终Core；
  后续Core更新只能通过新不可变Release/ZIP/SHA/lock和独立W0进入。
- 按TDD先建立三个公共接口红灯再实现：注册根目录外运行`doctor`、包内完整Core/消费方/两个Skill、PowerShell
  注册后launcher从任意cwd定位Core和数据目录。另补Core hash篡改拒绝、MCP默认关闭和数据目录建立合同。
- 普通用户默认路径从开发期D盘纠正为`%LOCALAPPDATA%\GoldenKeyOpenMontageForWorkBuddy`；当前维护者机器仍以
  `D:\WorkBuddyData`保存虚拟环境、缓存、构建和烟测。CLI/MCP默认值统一支持显式环境覆盖。
- `doctor`在既有Core、authority、四Pipeline、Python/Node/FFmpeg扫描上新增九项Python模块只读发现；
  `config inspect`继续只读取Tool Registry配置引用。扫描不下载组件、不读取密钥值，网络/Provider调用均为0。
- 两个WorkBuddy Skill改为先读取注册时生成的`WORKBUDDY-RUNTIME.json`并调用稳定launcher；不再要求普通用户
  自己寻找仓库或扫描磁盘猜路径。MCP保持可选且默认不启用。

### 首个完整候选与当前边界

- 使用真实v0.3.21 lock逐文件校验并打包1566个managed文件，最新ZIP候选大小`72,795,687`字节，SHA-256=
  `45aec88d6ae339c5ef83cd7d46978663f95a14473ad1bc3e1c9dfecb374317f1`；构建目录位于
  `D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-first-bundle-20260806-r4`。
- 在隔离D盘烟测目录完成完整包注册：两个Skill写入独立WorkBuddy profile，MCP=`false`，Core合同、direct-agent
  authority和四Pipeline均通过。系统Python 3.14被发现，但缺`dotenv/google.genai/jsonschema/openai`，证明首包
  下一步仍需实现“用户确认后准备Python依赖”；系统环境`doctor=degraded`。切换到已准备依赖的D盘Python后，
  `doctor/context/pipelines/config inspect`全部退出码0，四Pipeline完整且网络/Provider调用0。
- 当前切片专项：WorkBuddy=`83 passed`（其中portable bundle=`3 passed`、Skill合同=`6 passed`）；
  两个Skill格式均=`Skill is valid!`，`git diff --check`通过。
- 未调用真实/付费Provider，未修改Golden Key SaaS/private Core仓库或1566个managed Core文件；真实WorkBuddy
  普通用户触发、升级/卸载、依赖准备和`OFFLINE ADAPTER READY`仍未通过。

### 首包普通用户入口与`setup.py`边界

- 新增根目录`安装到WorkBuddy.cmd`作为普通用户双击入口；内部固定调用系统Windows PowerShell，注册结束立即执行
  离线`doctor`并把结果写入`WORKBUDDY-INSTALL.json`。检查仍不联网、不调用真实/付费Provider。
- 将安装包SHA-256校验从`Get-FileHash`改为.NET自带实现，避免PATH或PowerShell模块差异导致双击失败。
- `setup.py`最初具有官方OpenMontage历史，但当前已是WorkBuddy消费层自有Python包元数据；Core lock禁止携带或覆盖。
  开发仓库保留它供测试/维护，普通用户ZIP明确排除，用户无需运行传统Python源码安装。
- TDD先验证缺入口及`setup.py`误入包的红灯，再实现；当前portable bundle专项=`3 passed`。
- r4真实ZIP检查：共1593个归档条目、manifest记录1592个文件、Core为1566个；中文入口和内部启动器均存在，
  `setup.py`不存在。D盘隔离双击烟测退出码0，`doctor=pass`，两个Skill均注册，MCP保持关闭，网络/Provider调用0。

## 2026-08-07：公开README差异化重写

- 将根README的WorkBuddy项目介绍从内部阶段/审计叙事改为用户价值叙事，保留后半段官方OpenMontage README原文、
  上游归属和AGPLv3许可证说明。
- 新增与官方OpenMontage的对照表，重点说明WorkBuddy专用direct-agent调用层、四条Golden Key业务Pipeline、
  中文对话式新手引导、轻量ZIP、国内模型生态配置识别、持久任务与可选本地MCP。
- 分别解释产品营销、企业/品牌、线索转化和主体IP四种用户目标；说明每条Pipeline具有完整Stage Skill、Artifact、
  Reviewer、Checkpoint和Publish合同，不将其包装成四个提示词模板。
- 增加素材/参考内容交接示例和新手自然语言入口；说明无素材时从真实对象与观众行动开始，并在需求具体后交给生产Skill。
- 用户介绍区移除首次公开推送规则、仓库同步历史和其他维护者内部信息；保留Pre-Alpha、四条Pipeline为beta、
  未完成普通用户安装/升级卸载/依赖准备/真实Provider验收等边界，避免夸大当前可用性。
- 本轮仅修改消费方公开文档与项目留痕，没有修改1566个managed Core文件，也没有调用任何真实/付费Provider。

## 2026-08-07：GitHub Actions恢复后的跨平台安装测试修正

- GitHub官方状态已将Actions事故标记为Resolved，最新工作流可以正常完成checkout、依赖安装、W1 Gate和lint；
  完整测试暴露的唯一失败是Linux runner尝试启动Windows专用`cmd.exe`。
- 保留Windows对真实双击入口`install-to-workbuddy.cmd`的验证；非Windows runner改为直接调用同一包内的
  `install-to-workbuddy.ps1`公共注册合同，继续验证两个Skill、launcher、离线doctor和零Provider/网络调用。
- 安装后doctor允许诚实返回`pass`或`degraded`：缺少Python运行依赖属于首包已知待准备状态，但`errors`必须为空，
  安装和注册不能因此被误判为损坏。专项=`3 passed`，完整WorkBuddy专项=`83 passed`。

## 2026-08-07：W4经用户确认的轻量Python依赖准备

- 新增`runtime plan`公共接口：只读返回下载需求、目标解释器、requirements位置和确认参数；不创建数据目录，
  网络/Provider调用均为0。未带`--confirm-download`执行prepare必须失败且保持零写入。
- 用户明确同意后，`runtime prepare --confirm-download`使用已有Python创建
  `<data_root>/Runtime/Python`隔离环境，pip缓存固定在`<data_root>/Caches/pip`，不修改系统Python；
  requirements hash一致时幂等复用，既有目标漂移时拒绝覆盖。
- 注册launcher在有效托管环境记录和解释器同时存在时自动优先使用它；生产Skill必须先向用户解释下载和位置，
  不得把视频制作请求当作安装授权。冻结矩阵：Python必需；FFmpeg为合成/本地媒体必需；Node只在
  Remotion或HyperFrames路径需要。
- 新候选r5真实v0.3.21 Core仍为1566个managed文件；ZIP=`72,799,449`字节，SHA-256=
  `ff7af11546b3e4e0e72fb9f9822375825d7d8dc84476b38528195126d5c0bfb3`。D盘隔离注册通过；
  真实`runtime plan=needs_confirmation`，未确认prepare退出码1且Runtime目录不存在。
- WorkBuddy专项=`88 passed`，完整回归=`1148 passed, 10 skipped, 1 subtest passed`；依赖夹具真实创建venv并验证launcher切换和重复复用。没有修改managed Core，
  没有调用真实/付费Provider；真实完整requirements下载保留为明确同意后的普通用户验收项。
- GitHub Actions事故已Resolved；跨平台安装测试提交`b33a512`的CI `31147633115`完整通过。
- 最终W0=`PASS`：1566个managed Core文件精确匹配，Release/Pipeline/运行时隔离/公开lineage/风险扫描/回归
  全部通过；候选17个文件，private Core历史未扫描且不在候选中。测试生成的31个未跟踪`__pycache__`目录先移至
  `D:/WorkBuddyData/Temp/w0-pycache-quarantine-20260807`，没有删除或修改lock管理的Core文件。

## 2026-08-07：W4覆盖解压与手动删除后的重复注册修复

- 根据普通用户最常见行为纠偏安装模型：不要求先卸载或清空解压目录；解压目录是不受控临时来源，正式程序目录是
  可重建的干净副本，用户数据目录独立保存。
- TDD先证明原安装器会把覆盖解压残留文件复制进正式目录；改为逐项验证Manifest、拒绝路径越界，只复制Manifest
  白名单和Manifest本身。额外文件按相对路径写入`source_package.extra_files_ignored`，不复制、不执行。
- TDD再证明原安装器会拒绝重复运行；新增所有权预检和`fresh_install/repair`记录。已有程序只有有效
  `WORKBUDDY-INSTALL.json`时可替换，已有Skill只有有效`WORKBUDDY-RUNTIME.json`时可替换。
- 现可覆盖解压、从不同解压目录重复运行、补回被删除的项目自有Skill，并在正式程序目录被整体删除后重建；
  `Projects`数据哨兵在全部修复过程中保持不变。
- 同名外来Skill会fail closed并原样保留，且在任何程序安装变更前终止；现有安装版本与当前包不一致也拒绝替换，
  防止旧包静默降级或绕过未来升级合同。若程序目录已删除但遗留Skill属于另一版本，同样在任何写入前拒绝。
  缺文件和声明文件篡改也在写入前拒绝。portable bundle专项=`10 passed`。
- 真实v0.3.21候选r7：ZIP=`72,800,975`字节，SHA-256=
  `ebf95cd067dce94bdf25f979740484e453df9dcd91b0a3dadde5c08eb6e1589a`，位置为
  `D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-tolerant-install-20260807-r7`。
- D盘隔离烟测模拟覆盖残留、重复运行、移动一个Skill代表手动删除、移动正式程序目录代表手动删除、从第二个解压目录
  恢复和外来同名Skill冲突；最终两个Skill完整、用户数据哨兵不变、额外文件未进入正式目录、网络/Provider调用0。
- WorkBuddy专项=`95 passed`；完整回归=`1155 passed, 10 skipped, 1 subtest passed`；四Pipeline、44个阶段Skill、
  Schema/Tool Registry、Reviewer/Checkpoint和既有Core合同保持通过。
- W1消费方Gate=`PASS`：六个禁入路径不存在、静态隔离违规0、活动MCP配置不存在、Provider调用0。
- 最终W0公开性审计=`PASS`：1566个managed Core文件精确匹配，Release、四Pipeline合同、direct-agent运行时、
  公开lineage、风险扫描和回归均通过；private Core历史未扫描且不在候选中。最终证据目录为
  `D:/WorkBuddyData/Temp/w4-tolerant-install-publication-audit-20260807-r7-final`。
- 当前切片不是跨版本降级、完整卸载或事务级版本回滚；这些仍属于W4下一片。未修改v0.3.21 managed Core，
  未调用真实/付费Provider，也未修改Golden Key SaaS/private Core仓库。

## 2026-08-07：W4跨版本升级、失败回滚与默认保留数据的卸载

- 纠正上一片只完成“重复注册前置”但尚未实现真正升级/卸载的边界；本片继续只修改WorkBuddy消费方安装脚本、
  打包清单、合同测试和公开文档，v0.3.21 managed Core保持只读。
- TDD先证明更高版本会被旧安装器一律拒绝；新增Pre-Release版本比较，严格更高版本进入`upgrade`，相同版本仍为
  `repair`，较旧包继续fail closed。默认程序目录从Manifest动态读取版本，不再硬编码当前版本。
- TDD用缺失业务Pipeline的新包触发doctor失败，证明旧实现会错误提交失败升级并删除旧程序；新增事务边界，
  新程序/Skill只有doctor=`pass/degraded`才提交，任一步失败都撤销新版本并恢复旧程序和两个旧Skill。
- 新增`uninstall-workbuddy.ps1`和中文`从WorkBuddy卸载.cmd`；卸载前验证安装记录和Skill runtime marker，
  只移除所有权匹配的可重建内容，DataRoot固定保留，并写入`Logs/WORKBUDDY-LAST-UNINSTALL.json`。
- Windows自卸载先注销Skill并让CMD正常退出，再由隐藏延迟清理进程删除程序目录；外来或所有权标记不匹配的Skill
  原样保留并列入`protected_skills`。当前不提供默认删除用户数据或主动降级。
- portable bundle专项=`16 passed`，覆盖升级成功、失败回滚、动态默认目录、DataRoot漂移拒绝、真实中文CMD自卸载、数据哨兵、
  外来Skill保护、覆盖解压和既有修复合同。
- 最终真实候选r10：ZIP=`72,805,580`字节，SHA-256=
  `e0fd2ea1ee6831ee5652b32e13c42d92afca77773babdb341bc606e61bac46e4`，位置为
  `D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-upgrade-uninstall-20260807-r10`。
- r10 D盘矩阵先证明错误DataRoot在写入前退出1且不建立空数据目录；再从真实ZIP安装v1，使用同一包合同模拟v2
  向前升级，并以缺一个业务Pipeline的v3触发doctor失败；
  v2程序和Skill被恢复，坏v3目录撤销。随后从已安装v2双击中文卸载入口，程序和两个自有Skill移除，DataRoot哨兵保留。
- WorkBuddy专项=`101 passed`；完整回归=`1161 passed, 10 skipped, 1 subtest passed`；四Pipeline、44个阶段Skill、
  Schema/Tool Registry、Reviewer/Checkpoint和既有Core合同保持通过，网络/Provider调用0。
- W1消费方Gate=`PASS`：六个禁入路径不存在、静态隔离违规0、活动MCP配置不存在、Provider调用0。
- 最终W0公开性审计=`PASS`：1566个managed Core文件精确匹配，Release、四Pipeline合同、direct-agent运行时、
  公开lineage、风险扫描和回归均通过；private Core历史未扫描且不在候选中。最终证据目录为
  `D:/WorkBuddyData/Temp/w4-upgrade-uninstall-publication-audit-20260807-r10-final`。

## 2026-08-07：W4真实默认路径安装、自卸载修复与客户端清理

- 从r10继续执行真实Windows默认路径验收，发现已安装launcher从开发仓库cwd调用时会被仓库内同名Python包遮蔽。
  launcher现先切换到已安装runtime根再执行Python，真实输出的Core根已确认来自`%LOCALAPPDATA%`安装目录。
- 真实双击中文卸载入口暴露第二个缺陷：CMD自身仍占用已安装目录时，延迟清理可能提前放弃并留下程序根。
  CMD现先切换到`%TEMP%`再启动卸载器；延迟清理由10次增至60次、每次500ms，真实自卸载退出0且程序根最终消失。
- 新增安装launcher抵御调用者cwd同名包遮蔽的合同测试，并让Windows测试助手从真实staging cwd启动自卸载。
  portable bundle=`17 passed`，WorkBuddy专项=`102 passed`；contracts/backlot=`753 passed, 8 skipped`，
  lib/qa/tools=`307 passed, 2 skipped, 1 subtest passed`，合计=`1162 passed, 10 skipped, 1 subtest passed`。
- r11真实候选ZIP大小`72,805,854`字节，SHA-256=
  `C81516E6225BCFF43204F5FE17A5DD44F21D82285F913E8EBCB8704316297DE8`，位置为
  `D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-clean-uninstall-20260807-r11`。
- 默认路径安装与WorkBuddy Skill发现通过；本轮没有下载完整Python requirements，`doctor=degraded`只报告缺失依赖，
  Core/authority/四Pipeline合同无错误，网络/Provider调用0。自然语言`我不知道怎么开始做视频`被WorkBuddy通用
  视频流程接管，没有进入本项目新手引导，因此`WB-UX1`真实路由明确为`FAIL/PENDING`。
- r11代码候选当时W0=`PASS`：1566个managed Core文件精确匹配，Release、四Pipeline合同、direct-agent边界、公开lineage、
  风险扫描和回归均通过；候选4个文件，snapshot SHA=
  `a43143076b42a6ee9ba7c4e0a6ae6292e7b94d0bba78fbff09bb66577b01ccba`，证据目录为
  `D:/WorkBuddyData/Temp/w4-clean-uninstall-publication-audit-20260807-r11-final`。
- 按用户要求完成验收后清理：默认安装根、两个Golden Key Skill、MCP注册和后台进程均不存在；三条本项目
  验收会话标记删除，关联会话/trace文件移出WorkBuddy用户目录到
  `D:/WorkBuddyData/Temp/workbuddy-acceptance-trace-quarantine-20260807`。清理后重新启动并退出WorkBuddy，
  删除状态未被同步恢复，也未出现新的Golden Key MCP连接。未清空用户账号、其他项目或全局WorkBuddy数据。
- 本轮未修改v0.3.21 managed Core、Golden Key SaaS/private Core仓库，也未调用真实/付费Provider。
- 提交前在W0顺序执行Core大套件和PowerShell安装测试时，发现Windows未处理错误记录在重定向宿主中可能只返回退出码1、
  丢失错误文字。安装器现以顶层`trap`和原生stderr统一返回拒绝原因；测试助手也归一化异常空流。17项安装包专项通过。
- 最终r18 ZIP大小`72,806,177`字节，SHA-256=
  `310050115DA8EAD14B1131C9AC51C95B9A67CC478CA2B829C13C15E366429BF3`，位置为
  `D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-final-clean-baseline-20260807-r18`。
- 最终W0=`PASS`：contracts `716 passed, 7 skipped`、tools `284 passed, 1 subtest passed`、WorkBuddy
  `102 passed`；1566个Core文件及全部四Pipeline合同通过，候选9个文件，snapshot SHA=
  `bb47187cad702320da29dc7c3aa21bbde92bb3f2d9c0b269ede45477d849ad2c`。证据目录为
  `D:/WorkBuddyData/Temp/w4-clean-client-final-publication-audit-20260807-r17`。
- 首次推送提交`df89724`后，公开CI `31177430424`的Linux runner暴露测试助手跨平台cwd错误：Windows真实自卸载
  需要从安装目录启动中文CMD，Linux却直接运行PowerShell脚本；错误地共用安装目录cwd导致Linux认为目录正在使用。
  测试助手现只在Windows使用安装目录cwd，非Windows回到父目录。该修复不改变产品卸载合同或managed Core。

## 2026-08-07：生产工具API Key本地配置与新手引导

- 根据用户纠偏，本切片解决的是文生图、图生视频、文生视频、TTS和数字人等生产工具Provider的API Key配置，
  不是WorkBuddy对话模型扫描，也不修改Golden Key Core。
- 先补红灯合同，再实现`config guide`：按能力报告DashScope、豆包、火山即梦、可灵官方、Seedance网关和
  MiniMax网关的Key名称与`present_unverified/partial/not_configured`状态；输出不含Key值，静态检查不联网。
- 新增包内`配置API密钥.cmd`和`configure-provider-keys.ps1`。用户在本地窗口隐藏输入，凭据用Windows当前用户
  DPAPI保存到`<DataRoot>/Config/golden-key-provider-credentials.json`；launcher仅在当前进程解密注入且不覆盖
  已存在的进程环境变量。文件只接受8个白名单变量并限制为当前用户访问。
- 新手引导和生产Skill均禁止要求用户把Key粘贴到WorkBuddy聊天；只按当前目标推荐一到两个相关Provider。
  `present_unverified`统一解释为“已录入但未验证”，保存Key不授权网络、连通性测试、余额检查或真实/付费生成。
- 真实r21隔离安装发现普通用户缺`jsonschema`时`config guide`无法启动；该包随即作废。新增回归并实现依赖前
  fallback：仍按锁定消费方索引显示配置选择，同时明确`tool_registry_verification=deferred_missing_python_dependency`；
  依赖准备完成后继续使用实际Tool Registry做严格核验，不把fallback包装成Registry已通过。
- 最终r23 ZIP大小`72,812,987`字节，SHA-256=
  `ca71961edfd76c87cb91fb7b8f8857e599c748cea0b486ecc38baa1beeb8eb38`，位置为
  `D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-api-key-guide-20260807-r23`。
- r23隔离安装=`PASS`：Core 1566文件、direct-agent authority和四Pipeline正常；在系统Python依赖不完整时
  `config guide=pass`、6个Provider、Key值返回0、网络/Provider调用0；向导可打开并取消且不落凭据文件。
  验收后自卸载成功，隔离程序目录和两个Skill均不存在。
- DPAPI已安装launcher端到端合同通过；API Key专项、Skill和portable bundle合计`33 passed`，完整WorkBuddy专项
  `108 passed`；两个Skill均通过Skill Creator格式校验。前向测试证明无安装登记时Skill会诚实阻断、不搜索磁盘，
  并引导用户在本地隐藏输入而不是聊天发送Key。
- 最终W0=`PASS`：Release、1566个managed Core文件、四Pipeline/44个阶段Skill、Schema/Tool/Checkpoint合同、
  direct-agent边界、公开lineage、风险扫描和回归全部通过；contracts=`716 passed, 7 skipped`，tools=
  `284 passed, 1 subtest passed`，WorkBuddy=`108 passed`。证据目录为
  `D:/WorkBuddyData/Temp/w4-api-key-guide-publication-audit-20260807-r23-final`。
- 本轮未修改v0.3.21 managed Core、Golden Key SaaS/private Core仓库，未调用真实或付费Provider。

## 2026-08-08：API Key目标优先新手引导

- 根据用户确认，将API配置体验从“先列Provider和环境变量”改为“先选生产目标”：生成图片、生成视频、中文配音、
  数字人/口型驱动、语音识别与内容分析。每个目标只标记一到两个推荐Provider，其他接入保留为高级选择。
- 核验阿里云百炼、火山引擎IAM/豆包语音、可灵开发者平台、fal.ai和Replicate官方入口；配置报告新增中文Provider
  名称、友好凭据字段、厂商直连/第三方网关、官方申请与说明链接、账户/地区/权限限制和费用提醒。
- 本地向导先问目标，再列推荐Provider。普通列表不展示`VOLC_ACCESSKEY`、`KLING_API_KEY`等环境变量；只有用户
  选定Provider并进入隐藏录入时，才在友好字段名后标明内部变量。Key仍使用当前Windows用户DPAPI保护。
- WorkBuddy只有在用户明确选择“现在配置”后，才可用`Start-Process`打开可见本地窗口；宿主无法启动时回退到
  用户双击`配置API密钥.cmd`。Key不进入聊天、普通参数、Artifact或日志。
- 新增中文数据后发现Windows PowerShell/Python输出编码风险；launcher现固定`PYTHONUTF8=1`和
  `PYTHONIOENCODING=utf-8`，真实隔离安装确认中文Provider和能力标签无乱码。
- TDD初始6项红灯全部转绿。API配置、Skill和portable bundle专项=`35 passed`；完整WorkBuddy专项=`109 passed`；
  两个Skill通过Skill Creator格式校验，PowerShell脚本解析0错误。
- 首次安装态前向测试发现依赖不完整时错误建议重装ZIP；随后修正新手Skill：先运行`runtime plan`，解释下载到
  独立DataRoot并等待明确同意，不在依赖准备前运行严格`context/pipelines/config inspect`。第二次前向测试通过，
  正确区分“允许下载运行环境”和“现在配置API”两次授权。
- 最终r25 ZIP大小`72,817,257`字节，SHA-256=
  `d572aaff91e4863886e694a08af3f8148000e083d18978578d23fb9677cea725`，位置为
  `D:/WorkBuddyData/Temp/golden-key-workbuddy-w4-goal-first-api-guide-20260808-r25`。
- r25隔离安装=`PASS`：5类目标、6个Provider、中文输出、推荐过滤、取消不落凭据均通过；Key值返回0，
  网络/Provider调用0。未修改v0.3.21 managed Core或Golden Key SaaS/private Core仓库。
- 最终W0=`PASS`：Release、1566个managed Core文件、四Pipeline/44个阶段Skill、Schema/Tool/Checkpoint合同、
  direct-agent边界、公开lineage、风险扫描和回归全部通过；contracts=`716 passed, 7 skipped`，tools=
  `284 passed, 1 subtest passed`，WorkBuddy=`109 passed`。证据目录为
  `D:/WorkBuddyData/Temp/w4-goal-first-api-guide-publication-audit-20260808-r25-final`。
- 验收后r25隔离程序目录和两个Skill均已卸载；默认WorkBuddy安装根不存在，WorkBuddy进程为0，继续保留纯新人工验收起点。

## 2026-08-08：一次确认后的完整本地视频制作环境

- 根据用户对FFmpeg、Remotion和HyperFrames“发现缺失会被Core跳过”的纠偏，把W4从仅准备Python扩展为标准
  `complete_video_production`环境。轻量ZIP不内嵌大型运行时；用户接受一次下载、存储与许可提示后，统一准备
  Python、FFmpeg、Node、Remotion、HyperFrames和托管浏览器。大型生成模型与在线Provider继续按目标单独授权。
- 新增`WORKBUDDY-PRODUCTION-RUNTIME.lock.json`：固定Node 22.23.2和FFmpeg 8.1.2发行URL/SHA，锁定
  Remotion package-lock、HyperFrames 0.7.101 package-lock和Chrome for Testing 152.0.7928.2。计划预估下载
  0.5–1.2GB、Runtime落盘1.2–3GB，并在确认前披露FFmpeg GPLv3与Remotion许可条件。
- TDD按`runtime plan/prepare`、`doctor`、launcher和两个WorkBuddy Skill公开边界推进；用户不在安装阶段选择
  Remotion/HyperFrames，具体生产方案仍遵守Core要求的普通语言说明、推荐与批准合同。API Key配置与本地环境下载
  继续是两个独立Gate，未调用真实或付费Provider。
- r26首次真实准备完成Python、FFmpeg、Node和两个npm引擎后，Puppeteer浏览器下载在约18分钟后以
  `ECONNRESET`失败。没有换镜像或静默跳过；改为我们的固定SHA下载器先校验官方Google Storage资产，再把缓存
  交给Puppeteer原子解压，并给下载和外部命令增加总超时。浏览器资产大小`120,932,410`字节，SHA-256=
  `ec7d7cfbc9d97093c9269d6a26de78a3244a49f3112ff9616e2ccb5ac3afeb24`。
- r27真实D盘隔离准备=`PASS`：6个组件均创建；Runtime=`1,504,426,322`字节（1.401GiB），Caches=
  `500,145,944`字节（0.466GiB）。第二次prepare在2.1秒内`created=false/reused=true/network_calls=0`。
- 真实`doctor`又发现Remotion `.cmd --version`探测超时但总状态误报pass；改为托管Node直接运行Remotion
  `versions`与HyperFrames入口，并让总ready同时要求文件合同和可执行探测通过。r28安装复用DataRoot后
  `doctor=pass`，Remotion 4.0.484与HyperFrames 0.7.101均可执行。
- Core只读探测报告`render_engines={ffmpeg:true, remotion:true, hyperframes:true}`；托管Chrome进程返回
  `Google Chrome for Testing 152.0.7928.2`。HyperFrames doctor确认Node/FFmpeg/FFprobe/Chrome，另列出的
  Whisper/Kokoro/MusicGen/Docker为非标准可选能力，不纳入本次完整本地合成环境Gate。
- 复用既有DataRoot安装新App时发现Remotion junction不会自动出现在新程序目录；`runtime prepare`的ready路径
  现也执行幂等链接修复，安装器仅在只读plan已经是ready时无下载调用prepare，确保修复/升级后Core composer
  能解析托管依赖。该操作不修改系统PATH/Python，未知node_modules目录仍fail closed。
- 本轮所有改动均为WorkBuddy消费层；v0.3.21的1566个managed Core文件未修改，Golden Key SaaS/private Core
  仓库未触碰。真实WorkBuddy自然语言路由和Human Checkpoint仍未完成，不声明`OFFLINE ADAPTER READY`。
- r29轻量ZIP大小`72,849,518`字节，SHA-256=
  `abb350f5c004e19f390e56e0fe4b02ab8abe4f4a1581838f55de1c518485b2a2`。复用ready DataRoot安装后，安装器以
  `network_calls=0`修复新App的Remotion junction，`doctor=pass`，两个本地引擎版本与浏览器状态均可见。
- W0运行前清理了212个由实机导入生成的`.pyc`缓存文件；它们是可重建产物，不是Core清单文件。随后以
  `PYTHONDONTWRITEBYTECODE=1`执行权威审计，Gate=`PASS`：verified Core=`1566`，候选=`24`；contracts=
  `716 passed, 7 skipped`、tools=`284 passed, 1 subtest passed`、WorkBuddy=`111 passed`。证据目录为
  `D:/WorkBuddyData/Temp/w4-complete-runtime-publication-audit-20260808-r29-final-r3`。

## 2026-08-08：W4.1项目专用便携Python与完整首装闭环

- 本轮只继续WorkBuddy消费层W4.1；v0.3.23 Core集成按用户决定留到后续新对话。没有修改v0.3.21的1566个
  managed Core文件，没有同步Core main、调用Provider、读取凭据或制作正式Release。
- 新增`WORKBUDDY-BOOTSTRAP-RUNTIME.lock.json`：固定python.org Windows embeddable Python 3.13.15和
  PyPI官方pip 26.1.2 wheel的资产名与SHA-256。普通用户包由launcher优先使用该解释器，不要求系统Python，
  Python第三方依赖仍安装到`<DataRoot>/Runtime/Python/site-packages`，不修改系统Python/PATH。
- TDD真实资产探针发现pip wheel虽已复制进包，却没有进入嵌入式Python的`._pth`，因此`python -m pip`失败；
  构建器现把wheel名称写入唯一`._pth`，同时重算BUNDLE-MANIFEST中的文件大小和SHA，避免完整性清单失真。
- 下载器支持同一锁定资产的镜像URL列表、断点续传和最终SHA校验。生产锁更新为FFmpeg 9.0 gyan.dev构建；
  Node 22.23.2与Chrome 152优先使用已声明的大陆镜像，失败时只退到同一版本的官方URL，不自动换版本。
- 真实Windows隔离fresh install使用包内Python成功发现四条Pipeline；无系统PATH的`doctor`与`runtime plan`
  均可运行，确认前网络/Provider调用0。完整`runtime prepare`用时约631.6秒，网络调用6次、Provider调用0，
  Python依赖、FFmpeg 9.0、Node 22.23.2、Remotion 4.0.484、HyperFrames 0.7.101与Chrome 152全部ready。
- 首次安装后doctor发现Remotion冷启动`versions`超过旧20秒超时；直接命令随后在2.145秒完成，证明是冷启动容忍
  不足而非安装损坏。新增红测并把Remotion探针窗口提高到60秒；重建后同版本repair复用DataRoot、网络调用0，
  最终`doctor=pass`且无warnings/errors。
- HyperFrames真实doctor确认受管Node、FFmpeg、FFprobe和Chrome路径通过；Whisper/Kokoro/MusicGen与Docker daemon
  为可选能力，未纳入四Pipeline基础合成环境Gate。
- validation-only ZIP大小`85,860,139`字节，SHA-256=
  `2b54a4f5cbf8f8c53716a9d1a89684aae759149a3ffedceda56f58c0b3bfa423`，包含1637个Manifest文件项；状态仍为
  `first_installer_build_validation_only`，Core usage仍为`temporary_first_package_build_baseline_not_final_core`。
- 真实用户同款中文自卸载退出0，移除程序和`golden-key-openmontage`、`golden-key-openmontage-onboarding`两个Skill，
  无protected Skill或cleanup warning；随后删除整个隔离DataRoot与构建探针，只保留validation-only ZIP证据。
- 定向运行时/打包专项=`33 passed, 1 skipped`，WorkBuddy全量=`119 passed, 1 skipped`。最终W0=`PASS`：
  Release合同、四Pipeline/Skill/Schema/Tool/Checkpoint合同、direct-agent边界、公开lineage、风险扫描和回归均通过；
  contracts=`716 passed, 7 skipped`、tools=`284 passed, 1 subtest passed`、WorkBuddy=`119 passed, 1 skipped`。
  证据目录为`D:/WorkBuddyData/Temp/w41-publication-audit-20260808-final`。

## 2026-08-14：WB-OFFICIAL-SUCCESS-CLOSEOUT1 官方成功证据收口与环境隔离

### 范围和权威口径

- 收口官方 OpenMontage 在真实 WorkBuddy 中已经跑通的成功证据，不重新测试、渲染、修复、安装、打包或调用 Provider。
- 采用用户纠正后的权威结论：官方原包可被 WorkBuddy 跑通=`PASS`；`REAL_WORKBUDDY/CAPABILITY_REAL/LOCAL_RENDER_E2E/BUSINESS_EFFECTIVE=PASS`；`STRICT_MANIFEST_CONFORMANCE=PARTIAL`但不否决跑通。
- 外部平台发布、Provider/cloud/SaaS E2E 均为本阶段`OUT OF SCOPE`；下一 Gate 尚未执行。

### 收口前只读基线

- 主协调工作区：`D:\BlazingCD\Personal\Golden_Key_OpenMontage_for_WorkBuddy`，分支 `codex/w4.1-portable-python`，HEAD=`347272cf11eb774be64f63746edec92ccbf7d79d`，工作树仅 `?? .codex/config.toml`。
- `.codex/config.toml` 保持原样，36字节，SHA-256=`E5D533440B4EF6587293B3596DDA46DD8525F9A39107108B75C67B6F2E49AAFC`，未暂存。
- 官方目录：`D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-audit-4eab34c5`，detached HEAD=`4eab34c5cfcccaa4f1970554928feccce73ee930`，2038个tracked文件，tracked diff=0、staged=0，只有两份源码区未跟踪脚本。
- WorkBuddy 5.3.12 主进程和daemon/sidecar/agent子进程仍在运行；未关闭或操作客户端。

### D盘证据归档

- 建立固定目录：`D:\WorkBuddyData\Evidence\openmontage-official-success-closeout-20260814`，目标原先不存在，未覆盖任何文件。
- 逐文件复制并校验28个证据文件，共25,366,607字节；归档含：
  - 两份源码区未跟踪脚本原始副本；
  - 用户级`openmontage-ffmpeg-portrait-render` Skill完整目录；
  - `IDENTITY.md/SOUL.md/USER.md`当前版和WorkBuddy file-history可证明的任务前`@v1`字节版；
  - HY3/Kimi两条成功会话JSONL、公开链接和归因说明；
  - 项目关键artifacts、字幕、`events.jsonl`、`project.json`、项目级`render_full.py`；
  - 三份成片的绝对路径、大小、时间、SHA-256清单；大媒体保留原位，没有重复复制；
  - `RESTORE-MANIFEST.md`、运行路径差异和完整归档哈希清单。
- 两条会话归档副本：
  - HY3 JSONL 16,460,654字节，SHA-256=`05548CCD26AD29D14D74541FC0F8EA0D6740728D77C8A4CDCD6CBE0B5FC94BC9`；
  - Kimi JSONL 8,792,064字节，SHA-256=`D58ECCD59CB97CD88F83F7F522F9155ACB2891789EC706786113672CC9AFD5B2`。

### 官方目录清理

- `scripts\prepare_fresh_edit.py`：10,711字节，SHA-256=`91B9B262DD021B6435E1674358E8CEF6A044D63E712C5E4AF781EB7875BDE52F`。
- `scripts\render_portrait.py`：10,490字节，SHA-256=`D0E228FABD7249350DFA23D76D97CDEAE3C6374568EB46D21B738BE08E9E70AE`。
- 两文件均先复制到`source-originals\scripts`并逐文件比对SHA，再验证源/目标解析路径边界，最后移动到`quarantine\source-scripts`；没有永久删除。
- 收口后官方HEAD仍为`4eab34c5...`，tracked diff=0、staged=0、普通`git status`干净。
- `projects\toutouxiang-store-intro`保持153文件、323,541,631字节；三份成片仍存在且哈希不变：
  - 原始版=`5DC81BF08304430188AC01BE1A50C5D8AD846F59FE66CB4EDF80CFC506796F71`；
  - v2=`2AEF76501CFF007213B044030593CBC80FB8AEB753480F684DD8104C616A5887`；
  - fresh=`14E356A293FD9CB28CD43A54CC4182E79BC1D47FC27949A23AB09CA170764F22`。
- 未触碰任何tracked源码、`projects/`内容、`.venv`、`node_modules`、缓存或其他ignored文件。

### WorkBuddy持久干扰

- 用户级FFmpeg Skill已完整归档并复核两个文件SHA，但因WorkBuddy仍在运行，没有从active skills目录移动；活动路径和字节保持不变。
- Kimi会话首轮注入内容与file-history `@v1`共同证明三份任务前画像：
  - `IDENTITY=EA88682EFDE077F73D6D7625B03915455C87FEC5B4D5ADD6CA7C5842D8BB92E0`；
  - `SOUL=09E4782B1CE17312C22050947B3D5C699C3B51D391669A1BFB66A5CD36971EF4`；
  - `USER=5ABB73720FABC14F3C602CD0C0FFE6AC8D798BEB29278B3C12910617522ED06E`。
- 任务前版本和当前版本均已归档；因客户端活动占用，没有猜测性或竞争性回写，列为后续人工窗口决策。
- `.mcp.json`及其他无法归因配置未修改；已恢复启用的`golden-key-video-agent`仅只读记录为存在、2文件、21,960字节，未触碰。

### 成功/失败解释器路径差异

- 既有失败基线的裸`python/python3`默认落到WorkBuddy内置Python目录；该解释器缺`requests`，`registry.discover()`在导入ComfyUI client时失败。对照证明官方项目`.venv`可导入`requests 2.34.2`。
- HY3使用官方项目`.venv`执行registry preflight和`init_project()`；后续项目级`render_full.py`只依赖标准库、`subprocess`和FFmpeg，可在内置Python上完成成片。
- Kimi fresh明确使用官方项目`.venv\Scripts\python.exe`直接执行`prepare_fresh_edit.py`和`render_portrait.py`。
- Host解释器因此是与Agent命令路径和依赖集合相关的偶发可靠性风险，不是已证明的全局主阻断。
- HY3原始成片写入时间早于用户级Skill和两份Kimi源码脚本，故成功不依赖它们；Kimi v2/fresh直接依赖源码脚本，但现有成功命令没有通过用户级Skill作为必经入口。

### 中文fork和集成状态

- 正确中文fork为`https://github.com/noah-1106/openmontage-zh-mcp`，不是`OpenMontage-golden-key`。
- 本专项采用的已确认只读值为`main/HEAD=1aa30636325bb1dab60e81d1bf76d6df2dd662ca`；本轮没有下载或验证该fork，实际使用前仍需按运行时重新锁定。
- 文档改动只位于独立任务分支`codex/wb-official-success-closeout1`，只修改`PROJECT-STATE.md`和`WORK-LOG.md`；`PROJECT_CONTEXT.md`无需改动。
- 该任务分支需要后续选择性集成到主协调长期分支；主协调分支本轮没有更新，不建PR、不合并、不rebase、不从main同步。

### 零边界

- 零Provider调用、零费用、零新WorkBuddy运行/会话、零preflight/测试/W0/repair、零媒体生成。
- 未下载中文fork，未验证v0.3.23，未修改官方tracked源码，未修改或删除`.codex/config.toml`。

## 2026-08-14：WB-OFFICIAL-SUCCESS-CLOSEOUT1 后续环境隔离完成

### 执行前边界

- 用户确认 WorkBuddy 已完全退出并明确不保留门店任务写入的画像设置。
- 再次只读复核 `WORKBUDDY_RELATED_PROCESS_COUNT=0`；任务分支为 `codex/wb-official-success-closeout1@3ca7dfb` 且干净。
- 主协调工作区仍为 `codex/w4.1-portable-python@347272cf11eb774be64f63746edec92ccbf7d79d`，仅有 `?? .codex/config.toml`；该文件36字节、SHA-256=`E5D533440B4EF6587293B3596DDA46DD8525F9A39107108B75C67B6F2E49AAFC`。

### 临时 Skill 隔离

- 精确对象：`C:\Users\blazi\.workbuddy\skills\openmontage-ffmpeg-portrait-render`。
- 移动前再次复制到 `D:\WorkBuddyData\Evidence\openmontage-official-success-closeout-20260814\pre-isolation-copy\openmontage-ffmpeg-portrait-render-20260814T161526+0800`，不覆盖既有归档，并逐文件比对大小和SHA。
- 在移动前立即再次确认相关进程为0，再将整个活动目录可恢复地移动到 `quarantine\workbuddy-skill-openmontage-ffmpeg-portrait-render-20260814T161526+0800\`；没有永久删除。
- 移动后活动路径不存在；quarantine 中 `SKILL.md` SHA=`7D6664326DF1E7E304175EF7E9D1B2E03CBE5585E829912FDDC1B42D999BE017`，`scripts\render_portrait.py` SHA=`448CB22BF98E4D809BEF3B36648A25A40F62FF899094E3C08663B0243AEBED4C`。
- 未触碰 `golden-key-video-agent` 或其他 Skill。

### 画像恢复

- 覆盖前把当时活动的三文件再次复制到 `profiles\pre-restore-current-20260814T161526+0800\`，逐文件核对为初次收口时的当前版字节。
- 使用归档 `profiles\pre-store-tasks\` 中已证明的完整任务前版本恢复活动文件；恢复后SHA精确为：
  - `IDENTITY.md=EA88682EFDE077F73D6D7625B03915455C87FEC5B4D5ADD6CA7C5842D8BB92E0`；
  - `SOUL.md=09E4782B1CE17312C22050947B3D5C699C3B51D391669A1BFB66A5CD36971EF4`；
  - `USER.md=5ABB73720FABC14F3C602CD0C0FFE6AC8D798BEB29278B3C12910617522ED06E`。
- `.mcp.json`、`mcp.json`哈希前后不变，其他无法归因配置未修改。

### 归档、结论与集成

- `CLOSEOUT-SUMMARY.md`和`RESTORE-MANIFEST.md`已更新为环境隔离`COMPLETE`；归档现有44个文件，哈希清单覆盖除自身外的43项并重新验证43/43一致。
- 官方原包真实WorkBuddy跑通仍为`PASS`；`STRICT_MANIFEST_CONFORMANCE=PARTIAL`仍是非否决治理项；Publish/Provider/cloud/SaaS仍为`OUT OF SCOPE`。
- 正确中文fork仍为`https://github.com/noah-1106/openmontage-zh-mcp`；下一Gate未执行。
- 初始收口提交`3ca7dfb`与本完成提交按顺序选择性cherry-pick到长期分支`codex/w4.1-portable-python`并推送；不merge、不rebase、不从main同步。

### 零边界

- 零WorkBuddy启动、零Provider调用、零费用、零测试/渲染/安装/repair/W0、零媒体生成。

## 2026-08-15：WorkBuddy Shell V2统筹文档固化

- 根据用户明确要求，将Shell V2目标、职责边界、防漂移停止规则、任务todo/done、阶段1执行步骤和分层验收从聊天内容迁移为版本化项目文档。
- 新建`docs/workbuddy/v2/`权威入口及六份文档：`README.md`、`PROJECT-CHARTER.md`、`DRIFT-GUARD.md`、`TASK-REGISTER.md`、`STAGE-1-EXECUTION-PLAN.md`、`ACCEPTANCE-MATRIX.md`。
- 权威关系冻结为：任务状态以`TASK-REGISTER.md`为准；目标和职责以`PROJECT-CHARTER.md`为准；停止条件以`DRIFT-GUARD.md`为准；阶段1只按专门执行计划推进；旧架构和handoff只作历史输入。
- 最高原则明确为：WorkBuddy负责对话，OpenMontage负责生产决策与执行，Shell只负责安装、对象锁定、运行环境绑定、会话入口以及状态和结果转交。Shell不得选择Pipeline、创建Artifact、推进Checkpoint、选择Provider、判断媒体方案或形成第二套Director/FSM。
- 八阶段全部登记为任务；当前`V2-GOV-001=DONE`，`V2-S1=READY_NOT_STARTED`，阶段2至8均为`PLANNED`且受前序Gate阻断。
- 本次文档工作不是阶段1执行：没有创建`codex/workbuddy-shell-v2`分支或worktree，没有修改生产代码、Skill、安装器、测试、配置、lock或Core，没有运行测试、WorkBuddy、安装、Provider或媒体生成。
- 已批准的V2代码基线保持`2a2bf09832d558388dc2816c54b32a2dce4aa607`；阶段1必须在文档审阅和新授权后才能从该精确提交开始。
- 既有未跟踪`.codex/config.toml`和`docs/workbuddy/WORKBUDDY-SHELL-V2-REFACTOR-HANDOFF-2026-08-15.md`未修改、未暂存、未纳入本次文档范围。
