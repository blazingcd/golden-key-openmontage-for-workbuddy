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
- v0.3.21 managed Core快照只读；W1～W4只改消费方层。Core接口变化必须通过新Release合同迁移。

## W2目标

1. 先以Skill-first直接调用完成最小生产闭环，不预设MCP必选。
2. 保持现有权威上下文、Pipeline清单、项目状态、Artifact Schema和Checkpoint接口稳定。
3. WorkBuddy负责选择四Pipeline并读取当前Stage Skill；Adapter不得选择Pipeline、创作、Reviewer判断或启动第二个模型Agent。
4. 下一增量实现当前Manifest/Stage允许范围内的确定性工具发现/调用入口和结构化错误，但不得调用真实/付费Provider。
5. 分离WorkBuddy主对话模型配置与视频生产Provider配置；国内模型能力以WorkBuddy和Tool Registry实时支持面为准。
6. 在真实WorkBuddy中对比Skill+CLI与Skill+本地stdio MCP的安装、Schema发现、长任务、恢复、错误和权限，
   形成MCP=`default|optional|omit`裁决；裁决前不得创建活动`.workbuddy/mcp.json`。
7. 为首个生产入口增加离线网络拦截、嵌套模型调用拦截、路径封闭和Gate负测。

## 发布红线

- 按持续开发、持续留痕、持续提交和持续推送推进；任何Gate失败恢复fail-closed。
- 不修改Golden Key SaaS或Golden Key私有Core仓库，不直接同步官方OpenMontage或private Git ancestry。
- 不调用真实/付费Provider。
- 不声明完整安装、真实WorkBuddy验收或`OFFLINE ADAPTER READY`。
