---
name: golden-key-openmontage
description: Run the Golden Key OpenMontage WorkBuddy Shell through one fixed, non-user-facing CLI transport adapter.
---

# Golden Key OpenMontage WorkBuddy entry

WorkBuddy is the sole running Agent and the sole user conversation entry. This
Skill is the repository's one source asset; its client installation path is
managed and opaque. It must not create a second Skill, Agent, MCP control plane,
router, fallback, retry, replay, Provider selector, or media workflow.

The Skill passes exactly one versioned JSON request to the fixed package-private
module invocation `-I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli`.
The request keeps the user's literal message separate from closed executor
controls and carries the complete PackageToolDefinitionV1 and complete approved
capability evidence. Secret environment values are read only by the adapter's
allowlisted process environment and never belong in the request or output.

The adapter calls the accepted Stage 4 `launch_session_tool(...)` exactly once
after bridge preflight. It emits one complete LauncherReceiptV1 JSON mapping
only after validation. Non-zero bridge exits are fail-closed and their stdout
must not be consumed. Stage 4 failure outcomes remain real receipts and use
transport exit 0; bridge input, asset/environment, and output failures use only
the closed 64/78/70 meanings.

Release-specific skill identity, owner, interpreter, module, schema, fixed argv,
and hashes are supplied by the final Installer/Package gate. Unresolved
placeholders, identity drift, guessed physical paths, or missing provenance
must fail closed and cannot be treated as a production installation.

## Installer stamping contract

The final Installer must replace every `<installer:...>` value below before this
asset can be installed. Any remaining placeholder, missing value, or identity
hash mismatch is a fail-closed `78` bridge result:

```text
GOLDEN_KEY_WORKBUDDY_SKILL_IDENTITY=<installer:skill_identity>
GOLDEN_KEY_WORKBUDDY_RELEASE_IDENTITY=<installer:release_identity>
GOLDEN_KEY_WORKBUDDY_AUTHORITY_OWNER=<installer:authority_owner>
GOLDEN_KEY_WORKBUDDY_BRIDGE_CONTRACT_ID=golden-key-workbuddy-skill-cli-bridge-v1
GOLDEN_KEY_WORKBUDDY_REQUEST_SCHEMA_ID=golden-key-workbuddy-skill-cli-request-v1
GOLDEN_KEY_WORKBUDDY_REQUEST_SCHEMA_SHA256=<installer:canonical_request_schema_descriptor_sha256>
GOLDEN_KEY_WORKBUDDY_RESULT_SCHEMA_ID=golden-key-workbuddy-launcher-receipt-v1
GOLDEN_KEY_WORKBUDDY_RESULT_SCHEMA_SHA256=<installer:canonical_result_schema_descriptor_sha256>
GOLDEN_KEY_WORKBUDDY_MODULE_NAME=golden_key_openmontage_workbuddy.workbuddy_entry_cli
GOLDEN_KEY_WORKBUDDY_MODULE_SHA256=<installer:module_sha256>
GOLDEN_KEY_WORKBUDDY_FIXED_ARGV=["-I","-m","golden_key_openmontage_workbuddy.workbuddy_entry_cli"]
GOLDEN_KEY_WORKBUDDY_FIXED_ARGV_SHA256=<installer:fixed_argv_sha256>
GOLDEN_KEY_WORKBUDDY_INTERPRETER_PATH=<installer:absolute_package_private_interpreter_path>
GOLDEN_KEY_WORKBUDDY_INTERPRETER_SHA256=<installer:absolute_interpreter_sha256>
```

The process environment is scrubbed before invocation. Its exact allowed name
set is the fourteen fixed names above, plus the request's sorted
`provider_environment_names`; on Windows only, the fixed non-Provider runtime
names `SystemRoot`, `WINDIR`, `COMSPEC`, `PATHEXT`, `TEMP`, and `TMP` are also
allowed so Stage 4 can construct its bounded child environment. POSIX adds no
implicit host environment names. The Skill must never inherit or forward the
entire host environment. Provider values are read only by the adapter and are
never placed in stdin, argv, stdout, stderr, hashes, lengths, logs, exceptions,
or receipts.

The request and result schema hashes are hashes of the module's canonical closed
schema descriptors (field set, version, UTF-8 canonical-wire rules, and the
closed outcome constraint), not hashes of a schema identifier string. The fixed
command is the literal argv `-I -m
golden_key_openmontage_workbuddy.workbuddy_entry_cli`; it is not generated from
the user message or controls.
