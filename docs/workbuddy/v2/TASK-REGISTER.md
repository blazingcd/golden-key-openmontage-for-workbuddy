# WorkBuddy Shell V2 任务账本

状态：`V2-S4-SECRET-NONDISCLOSURE-CONTRACT-CLARIFICATION-BUILDER1 / WORKTREE_RESULT_READY_FOR_REVIEW`

更新时间：2026-08-20

## 当前任务

```text
task_id: V2-S4-SECRET-NONDISCLOSURE-CONTRACT-CLARIFICATION-BUILDER1
task_status: WORKTREE_RESULT_READY_FOR_REVIEW
task_kind: STAGE4_SECRET_NONDISCLOSURE_CONTRACT_CLARIFICATION / DOCS_ONLY
user_authorization: 2026-08-20 / 修正Implementation Reviewer发现的secret nondisclosure合同不可表示P1；不是重新规划或扩大边界
start_commit: 3a64a0b4c103ea3cbe254fce60889396cd18ff30
start_tree: 77011e73c2f1dcca86e4290035018af6c06ef7dd
result_commit: THIS_COMMIT
branch: codex/v2-s4-secret-contract1
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_at_start: 3a64a0b4c103ea3cbe254fce60889396cd18ff30
formal_tree_at_start: 77011e73c2f1dcca86e4290035018af6c06ef7dd
review_range: 3a64a0b4c103ea3cbe254fce60889396cd18ff30..THIS_COMMIT
independent_review: NOT_STARTED / V2-S4-SECRET-NONDISCLOSURE-CONTRACT-CLARIFICATION-REVIEW1 / REQUIRED_ZERO_WRITE
formal_promotion: NOT_STARTED / CLARIFICATION_EFFECTIVE_ONLY_AFTER_APPROVE_AND_ORDINARY_FAST_FORWARD
repository_allowed_paths: docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md
production_code_changes: 0
test_changes: 0
ci_changes: 0
new_tracked_files: 0
tracked_files_expected: 35
clarification_scope: distinguish Provider-secret propagation from accidental equality with fixed secret-independent protocol constants; freeze dynamic-field safe substitution and cross-chunk child-output detection
contract_invariants_retained: Provider/runtime opaque; receipt outcomes=9; reason codes=23; priority levels=11; implementation paths=5; tracked transition=35->37; Stage5/6 and production Launcher remain unauthorized
implementation_candidate_promotion: BLOCKED / existing code candidate must not be promoted before this clarification is independently approved and ordinary-fast-forwarded, then must be revised and re-reviewed through the original implementation Builder
clarification_effective_only_if: V2-S4-SECRET-NONDISCLOSURE-CONTRACT-CLARIFICATION-REVIEW1 APPROVE / P0=0 / P1=0 / P2=0 AND THIS_COMMIT ordinary-fast-forwarded as formal head
next_authorized_task: V2-S4-SECRET-NONDISCLOSURE-CONTRACT-CLARIFICATION-REVIEW1 / ZERO_WRITE_ONLY
stage_4_planning: PASS_ACCEPTED / CONTRACT_CLARIFICATION_PENDING
stage_4_implementation_authorization: FORMALLY_GRANTED_TO_V2-S4-IMPLEMENTATION-BUILDER1 / CANDIDATE_PROMOTION_HELD_FOR_THIS_CLARIFICATION
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
final_package_gate_authorization: NOT_GRANTED
```

## 已完成的Stage 4实现权威同步（历史证据）

```text
task_id: V2-S4-IMPLEMENTATION-AUTHORITY-SYNC-FIX1
task_status: WORKTREE_RESULT_READY_FOR_REVIEW
task_kind: STAGE4_IMPLEMENTATION_AUTHORITY_SYNC / DOCS_ONLY
user_authorization: 2026-08-20 / Stage4实施与审查执行授权已正式固化；在实现前一次性同步六权威，不扩大边界
start_commit: 2c3d87bedfa4a3cef3cfd952641199300f2715dc
start_tree: c196dbf6b094cad05076d01ac2496f7425cf6fac
result_commit: THIS_COMMIT
branch: codex/v2-s4-impl-auth1
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_at_start: 2c3d87bedfa4a3cef3cfd952641199300f2715dc
formal_tree_at_start: c196dbf6b094cad05076d01ac2496f7425cf6fac
review_range: 2c3d87bedfa4a3cef3cfd952641199300f2715dc..THIS_COMMIT
independent_review: NOT_STARTED / V2-S4-IMPLEMENTATION-AUTHORITY-SYNC-REVIEW1 / REQUIRED_ZERO_WRITE
formal_promotion: NOT_STARTED / BUILDER_START_EFFECTIVE_ONLY_AFTER_APPROVE_AND_ORDINARY_FAST_FORWARD
repository_allowed_paths: AGENT_GUIDE.md; PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md; docs/workbuddy/v2/PROJECT-CHARTER.md
production_code_changes: 0
test_changes: 0
ci_changes: 0
new_tracked_files: 0
tracked_files_expected: 35
stage_4_plan_formal_result: 5cb3f585a0cddffbd823c785b1d39ebd1834c1df
stage_4_plan_formal_tree: 144df76b3a307fa8944ccd7bd384bddb1b340516
stage_4_plan_promotion: ORDINARY_FAST_FORWARD / origin/codex/workbuddy-shell-v2=5cb3f585a0cddffbd823c785b1d39ebd1834c1df
stage_4_plan_reviewer: V2-S4-PLAN-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_plan_review_history_1: REQUEST_CHANGES / CLOSED / definition hash-cycle + receipt outcome/priority/invalid-input
stage_4_plan_review_history_2: REQUEST_CHANGES / CLOSED / forged-summary evidence + Stage3 managed/explicit/PATH handoff
stage_4_plan_ci: run 32337744225 / completed / success
embedded_plan_candidate_labels: HISTORICAL_CONDITIONAL_TEXT / review-and-promotion conditions satisfied by V2-S4-PLAN-REVIEW1 APPROVE and formal result 5cb3f585a0cddffbd823c785b1d39ebd1834c1df / not live authorization
stage_4_plan_closeout: PASS_ACCEPTED / dfd97f3d2e05a4c448448fc14514d1cfe76836e8 / tree 5eeb8a9337c5b38be60d3b0cef184b8898f2fedc
stage_4_plan_closeout_reviewer: V2-S4-PLAN-CLOSEOUT-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_plan_closeout_ci: run 32338998075 / completed / success / head_sha=dfd97f3d2e05a4c448448fc14514d1cfe76836e8
package_tool_definition_contract: FORMALLY_PROMOTED / PackageToolDefinitionV1
launcher_public_api_and_receipt_contract: FORMALLY_PROMOTED / launch_session_tool + nine-outcome recursively immutable LauncherReceiptV1
official_model_correction: dynamic capability/provider registry / Provider and local runtime are opaque to Shell / no hard-coded Provider or renderer routing in Stage4
stage_3_evidence_boundary: current implementation supplies local Remotion/HyperFrames evidence only; Stage4 accepts the complete approved definition plus the unmodified original Stage3 fact only when PackageToolDefinition declares a requirement, then independently applies the accepted managed/explicit/PATH source semantics and revalidates actual bytes
provider_boundary: image/video/TTS/music/stock/local-GPU and future Providers are optional external configuration selected by WorkBuddy/OpenMontage; Stage4 only passes allowlisted environment names and secret values to the fixed child process
stage_4_planning: PASS_ACCEPTED
stage_4_implementation_authorization_formal_result: 2c3d87bedfa4a3cef3cfd952641199300f2715dc
stage_4_implementation_authorization_formal_tree: c196dbf6b094cad05076d01ac2496f7425cf6fac
stage_4_implementation_authorization_review: V2-S4-IMPLEMENTATION-AUTHORIZATION-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_implementation_authorization_promotion: ORDINARY_FAST_FORWARD / origin/codex/workbuddy-shell-v2=2c3d87bedfa4a3cef3cfd952641199300f2715dc
stage_4_implementation_authorization_ci: run 32340096961 / completed / success / head_sha=2c3d87bedfa4a3cef3cfd952641199300f2715dc
stage_4_implementation_authorization: FORMALLY_GRANTED_TO_V2-S4-IMPLEMENTATION-BUILDER1 / START_BLOCKED_UNTIL_SIX_AUTHORITY_SYNC_APPROVE_AND_ORDINARY_FAST_FORWARD
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
final_package_gate_authorization: NOT_GRANTED
next_authorized_task: V2-S4-IMPLEMENTATION-AUTHORITY-SYNC-REVIEW1 / ZERO_WRITE_ONLY

authority_sync_effective_only_if: V2-S4-IMPLEMENTATION-AUTHORITY-SYNC-REVIEW1 APPROVE / P0=0 / P1=0 / P2=0 AND THIS_COMMIT ordinary-fast-forwarded as formal head
effective_stage_4_implementation_authorization: GRANTED_TO_V2-S4-IMPLEMENTATION-BUILDER1_ONLY
effective_stage_4_launcher_authorization: NOT_GRANTED
effective_next_authorized_task: V2-S4-IMPLEMENTATION-BUILDER1
effective_stage_5_workbuddy_entry_authorization: NOT_GRANTED
effective_stage_6_status_result_relay_authorization: NOT_GRANTED
effective_final_package_gate_authorization: NOT_GRANTED
implementation_builder_branch: codex/v2-s4-implementation-builder1
implementation_builder_base_rule: exact latest origin/codex/workbuddy-shell-v2 commit and tree after this six-authority sync candidate is approved and ordinary-fast-forwarded; never use this temporary sync branch as implementation base
implementation_exact_allowed_paths: golden_key_openmontage_workbuddy/session_launcher.py; golden_key_openmontage_workbuddy/__init__.py; tests/workbuddy/test_session_launcher.py; tests/workbuddy/test_repository_hygiene.py; .github/workflows/ci.yml
implementation_tracked_files_transition: 35 -> 37
implementation_stop_scope_expansion: any sixth path; any edit to golden_key_openmontage_workbuddy/package_registration.py; golden_key_openmontage_workbuddy/runtime_prepare.py; pyproject.toml; any dynamic relaxation of the fixed tree contract
implementation_test_environment: implementation worktree private D-drive .venv only / no global Python packages
implementation_required_tests: Stage4 direct tests; repository hygiene; complete repository suite / every final exit 0 with untruncated output
implementation_delivery: one bounded Builder / non-force temporary-branch push / independent zero-write Reviewer / REQUEST_CHANGES only to original Builder / APPROVE P0=0 P1=0 P2=0 then ordinary fast-forward and formal CI
implementation_product_boundary: implements and tests only the approved Launcher contract / no real production Launcher execution / no WorkBuddy / no Provider or runtime choice / no media / no Stage5 or Stage6 / no final Package materialization
```

## 已完成的前置收口（历史证据）

```text
task_id: V2-CI-STAGE3-STATE-ASSERTION-CLOSEOUT-BUILDER1
task_status: WORKTREE_RESULT_READY_FOR_REVIEW
task_kind: CI_MAINTENANCE_STATE_CLOSEOUT / DOCS_ONLY
user_authorization: 2026-08-20 / 收口已进入正式分支的Stage3状态断言修复，并在独立审查与正式推广后衔接Stage4规划
start_commit: e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3
result_commit: THIS_COMMIT
branch: codex/v2-ci-stage3-state-assertion-closeout1
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_at_start: e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3
formal_tree_at_start: a4d8034f6cf76c6eedd2f4bbe3c30dbe1b4e382a
review_range: e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3..THIS_COMMIT
independent_review: NOT_STARTED / REQUIRED_ZERO_WRITE
formal_promotion: NOT_STARTED / CLOSEOUT_EFFECTIVE_ONLY_AFTER_APPROVE_AND_ORDINARY_FAST_FORWARD
repository_allowed_paths: docs/workbuddy/v2/TASK-REGISTER.md; PROJECT-STATE.md; WORK-LOG.md
production_code_changes: 0
test_changes: 0
ci_changes: 0
new_tracked_files: 0
tracked_files_expected: 35
external_writes_performed: NON_FORCE_PUSH_OF_TEMPORARY_BRANCH_ONLY
task_temp_root_status: NOT_CREATED
ci_fix_authorization_commits: c258da0; ca27ae0
ci_fix_formal_result: e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3 / ALREADY_AT_FORMAL_HEAD
ci_fix_exact_implementation_allowlist: tests/workbuddy/test_repository_hygiene.py only
ci_fix_exact_change: exactly two Stage3 state assertions / stage3_implementation PASS_ACCEPTED / stage_3_implementation_authorization CONSUMED_COMPLETE
ci_fix_exact_diff: 1 changed path / 2 insertions / 2 deletions / no production or workflow change
ci_evidence_run: 32218904419 / codex/workbuddy-shell-v2 / head_sha=e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3
ci_evidence_result: completed / success / 198 passed / 1 skipped / final exit 0
ci_evidence_command: python -m pytest -p no:cacheprovider tests/workbuddy/test_package_registration.py tests/workbuddy/test_runtime_prepare.py tests/workbuddy/test_repository_hygiene.py -q
first_independent_review: INCOMPLETE / P0=0 / P1=0 / P2=0 / authority mismatch only / exact code diff had no finding
governance_deviation: formal branch advanced to e5ae6f8 before the live authority and state mirrors were closed out
governance_deviation_handling: retain Git and review history unchanged; close only the current authority mirrors; do not retroactively claim the first review was APPROVE
closeout_test_execution: NOT_RUN_DOCS_ONLY / official CI run 32218904419 is the retained execution evidence
stage_3_builder_base: 1c18edf9910e57541c37614c3e7cedf2fb11e372
stage_3_reviewed_implementation: a3f8959682d296301dc573c2835f8c705a52e8b2 / APPROVE / P0=0 / P1=0 / P2=0
stage_3_implementation_tree: eca057c3643c36248cccbfb9606d9aea12b3dc42
stage_3_implementation_commits: 300894359780684fed69a62f9b6c6b5902d51735; d77a69098e212ef2b5e0622ea589527798ec59d3; a3f8959682d296301dc573c2835f8c705a52e8b2
stage_3_closeout: 7c15aae4e77c579309312b21c79076f930970214 / FORMALLY_PROMOTED
stage_3_status: PASS_ACCEPTED
implementation_exact_changed_path_count: 5
implementation_exact_changed_paths: .github/workflows/ci.yml; golden_key_openmontage_workbuddy/__init__.py; golden_key_openmontage_workbuddy/runtime_prepare.py; tests/workbuddy/test_repository_hygiene.py; tests/workbuddy/test_runtime_prepare.py
stage_3_public_entry: prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)
stage_3_result_set: DETECTION_REPORT / CONSENT_REQUIRED / INTEGRATED / SKIPPED / BLOCKED
builder_direct_test_evidence: 55 passed / final exit 0 / no skip
builder_hygiene_test_evidence: 10 passed / final exit 0 / no skip
builder_ci_equivalent_evidence: 199 passed / final exit 0 / no skip
stage_3_reviewer_evidence: independent zero-write review of exact Git objects, code, test definitions and original Builder output / tests not rerun by Reviewer
evidence_boundary: no real third-party or mainland-mirror download; no production DataRoot integration; no WorkBuddy, Stage4, Provider, media or video E2E proof / these are not Stage3 failures or coding prerequisites
single_transaction: bounded detect Remotion and HyperFrames -> report PRESENT/MISSING/INCOMPATIBLE -> zero-download per-capability plan -> WorkBuddy asks -> approve integrates only named items / decline or defer returns SKIPPED -> verify and report
product_code_paths: golden_key_openmontage_workbuddy/runtime_prepare.py; export-only golden_key_openmontage_workbuddy/__init__.py; tests/workbuddy/test_runtime_prepare.py
acceptance_infrastructure_paths: tests/workbuddy/test_repository_hygiene.py; .github/workflows/ci.yml
accepted_builder_exact_path_count: 5 / 3 product paths + 2 acceptance-infrastructure edits
accepted_acceptance_infrastructure_reason: prior fixed-33 hygiene assertions forbade the two new tracked files and prior CI omitted the direct Stage3 test; the accepted implementation updated both atomically and the repository now tracks exactly 35 files
stage2_temporary_release_f00e83_status: STAGE2_TEMPORARY_PROOF_ONLY / MUST_NOT_PUBLISH_AS_FINAL / NOT_A_STAGE3_INPUT
optional_capability_catalog: remotion / hyperframes
capability_definition_rule: approved OpenMontage definitions provide source/version/size/hash/license/target facts; they are not Package Release declarations or capability Locks
bounded_detection_rule: managed DataRoot + explicitly registered/configured candidate paths + normal command resolution only / no drive or system-software enumeration
missing_or_declined_rule: MISSING or INCOMPATIBLE -> ask; decline/defer -> SKIPPED/NOT_INTEGRATED / not a Package or project blocker
consumer_interface_contract: CORRECTED_RESULT_TO_ACTION_MAPPING
consumer_mapping: DETECTION_REPORT=display_facts; CONSENT_REQUIRED=display_plan_and_ask; INTEGRATED=report_available; SKIPPED=continue_with_other_or_base_capabilities; BLOCKED=report_invalid_definition_or_failed_authorized_integration
consent_binding: capability + definition_sha256 + plan_sha256 / explicit per-capability approve only
real_workbuddy_evidence_stage: STAGE_5_ACCEPTANCE_ONLY
same_task_continuation_rule: verify in Stage5; if unsupported ask user to reply 继续刚才的任务; Shell never auto-replays
validation_diff_check: PASS / exact three-path allowlist / tracked 35 / untracked 0 / git diff --check exit 0 / state mirrors consistent
validation_full_test: NOT_RUN_DOCS_ONLY / official CI run 32218904419 already supplies the execution evidence
validation_scope: docs/workbuddy/v2/TASK-REGISTER.md; PROJECT-STATE.md; WORK-LOG.md / production=0 / tests=0 / CI=0 / new tracked=0 / tracked total=35
future_final_package_gate_rule: V2-FINAL-PACKAGE-MATERIALIZATION-AND-PRODUCTION-REGISTRATION-GATE1 is a later final-delivery or Installer task due before Stage5 real WorkBuddy production acceptance; it is not a Stage3 or Stage4 coding/planning prerequisite
future_cleanup_rule: always remove task-owned temp/staging on success or failure; never touch foreign objects; explicitly report any partial Release/PackageRoot/Registration state
historical_stage_4_takeover_boundary: PLANNING_ELIGIBLE / implementation_authorization=NOT_GRANTED
historical_stage_4_registration_audit: locate_active_package returns revalidated Registration, PackageRoot, required toolchain, Guide, Manifest and Lock identities; it does not return an authoritative fixed Package tool entry identity
historical_stage_4_contract_gap: exact public entry and immutable process receipt field names were not frozen; fixed Package tool identity source/path/hash/owner/fixed argv shape was not present in Registration output
historical_stage_4_gap_owner_package_tool_identity: approved OpenMontage Package definition plus later final-delivery or Installer owner / must provide a verifiable fixed tool identity without reopening Stage2 or making final Package a Stage4 planning prerequisite
historical_stage_4_gap_owner_launcher_api_and_receipt: separately authorized Stage4 planning task / freeze one public entry and exact immutable receipt fields before any implementation grant
historical_stage_5_deferred_scope: real new WorkBuddy session, single entry, unchanged literal user_message, per-capability authorization question and same-task continuation / implementation and acceptance only
historical_stage_6_deferred_rule: evaluate only after Stage4 receipt and Stage5 real consumer exist; direct consumption means STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE and production code 0
forbidden_scope: production code; docs other than this ledger; workflow; pyproject; Stage4/5/6 implementation; final Package; old main historical red runs; Node deprecation warning; any second implementation path
historical_next_authorized_task: V2-S4-PLAN-BUILDER1 / EFFECTIVE_ONLY_AFTER_THIS_CLOSEOUT_INDEPENDENT_REVIEW_APPROVE_AND_ORDINARY_FORMAL_FAST_FORWARD
historical_stage_4_planning: ELIGIBLE / START_NOT_PERMITTED_UNTIL_CURRENT_CLOSEOUT_APPROVE_AND_FORMAL_FAST_FORWARD
historical_stage_4_implementation_authorization: NOT_GRANTED
historical_stage_4_launcher_authorization: NOT_GRANTED
historical_stage_5_workbuddy_entry_authorization: NOT_GRANTED
historical_stage_6_status_result_relay_authorization: NOT_GRANTED
historical_final_package_gate_authorization: NOT_GRANTED
```

历史产品模型纠偏已撤销膨胀模型：真实Package、Registration和Package绑定能力元数据都不是Stage 3输入。Stage 3只对Remotion和HyperFrames做有界探测与事实报告，对缺失/不兼容项生成零下载计划，并在WorkBuddy取得用户逐能力明确同意后集成批准项；拒绝或暂缓返回`SKIPPED/NOT_INTEGRATED`。已接受实现严格落在三个产品路径加两个验收基础设施路径；该历史closeout没有新增生产代码、测试、CI、Package字节或外部写入。阶段2临时ZIP `f00e83d6154e7593b765a3d6c863b6653fc642818133acd7924f3fd91aab5d03`只保留历史证据边界，不是Stage 3输入。

## Stage 4执行任务包（已审并正式推广的规划合同）

### 产品目标与官方模型纠正

Stage 4只把一次WorkBuddy拥有的会话安全地交给一个经Release锁定的Package工具进程，并返回一次不可改写的真实进程回执。上游OpenMontage是instruction-driven、Agent-first且运行时查询动态capability/provider registry；生图、生视频、TTS、音乐、stock、local GPU及未来Provider都是可选外部配置，FFmpeg/Remotion/HyperFrames只是合成运行时类别，不是能力全集。上游没有可直接充当Golden Key固定Launcher身份的通用standalone入口，因此Stage 4不得从上游Guide、目录、registry或调用者命令猜工具入口。

Stage 4对Provider和Runtime保持opaque：不硬编码Provider、Remotion或HyperFrames，不配置、选择或执行registry routing。它只把`executor_controls.provider_environment`中已经由Stage 5/WorkBuddy解析的配置，按固定工具定义允许的环境变量名传给唯一子进程。Provider API key存在、缺失或错误永远不是Stage 3能力证据。当前Stage 3的Remotion/HyperFrames定义与原始回执只属于已实现的本地可选运行时证据来源；Stage 4公共接口只有在固定工具定义声明要求时才接受完整approved capability definition与未改写original Stage3 fact，并独立复核实际资产。

### V2-S4-T1：PackageToolDefinitionV1固定工具身份合同

权威来源冻结为：批准的Golden Key OpenMontage Package定义与最终交付/Installer owner为每个Package Release提供一个release-specific immutable `PackageToolDefinitionV1`实例。Stage 4只能消费该实例并与Locator事实交叉验证；调用者、未验证Guide、目录名、动态registry及系统PATH均无权生成或补全它。最终Package物化不是规划或编码前置，但真实启动前实例的每个release-specific字段都必须存在；缺实例或无法绑定时返回`PRELAUNCH_BLOCKED/TOOL_DEFINITION_UNBOUND`，spawn为0。

定义根对象必须是closed Mapping，字段、类型和规则精确如下：

```text
schema_version: Literal["golden-key-workbuddy-package-tool-definition-v1"]
definition_id: str                         # 1..128 NFC非空标识
definition_sha256: str                     # 64位小写hex；规范JSON排除本字段后计算
definition_relative_path: str              # 定义文件本身的规范Package内相对路径
authority_owner: str                       # 必须等于定义文件的精确Manifest owner
package_release: str                       # 必须等于Locator.openmontage_release
package_commit: str                        # 40位小写hex；等于Locator.openmontage_commit
tool_id: str                               # 1..128 NFC非空；Release内唯一
relative_path: str                         # 规范POSIX相对路径；Release实例必填
sha256: str                                # 工具文件64位小写hex；Release实例必填
size: int                                  # 工具文件正整数；Release实例必填
owner: str                                 # 精确Manifest owner；Release实例必填
execution_kind: Literal["PACKAGE_PYTHON_SCRIPT", "DIRECT_EXECUTABLE"]
interpreter_binding: Literal["LOCATOR_PACKAGE_PYTHON", "SELF"]
fixed_argv_template: tuple[str, ...]        # 每个token非空、无NUL；调用者不得追加
fixed_argv_placeholders: tuple[str, ...]    # 只能是()或("{verified_tool_path}",)
request_schema_sha256: Literal["c5b196bfe69c6a6db7073fb7fa7503a58837907e939fceeb5436fa7d19f80ce1"]
result_schema_sha256: Literal["8a96aceb463da2ea39549de44b06a765a3ac859260001ae277b99dbf2a8ca1b3"]
allowed_environment_names: tuple[str, ...] # ASCII env名，大小写折叠后唯一、规范排序
secret_environment_names: tuple[str, ...]  # allowed子集，规范排序
required_local_capabilities: tuple[Mapping, ...]
  each exact Mapping:
    evidence_schema_version: Literal["golden-key-workbuddy-local-capability-evidence-v1"]
    capability_id: str                     # opaque NFC非空，不设枚举
    definition_sha256: str                 # 64位小写hex
    compatibility_basis: Literal["EXACT_ASSET_IDENTITY"]
```

`PACKAGE_PYTHON_SCRIPT`必须使用`LOCATOR_PACKAGE_PYTHON`，且`fixed_argv_placeholders`精确为`("{verified_tool_path}",)`、模板中该占位符恰好一次；进程executable只能是Locator返回的私有Python。`DIRECT_EXECUTABLE`必须使用`SELF`且占位符闭集为空；进程executable只能是工具本身。所有业务数据均走stdin envelope，模板不得出现`user_message`、DataRoot、Provider值、shell元字符解释、会话命令或任意argv占位符。

两个schema hash的输入字节也已冻结，均为下列单行UTF-8、无BOM、无LF文本；不得由实现Builder重算另一种shape：

```text
request: {"fields":["schema_version","session_id","request_id","user_message","executor_controls","package","tool_definition_sha256","local_capability_evidence_identities"],"schema_version":"golden-key-workbuddy-package-tool-request-v1"}
result: {"fields":["schema_version","session_id","request_id","outcome","result_pointer","error"],"schema_version":"golden-key-workbuddy-package-tool-result-v1"}
```

规范JSON固定为UTF-8、NFC、`ensure_ascii=False/allow_nan=False/sort_keys=True/separators=(",", ":")`并以一个LF结尾；`definition_sha256`对同规则但排除自身字段的对象计算。定义字节只绑定稳定的Package release/commit、定义文件、工具、解释器、argv、环境名和本地能力要求；`registration_sha256/manifest_sha256/lock_sha256`绝不进入定义，避免定义文件被Manifest/Lock覆盖时形成hash环。

验证顺序固定为：先调用`locate_active_package(data_root)`并把当次Registration/Manifest/Lock身份保存在preflight事实与最终receipt，而不是写回定义；验证定义closed-schema与自hash；`package_release/package_commit`必须与Locator相同；`definition_relative_path`对应文件必须位于PackageRoot内、在当前Locator已验证的Manifest与Lock中各唯一覆盖、Manifest owner等于`authority_owner`，且其字节与传入Mapping的完整规范JSON字节完全相同；再从当前Manifest与Lock分别找到唯一工具条目并核对owner/hash/size；逐组件lstat并拒绝symlink/junction/reparse/ADS/保留名/别名/`..`；resolved路径必须在PackageRoot内且为regular file；核对工具hash/size；按execution kind核对解释器身份。spawn前再次调用Locator并逐字节复核Registration、Manifest、Lock、定义文件、工具、解释器及所有路径组件；任何替换或漂移均拒绝，spawn为0。不得修改Stage 2 Registration schema或实现。

### V2-S4-T2：唯一公共入口与输入合同

唯一公共入口冻结为：

```python
launch_session_tool(
    data_root: str | os.PathLike[str],
    user_message: str,
    executor_controls: Mapping[str, Any],
    package_tool_definition: Mapping[str, Any],
    local_capability_evidence: Sequence[Mapping[str, Any]] = (),
    cancel_event: threading.Event | None = None,
) -> Mapping[str, Any]
```

返回对象及所有后代Mapping/List必须递归冻结为`MappingProxyType`/tuple。`user_message`必须是原样UTF-8可编码、NFC、无surrogate的字符串；允许空白和业务文本，不解析、不规范化、不追加技术词。Launcher只记录UTF-8字节SHA-256和字节长度，不在receipt/log返回原文。

`executor_controls`为closed Mapping：

```text
schema_version: Literal["golden-key-workbuddy-launcher-executor-controls-v1"]
session_id: str                 # 1..128 ASCII [A-Za-z0-9._-]
request_id: str                 # 1..128 ASCII [A-Za-z0-9._-]
timeout_seconds: int            # 1..3600，bool拒绝
termination_grace_seconds: int  # 1..30，bool拒绝
result_root: str                # 已存在绝对非根目录，canonical且位于DataRoot内，无reparse
provider_environment: Mapping[str, str]
```

`provider_environment`的name必须为ASCII环境变量名、大小写折叠后唯一，并属于定义的`allowed_environment_names`；value必须是UTF-8可编码字符串。所有非空value无条件成为Provider-secret来源，不因name未列入`secret_environment_names`而降级；它们的唯一授权sink是固定child的环境。Receipt只记录经定义allowlist独立验证并规范排序的name。未提供Provider配置、Provider配置错误或Package动态registry未找到Provider，不触发Stage 3；若固定工具启动后因其业务配置退出，则保留真实非零退出。

定义中的allowed/secret环境名不得与`SystemRoot/WINDIR/COMSPEC/PATHEXT/TEMP/TMP/PATH/PYTHONNOUSERSITE/PYTHONUTF8/PYTHONUNBUFFERED`大小写折叠后相交。实现必须在函数入口保守提取raw `provider_environment`中所有可安全读取的非空字符串值及其完整UTF-8 bytes，先建立secret source set，再生成session/request/user-message hints、异常或日志；读取raw controls/value失败时不得回显对象，且对应未证实动态hints一律使用安全空值。Provider-secret来源不得经复制、切片、拼接、插值、编码、hash、长度或其他派生进入argv、canonical stdin、任何不可信动态receipt字段、log或exception；只有child环境可以持有原值。

non-disclosure按provenance而不是对最终receipt做无差别substring禁令：

1. 固定且不读取secret source构造的协议常量——`schema_version`、九值outcome、23个reason、receipt/result/request字段名、固定error origin和预冻结sanitized identifier text——即使与某个secret完整字节或子串偶然相同，也不构成Provider值回显/传播，不得因此改写闭集token或字段类型。
2. 经独立权威重建并验证的环境变量name、Registration/Package/Manifest/Lock、PackageToolDefinition、工具/解释器和本地能力身份同理；允许偶然字节相同的前提是实现的数据流能证明该值来自对应权威对象而非Provider value。固定argv也只能从已验证PackageToolDefinition构造，绝不能读取Provider value。
3. caller/child提供或从其内容计算的session、request、user-message hints、result root/pointer、child error/message、stdout/stderr摘要及其他不可信动态域必须在进入canonical stdin或最终递归freeze前执行secret-source non-propagation检查。无法证明独立来源且包含任一完整非空secret bytes，或由secret-tainted值派生时，必须fail closed并清除该动态值；不得因为静态常量恰好相同而失败，也不得让动态泄漏借“常量例外”通过。

非cancel调用在session/request/user_message/result_root或其他待写stdin动态值中发现上述潜在传播时，固定为`PRELAUNCH_BLOCKED/INVALID_INPUT`、spawn 0。安全替换必须保持receipt全字段与原类型：schema允许nullable的str/int使用`None`，tuple字段使用空tuple而不是插入`None`，result pointer使用全`None`且`valid=false`，动态sanitized message使用预冻结secret-independent文本。若某个stdout/stderr流或由其解析出的动态字段受污染，该流的公开摘要固定为`size=0`、`sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`、`truncated=true`作为“已抑制”安全事实；不受污染的独立进程事实仍保留。最终freeze前必须再递归断言所有非固定、非独立权威动态域对secret source零传播。

`local_capability_evidence`不是Stage 5重包装的摘要。每项必须原样携带完整批准定义和Stage 3原始事实，root为closed Mapping：

```text
schema_version: Literal["golden-key-workbuddy-local-capability-evidence-v1"]
approved_capability_definition: Mapping       # 原始完整批准定义，不删字段、不改字段
approved_capability_definition_sha256: str    # Stage3规范化定义内容的64位小写hex
original_stage3_fact: Mapping                 # 原始PRESENT capability fact或原始INTEGRATED item
original_stage3_fact_sha256: str              # 原始fact规范JSON的64位小写hex
```

`approved_capability_definition`必须按已接受Stage3 closed shape独立验证：根只含`capability/definition_sha256/version/verified_entrypoint/approved_mainland_sources/assets`及两个可选字段`explicit_registered_or_configured_candidate_paths/normal_command_name`；sources与assets子项字段也必须closed。Stage 4按Stage3已经冻结的规范化算法重算定义内容hash，要求同时等于定义内`definition_sha256`、input的`approved_capability_definition_sha256`及工具定义requirement的`definition_sha256`。`capability`值作为opaque字符串与requirement的`capability_id`相等，不在Stage4设置Remotion/HyperFrames枚举。

`original_stage3_fact`只允许两种未改写原始shape：`PRESENT`是Stage3 `capabilities`中的完整`capability/status/evidence`对象，source/runtime/entrypoint位于其`evidence`内；`INTEGRATED`是Stage3 `integrated`中的完整item，同一组evidence字段位于item根。Stage 4重算完整fact canonical hash，并核对其中capability、definition、status、runtime root、entrypoint和source与批准定义一致；fact里的`version_evidence/asset_evidence`只保留来源审计，绝不是信任依据。`INTEGRATED`必须`status=INTEGRATED/source=managed`，保留原始64位小写`plan_sha256`及`reused`字段，且`original_stage3_fact_sha256`必须覆盖这些未改写字段；非managed INTEGRATED或缺失/非法plan identity一律fail closed。

每个requirement的`compatibility_basis`固定为`EXACT_ASSET_IDENTITY`。Stage 4不得硬编码capability或Provider，但必须按原始fact的source精确镜像已接受Stage3来源语义并重新读实际文件：

1. `source=managed`：opaque capability必须是不设业务枚举的安全单路径段；`runtime_root`必须规范等于`<DataRoot>/Runtime/Composition/<opaque capability>/<definition_sha256>/`且是DataRoot内逐组件无symlink/junction/reparse的安全目录；entrypoint必须是定义内相对目标。实际文件集合、结构目录集合必须与定义全部assets及其父目录精确相等，全部asset逐项核对expected size/SHA-256；任何额外文件/目录也使closed-tree失败。
2. `source=explicit`：`runtime_root`必须是安全绝对目录，canonical identity必须精确等于完整批准定义的`explicit_registered_or_configured_candidate_paths`之一；entrypoint和定义全部assets按各自`managed_target`位于该root内，逐组件无reparse并逐项核对size/SHA-256。允许定义外的外来文件/目录存在，不做closed-tree；Stage 4只读，绝不删除、改写或清理它们。
3. `source=PATH`：完整批准定义必须声明非空`normal_command_name`；`runtime_root`与`verified_entrypoint`必须规范后完全相等，且是绝对、逐组件无reparse的regular command file。只用定义中`managed_target == verified_entrypoint`的唯一entrypoint asset核对该文件size/SHA-256；不要求目录、不核对其他assets、不做closed-tree，也不得重新查询宿主PATH或接收调用者命令。

上述source闭集只有`managed/explicit/PATH`；未知source、source与fact shape不符、路径/asset/entrypoint任一漂移均为`PRELAUNCH_BLOCKED/LOCAL_CAPABILITY_EVIDENCE_MISMATCH`，spawn为0。只有定义绑定且满足对应source profile的精确asset identity能够证明本次version相容性时才接受；Launcher不执行第二探针，也不信任调用者或fact中的version输出。若该source profile仍不足以唯一证明相容性，同样fail closed。

Launcher只按`required_local_capabilities`逐项消费上述完整对象；定义要求为空时，任何额外local evidence都返回`PRELAUNCH_BLOCKED/INVALID_INPUT`以避免隐式路由。Stage 5只能原样传递approved definition和original Stage3 fact，不得生成替代摘要或信任hash。Provider环境绝不映射成能力证据；未来扩展Stage3能力目录需另行授权，不能借Stage4通用字段扩大当前Stage3实现。

stdin只发送一个UTF-8规范JSON对象并立即关闭，closed shape为：

```text
schema_version: Literal["golden-key-workbuddy-package-tool-request-v1"]
session_id: str
request_id: str
user_message: str                         # 与入参逐字节相同
executor_controls:
  timeout_seconds: int
  result_root: str
  provider_environment_names: tuple[str, ...]
package:
  registration_sha256: str
  openmontage_release: str
  openmontage_commit: str
tool_definition_sha256: str
local_capability_evidence_identities: tuple[Mapping, ...]
  each: capability_id + definition_sha256 + approved_capability_definition_sha256 + original_stage3_fact_sha256 + status + source + plan_sha256 + entrypoint_sha256 + entrypoint_size
```

Provider secret值只进入子进程环境，不进入canonical stdin；`provider_environment_names`仅因其逐项来自已验证definition allowlist而可保留，绝不能从value生成。

### V2-S4-T3：单进程生命周期

1. 完成全部preflight后构造executable与不可追加的固定argv；`shell=False`，不调用`cmd.exe /c`、PowerShell、PATH工具发现或用户命令。
2. `cwd`精确为已重验PackageRoot。环境不继承整份宿主环境：Windows只复制启动所需`SystemRoot/WINDIR/COMSPEC/PATHEXT/TEMP/TMP`的安全值，PATH由Package内Python/FFmpeg/Node固定目录构造，并设置`PYTHONNOUSERSITE=1/PYTHONUTF8=1/PYTHONUNBUFFERED=1`；之后只注入定义allowlist内的Provider环境。保留名不得被Provider覆盖。
3. 为唯一子进程建立可终止的独立进程组/Windows Job Object；恰好一次spawn，`spawn_count`只可0或1，`retry_count`恒为0。
4. stdin只写上述单一envelope。stdout/stderr是不可信child输出，分别流式计数和SHA-256，内存保留上限各1 MiB；对每个非空secret的完整UTF-8 bytes做跨chunk匹配，匹配器必须保留足以发现边界命中的overlap。任一流任一位置命中都精确裁决`SECRET_DISCLOSURE_DETECTED`，固定协议常量偶然碰撞例外绝不适用于child输出。receipt不返回原文；受污染流只返回上述安全抑制摘要。仅stdout前64 KiB可用于解析单个结果envelope，超限或额外非空字节视为无效；即使raw bytes因JSON escape未直接命中，解析后的result pointer/error等动态字段重建出secret也必须同样阻断。
5. 正常退出保留真实exit code。timeout或`cancel_event.is_set()`后终止整个自有进程树，等待`termination_grace_seconds`，随后检测残留；不重试、不重放user message。
6. timeout、取消、进程退出、输出读取、结果校验或终止证据不完整时不得伪造成功；任务自有临时缓冲必须清理，不删除Package、result或外来对象。

固定工具stdout成功协议为单个UTF-8规范JSON对象：

```text
schema_version: Literal["golden-key-workbuddy-package-tool-result-v1"]
session_id: str                 # 与请求相同
request_id: str                 # 与请求相同
outcome: Literal["SUCCEEDED", "FAILED"]
result_pointer: null | Mapping
  exact Mapping: relative_path: str; sha256: str; size: int
error: null | Mapping
  exact Mapping: code: str; origin: str; message: str
```

`SUCCEEDED`要求exit 0、`error=null`和非空result pointer；`FAILED`要求exit 0、`result_pointer=null`和非空error，并映射为Launcher outcome/reason均为`CHILD_REPORTED_FAILURE`。pointer相对路径必须规范、安全，解析后位于`executor_controls.result_root`内，逐组件无reparse，目标为regular file且hash/size匹配。非零退出事实优先保留，不因stdout内容改写为成功或child-reported failure。

### V2-S4-T4：不可改写LauncherReceiptV1

公共函数对输入错误、preflight错误、spawn错误和运行结果一律返回receipt，不向调用者泄漏合同异常。结果闭集精确为`PRELAUNCH_BLOCKED`、`SPAWN_FAILED`、`EXITED_SUCCESS`、`EXITED_NONZERO`、`CHILD_REPORTED_FAILURE`、`TIMED_OUT`、`CANCELLED`、`INCOMPLETE`、`RESIDUAL_PROCESS`九值。若终止后仍有自有进程残留，最终outcome必须为`RESIDUAL_PROCESS`并保留timeout/cancel事实；exit 0但结果envelope或pointer无效为`INCOMPLETE`；exit 0且child明确返回`FAILED`为`CHILD_REPORTED_FAILURE`；只有exit 0、child `SUCCEEDED`、无泄密、无残留且有效pointer才可`EXITED_SUCCESS`。

Receipt为closed、递归冻结Mapping，根字段和嵌套类型精确如下：

```text
schema_version: Literal["golden-key-workbuddy-launcher-receipt-v1"]
outcome: 上述9值之一
reason_code: Literal[
  "NONE", "INVALID_INPUT", "CANCELLED_BEFORE_SPAWN", "LOCATOR_FAILED", "REGISTRATION_DRIFT",
  "TOOL_DEFINITION_INVALID", "TOOL_DEFINITION_UNBOUND", "TOOL_PATH_VIOLATION",
  "TOOL_IDENTITY_MISMATCH", "INTERPRETER_IDENTITY_MISMATCH",
  "LOCAL_CAPABILITY_EVIDENCE_REQUIRED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH",
  "ENVIRONMENT_NOT_ALLOWED", "SPAWN_OS_ERROR", "EXITED_NONZERO", "TIMEOUT",
  "CANCELLED", "CHILD_REPORTED_FAILURE", "OUTPUT_INVALID", "RESULT_POINTER_INVALID",
  "SECRET_DISCLOSURE_DETECTED", "EVIDENCE_INCOMPLETE", "RESIDUAL_PROCESS_DETECTED"]
session: {session_id: str | None}
request: {request_id: str | None}
registration: {registration_sha256: str | None}
package: {openmontage_release: str | None; openmontage_commit: str | None; package_root: str | None}
manifest: {sha256: str | None; size: int | None}
lock: {sha256: str | None; size: int | None; bundle_sha256: str | None}
tool_definition: {definition_id: str | None; definition_sha256: str | None; authority_owner: str | None}
tool_file: {tool_id: str | None; relative_path: str | None; path: str | None; sha256: str | None; size: int | None; owner: str | None}
interpreter: {binding: str | None; path: str | None; sha256: str | None; size: int | None}
user_message: {sha256: str | None; byte_length: int | None}
provider_environment_names: tuple[str, ...]
local_capability_evidence_identities: tuple[Mapping, ...]
  each: {capability_id: str; definition_sha256: str; approved_capability_definition_sha256: str; original_stage3_fact_sha256: str; status: Literal["PRESENT", "INTEGRATED"]; source: Literal["managed", "explicit", "PATH"]; plan_sha256: str | None; entrypoint_sha256: str; entrypoint_size: int} # PRESENT plan=None；INTEGRATED plan=原始64hex
launched: bool
spawn_count: int                 # 0|1
pid: int | None
started_at_utc: str | None       # RFC3339 UTC
ended_at_utc: str                # RFC3339 UTC
duration_ms: int                 # >=0
exit_code: int | None
timed_out: bool
cancelled: bool
retry_count: Literal[0]
stdout: {size: int; sha256: str; truncated: bool}
stderr: {size: int; sha256: str; truncated: bool}
result_pointer: {path: str | None; sha256: str | None; size: int | None; valid: bool}
error: null | {code: str; origin: Literal["PREFLIGHT", "SPAWN", "CHILD", "TIMEOUT", "CANCEL", "OUTPUT", "RESULT", "RESIDUAL"]; sanitized_message: str}
residual_process: {detected: bool; termination_attempted: bool; termination_succeeded: bool | None; observed_pids: tuple[int, ...]}
```

所有字段始终存在。`PRELAUNCH_BLOCKED/INVALID_INPUT`以及无法安全解析对应输入时，`session.session_id`、`request.request_id`、`user_message.sha256/byte_length`允许为`None`；已成功验证且可证明不来自secret source的动态字段填真实值，未到达或受污染字段按上述类型安全值替换，不得删除字段或改变tuple元素类型。固定协议常量与独立权威身份的偶然字节相同不算泄漏；Provider value从来源传播到任何不可信动态receipt字段、异常文本、日志或回传原文的次数必须为0。若child stdout/stderr完整secret bytes跨chunk命中，或解析动态字段重建出secret，丢弃原文并安全替换受污染动态域，outcome=`INCOMPLETE`、reason=`SECRET_DISCLOSURE_DETECTED`。

结果裁决优先级精确如下，命中后不得被较低项覆盖；真实`exit_code/timed_out/cancelled/residual_process`字段始终保留：

| 优先级 | 条件 | outcome / reason | spawn_count |
|---|---|---|---|
| 1 | `cancel_event`类型无效，或其他输入无法安全读取且无法先确认有效取消对象 | `PRELAUNCH_BLOCKED / INVALID_INPUT` | 0 |
| 2 | 有效`cancel_event`在函数入口已经set；先于Locator和其他preflight裁决 | `CANCELLED / CANCELLED_BEFORE_SPAWN` | 0 |
| 3 | 输入/Locator/定义/路径/环境/本地证据任一preflight失败 | `PRELAUNCH_BLOCKED /`对应精确reason | 0 |
| 4 | OS创建唯一进程失败 | `SPAWN_FAILED / SPAWN_OS_ERROR` | 0 |
| 5 | spawn后终止宽限结束仍检测到自有残留进程 | `RESIDUAL_PROCESS / RESIDUAL_PROCESS_DETECTED` | 1 |
| 6 | 任一非空Provider secret完整UTF-8 bytes出现在不可信child stdout/stderr（含跨chunk），或解析动态字段重建出secret；无固定常量例外 | `INCOMPLETE / SECRET_DISCLOSURE_DETECTED` | 1 |
| 7 | timeout与cancel中先发生/先被monotonic观察者记录者；同一tick同时观察时cancel优先 | `TIMED_OUT / TIMEOUT`或`CANCELLED / CANCELLED` | 1 |
| 8 | child真实exit code非0 | `EXITED_NONZERO / EXITED_NONZERO` | 1 |
| 9 | 输出捕获、JSON envelope、session/request或result pointer无效/证据不完整 | `INCOMPLETE / OUTPUT_INVALID|RESULT_POINTER_INVALID|EVIDENCE_INCOMPLETE` | 1 |
| 10 | exit 0且有效result envelope明确`outcome=FAILED` | `CHILD_REPORTED_FAILURE / CHILD_REPORTED_FAILURE` | 1 |
| 11 | exit 0且有效`SUCCEEDED` envelope、有效pointer、无泄密和残留 | `EXITED_SUCCESS / NONE` | 1 |

preflight reason不得合并或留给Builder选择：closed input/type/range/未知字段错误，或Provider-secret潜在传播进入非cancel动态input/canonical stdin=`INVALID_INPUT`；Locator无活动Registration或首次读取失败=`LOCATOR_FAILED`；首次快照后Registration/Manifest/Lock身份变化=`REGISTRATION_DRIFT`；release-specific定义实例缺失、定义文件不在当前Manifest+Lock中各唯一覆盖、传入定义字节不等于Package文件、authority owner不绑定或release/commit不属于当前Locator=`TOOL_DEFINITION_UNBOUND`；定义closed shape/self-hash/execution kind/interpreter binding/argv/schema hash/env/local requirement非法=`TOOL_DEFINITION_INVALID`；工具路径逃逸或组件不安全=`TOOL_PATH_VIOLATION`；工具Manifest/Lock覆盖、hash/size/owner不匹配=`TOOL_IDENTITY_MISMATCH`；解释器路径或身份不匹配=`INTERPRETER_IDENTITY_MISMATCH`；声明能力但缺项=`LOCAL_CAPABILITY_EVIDENCE_REQUIRED`；能力完整定义、原始fact、实际asset或closed-tree任一不匹配=`LOCAL_CAPABILITY_EVIDENCE_MISMATCH`；环境名越权=`ENVIRONMENT_NOT_ALLOWED`；其余无法完成的preflight事实=`EVIDENCE_INCOMPLETE`。

非成功receipt的`error`必须非空且与最终reason同源：全部preflight=`PREFLIGHT`，spawn失败=`SPAWN`，残留=`RESIDUAL`，泄密/输出无效=`OUTPUT`，timeout=`TIMEOUT`，取消=`CANCEL`，非零和child FAILED=`CHILD`，pointer无效=`RESULT`；只有`EXITED_SUCCESS/NONE`的`error=null`。spawn=0时`launched=false/pid=None/started_at_utc=None/exit_code=None/timed_out=false/retry_count=0`，stdout/stderr固定为空字节的size/SHA-256/truncated事实，result pointer全`None`且`valid=false`，residual固定未检测/未终止/空PID；provider名称和local evidence identities只保留已完整验证项，否则为空tuple。

函数入口cancel不启动Locator、不访问Package、不spawn，但必须先从raw controls保守提取可安全读取的Provider secret source，再决定哪些session/request/message hints可公开；任何hint包含完整secret bytes、由secret派生或来源无法安全判断时，对应nullable字段为`None`，未验证的provider name tuple为空。即使secret value恰好等于session/request，最终仍必须是`CANCELLED/CANCELLED_BEFORE_SPAWN`、Locator 0、spawn 0，只是相关hints安全清空；固定schema/outcome/reason常量保持不变。spawn后timeout/cancel的“先发生”使用首次记录的`time.monotonic_ns()`；不得由线程调度顺序或Builder自行选择。任何未分类内部错误：spawn前映射`PRELAUNCH_BLOCKED/EVIDENCE_INCOMPLETE`，spawn后映射`INCOMPLETE/EVIDENCE_INCOMPLETE`。

### V2-S4-T5：直接与负面测试矩阵

未来直接测试必须至少覆盖原21项，并增加动态registry/Provider、定义可实例化和结果裁决边界：

1. 无活动Registration；2. Registration损坏/漂移；3. PackageRoot或任一必带工具链漂移；4. 定义缺字段/未知字段/自hash错误；5. 工具未被Manifest或Lock唯一覆盖；6. 工具hash/size/owner不匹配；7. 路径逃逸/ADS/别名；8. 任一路径组件symlink/junction/reparse；9. 任意命令/额外argv/placeholder注入；10. user_message字节被改写；11. controls拼入user_message；12. 定义要求的本地证据缺失；13. capability/definition/entrypoint身份不匹配；14. 定义不要求本地能力时不得要求Remotion/HyperFrames；15. 真实非零退出保真；16. timeout；17. result envelope/pointer缺失、越界、漂移或hash/size错误；18. stdout/stderr含secret时原文回传与日志为0；19. 残留子进程；20. spawn<=1且retry=0；21. 第二Agent/调度/服务/数据库/媒体/Artifact/Checkpoint代码为0；22. Provider和capability名无硬编码枚举；23. 未allowlist的任意env名拒绝且spawn=0；24. secret值不进入argv/stdin/receipt/hash前日志/异常；25. Provider配置缺失不会被映射为Stage3证据缺失；26. 只有定义明确声明的本地能力才校验证据；27. spawn前Registration/tool/interpreter替换漂移；28. cancel前/后及终止宽限；29. 输出截断仍保留真实size/hash且不产生成功；30. 所有返回Mapping递归不可修改；31. invalid input也总是返回全字段receipt，无法安全读取的session/request/message字段为`None`；32. 入口已取消为`CANCELLED/CANCELLED_BEFORE_SPAWN`、Locator访问0、spawn=0；33. OS spawn失败为`SPAWN_FAILED/SPAWN_OS_ERROR`、spawn_count=0；34. residual、secret、timeout/cancel先发生、nonzero、invalid output、child FAILED和success严格按优先级裁决；35. exit 0且child `FAILED`精确映射`CHILD_REPORTED_FAILURE/CHILD_REPORTED_FAILURE`；36. 定义closed字段不含Registration/Manifest/Lock hash，避免hash环；37. 使用真实Stage2 fixture组装含定义文件和工具文件的Package，完成`register -> locate -> Stage4 definition/tool validate`往返；38. Stage5摘要envelope或只给摘要hash必须拒绝，输入必须含完整批准定义和未改写Stage3原始fact；39. Stage4独立重验runtime root、entrypoint与source-specific asset identity，fact证据不得替代字节验证；40. caller/fact的version_evidence不受信，精确asset identity不足以证明相容性时fail closed；41. `managed/explicit/PATH`三种合法`PRESENT`原始交接分别成功且receipt保留source；42. managed root存在任一额外文件或目录时拒绝；43. explicit定义资产漂移时拒绝，但定义外额外文件/目录始终保留且零写入；44. PATH命令文件被替换、非绝对、非regular或任一组件不安全时拒绝；45. `INTEGRATED`使用explicit/PATH或缺失plan identity时拒绝；46. 合法managed `INTEGRATED`的receipt保留原始`plan_sha256`，`original_stage3_fact_sha256`绑定未改写`reused`；47. 未知source拒绝且spawn=0；48. secret为`-`或`I`并只与固定schema/outcome/reason/field name偶然碰撞时仍返回全字段、类型合法receipt；49. pre-cancel时secret完整值等于session/request，仍为`CANCELLED/CANCELLED_BEFORE_SPAWN`、Locator 0、spawn 0且相关hints为`None`；50. secret被复制/派生到user_message/session/request/result_root或其他canonical-stdin动态域时preflight阻断且安全替换；51. child stdout与stderr分别在单chunk和跨chunk出现完整secret bytes时均为`SECRET_DISCLOSURE_DETECTED`且受污染流只返回安全抑制摘要；52. child JSON escape后解析出的result pointer/error重建secret时同样阻断，动态pointer/message不传播；53. 经definition allowlist验证的env name或独立Package/definition identity与secret偶然相同不误报，并证明无value数据流；54. 动态域清除使用`None`/空tuple/固定文本且不向`tuple[str]`插入`None`、不删除receipt字段、不改变九值/23 reason/字段类型；55. argv、canonical stdin、最终动态receipt、log和exception对Provider-secret来源复制/派生均为0，最终递归non-propagation断言命中时fail closed。

成功测试至少覆盖`PACKAGE_PYTHON_SCRIPT`与`DIRECT_EXECUTABLE`各一次、空Provider环境、allowlisted动态Provider环境、required_local_capabilities为空和非空、exit 0有效pointer、Stage 6直接消费同一receipt shape。真实Stage2 fixture往返必须在临时DataRoot内创建由Manifest/Lock覆盖的定义文件与固定工具，调用现有registration API登记、激活并由Locator读取，再由Stage4完成定义/工具验证；它证明合同可实例化，但不要求最终交付Package成为实现前置。测试只用任务fixture进程，不运行真实WorkBuddy、Provider、媒体生产或未验证Package Guide。

第24项“secret值不进入”精确指Provider-secret source不得被Launcher复制/派生，不是禁止secret-independent固定常量或独立权威身份偶然字节相同。第29项“输出截断保留真实size/hash”只适用于未受secret污染的流；命中secret的流必须使用T2/T4冻结的安全抑制摘要，不能为保留真实digest而派生或传播secret。上述clarification在`V2-S4-SECRET-NONDISCLOSURE-CONTRACT-CLARIFICATION-REVIEW1`独立`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward为formal head前不是implementation authority；现有实现candidate保持禁止推广，批准后仍须返回原Implementation Builder修订并独立复审。

### V2-S4-T6：未来实现精确文件白名单

未来实现只能评估并授权以下5个路径：

```text
golden_key_openmontage_workbuddy/session_launcher.py       # 唯一新增生产模块
golden_key_openmontage_workbuddy/__init__.py               # 只导出launch_session_tool
tests/workbuddy/test_session_launcher.py                    # 唯一新增直接测试
tests/workbuddy/test_repository_hygiene.py                  # 固定树/API/source断言35->37
.github/workflows/ci.yml                                    # 唯一pytest命令加入直接测试
```

新增生产文件与直接测试使tracked从35精确变为37；hygiene必须同步固定37文件白名单、4个Python源文件和唯一Stage4 API，否则新增合法文件会被现有固定35合同拒绝；CI必须把唯一Stage4直接测试加入现有唯一pytest命令，否则正式门禁不执行新合同。不得动态放宽树断言或使用glob接受未来文件。`package_registration.py`、`runtime_prepare.py`、`pyproject.toml`原则上禁止修改；任何需要它们或第6个路径的方案立即`STOPPED_SCOPE_EXPANSION`并回到用户重新授权。

### V2-S4-T7：Builder、Reviewer与推广

规划推广时要求用户另行明确说“启动阶段四实现”；该历史条件已由用户2026-08-20指令满足，并由正式授权结果`2c3d87bedfa4a3cef3cfd952641199300f2715dc`固化。实施Builder接管时live authority必须从最新`origin/codex/workbuddy-shell-v2`冻结精确base/tree/37目标文件合同，创建一个临时Builder分支，只允许上述5路径。Builder必须使用项目D盘独立`.venv`，运行Stage4直接测试、repository hygiene和完整仓库测试，保留未截断输出和最终exit 0；检查精确diff、37文件等值、clean/untracked0/stash0后提交并非force推送。独立Reviewer零写，只审精确base..candidate，核对公共合同最小性、fail-closed反例、secret为0和真实测试定义；`REQUEST_CHANGES`只回原Builder。只有`APPROVE/P0=0/P1=0/P2=0`、formal仍等于base、对象一致时才允许普通fast-forward推广。推广完成也不得自动启动Stage 5、Stage 6或最终Package Gate。

任务执行顺序、输入、交付与退出条件固定为：

| 任务 | 输入 | 交付输出 | PASS退出条件 / fail-closed停止 |
|---|---|---|---|
| T1 工具身份 | Locator当前返回合同、批准Package/Installer authority边界 | 不含Locator hash环的`PackageToolDefinitionV1`、外部Registration/Manifest/Lock绑定与真实fixture往返 | schema/authority/path/hash/size/owner/interpreter/argv全部唯一；`register -> locate -> validate`可实例化；具体Release缺实例时记录`TOOL_DEFINITION_UNBOUND`，不猜入口 |
| T2 公共入口 | T1定义、Stage2 Locator、Stage3现有证据边界 | 唯一`launch_session_tool(...)`、closed controls、完整批准能力定义+原始Stage3 fact、source-aware复核与stdin envelope | user message/controls/provider secret三者分离；managed/explicit/PATH按已接受语义独立重验；Provider缺失不转成Stage3缺失 |
| T3 生命周期 | T1/T2验证后对象 | cwd/env/stdin/output/timeout/cancel/termination/residual规则 | shell=false、spawn=1、retry=0；身份漂移或环境越权则spawn=0 |
| T4 回执 | T1身份、T3真实进程事实、结果envelope | 总是返回的全字段`LauncherReceiptV1`、9值outcome闭集、23 reason与11级裁决优先级 | provenance-aware动态域零传播、静态常量偶撞可表示、递归冻结；证据不完整不得成功 |
| T5 测试矩阵 | T1-T4合同及原21项反例 | 55类直接/负面测试、secret碰撞/传播、三类source交接、真实Stage2 fixture往返与成功夹具 | 所有反例断言spawn/outcome/reason/残留；外来explicit文件零改写；不运行真实Provider/媒体/WorkBuddy |
| T6 文件范围 | 当前35文件固定树与现有hygiene/CI | 精确5路径、37文件终态 | 只新增生产+直接测试两文件；第6路径或动态放宽立即停止 |
| T7 交付治理 | 最新formal精确对象、T1-T6 | Builder证据、零写Reviewer、普通FF推广路径 | REVIEW APPROVE且P0/P1/P2=0、对象/路径/测试/clean全匹配；否则只回原Builder |

T1到T4是同一个单生产模块内的私有实现职责，不得为了任务编号拆成新模块。T5/T6只提供直接证据和固定仓库门禁。T7完成后Stage4仓库实现才可收口，但Stage5/6仍保持未授权。

以下是规划推广时冻结的历史closeout目标；它已经由`V2-S4-PLAN-CLOSEOUT-REVIEW1`独立`APPROVE / P0=0 / P1=0 / P2=0`及`dfd97f3d2e05a4c448448fc14514d1cfe76836e8`普通fast-forward全部满足，不再是当前授权状态：

```text
historical_closeout_target_stage_4_planning: PASS_ACCEPTED
historical_closeout_target_stage_4_implementation_authorization: NOT_GRANTED
historical_closeout_target_stage_4_launcher_authorization: NOT_GRANTED
historical_closeout_target_next_authorized_task: NONE
historical_closeout_target_stage_5_workbuddy_entry_authorization: NOT_GRANTED
historical_closeout_target_stage_6_status_result_relay_authorization: NOT_GRANTED
historical_closeout_target_final_package_gate_authorization: NOT_GRANTED
```

这些字段只记录当时的历史目标，不得覆盖文件顶部的当前六权威同步候选和条件生效字段。

### 与Stage 5/6不断档

Stage 5只保留literal `user_message`，形成closed `executor_controls`、从已批准Package/Installer对象取得`PackageToolDefinitionV1`、按用户单独授权解析Provider环境，并在固定定义确有本地要求时原样传递完整approved capability definition和未改写original Stage3 fact；它不生成命令或argv，也不生成替代摘要。Stage 4按fact原始source独立复核定义与实际资产：managed closed-tree、explicit全部定义资产但允许且保留额外文件、PATH仅entrypoint asset；只启动一次并返回`LauncherReceiptV1`。Stage 6优先原样复用该receipt；若真实Stage 5消费者不需要转换，则以`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`和生产代码0完成。该规划不预建Stage 5/6。

## 阶段2已完成任务证据

```text
completed_task_id: V2-S2-REQUIRED-TOOLCHAIN-PACKAGE-REFRESH-BUILDER1
completed_task_start_commit: 55781b45ac9217693843f2c73cec994805e4024c
completed_task_initial_result_commit: 62a47afa2301eb187a8b63e33ad08f1b5476c318
completed_task_final_result_commit: 709c8e880b144fa9e9be26e9feb5d776dd6025e2
completed_task_review_range: 55781b45ac9217693843f2c73cec994805e4024c..709c8e880b144fa9e9be26e9feb5d776dd6025e2
completed_task_reviewer_verdict: APPROVE / P0=0 / P1=0 / P2=0
completed_task_promotion: ORDINARY_FAST_FORWARD / origin/codex/workbuddy-shell-v2=709c8e880b144fa9e9be26e9feb5d776dd6025e2
completed_task_authorization: CONSUMED_COMPLETE
review1_initial_verdict_history: REQUEST_CHANGES / P0=0 / P1=1 / P2=1 / resolved by 709c8e880b144fa9e9be26e9feb5d776dd6025e2
previous_contract_correction_status: PASS_ACCEPTED
previous_contract_correction_formal_commit: 29a890db22181db9532263a168dcbe5f708b7149
previous_contract_correction_review: INDEPENDENT_APPROVE_AND_FAST_FORWARD_PROMOTED
stage_2_completed_allowed_paths:
  - golden_key_openmontage_workbuddy/package_registration.py
  - tests/workbuddy/test_package_registration.py
  - docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md
  - docs/workbuddy/v2/TASK-REGISTER.md
production_code_limit: 1 file
test_change_limit: 1 file
documentation_change_limit: 2 files
source_repository: D:\BlazingCD\Personal\golden_key_short_video_agent-openmontage-agent-cleanroom
source_commit: 8395e578165e802990d53fef5a166f8b4cf0461a
source_package_tree_path: packages/golden-key-openmontage
source_package_tree: 0464861c5985c7c9072e789b94889d29cf9a937a
source_export_rule: 只允许从上述Git对象导出；不得触碰、修改或清理source repository当前dirty worktree
python_archive: D:\Downloads\Working\python-3.14.7-embed-amd64.zip
python_archive_size: 12673227
python_archive_sha256: d297e5ff019966817ad8502465176139f2d3d840fa4ed84b13bed399a6ab1f15
node_version: v22.23.2-win-x64
node_archive_url: https://npmmirror.com/mirrors/node/v22.23.2/node-v22.23.2-win-x64.zip
node_archive_size: 35683585
node_archive_sha256: 1177b4137ba5adaa56354ae40f1080c7450e8ae09cecb47da459d1c52ac99f97
ffmpeg_publisher_channel_label: 9.0 essentials
ffmpeg_actual_binary_version: 9.0.1-essentials_build
ffmpeg_archive_url: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z
ffmpeg_archive_size: 34372199
ffmpeg_archive_sha256: 49a73bdf0850092a252ac4641d922f3048d63ed113e196cc65ce1e4f7fb33e85
rejected_ffmpeg_archive: D:\Downloads\Working\ffmpeg-9.0-essentials_build.7z / SHA256 prefix ffb866 / MUST_NOT_USE
temporary_build_root: D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1
project_venv_rule: 必须使用该任务在D盘的独立.venv；不得混用系统或其他项目Python包
package_build_scope: 一次真实临时Package；源树+干净私有Python及锁定核心依赖+FFmpeg/ffprobe+Node/npm/npx
registration_scope: Stage2必须验证并返回全部必带工具身份与固定路径；负面测试fail closed
forbidden_scope: external source repo、官方OpenMontage、Installer、Runtime、Launcher、Stage3、Skill、config、其他测试、生产DataRoot激活、WorkBuddy、Provider、媒体
resolved_python_distributions: 47
offline_dependency_rebuild: 4555 files / missing=0 / extra=0 / changed=0
real_package_core_files: 2155
real_package_toolchain_files: 6670
real_package_manifest_entries: 8826
real_release_size: 223112435
real_release_sha256: f00e83d6154e7593b765a3d6c863b6653fc642818133acd7924f3fd91aab5d03
real_registration_sha256: aa5aba5ff543258d58acf944a0f4e87d80b9f38e62205268ae23b5266b78659b
real_register_activate_locate: PASS / task-only DataRoot
builder_changed_files_cumulative: production=1 / test=1 / docs=2
fix1_changed_files: production=1 / test=1 / docs=1
pre_fix_full_test_command: D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\.venv\Scripts\python.exe -m pytest -q
pre_fix_full_test_result: 141 passed in 22.49s / final exit 0
fix1_target_test_command: D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\.venv\Scripts\python.exe -m pytest tests/workbuddy/test_package_registration.py -q -k "required_toolchain_rejects_internal_and_cyclic or required_toolchain_resolve_runtime_error"
fix1_target_test_result: 3 passed / 131 deselected in 3.03s / final exit 0 / real Windows reparse tests not skipped
fix1_full_test_command: D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\.venv\Scripts\python.exe -m pytest -q
fix1_full_test_result: 144 passed in 20.46s / measured wrapper 20.84s / final exit 0
real_package_assembly_command: D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\.venv\Scripts\python.exe D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\assemble.py D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\export\package D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\release
real_package_assembly_result: final exit 0 / Release size and SHA-256 unchanged
real_registration_command: PYTHONPATH=<ShellRepo>; D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\.venv\Scripts\python.exe D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\register_evidence.py D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1
real_registration_result: register + task-only activate + locate / final exit 0 / registration SHA-256 unchanged
real_tool_commands: bootstrap/python/python.exe -B -c <core imports + SSL + same-interpreter subprocess>; bootstrap/ffmpeg/bin/ffmpeg.exe -version; bootstrap/ffmpeg/bin/ffprobe.exe -version; bootstrap/node/node.exe --version; bootstrap/node/npm.cmd --version; bootstrap/node/npx.cmd --version
real_tool_results: Python 3.14.7/OpenSSL 3.5.7; FFmpeg+ffprobe 9.0.1; Node 22.23.2; npm+npx 10.9.8 / every command final exit 0
exit_evidence: Stage2 task-only Package build and DataRoot cleaned after evidence capture; no retained final Release, installed production PackageRoot, or production Registration
```

上述证据证明完整工具链组装能力、Stage 2 Registration/Locator实现，以及一次真实register、task-only activate和new-process locate已经完成并正式接受；临时实例清理不重开、不重做阶段2。它仍不证明最终交付Package持续存在。最终Package持久构建、安装、生产登记和激活仍是强制交付要求，但只属于后续最终交付或Installer收口门禁，最迟在Stage 5真实WorkBuddy入口和生产验收前完成；它绝不是Stage 3编码前置，也不得塞入Stage 3 Runtime代码。

历史Stage 3授权顺序要求五文档纠偏先完成独立审阅和正式推广，再由live authority给出精确Builder基线、五路径白名单和Reviewer范围；该顺序已完成并由上述正式实施结果消费。不得增加Package、Registration、Package绑定能力元数据、task-only登记验证或Stage 5输入Gate。持久最终Package与生产Registration仍在后续最终交付或Installer Gate收口，但不属于Stage 3失败或编码前置。开发或测试任务不得随意写入外部对象或DataRoot；未来产品运行时只有在用户对具体能力明确`approve`后，才允许Stage 3在受管DataRoot执行合同规定的staging和集成。已接受Builder没有进行真实第三方下载。

## 当前正式状态

```text
formal_branch: codex/workbuddy-shell-v2
accepted_authority_result: 2c3d87bedfa4a3cef3cfd952641199300f2715dc
historical_formal_handoff_before_stage3_correction: 068408f02c87a1eabeda58ea1ebce3df606c0a0c
historical_accepted_stage3_correction_result: 7ba6ad64270c7ccdd7500e2a59b05cf55c73d7ed
formal_head: 2c3d87bedfa4a3cef3cfd952641199300f2715dc
formal_tree: c196dbf6b094cad05076d01ac2496f7425cf6fac
stage_3_implementation_formal_result: a3f8959682d296301dc573c2835f8c705a52e8b2
stage_3_closeout_formal_result: 7c15aae4e77c579309312b21c79076f930970214
stage_3_to_stage_4_docs_sync_formal_result: 513e5ca10d1ba04878295be110096b013f47974a
stage_3_to_stage_4_docs_closeout_formal_result: a8d024ca9001184e9c2a5a995598d64024eef51b
ci_stage3_state_assertion_fix_formal_result: e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3
ci_stage3_state_assertion_fix_review_history: first independent review INCOMPLETE / P0=0 / P1=0 / P2=0 / authority mismatch only / code diff no finding
ci_stage3_state_assertion_fix_ci: run 32218904419 / completed / success / 198 passed / 1 skipped / final exit 0
ci_stage3_state_assertion_closeout: PASS_ACCEPTED / 26bfe60ab9da62797559eb9a459b8daa345f8d80 / FORMALLY_PROMOTED
stage_1_status: PASS_ACCEPTED
stage_2_status: PASS_ACCEPTED_REGISTRATION_AND_TEMPORARY_PACKAGE_PROOF_ONLY
stage_2_registration_implementation: PASS_ACCEPTED
stage_2_temporary_package_validation: PASS_ACCEPTED
stage_2_required_toolchain_refresh: PASS_ACCEPTED
stage_2_required_toolchain_refresh_result: 709c8e880b144fa9e9be26e9feb5d776dd6025e2
stage_2_required_toolchain_refresh_review: APPROVE / P0=0 / P1=0 / P2=0
stage_2_required_toolchain_refresh_promotion: origin/codex/workbuddy-shell-v2=709c8e880b144fa9e9be26e9feb5d776dd6025e2
stage_2_previous_package_status: PASS_ACCEPTED_HISTORICAL
stage_2_integration_commit: ca6e93b7da108732f2034239da340a986ba3da3a
repository_hygiene_status: PASS_ACCEPTED
repository_final_tree_commit: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
repository_final_audit: APPROVE
repository_final_audit_source: USER_ACCEPTED_HANDOFF_2026_08_17
repository_tracked_files: 35
final_package_artifact: NOT_MATERIALIZED
installed_production_package_root: NOT_CREATED
production_package_registration: NOT_CREATED
production_package_activation: NOT_CREATED
stage_3_planning_authorization: CONSUMED_COMPLETE
stage3_planning: PASS_ACCEPTED_FORMALLY_PROMOTED_AT_061AC8428823C8732F241B01A7FD9E54A732599A
stage_3_implementation_authorization: CONSUMED_COMPLETE
stage_3_conditional_authorization: CONSUMED_COMPLETE
stage_3_start_gate: PASS_ACCEPTED
stage_3_final_package_dependency: NOT_REQUIRED_FOR_CODING_START
final_package_gate: DEFERRED_TO_FINAL_DELIVERY_OR_INSTALLER_CLOSEOUT_BEFORE_STAGE5_PRODUCTION_ACCEPTANCE
stage_3_package_release_input: NOT_REQUIRED
stage_3_registration_input: NOT_REQUIRED
stage_3_package_bound_capability_metadata: REMOVED_FROM_INPUT_MODEL
stage_3_consumer_interface_contract: PASS_ACCEPTED_FORMALLY_PROMOTED_AT_061AC8428823C8732F241B01A7FD9E54A732599A
stage_3_product_execution_contract: PASS_ACCEPTED_FORMALLY_PROMOTED_AT_061AC8428823C8732F241B01A7FD9E54A732599A
real_workbuddy_validation: DEFERRED_TO_STAGE_5_ACCEPTANCE
stage_3_execution_packet: CONSUMED_COMPLETE / EXACT_5_PATHS
stage3_implementation: PASS_ACCEPTED
stage_3_status: PASS_ACCEPTED
stage_4_plan_formal_result: 5cb3f585a0cddffbd823c785b1d39ebd1834c1df
stage_4_plan_formal_tree: 144df76b3a307fa8944ccd7bd384bddb1b340516
stage_4_plan_promotion: ORDINARY_FAST_FORWARD / origin/codex/workbuddy-shell-v2=5cb3f585a0cddffbd823c785b1d39ebd1834c1df
stage_4_plan_review: V2-S4-PLAN-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_plan_ci: run 32337744225 / completed / success
stage_4_plan_closeout: PASS_ACCEPTED / dfd97f3d2e05a4c448448fc14514d1cfe76836e8 / tree 5eeb8a9337c5b38be60d3b0cef184b8898f2fedc
stage_4_plan_closeout_review: V2-S4-PLAN-CLOSEOUT-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_plan_closeout_ci: run 32338998075 / completed / success / head_sha=dfd97f3d2e05a4c448448fc14514d1cfe76836e8
stage_4_planning: PASS_ACCEPTED
stage_4_implementation_authorization_formal_result: 2c3d87bedfa4a3cef3cfd952641199300f2715dc
stage_4_implementation_authorization_formal_tree: c196dbf6b094cad05076d01ac2496f7425cf6fac
stage_4_implementation_authorization_review: V2-S4-IMPLEMENTATION-AUTHORIZATION-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_implementation_authorization_ci: run 32340096961 / completed / success / head_sha=2c3d87bedfa4a3cef3cfd952641199300f2715dc
stage_4_implementation_authorization: FORMALLY_GRANTED_TO_V2-S4-IMPLEMENTATION-BUILDER1 / START_BLOCKED_UNTIL_SIX_AUTHORITY_SYNC_APPROVE_AND_ORDINARY_FAST_FORWARD
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
final_package_gate_authorization: NOT_GRANTED
current_task: V2-S4-IMPLEMENTATION-AUTHORITY-SYNC-FIX1
current_task_status: WORKTREE_RESULT_READY_FOR_REVIEW
next_authorized_task: V2-S4-IMPLEMENTATION-AUTHORITY-SYNC-REVIEW1 / ZERO_WRITE_ONLY
authority_sync_effective_only_if: V2-S4-IMPLEMENTATION-AUTHORITY-SYNC-REVIEW1 APPROVE / P0=0 / P1=0 / P2=0 AND six-authority sync candidate ordinary-fast-forwarded as formal head
effective_stage_4_implementation_authorization: GRANTED_TO_V2-S4-IMPLEMENTATION-BUILDER1_ONLY
effective_next_authorized_task: V2-S4-IMPLEMENTATION-BUILDER1
effective_stage_4_launcher_authorization: NOT_GRANTED
effective_stage_5_workbuddy_entry_authorization: NOT_GRANTED
effective_stage_6_status_result_relay_authorization: NOT_GRANTED
effective_final_package_gate_authorization: NOT_GRANTED
stage_3_to_6_scope_reduction: ACTIVE_REPLANNED_BOUNDARY
runtime_correction: REQUIRED_TOOLCHAIN_REFRESH_PASS_ACCEPTED
```

`709c8e880b144fa9e9be26e9feb5d776dd6025e2`完成了Stage 2必带工具链和Registration/Locator的真实临时证明；该历史事实不重开，也不再作为Stage 3输入。Stage 3实现已经独立审阅并正式推广为`a3f8959682d296301dc573c2835f8c705a52e8b2`，closeout `7c15aae4e77c579309312b21c79076f930970214`也已正式推广，因此Stage 3继续为`PASS_ACCEPTED`。

CI状态断言修复`e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3`已经位于正式分支，精确代码差异仅为`tests/workbuddy/test_repository_hygiene.py`中的两条Stage3状态断言；正式CI run `32218904419`为`completed/success`，输出`198 passed / 1 skipped`。第一次独立Reviewer结论保持为`INCOMPLETE / P0=0 / P1=0 / P2=0`，原因只有当时authority mismatch，代码差异无finding。正式分支在账本收口前前移属于治理偏差，本closeout只同步实时权威，不改写审查或Git历史。

CI状态断言closeout已在`26bfe60ab9da62797559eb9a459b8daa345f8d80`正式收口。Stage4规划最终结果`5cb3f585a0cddffbd823c785b1d39ebd1834c1df`已经`V2-S4-PLAN-REVIEW1`独立`APPROVE / P0=0 / P1=0 / P2=0`、正式CI run `32337744225 completed/success`并普通fast-forward；两轮历史`REQUEST_CHANGES`已经关闭。规划状态closeout也已由`V2-S4-PLAN-CLOSEOUT-REVIEW1`独立`APPROVE / P0=0 / P1=0 / P2=0`，并以`dfd97f3d2e05a4c448448fc14514d1cfe76836e8`、tree `5eeb8a9337c5b38be60d3b0cef184b8898f2fedc`正式推广，正式CI run `32338998075 completed/success`，因此`stage_4_planning=PASS_ACCEPTED`。实施授权已经`V2-S4-IMPLEMENTATION-AUTHORIZATION-REVIEW1`独立`APPROVE / P0=0 / P1=0 / P2=0`，并以`2c3d87bedfa4a3cef3cfd952641199300f2715dc`、tree `c196dbf6b094cad05076d01ac2496f7425cf6fac`普通fast-forward正式推广，正式CI run `32340096961 completed/success`。当前只允许`V2-S4-IMPLEMENTATION-AUTHORITY-SYNC-REVIEW1`零写审查六权威同步候选；只有其最终`APPROVE / P0=0 / P1=0 / P2=0`且候选普通fast-forward后，下一任务才为`V2-S4-IMPLEMENTATION-BUILDER1`。真实生产Launcher运行、Stage5、Stage6及最终Package Gate仍为`NOT_GRANTED`。

仓库卫生历史基线`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`为tracked精确33且等于当时固定白名单；Stage 3按已审五路径新增两个受控文件并同步更新卫生断言后，正式结果`a3f8959682d296301dc573c2835f8c705a52e8b2`为tracked精确35。没有恢复任何已清理内容。

## 阶段3至阶段6建设与交付顺序

```text
Stage 3: Runtime Preparation on Demand
Stage 4: Session Launcher
Stage 5: WorkBuddy Entry
Stage 6: Status and Result Relay
```

该顺序只表示建设、审阅和正式交付顺序，不是最终用户运行时的调用顺序。每个阶段都从当时最新的`origin/codex/workbuddy-shell-v2`精确提交开始，经单一有界Builder、独立只读Reviewer、普通非force fast-forward推广、远端临时分支清理和本地worktree关闭后，下一阶段才可接管。规划接受、Builder提交或Reviewer批准均不等于正式交付。

新的固定关系是：阶段4基础调用依赖阶段2必带工具链；阶段3有界探测Remotion和HyperFrames并报告事实，缺失/不兼容时由WorkBuddy询问用户，只有逐能力批准才集成。拒绝或暂缓不阻塞其他已有/基础能力。OpenMontage决定生产使用哪项实际可用能力；Shell不选渲染器、不自动重放原业务请求。

阶段3至阶段6共同约束：每阶段最多一个公共入口；没有可验证输入或直接下游消费者时必须零代码退出；不得预建通用Runtime管理器、CLI/MCP镜像、任务平台、后台服务、第二Agent Host、生产FSM或状态数据库。WorkBuddy是唯一运行中的Agent；所谓OpenMontage Agent只能指WorkBuddy读取已验证Package Guide后承担的逻辑生产角色。

## 阶段授权与零代码出口

```text
stage_3_scope: bounded detect Remotion and HyperFrames; report PRESENT/MISSING/INCOMPATIBLE; integrate only explicitly approved missing/incompatible items under managed DataRoot; decline/defer is SKIPPED/NOT_INTEGRATED; never detect/download Python/FFmpeg/Node
stage_3_public_entry: prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)
stage_3_result_set: DETECTION_REPORT / CONSENT_REQUIRED / INTEGRATED / SKIPPED / BLOCKED
stage_3_capability_fact_set: PRESENT / MISSING / INCOMPATIBLE / NOT_INTEGRATED
stage_3_zero_write_result: DETECTION_REPORT / CONSENT_REQUIRED / SKIPPED / BLOCKED(reason_code=INVALID_DEFINITION_OR_TARGET)
stage_3_download_policy: OPTIONAL_CAPABILITY_APPROVED_MAINLAND_CHINA_MIRRORS / NO_AUTOMATIC_OVERSEAS_FALLBACK
stage_3_definition_authority: APPROVED_OPENMONTAGE_CAPABILITY_DEFINITION / INDEPENDENT_OF_PACKAGE_IDENTITY_METADATA
stage_3_product_code_paths: golden_key_openmontage_workbuddy/runtime_prepare.py + export-only golden_key_openmontage_workbuddy/__init__.py + tests/workbuddy/test_runtime_prepare.py
stage_3_acceptance_infrastructure_paths: tests/workbuddy/test_repository_hygiene.py + .github/workflows/ci.yml
stage_3_accepted_builder_exact_allowlist_rule: exactly the 3 product paths plus the 2 acceptance-infrastructure paths; no other path; the latter only updates fixed tracked/API/source assertions and the one CI pytest command
stage_4_scope: 基础固定工具调用接受阶段2必带工具链事实；只在PackageToolDefinitionV1声明required_local_capabilities时接受完整approved capability definition与未改写original Stage3 fact并按managed/explicit/PATH原始source独立重验；Provider配置与本地能力证据分离；阶段4不硬编码Provider/Runtime、不查询registry、不自行安装、不启动第二Agent、无任意Shell、无自动重试。
stage_5_scope: 用户实际运行起点；只保留一种真实WorkBuddy显式入口，literal user_message不变，技术控制独立。
stage_6_scope: 直接转交Runtime计划/准备事实与Launcher回执；仅有真实格式转换缺口时才允许独立实现；不解释、不安装、不重试。
stage_6_zero_code_exit: STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE
```

上述范围定义产品边界，本身不单独产生实现授权；当前实施授权及接管条件只以文件顶部live authority为准。任何需要阶段3扫描盘符、发现/下载/替换包内Python/FFmpeg/Node、一次安装全部可选能力、选择渲染引擎/版本、使用未批准海外默认源或覆盖外来目录，阶段4启动第二Agent、解析意图或调度任务，阶段5建立第二聊天Agent，阶段6解释Artifact或自动重试的方案，必须停止并返回`STOPPED_SCOPE_EXPANSION`。

## 阶段3重新规划合同

上一版阶段3执行包、`prepare_runtime_on_demand(...)`签名，以及Package绑定能力元数据、Registration绑定和零能力零代码模型全部`SUPERSEDED`，不得交给Builder。新阶段3只做Remotion和HyperFrames的有界探测、事实报告、零下载计划、逐能力用户决定和批准项受管集成。

### 历史实现启动Gate（已满足并消费）

以下两项是Stage 3实现前的历史Gate，现已满足并由正式结果消费：

1. 当前五文档产品模型纠偏完成独立审阅，并正式fast-forward推广到`origin/codex/workbuddy-shell-v2`；
2. `TASK-REGISTER.md`基于当时最新正式Git对象明确授予精确Builder基线、五文件允许路径、直接测试和独立Reviewer范围。

不得再增加Package、Registration、Package绑定能力元数据、task-only登记验证或Stage 5输入Gate。授权前缺一项时零代码停止；不得创建占位实现、通用Runtime框架或测试假合同。

### 唯一输入合同

`capability_definitions`中Remotion和HyperFrames每项最少固定为：

```text
capability: remotion | hyperframes
definition_sha256
version
verified_entrypoint
approved_mainland_sources
assets: filename + size + sha256 + license + managed_target
explicit_registered_or_configured_candidate_paths: optional
normal_command_name: optional
```

能力定义来自批准的OpenMontage能力定义权威。调用方不能提供定义外URL、任意命令、任意安装目录、盘符扫描或系统软件枚举请求。`user_decisions`只能对精确`capability + definition_sha256 + plan_sha256`表达`approve/decline/defer`；任一事实变化使旧批准失效。literal `user_message`永远不进入本接口。

### 固定执行步骤

1. **定义验证**：验证两项批准OpenMontage能力定义的版本、入口、批准大陆来源、大小、SHA-256、许可证和受管目标；拒绝任意URL、命令和目标注入。
2. **有界探测**：只检查受管DataRoot目标、明确登记/配置的候选路径和正常命令解析；禁止遍历盘符、系统软件清单、全局npm状态和猜目录。
3. **事实报告**：分别报告Remotion和HyperFrames的`PRESENT/MISSING/INCOMPATIBLE`、入口、版本和来源。存在则复用；缺失或不兼容不是失败。
4. **零下载计划**：为每个缺失/不兼容项返回来源、版本、hash、大小、许可证、受管目标、总下载量和`plan_sha256`，状态`CONSENT_REQUIRED`；不得下载或写入。
5. **用户决定**：WorkBuddy逐项询问。`decline/defer`返回`SKIPPED/NOT_INTEGRATED`，不影响其他能力或基础能力。
6. **授权复核与集成**：仅对仍匹配`capability + definition_sha256 + plan_sha256`的`approve`项，使用阶段2必带Node/npm/npx从批准大陆来源下载到同卷staging，核验后发布到`<DataRoot>/Runtime/Composition/<capability>/<definition_sha256>/`。
7. **失败处理**：外来目标保留并fail closed；hash、大小、许可、来源、命令或探针失败即回滚，清除staging和任务临时文件，不修改系统PATH、注册表或全局npm，不自动海外回退。
8. **最终报告**：重新探针批准项，确认未批准能力和必带Python/FFmpeg/Node零变化后返回`INTEGRATED`及能力、定义、runtime root、入口、版本和资产证据。

### 后续阶段交接

- 阶段4基础调用只消费阶段2必带工具链事实；只有固定工具定义声明本地能力要求时才接收完整批准定义与未改写原始Stage3 fact，并按managed closed-tree、explicit定义资产、PATH entrypoint asset的原始source语义独立重验。当前Stage3的Remotion/HyperFrames定义与事实只是现有来源；Provider配置不是Stage3能力证据，Launcher不能自行安装或路由。
- 阶段5拥有用户对话、计划展示、明确同意和真实WorkBuddy继续动作；真实验收优先同任务继续，不能时固定提示“继续刚才的任务”；技术控制与用户原话分离。
- 阶段6优先原样转交探测、`CONSENT_REQUIRED`、`INTEGRATED`、`SKIPPED`、`BLOCKED`和Launcher事实；不安装、不解释Artifact、不自动重试。
- Shell不得声称已无缝继续；阶段5真实WorkBuddy测试证明同一任务可继续后才允许该说法，否则由WorkBuddy要求用户回复“继续刚才的任务”。

### 已接受的最小文件和交付

已接受产品实现只新增`golden_key_openmontage_workbuddy/runtime_prepare.py`，最小编辑`golden_key_openmontage_workbuddy/__init__.py`导出唯一入口，并新增`tests/workbuddy/test_runtime_prepare.py`；同一Builder只为验收同步编辑了`tests/workbuddy/test_repository_hygiene.py`和`.github/workflows/ci.yml`。正式结果保持单一入口、稳定结果集、有界探测/计划/用户决定/集成事实及直接测试证据；它不是Installer、最终Package、WorkBuddy入口、Launcher或视频E2E证明。

## 已接受对象与证据边界

```text
immutable_v1_code_baseline: 2a2bf09832d558388dc2816c54b32a2dce4aa607
stage_1_reviewed_commit: 041c6600dc8eb9094b5c93cb4a4ed088894578af
stage_1_integrated_boundary: fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9
stage_1_reviewer_task: 01a004a6-aab1-7992-abe0-6dcbe8490a71
stage_1_reviewer_verdict: APPROVE / P0=0 / P1=0 / P2=0
stage_2_contract_commit: 5dd144e40ff1bf8682c8b43ac9973e40fc0be946
stage_2_final_implementation_commit: ab1eddf474233859c6a3b32056a503f82ecdc117
stage_2_gate_prep_commit: 104fe684c0bae6604c278fcf756579700bd8e1e0
stage_2_integration_commit: ca6e93b7da108732f2034239da340a986ba3da3a
stage_2_final_reviewer_task: 01a005c3-692c-7761-9f11-45e178c0d599
stage_2_final_reviewer_verdict: APPROVE / P0=0 / P1=0 / P2=0
stage_2_integration_reviewer_task: 01a00606-a1d3-7ab3-ab75-8d16efd064fa
stage_2_integration_reviewer_verdict: APPROVE / P0=0 / P1=0 / P2=0
stage_1_stage_2_consolidation_audit: 01a00617-e037-72a3-b1e5-d88b3d0be19f / APPROVE
repository_hygiene_wave_a_result: 830d44ab7b910e20bfc9093bf2c505850860880a
repository_hygiene_wave_a_closeout: 385a20bbff9624703682eecba3b38fc3c6d2d6b9
repository_hygiene_sequence_authority: cf04dc20d428233e2d328578a1e5d58ebaca2feb
repository_hygiene_wave_b_result: a9e660d5f059a2b8e20cd35dde761b941811494d
repository_hygiene_wave_b_ci_scope_fix: 2f70e426d52a2ea939f5b00e276f9da6bc108a69
repository_hygiene_final_ci_freeze: 2e4858bdd5142a8f041d708bdb385a197c4436a9
repository_hygiene_wave_c_result: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
```

刷新前的旧Stage2对象只证明早期Package的Python登记合同；当前已接受对象另行证明完整必带工具链Registration/Locator实现及一次真实临时Package验证。两代证据都不证明最终Release仍然存在，也不证明生产安装/登记、Installer、Runtime、Launcher、真实WorkBuddy、Provider、SaaS、网络或媒体E2E。阶段3至阶段6不得读取未验证Package Guide、扫描磁盘猜测对象，或把技术控制词写入literal `user_message`。

老项目可迁移证据：`347272c`固定包内便携Python；`899592d`固定完整Runtime、hash、许可、DataRoot和大陆PyPI/npm/Node/浏览器镜像；`639978d`增加`managed`、`registered_host`、`PATH_host`、`missing`发现与missing-only准备。旧锁中的“FFmpeg 9.0 essentials”只提供候选来源标签；本次冻结URL与hash对应二进制实际报告`9.0.1-essentials_build`。它不形成阶段3下载授权，也不得扩展为其他可选能力的海外回退权。
