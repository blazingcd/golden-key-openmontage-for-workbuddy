# Golden Key OpenMontage for WorkBuddy：W0执行启动Prompt

> **历史交接，已被取代。** 本文件描述`golden-key-v0.3.18`整仓/private ancestry旧方案，禁止继续执行。
> 当前权威交接为`NEXT-CONVERSATION-PROMPT-2026-08-05-W1.md`，同步源只能是
> `golden-key-v0.3.21` WorkBuddy Callable Core Release资产和lock。

请在以下本地仓库继续工作：

`<WORKBUDDY_REPO_ROOT>`

本轮不要只重新规划，也不要停在口头分析。请读取权威文件、核对真实Git状态，然后直接执行W0公开性、架构和接口审计；留下可复核证据、更新项目状态并提交安全的本地变更。特别注意：本地已经同步完整Golden Key核心，但公开WorkBuddy fork目前仍只有官方OpenMontage代码，不能把这两个状态混为一谈。

## 开始前必须完整读取

1. `AGENTS.md`
2. `AGENT_GUIDE.md`
3. `PROJECT-STATE.md`
4. `WORK-LOG.md`
5. `docs/workbuddy/ARCHITECTURE.md`
6. `docs/workbuddy/CORE-SYNC-POLICY.md`
7. `docs/workbuddy/ROADMAP.md`
8. `docs/workbuddy/PACKAGING-DECISION.md`
9. `config/openmontage.sync.json`
10. `README.md`中位于官方README之前的WorkBuddy项目说明

`NEXT-CONVERSATION-PROMPT-2026-08-05.md`只是历史交接文件；如有冲突，以`PROJECT-STATE.md`和`docs/workbuddy/`中的最新冻结文档为准。

## 已冻结的项目边界

- 这是独立的WorkBuddy项目，与Golden Key SaaS没有产品或运行时依赖。
- `https://github.com/blazingcd/golden-key-openmontage`是唯一Golden Key核心同步源。
- WorkBuddy仓库只拉取Golden Key核心的正式、不可变、已测试tag；不得直接从官方OpenMontage同步代码。
- 官方OpenMontage更新必须先进入Golden Key核心，经过解决、测试和tag发布，再由本项目拉取。
- `core-sync`必须保持为完全相同的Golden Key核心提交；`main`是完整核心加WorkBuddy增量。
- WorkBuddy自身是唯一上层Agent。WorkBuddy运行链不得使用`lib/model_driven_agent_host.py`或`lib/openai_compatible_transport.py`发起第二次模型请求，也不得接入SaaS Agent Worker。
- 上述Golden Key核心文件必须完整保留；不得为解决不存在的源码层冲突而删除或改写它们。
- Skill负责用户理解、引导、提示、Rule Zero和Agent侧创作；MCP只负责确定性检查、读取、Schema校验、受限持久化、工具执行、异步状态和取消。
- 不得在W0中调用真实Provider、付费模型或生成付费素材。
- `PKG-001`中的Python、Node、FFmpeg打包方案保持`DEFERRED`，W0不要替用户提前决定。

## 当前已核对基线

- Golden Key核心tag：`golden-key-v0.3.18`
- Golden Key核心commit：`381a08e8dbdea025367c4970174ae0cd29980337`
- 官方上游基线commit：`4eab34c5cfcccaa4f1970554928feccce73ee930`
- 公开fork：`https://github.com/blazingcd/golden-key-openmontage-for-workbuddy`
- `golden-key-core/main`、本地`core-sync`均精确指向`381a08e8dbdea025367c4970174ae0cd29980337`，二者全仓差异为空。
- 本地WorkBuddy `main`以该完整核心为祖先；在Pipeline、Skill、Schema、Tool和核心合同测试等受保护路径上，与`core-sync`差异为空。
- 本地已存在并完整保留四个Golden Key业务Pipeline：
  - `pipeline_defs/golden-key-brand-company.yaml`
  - `pipeline_defs/golden-key-lead-conversion.yaml`
  - `pipeline_defs/golden-key-product-marketing.yaml`
  - `pipeline_defs/golden-key-subject-ip.yaml`
- Golden Key相对官方新增的不只是四个manifest，还包括44个对应Pipeline Skill、相关规则和11个新增合同测试；四个Pipeline复用OpenMontage通用Schema和Tool Registry，而不是各自复制一套Schema/工具系统。
- 公开fork当前`main`仍为官方提交`4eab34c5cfcccaa4f1970554928feccce73ee930`，因此GitHub网页上看不到上述四个Pipeline。这是“尚未发布到公开远端”，不是“本地只同步了官方核心”。
- W0审计的直接目的之一，就是确认本地完整Golden Key核心能否安全公开；审计通过并获得用户明确授权后，才把完整核心加WorkBuddy增量发布到公开fork。

开始时请重新验证这些事实，不要把本Prompt中的值当作免检结论。

## 必须先纠正的状态判断

开始工作后必须分别报告以下四个位置，禁止只查看公开GitHub页面就判断同步情况：

1. `golden-key-core/main`：Golden Key核心远端真相源。
2. 本地`core-sync`：必须与正式Golden Key tag/commit完全一致。
3. 本地WorkBuddy `main`：完整核心加WorkBuddy增量。
4. 公开`origin/main`：当前仍为官方fork基线，尚未接收Golden Key派生内容。

请对四个Golden Key Pipeline逐一验证manifest、Stage Skill、Reviewer/Checkpoint规则、通用Schema引用、Tool Registry引用和合同测试。不得仅依据提交号相同或文件名存在就声明同步完整，也不得把“公开远端尚未发布”误报成“本地核心缺失”。

## 本轮目标：完成W0并给出Gate裁决

至少完成以下工作：

1. 核对工作树、remotes、分支、tag、提交祖先关系和`config/openmontage.sync.json`，分别给出上述四个位置的commit和差异结论。
2. 逐项核验四个Golden Key业务Pipeline及其44个Stage Skill、Review/Checkpoint规则、Schema/Tool引用和相关合同测试在Golden Key远端、本地`core-sync`、本地`main`中的一致性。
3. 审计Golden Key核心相对官方基线的全部代码差异，并检查相关新增Git历史；明确哪些文件将进入首次公开发布。
4. 扫描密钥、令牌、内部地址、私有路径、客户或SaaS数据、Provider专有配置及日志样例。
5. 审查素材、字体、品牌、测试夹具、第三方代码和许可证的公开发布风险。
6. 明确区分：
   - Golden Key OpenMontage核心能力；
   - WorkBuddy适配层；
   - 仅供参考、不得进入运行时的Golden Key SaaS能力。
7. 形成WorkBuddy运行时隔离验证方案：
   - 静态依赖检查；
   - 运行时网络调用拦截；
   - 不导入或启动SaaS Worker；
   - 不发起嵌套Agent模型请求。
8. 输出并保存W0审计报告、Golden Key相对官方的完整差异清单、首次公开发布文件清单、风险项、处理建议和证据路径。
9. 给出明确Gate裁决：`PASS`、`CONDITIONAL PASS`或`FAIL`，不得用模糊措辞代替。
10. 更新`PROJECT-STATE.md`，并向`WORK-LOG.md`追加本轮范围、动作、结果、命令证据、提交和后续Todo。
11. 对可安全提交的本地文档、检查脚本和测试进行本地commit。

## 发布与修改限制

- W0 Gate通过前，不得把Golden Key派生内容推送到公开`origin`。
- 即使W0通过，本轮也不要自行推送公开远端；先向用户报告审计结论并等待明确发布授权。
- 除非为只读核对SaaS lock，否则不要修改`<GOLDEN_KEY_SAAS_REPO_ROOT>`。
- 不要修改Golden Key核心拥有的路径来实现WorkBuddy特殊逻辑；如果发现核心缺陷，记录为应先回到核心仓库修复的问题。
- 不要删除`lib/model_driven_agent_host.py`或`lib/openai_compatible_transport.py`。
- 保留并报告任何开始工作前已存在的用户修改，不得覆盖无关改动。

## W0完成标准

只有同时具备以下证据，才能把W0标为`DONE`：

- 可定位的审计报告和差异清单；
- 四个Golden Key Pipeline从远端核心到本地`core-sync`、本地`main`的完整性证据；
- 公开`origin/main`仍缺少Golden Key内容的明确差异证据和待发布文件清单；
- 秘密、路径、数据、素材和许可证检查证据；
- 运行时隔离测试方案；
- 所有未解决风险的责任归属与下一步；
- 明确的Gate裁决；
- 已更新的`PROJECT-STATE.md`与追加式`WORK-LOG.md`；
- 干净或已解释的工作树状态及本地提交记录。

如果只能达到`CONDITIONAL PASS`或`FAIL`，不要停在问题描述；请完成所有安全、可逆且不越界的修正，然后列出仍然阻止公开发布的最小剩余项。

最终向我汇报：结论、已完成项、未完成项、风险、证据文件、测试结果、本地commit，以及是否仍禁止公开推送。
