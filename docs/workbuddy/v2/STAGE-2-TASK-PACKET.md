# WorkBuddy Shell V2 阶段2执行任务包

状态：`PLAN_REVIEW_READY / IMPLEMENTATION_NOT_AUTHORIZED`

规划起点：`fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9`

## 1. 唯一范围和停止线

阶段2只实现六模块中的 **Core登记与定位（Core Registration）**。WorkBuddy继续只负责对话，OpenMontage Core继续拥有全部生产决策和执行；本模块只把生命周期模块已经安装并提供的Core候选登记为可核验对象，再让后续Launcher只读取得唯一活动对象。

出现下列任一需要时立即返回`STOPPED_SCOPE_EXPANSION`：修改或执行Core；实现Installer、Runtime或Launcher；扫描磁盘猜对象；选择Pipeline、Stage、Provider、模型、媒体或创意；创建Artifact、推进Checkpoint；导入Core业务内部模块；新增CLI/MCP/Jobs生产控制面；处理`user_message`或`executor_controls`。

阶段2实现开始前，统筹必须把经独立审阅和用户计划Gate接受的40位提交写入派发Prompt，命名为`implementation_start_commit`。该值不是`HEAD`、分支名或`immutable_code_baseline`；缺失或与本地/远端不一致时为`INCOMPLETE_CONTEXT_MISMATCH`。`immutable_code_baseline=2a2bf09832d558388dc2816c54b32a2dce4aa607`仅用于V1来源和代码谱系核验。

## 2. 冻结合同

### 2.1 最小职责、输入和输出

唯一常规写入口为`register_core(...)`和`activate_core(...)`，损坏指针的唯一修复入口为`recover_active_core(...)`；唯一只读入口为`locate_active_core(...)`。四者放在新文件`golden_key_openmontage_workbuddy/core_registration.py`，不得加入CLI、MCP或WorkBuddy入口。

- `register_core(data_root, release_archive, release_sha256_sidecar, core_root, core_python)`：只读取显式路径，验证Release包、SHA sidecar、Manifest、Lock、安装后的Core文件、Python和Guide，写入一个不可变Registration对象；不自动激活。
- `activate_core(data_root, registration_sha256)`：只把已存在且当前仍完全有效的Registration设为唯一活动对象。调用方必须显式给出对象SHA；不得按版本、时间或目录名选择。
- `recover_active_core(data_root, expected_broken_pointer_sha256, replacement_registration_sha256)`：只在现有`active.json`原始字节SHA与显式损坏对象锁完全一致时，以完整复核通过的显式Registration替换它；不得创建Registration或选择回退对象。
- `locate_active_core(data_root)`：只读固定活动指针和其精确对象，重新验证身份、路径和hash，返回后续Launcher所需的不可变字段；零写入、零修复、零执行Core。

固定存储位置：

```text
<DataRoot>/State/CoreRegistration/v1/objects/<registration_sha256>.json
<DataRoot>/State/CoreRegistration/v1/active.json
```

`DataRoot`必须由调用方以已绑定的绝对路径传入；模块不得使用环境变量、用户目录、注册表、盘符搜索或“最新”目录作为回退。

### 2.2 Registration v1 唯一JSON shape

对象根和每个嵌套对象都执行`additionalProperties=false`：下列键全部必需、不得为`null`，未知键、缺键、重复JSON key全部拒绝。`string`是Unicode NFC；`sha256`是小写64位hex；`size`是大于0的JSON整数。

```json
{
  "schema_version": "golden-key-workbuddy-core-registration-v1",
  "owner": "golden-key-workbuddy-shell-v2",
  "contract_id": "string",
  "core_release": "string",
  "core_commit": "lowercase-40-hex",
  "authority": {
    "manifest": {
      "invocation_model": "direct_agent",
      "nested_agent_host_allowed": false
    },
    "lock": {
      "consumer": "workbuddy",
      "consumer_direct_official_sync_allowed": false,
      "invocation_model": "direct_agent",
      "nested_agent_host_allowed": false,
      "official_openmontage_role": "reviewed_upstream_baseline_only",
      "source": "golden-key-core"
    }
  },
  "release": {
    "asset_name": "basename.zip",
    "archive_sha256": "sha256",
    "sha256_sidecar_name": "basename.zip.sha256"
  },
  "core_root": "canonical-absolute-path",
  "core_python": {
    "relative_path": "bootstrap/python/python.exe",
    "path": "canonical-absolute-path",
    "sha256": "sha256",
    "size": 1,
    "version": "manifest-bootstrap-runtime-version",
    "source": "python.org_windows_embeddable_x64",
    "source_archive_sha256": "sha256"
  },
  "manifest": {
    "relative_path": "BUNDLE-MANIFEST.json",
    "path": "canonical-absolute-path",
    "schema_version": "golden-key-workbuddy-portable-bundle-v1",
    "sha256": "sha256",
    "size": 1
  },
  "lock": {
    "relative_path": "GOLDEN_KEY_WORKBUDDY_CORE.lock.json",
    "path": "canonical-absolute-path",
    "schema_version": 2,
    "sha256": "sha256",
    "size": 1,
    "bundle_sha256": "sha256"
  },
  "guide": {
    "relative_path": "AGENT_GUIDE.md",
    "path": "canonical-absolute-path",
    "sha256": "sha256",
    "size": 1
  }
}
```

`contract_id / core_release / core_commit`分别来自Manifest `core.contract_id / core.tag / core.source_commit`和Lock `contract_id / source_ref / source_commit`，每对逐字一致。Manifest和Lock authority不要求完整对象相同：Manifest authority必须且只能是上列2键shape；Lock authority必须且只能是上列6键shape；只交叉比较共有的`invocation_model`和`nested_agent_host_allowed`，并分别对各自完整shape精确验证。

`core_python`的唯一权威来源是已验证Release Manifest：`installation.runtime_roles.python`必须为`bundled_private_interpreter`；`files`中必须有且只有一个`path=bootstrap/python/python.exe`且`owner=workbuddy_bootstrap_runtime`的条目；其`sha256 / size`必须与文件一致；`bootstrap_runtime.python`必须且只能含`version / source / archive_sha256 / system_python_required`，其中version非空、source固定为`python.org_windows_embeddable_x64`、archive hash为sha256、`system_python_required=false`。调用方传入的`core_python`必须规范化后精确等于`CoreRoot/bootstrap/python/python.exe`；外部或任意Python一律`IDENTITY_MISMATCH`，本阶段不建立第二Runtime合同。

所有路径来自固定相对路径与显式绝对`CoreRoot`，存储为`str(Path.resolve(strict=True))`；不展开`~`。比较使用平台路径语义。规范JSON使用UTF-8无BOM、上述唯一shape、Unicode NFC、key排序、`separators=(",", ":")`和尾部一个LF；`registration_sha256`是完整规范字节SHA-256，也是对象文件名，不写入对象本身。

Registration只接受精确`v1`，Manifest只接受上列v1，Lock只接受整数`2`；未知版本必须新建合同。错误类别固定为`INPUT_INVALID / PATH_VIOLATION / OBJECT_MISSING / DUPLICATE / IDENTITY_MISMATCH / HASH_MISMATCH / TAMPERED / ATOMIC_WRITE_FAILED`。

### 2.3 相互验证链

登记时必须一次完成以下闭环，失败则不写对象或指针：

1. sidecar只允许一个64位digest及可选精确archive basename；archive实际hash、sidecar和Registration `release.archive_sha256`一致。
2. archive内Manifest和Lock各唯一、安全且字节与`CoreRoot`固定文件相同；Manifest `files`还必须锁定Python、Lock和Guide的hash/size/owner。
3. 按2.2分别验证两个authority完整shape，只交叉比较两个共有键；身份三元组逐对一致，Manifest `core.file_count`等于Lock `files`长度。
4. Lock `bundle_sha256`固定为对原顺序`files`执行`json.dumps(entries, ensure_ascii=False, sort_keys=True, separators=(",", ":"))`后取UTF-8字节SHA-256。
5. Lock每个`source_path`安全且唯一；Manifest有唯一对应`managed_core`条目，hash/size一致；`CoreRoot`实际受管文件逐项一致且解析后不得逃出根。
6. Guide固定为`AGENT_GUIDE.md`并同时通过Manifest、Lock和Registration验证；Python按2.2的Manifest私有解释器合同验证，不执行解释器。

Locator每次重做对象内容hash、唯一shape、规范路径、Manifest/Lock/Guide/Python hash及Lock受管文件验证。Release archive可由生命周期模块在登记后回收，Locator只核验已冻结Release SHA事实，不声称重新验证远端Release。

### 2.4 唯一活动指针和失败恢复

`active.json`必须且只能含`schema_version=golden-key-workbuddy-active-core-v1`、固定`owner`和小写64位`registration_sha256`，同样拒绝未知/缺失/重复字段。

- Registration对象先同目录临时写入、flush、`fsync`、回读核验，再原子发布；同hash同字节幂等，不同字节或外来对象拒绝覆盖。
- 常规激活前完整验证目标和现有有效指针；现有指针损坏时`activate_core`必须拒绝，不能静默覆盖。
- 新指针同目录完整写入并核验后`os.replace`；替换前失败保留旧指针，临时文件永远不被Locator读取。
- 损坏指针只允许调用`recover_active_core`：调用方显式给出当前损坏`active.json`原始字节SHA和目标Registration SHA；函数先完整验证目标，再在替换前重新读取当前原始字节并要求SHA仍精确相同，随后只原子替换`active.json`。损坏文件缺失、对象锁错误、期间字节变化、目标失效均零写入失败。
- 回滚只允许显式激活给定旧Registration SHA，且旧对象及其Core身份完整重验通过；不得扫描、猜测、按时间选择或自动回退。
- Locator遇到无/坏指针、缺目标、对象hash不符或目标失效直接fail closed；objects中即使只有一个对象也不得采用。

objects目录可保留多个已验证对象供显式升级/回滚；活动对象始终只有固定指针所指的一个SHA。`DUPLICATE`专指重复JSON key、ZIP成员、Manifest/Lock清单路径或同内容寻址文件名不同字节。

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
- 输入合同：五个显式绝对路径参数；`core_python`必须是Manifest锁定的`CoreRoot/bootstrap/python/python.exe`，其余文件由测试夹具或已授权生命周期调用方提供。
- 输出合同：规范Registration字节、`registration_sha256`和只读字段对象；失败抛出稳定的Registration合同错误并产生零写入。
- 实现步骤：定义2.2唯一shape与严格JSON加载器；实现路径/Unicode/hash规范化；分别验证Manifest/Lock authority；验证sidecar、ZIP唯一条目、身份、bundle digest、全Lock清单、Guide和Manifest锁定Python；生成规范对象。
- 必须测试：有效最小候选；根及每个嵌套对象的必需/未知/重复字段；两种authority完整shape及仅共有键交叉比较；commit/hash/size类型；sidecar/archive不一致；Manifest/Lock身份不一致；Python相对路径/owner/hash/size/bootstrap metadata；外部Python拒绝；安全路径、NFC和确定性对象SHA；失败前后文件系统快照相同。
- `PASS`：上述测试全部通过且纯验证路径零写入。`FAIL`：在精确对象上得到最终测试失败。`INCOMPLETE`：对象/环境漂移、命令无最终退出或证据缺失。
- 提交推送：T1不单独提交；只在T5以精确白名单一次提交并推送。
- Reviewer只读范围：最终`implementation_start_commit..implementation_result_commit`中的两个白名单文件，按本节合同定位T1变化。

### V2-S2-T2：不可变存储与原子活动指针

- `task_id`：`V2-S2-T2`
- 单一目标：实现第2.4节内容寻址对象存储、显式激活和对象锁定的损坏指针恢复，不实现安装或升级策略。
- 精确前置Git对象：同一Builder中已完成T1且HEAD仍为`implementation_start_commit`，未产生中间commit；任何其他HEAD为`INCOMPLETE`。
- 允许/禁止修改路径：第4节。
- 输入合同：T1已验证的规范对象或显式`registration_sha256`；恢复还必须显式给出损坏指针原始字节SHA；`DataRoot`为调用方给出的绝对路径。
- 输出合同：固定registry路径下的一个不可变对象和至多一个原子活动指针；返回精确对象SHA，不返回生产状态。
- 实现步骤：冻结目录与owner；temp同目录写入、flush/fsync、回读；对象内容寻址发布和幂等；激活前验证旧/新对象；`os.replace`切换；实现损坏指针原始字节SHA二次比对后替换；显式旧对象重新激活作为唯一回滚入口。
- 必须测试：首次写、同对象幂等、外来/冲突对象拒绝、旧指针保留、replace失败、stale temp忽略；损坏指针正确对象锁恢复、错误锁/缺文件/并发字节变化/失效目标均拒绝；显式回滚成功/失效旧对象拒绝；固定路径外零写入。
- `PASS/FAIL/INCOMPLETE`：与T1相同，并额外要求注入写入/替换失败时旧活动对象可读且无半成品被消费。
- 提交推送：不单独提交；T5统一提交推送。
- Reviewer只读范围：同T1，重点比较对象写入和指针函数，不审生命周期策略。

### V2-S2-T3：只读Locator与身份复核

- `task_id`：`V2-S2-T3`
- 单一目标：实现`locate_active_core(data_root)`，让后续Launcher只读获得精确Core绑定，不实现Launcher。
- 精确前置Git对象：同一Builder中T1、T2完成且HEAD仍为`implementation_start_commit`。
- 允许/禁止修改路径：第4节。
- 输入合同：显式绝对`DataRoot`；固定`active.json`及其内容寻址对象。
- 输出合同：不可变值对象，仅含`registration_sha256 / contract_id / core_release / core_commit / authority / release / core_root / core_python / guide / manifest / lock`，嵌套shape与2.2一致；不得返回命令字符串、Pipeline或生产状态。
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
- 实现步骤：逐类单点破坏；记录预期错误；覆盖JSON重复key、两种authority shape、清单重复路径、archive重复条目、缺失、字节篡改、root/python/guide漂移、外部Python、path traversal和symlink/reparse逃逸；证明恢复只接受显式损坏指针对象锁和显式有效Registration SHA。
- 必须测试：本节全部矩阵；损坏指针恢复的错误当前SHA、替换前竞态、无目标及坏目标；并证明“objects中仅一个候选”也不能替代缺失活动指针。
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
- 实现步骤：先对未提交修改执行`git diff --check`，并用`git status --porcelain=v1`确认worktree/index只含两个白名单路径；精确`git add -- <path1> <path2>`后执行`git diff --cached --check`并核验`git diff --cached --name-only`仍是精确白名单。在D盘任务专用Temp下执行两条pytest和禁止导入静态检查；提交、推送后记录`implementation_result_commit`，再执行`git diff --check "implementation_start_commit..implementation_result_commit"`、`git diff --name-only`路径分类、所有禁止类别计数、本地/远端SHA及clean复核。
- 必须测试：上述两条pytest命令，均须有最终退出0；不得安装依赖、运行安装器、WorkBuddy、Provider或媒体。
- `PASS`：提交前worktree/index检查、测试、提交后精确累计diff、路径、零边界、本地/远端/审阅对象全部满足；不得用提交前的`implementation_start_commit..HEAD`空范围作证。`FAIL`：精确环境中的最终测试失败。`INCOMPLETE`：任一命令无最终退出、对象/环境不一致或证据缺失。
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
