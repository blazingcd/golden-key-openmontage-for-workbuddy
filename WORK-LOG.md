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
