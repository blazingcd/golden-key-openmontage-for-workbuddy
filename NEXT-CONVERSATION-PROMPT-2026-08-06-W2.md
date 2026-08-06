# Golden Key OpenMontage for WorkBuddy：W2继续开发Prompt

请在`<WORKBUDDY_REPO_ROOT>`继续工作。先完整读取`AGENT_GUIDE.md`，然后读取：

1. `PROJECT-STATE.md`
2. `docs/workbuddy/ARCHITECTURE.md`
3. `docs/workbuddy/ROADMAP.md`
4. `docs/workbuddy/LOCAL-STORAGE-POLICY.md`
5. `docs/workbuddy/W0-RUNTIME-ISOLATION-TEST-PLAN.md`
6. `docs/workbuddy/CORE-SYNC-POLICY.md`
7. `WORK-LOG.md`最后一条记录

## 当前权威基线

- Core=`golden-key-v0.3.21`；contract ID=`golden-key-workbuddy-callable-core-v1`。
- source commit仅作provenance：`757ea3822e5f2eef7f341389983119021e827c8d`。
- authority=`direct_agent`；nested Agent Host forbidden。
- 四个Golden Key业务Pipeline、44个Pipeline Skill、Schema/Reviewer/Checkpoint/Tool Registry合同完整。
- W0=`PASS`且首个Pre-Alpha公开基线已发布；W1同步、包、doctor/gate、Skill骨架和CI已完成。
- Python发行=`golden-key-openmontage-workbuddy==0.1.0a0`；入口=`golden-key-workbuddy`。
- D盘数据根目录=`D:\WorkBuddyData`。
- W2第一段已完成`context`、`pipelines`、`project create/status`、`stage inspect`、
  `artifact validate`和`checkpoint submit`；对应路径封闭、Manifest完整产物、Human Gate和离线负测通过。
- W2 Tool切片已完成`tool list/execute`：只读取当前Stage Manifest allowlist，返回Registry Schema和Layer 3 Skill；
  请求及路径封闭在项目内，必须确认Layer 3 Skill，本地`scene_detect`在socket封锁下真实执行成功；
  API/Hybrid在状态探测、执行和网络前拒绝，Provider调用为0。
- W2模型配置分层已完成`config inspect/template`：WorkBuddy主对话模型归WorkBuddy Host，生产Provider归Registry；
  国内生态工具以Registry实际注册为准，厂商直连与第三方网关分列，模板只写环境变量名称、不写密钥值。
- W2本地Tool持久任务已完成`task submit/status/run/cancel/recover`：状态位于D盘`Jobs`，输入hash与稳定ID
  防篡改/防重复执行；queued可取消，running因Core无通用取消合同而明确不可安全取消；中断恢复只标记failed、
  不自动重试。local Tool执行期间封锁socket，API/Hybrid在任务落盘和网络前拒绝。
- v0.3.21 managed Core快照只读；W1～W4只改消费方层。Core接口变化必须通过新Release合同迁移。

## W2目标

1. 先以Skill-first直接调用完成最小生产闭环，不预设MCP必选。
2. 保持现有权威上下文、Pipeline清单、项目状态、Artifact Schema和Checkpoint接口稳定。
3. WorkBuddy负责选择四Pipeline并读取当前Stage Skill；Adapter不得选择Pipeline、创作、Reviewer判断或启动第二个模型Agent。
4. 保持已完成的主对话模型/生产Provider分层；不得把第三方网关误报为国内直连，也不得在Adapter中伪造WorkBuddy模型端点。
5. 下一增量是在真实WorkBuddy中对比Skill+CLI与Skill+本地stdio MCP的安装、Schema发现、长任务、恢复、错误和权限，
   形成MCP=`default|optional|omit`裁决；裁决前不得创建活动`.workbuddy/mcp.json`。
6. 对比时必须使用现有任务语义作为共同基线，不允许MCP偷偷增加第二套Pipeline选择、任务重试或虚假取消。
7. 裁决后完成跨任务并发/超时策略，并保持v0.3.21 managed Core只读；若Core接口变化，停止消费方开发并切换到新Release迁移Gate。

## 发布红线

- 按持续开发、持续留痕、持续提交和持续推送推进；任何Gate失败恢复fail-closed。
- 不修改Golden Key SaaS或Golden Key私有Core仓库，不直接同步官方OpenMontage或private Git ancestry。
- 不调用真实/付费Provider。
- 不声明完整安装、真实WorkBuddy验收或`OFFLINE ADAPTER READY`。
