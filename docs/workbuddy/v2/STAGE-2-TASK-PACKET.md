# WorkBuddy Shell V2 阶段2执行任务包

状态：`PLAN_REVIEW_READY / IMPLEMENTATION_NOT_AUTHORIZED`

规划起点：`fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9`

## 1. 唯一范围和停止线

阶段2只实现六模块中的 **Core登记与定位（Core Registration）**。WorkBuddy继续只负责对话，OpenMontage Core继续拥有全部生产决策和执行；本模块只把生命周期模块已经安装并提供的Core候选登记为可核验对象，再让后续Launcher只读取得唯一活动对象。

出现下列任一需要时立即返回`STOPPED_SCOPE_EXPANSION`：修改或执行Core；实现Installer、Runtime或Launcher；扫描磁盘猜对象；选择Pipeline、Stage、Provider、模型、媒体或创意；创建Artifact、推进Checkpoint；导入Core业务内部模块；新增CLI/MCP/Jobs生产控制面；处理`user_message`或`executor_controls`。

阶段2实现开始前，统筹必须把经独立审阅和用户计划Gate接受的40位提交写入派发Prompt，命名为`implementation_start_commit`。该值不是`HEAD`、分支名或`immutable_code_baseline`；缺失或与本地/远端不一致时为`INCOMPLETE_CONTEXT_MISMATCH`。`immutable_code_baseline=2a2bf09832d558388dc2816c54b32a2dce4aa607`仅用于V1来源和代码谱系核验。

## 2. 冻结合同

### 2.1 最小职责、输入和输出

唯一写入口为`register_core(...)`和`activate_core(...)`；唯一只读入口为`locate_active_core(...)`。三者放在新文件`golden_key_openmontage_workbuddy/core_registration.py`，不得加入CLI、MCP或WorkBuddy入口。

- `register_core(data_root, release_archive, release_sha256_sidecar, core_root, core_python)`：只读取显式路径，验证Release包、SHA sidecar、Manifest、Lock、安装后的Core文件、Python和Guide，写入一个不可变Registration对象；不自动激活。
- `activate_core(data_root, registration_sha256)`：只把已存在且当前仍完全有效的Registration设为唯一活动对象。调用方必须显式给出对象SHA；不得按版本、时间或目录名选择。
- `locate_active_core(data_root)`：只读固定活动指针和其精确对象，重新验证身份、路径和hash，返回后续Launcher所需的不可变字段；零写入、零修复、零执行Core。

固定存储位置：

```text
<DataRoot>/State/CoreRegistration/v1/objects/<registration_sha256>.json
<DataRoot>/State/CoreRegistration/v1/active.json
```

`DataRoot`必须由调用方以已绑定的绝对路径传入；模块不得使用环境变量、用户目录、注册表、盘符搜索或“最新”目录作为回退。

### 2.2 Registration v1 必需字段

`schema_version`固定为`golden-key-workbuddy-core-registration-v1`，`owner`固定为`golden-key-workbuddy-shell-v2`。对象JSON必须且只能含以下字段；未知字段、缺字段和重复JSON key全部拒绝：

| 字段 | 来源 | 规则 |
|---|---|---|
| `contract_id` | Lock与Manifest的`core.contract_id` | 两者逐字一致、非空 |
| `core_release` | Lock `source_ref`与Manifest `core.tag` | 两者逐字一致；只作不可变标识，不按字符串排序 |
| `core_commit` | Lock `source_commit`与Manifest `core.source_commit` | 两者一致且为小写40位hex |
| `authority` | Lock与Manifest顶层`authority` | 两者必须精确等于`{"invocation_model":"direct_agent","nested_agent_host_allowed":false}` |
| `release_asset_name` | `release_archive`文件名 | 非空basename；不得含路径 |
| `release_archive_sha256` | 对Release archive逐字节SHA-256 | 与sidecar唯一digest一致，小写64位hex |
| `core_root` | 调用方显式输入 | 必须已存在、绝对、`resolve(strict=True)`后的规范路径 |
| `core_python` | 调用方显式输入 | 必须为已存在普通文件；记录规范路径和逐字节SHA-256，不执行解释器 |
| `manifest` | `<CoreRoot>/BUNDLE-MANIFEST.json` | 固定相对路径、schema version、逐字节SHA-256 |
| `lock` | `<CoreRoot>/GOLDEN_KEY_WORKBUDDY_CORE.lock.json` | 固定相对路径、schema version、逐字节SHA-256、`bundle_sha256` |
| `guide` | `<CoreRoot>/AGENT_GUIDE.md` | 固定相对路径、逐字节SHA-256；必须同时出现在Manifest和Lock清单 |

路径存储为`str(Path.resolve(strict=True))`的本机规范绝对路径；调用输入必须已是绝对路径，不展开`~`。比较使用平台路径语义，文件落盘使用规范路径值。所有hash统一为小写64位hex。JSON使用UTF-8无BOM、Unicode NFC、key排序和固定紧凑分隔符，尾部一个LF；`registration_sha256`是上述规范JSON全部字节的SHA-256，也是对象文件名，不写入对象本身，避免自引用。

Registration只接受精确`v1`，Manifest只接受`golden-key-workbuddy-portable-bundle-v1`，Lock只接受整数`2`；不猜测、迁移或宽容解析未知schema。未来字段变化必须新建schema版本和独立任务，不能在v1静默增加可选语义。所有合同错误必须带稳定类别：`INPUT_INVALID / PATH_VIOLATION / OBJECT_MISSING / DUPLICATE / IDENTITY_MISMATCH / HASH_MISMATCH / TAMPERED / ATOMIC_WRITE_FAILED`；不得只返回自由文本供调用方猜语义。

### 2.3 相互验证链

登记时必须一次完成以下闭环，任何一步失败均不写对象或指针：

1. sidecar只允许一个64位digest及可选的精确archive basename；实际archive hash必须一致。
2. archive内的Manifest和Lock条目必须各唯一、为普通文件、无绝对路径或`..`；其字节必须与`CoreRoot`下固定文件逐字节一致。
3. Manifest与Lock的`contract_id / release / commit / authority`必须一致，且authority是`direct_agent`并禁止nested Agent Host；Manifest `core.file_count`必须等于Lock `files`长度。Lock `bundle_sha256`的算法固定为：对Lock中原顺序的`files`数组执行`json.dumps(entries, ensure_ascii=False, sort_keys=True, separators=(",", ":"))`，取UTF-8字节SHA-256，结果必须与字段一致。
4. Lock每个`source_path`必须安全、唯一；Manifest中必须有且只有一个对应的`managed_core`条目，且`sha256 / size`一致。
5. `CoreRoot`下每个Lock受管文件必须存在于根内且逐文件`sha256 / size`一致；禁止symlink/reparse解析后逃出`CoreRoot`。
6. Guide固定为`AGENT_GUIDE.md`，同时通过第4、5步及Registration中独立hash验证。
7. Python只作为Shell绑定身份：验证显式规范路径、普通文件和hash；不探测版本、不准备依赖、不声称Runtime ready。

Locator每次读取时重做对象内容hash、固定字段/schema、规范路径、Manifest/Lock/Guide/Python hash以及Lock受管Core文件验证。Release archive可在登记后由生命周期模块回收，因此Locator只核验Registration内已冻结的Release SHA事实，不声称重新验证远端Release。

### 2.4 唯一活动指针和失败恢复

`active.json` schema固定为`golden-key-workbuddy-active-core-v1`，只含`schema_version`、固定`owner`和小写64位`registration_sha256`。它不复制Registration字段。

- Registration对象先在同目录唯一临时文件写入、flush、`fsync`、回读并核验hash，再原子发布到内容寻址目标；同hash同字节为幂等，不同字节或外来对象一律拒绝覆盖。
- 激活前必须完整验证目标Registration；现有`active.json`若存在也必须先验证，损坏时不得用新对象静默覆盖。
- 新指针在同目录临时文件完整写入并核验后用`os.replace`原子切换。替换前失败保留旧指针；替换成功即以新指针为唯一结果。临时文件永远不被Locator读取。
- 回滚不是自动策略：生命周期模块只能显式调用`activate_core(previous_registration_sha256)`；旧对象必须仍存在且重新验证通过。不得因当前对象失败而扫描或自动退回旧对象。
- 无指针、指针损坏、目标缺失、对象hash不符或目标失效时Locator直接fail closed；即使objects目录恰有一个或多个看似可用对象，也不得猜测。

objects目录允许保留多个已验证对象供显式升级/回滚，这不是“重复活动Core”；活动对象始终只有固定指针指向的一个SHA。`DUPLICATE`专指重复JSON key、重复ZIP成员、重复Manifest/Lock清单路径或同一内容寻址文件名出现不同字节。

## 3. V1处置

固定只读来源均为`2a2bf09832d558388dc2816c54b32a2dce4aa607`：

| V1来源 | 阶段2裁决 | 仅允许的最小元素 | 禁止带入 |
|---|---|---|---|
| `golden_key_openmontage_workbuddy/paths.py` | `ADAPT_NAMED_ELEMENTS` | `Path.resolve`式规范化思路 | 环境变量默认、包目录回退、用户目录猜测 |
| `packaging/workbuddy/install-workbuddy.ps1` | `ADAPT_NAMED_ELEMENTS` | SHA-256、清单安全路径、staging后切换、所有权拒绝覆盖的合同 | 安装/升级/repair、Skill写入、doctor/runtime调用、整文件复制 |
| `scripts/core_sync/sync_workbuddy_core.py` | `HISTORICAL_REFERENCE_ONLY` | ZIP/Lock/逐文件hash和bundle digest的负面夹具与算法事实 | 运行时导入、下载、同步、镜像、删除和维护者流程 |
| `golden_key_openmontage_workbuddy/doctor.py`、`gate.py` | `REWRITE` | “身份不一致即失败”这一问题定义 | v0.3.21硬编码、Pipeline/runtime/provider探测、PASS聚合 |
| `runtime.py`、`tasks.py`、`mcp_server.py`、旧CLI与Skill | `DROP_FOR_STAGE_2` | 无 | 任何生产控制、Core内部导入、Artifact/Checkpoint/Stage/Tool逻辑 |

阶段2不得修改上述V1来源文件。实现Builder必须在最终证据中列明新模块没有从任何V1文件整文件复制。

## 4. 实现白名单和统一禁止路径

全部T1至T4只允许：

```text
golden_key_openmontage_workbuddy/core_registration.py
tests/workbuddy/test_core_registration.py
```

T5不允许再修改文件。除此之外全部禁止，尤其包括：`golden_key_openmontage_workbuddy/{__init__,__main__,cli,doctor,gate,paths,runtime,runtime_prepare,tasks,mcp_server,model_config}.py`、`packaging/**`、`scripts/**`、`workbuddy-skill/**`、`.agents/**`、`skills/**`、`config/**`、`*lock*`、`AGENT_GUIDE.md`、`pipeline_defs/**`、`lib/**`、`schemas/artifacts/**`和本文档以外的治理文档。

如两个白名单文件不足，Builder必须停止为`STOPPED_SCOPE_EXPANSION`并报告所需路径，不得自行增加。

## 5. 未来实现任务（单一Builder串行T1至T5）

所有任务共享以下Git合同：分支从统筹Prompt给出的精确`implementation_start_commit`创建；本地HEAD、远端对应来源分支、Prompt三者必须一致，工作树必须clean，且`2a2bf09832d558388dc2816c54b32a2dce4aa607`为祖先。不得reset、stash、merge或rebase。T1至T5由一个`V2-S2-BUILDER1`串行完成并形成一个结果commit，避免同文件多Builder并发。

### V2-S2-T1：Schema和版本合同

- `task_id`：`V2-S2-T1`
- 单一目标：在新模块中实现第2节的纯解析、规范化、Release/Manifest/Lock/Core/Python/Guide验证和规范Registration字节生成，不写登记目录。
- 精确前置Git对象：派发Prompt中的40位`implementation_start_commit`；T1开始时必须仍等于Builder分支HEAD。
- 允许修改路径：第4节两个白名单文件。
- 禁止修改路径：第4节统一禁止路径。
- 输入合同：五个显式绝对路径参数；文件均由测试夹具或已授权生命周期调用方提供。
- 输出合同：规范Registration字节、`registration_sha256`和只读字段对象；失败抛出稳定的Registration合同错误并产生零写入。
- 实现步骤：定义精确schema常量与严格JSON加载器；实现路径/Unicode/hash规范化；验证sidecar、ZIP唯一条目、Manifest/Lock身份和bundle digest；验证全Lock清单、Guide和Python；生成规范对象。
- 必须测试：有效最小候选；每个必需字段缺失/未知/重复；commit/hash格式；sidecar/archive不一致；Manifest/Lock身份不一致；安全路径、NFC和确定性字节；失败前后文件系统快照相同。
- `PASS`：上述测试全部通过且纯验证路径零写入。`FAIL`：在精确对象上得到最终测试失败。`INCOMPLETE`：对象/环境漂移、命令无最终退出或证据缺失。
- 提交推送：T1不单独提交；只在T5以精确白名单一次提交并推送。
- Reviewer只读范围：最终`implementation_start_commit..implementation_result_commit`中的两个白名单文件，按本节合同定位T1变化。

### V2-S2-T2：不可变存储与原子活动指针

- `task_id`：`V2-S2-T2`
- 单一目标：实现第2.4节内容寻址对象存储、显式激活和失败恢复语义，不实现安装或升级策略。
- 精确前置Git对象：同一Builder中已完成T1且HEAD仍为`implementation_start_commit`，未产生中间commit；任何其他HEAD为`INCOMPLETE`。
- 允许/禁止修改路径：第4节。
- 输入合同：T1已验证的规范对象，或显式`registration_sha256`；`DataRoot`为调用方给出的绝对路径。
- 输出合同：固定registry路径下的一个不可变对象和至多一个原子活动指针；返回精确对象SHA，不返回生产状态。
- 实现步骤：冻结目录与owner；temp同目录写入、flush/fsync、回读；对象内容寻址发布和幂等；激活前验证旧/新对象；`os.replace`切换；显式旧对象重新激活作为唯一回滚入口。
- 必须测试：首次写、同对象幂等、外来/冲突对象拒绝、旧指针保留、replace失败、stale temp忽略、显式回滚成功/失效旧对象拒绝、固定路径外零写入。
- `PASS/FAIL/INCOMPLETE`：与T1相同，并额外要求注入写入/替换失败时旧活动对象可读且无半成品被消费。
- 提交推送：不单独提交；T5统一提交推送。
- Reviewer只读范围：同T1，重点比较对象写入和指针函数，不审生命周期策略。

### V2-S2-T3：只读Locator与身份复核

- `task_id`：`V2-S2-T3`
- 单一目标：实现`locate_active_core(data_root)`，让后续Launcher只读获得精确Core绑定，不实现Launcher。
- 精确前置Git对象：同一Builder中T1、T2完成且HEAD仍为`implementation_start_commit`。
- 允许/禁止修改路径：第4节。
- 输入合同：显式绝对`DataRoot`；固定`active.json`及其内容寻址对象。
- 输出合同：不可变值对象，仅含`registration_sha256 / contract_id / core_release / core_commit / core_root / core_python / guide / manifest / lock / release_archive_sha256`；不得返回命令字符串、Pipeline或生产状态。
- 实现步骤：严格读指针；按SHA读单一对象；验证对象hash和schema；重做第2.3节本地身份验证；返回字段副本。不得枚举对象作为fallback。
- 必须测试：有效定位；无指针、坏指针、缺对象、改对象、改Manifest/Lock/Guide/Python/Core文件、路径移动/alias、多个对象无指针；成功和失败调用前后registry及Core树字节/mtime快照完全一致。
- `PASS`：全部测试通过且Locator零写入、零子进程、零网络。`FAIL/INCOMPLETE`：与T1相同。
- 提交推送：不单独提交；T5统一提交推送。
- Reviewer只读范围：同T1；确认未来Launcher只能消费返回对象，Locator不接受用户消息或执行控制。

### V2-S2-T4：fail-closed负面矩阵

- `task_id`：`V2-S2-T4`
- 单一目标：以参数化测试冻结缺失、重复、篡改、漂移、hash和路径异常的拒绝结果，不新增能力。
- 精确前置Git对象：同一Builder中T1至T3完成且HEAD仍为`implementation_start_commit`。
- 允许修改路径：优先只改`tests/workbuddy/test_core_registration.py`；只有测试证明合同缺陷时才可最小改`core_registration.py`。
- 禁止修改路径：第4节统一禁止路径。
- 输入合同：由测试独立生成的本地小型ZIP、sidecar、Manifest、Lock、CoreRoot、Python与registry夹具；不得使用真实Release、网络或安装。
- 输出合同：每个负例得到稳定错误类别、零活动指针前移、零对象猜测、零范围外写入。
- 实现步骤：逐类单点破坏；记录预期错误；覆盖JSON重复key、清单重复路径、archive重复条目、缺失、字节篡改、root/python/guide漂移、path traversal和symlink/reparse逃逸；证明恢复只接受显式有效旧SHA。
- 必须测试：本节全部矩阵，并证明“objects中仅一个候选”也不能替代缺失活动指针。
- `PASS`：所有负例明确拒绝且正例仍通过。`FAIL/INCOMPLETE`：与T1相同。
- 提交推送：不单独提交；T5统一提交推送。
- Reviewer只读范围：同T1；只检查负面合同覆盖，不要求真实安装或Core。

### V2-S2-T5：REVIEW_READY证据收口

- `task_id`：`V2-S2-T5`
- 单一目标：在零新增修改下验证白名单、测试、Git对象和零越界，形成可审阅结果commit。
- 精确前置Git对象：提交前HEAD必须仍为`implementation_start_commit`；提交后记录唯一40位`implementation_result_commit`。
- 允许修改路径：无新增；只可精确暂存第4节两个白名单文件。
- 禁止修改路径：除两白名单文件外全部路径；禁止`git add .`。
- 输入合同：T1至T4完成的工作树和已绑定Python；Python解释器绝对路径、版本和最终退出码必须进入证据。
- 输出合同：一个只含白名单文件的提交，推送到`origin/codex/v2-s2-builder1`，本地/远端SHA一致、工作树clean、状态最多`REVIEW_READY`。
- 实现步骤：在D盘任务专用Temp下执行`python -m pytest tests/workbuddy/test_core_registration.py -q`，再执行`python -m pytest tests/workbuddy/test_core_registration.py tests/workbuddy/test_portable_bundle.py -q`；执行`git diff --check implementation_start_commit..HEAD`、路径分类和禁止导入静态检查；精确暂存、提交、推送、复核。
- 必须测试：上述两条pytest命令，均须有最终退出0；不得安装依赖、运行安装器、WorkBuddy、Provider或媒体。
- `PASS`：测试、diff、路径、零边界、本地/远端/审阅对象全部满足。`FAIL`：精确环境中的最终测试失败。`INCOMPLETE`：任一命令无最终退出、对象/环境不一致或证据缺失。
- 提交推送：提交信息`docs`以外不得伪装；实现提交必须精确包含两个白名单文件，推送后不得改写。
- Reviewer只读范围：`implementation_start_commit..implementation_result_commit`；生产代码变化只允许新`core_registration.py`，其他生产代码变化为0。

## 6. 审阅、Gate和状态转换

### 当前规划链

```text
V2-S2-PLAN-BUILDER1@fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9 -> PLAN_REVIEW_READY
V2-S2-PLAN-REVIEW1: 只读比较 fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9..planning_result_commit
APPROVE -> V2-S2-PLAN-GATE
REQUEST_CHANGES -> 仅开 V2-S2-PLAN-FIX<n> 并复审直接diff
INCOMPLETE -> 停止，保持 implementation_authorization=NOT_GRANTED
```

规划Reviewer必须确认本文可直接派发、两个实现白名单精确、每任务测试/退出条件齐全、其他五模块和生产控制面为零、相对规划起点生产代码变化为0；零修改、零commit、零push，结论只允许`APPROVE / REQUEST_CHANGES / INCOMPLETE`。

用户接受`V2-S2-PLAN-GATE`只把`stage_2_plan_status`设为`PASS_ACCEPTED`，不会授权实现。只有用户随后明确授权“启动阶段二实现”，统筹才可锁定精确`implementation_start_commit`并创建`V2-S2-BUILDER1`。

### 未来实现链

```text
V2-S2-BUILDER1@implementation_start_commit
  -> 串行完成 T1..T5 -> REVIEW_READY@implementation_result_commit
V2-S2-T6 / V2-S2-REVIEW1
  -> 只读比较 implementation_start_commit..implementation_result_commit
APPROVE -> V2-S2-GATE（用户接受阶段2实现）
REQUEST_CHANGES -> 最小 V2-S2-FIX<n>，只复审修订diff及原finding
INCOMPLETE -> 停止，不得提交用户实现Gate
```

实现Reviewer必须独立、只读、零修改/commit/push；核验任务合同、全部测试最终退出、唯一活动指针、Locator零写入、全负面矩阵、白名单和禁止路径、生产控制面为零。最终只允许`APPROVE / REQUEST_CHANGES / INCOMPLETE`。

只有结果已推送、Reviewer `APPROVE`、本地/远端/审阅对象一致、工作树clean、实现仅限本模块且用户接受`V2-S2-GATE`后，`stage_2_status`才可变为`PASS_ACCEPTED`。在此之前不得创建阶段3任务、实现其他五模块或声称真实WorkBuddy、Runtime、Core流程、Provider或媒体已验证。
