# OpenMontage Package Registration and Locator Contract

Status: `ACTIVE / REGISTRATION_ACTIVATION_LOCATOR_CONTRACT`

This document records the technical contract used by production code. It does not
define WorkBuddy's production decisions. WorkBuddy is the only harness Agent; the
Shell binds and locates an explicitly supplied Package and relays facts.

## 1. Scope and public API

Registration accepts one explicitly supplied, already assembled portable Package
archive and its installed PackageRoot. The Package contains the verified
OpenMontage resources and the private required toolchain. Registration does not
activate, launch, download, repair, interpret the Package Guide, select a
renderer/provider, or perform media production.

The public entries are:

```python
register_package(data_root, release_archive, release_sha256_sidecar,
                 package_root, package_python)
activate_package(data_root, expected_active_pointer_sha256_or_missing,
                  registration_sha256)
recover_active_package(data_root, expected_broken_pointer_sha256,
                       replacement_registration_sha256)
locate_active_package(data_root)
```

`package_python` remains a compatibility input and must equal the fixed Python
executable declared by the Package. Registration never activates; all candidate
validation completes before any registry object is published.

## 2. Schemas and fixed layout

```text
registration schema: golden-key-workbuddy-openmontage-package-registration-v2
registration owner: golden-key-workbuddy-shell-v2
active pointer schema: golden-key-workbuddy-active-openmontage-package-v1
active lock schema: golden-key-workbuddy-active-package-lock-v1
manifest schema: golden-key-workbuddy-portable-bundle-v2
core lock schema: 2
dependency lock schema: golden-key-workbuddy-python-core-dependencies-v1
manifest: BUNDLE-MANIFEST.json
core lock: GOLDEN_KEY_WORKBUDDY_CORE.lock.json
guide: AGENT_GUIDE.md
python: bootstrap/python/python.exe
python dependency lock: bootstrap/python/CORE-DEPENDENCIES.lock.json
ffmpeg: bootstrap/ffmpeg/bin/ffmpeg.exe
ffprobe: bootstrap/ffmpeg/bin/ffprobe.exe
node: bootstrap/node/node.exe
npm: bootstrap/node/npm.cmd
npx: bootstrap/node/npx.cmd
```

Manifest authority is exactly `invocation_model=direct_agent` and
`nested_agent_host_allowed=false`. Core Lock authority is the WorkBuddy direct
agent authority. The Shell does not become a second Agent.

Registry storage is fixed below the supplied DataRoot:

```text
DataRoot/State/PackageRegistration/v1/active.lock
DataRoot/State/PackageRegistration/v1/active.json
DataRoot/State/PackageRegistration/v1/objects/<registration_sha256>.json
```

## 3. Required toolchain binding

Manifest runtime roles are exactly `python`, `ffmpeg`, and `node`; required
toolchain entries are exactly those three plus `managed_files`. Every byte below
`bootstrap/python`, `bootstrap/ffmpeg`, and `bootstrap/node` is listed exactly once
in the managed-file inventory and Manifest, with owner
`workbuddy_required_toolchain`. The actual filesystem set must equal that inventory.

The private Python dependency lock has a closed root of schema version, Python
version, requirements, and packages. Each package records normalized-unique name,
version, and its managed `.dist-info/METADATA` path; all installed distributions
must be covered and their recorded Name/Version must match.

The registration object binds the PackageRoot, release archive/sidecar, Manifest,
Core Lock, Guide, `package_python`, and required toolchain identities (path,
canonical path, hash, size, version, source archive, dependency lock, FFmpeg/
ffprobe, and Node/npm/npx). The Manifest hash binds the managed-file closure.

## 4. Validation and fail-closed behavior

Registration, Activation, Recovery, and Locator validate the Release sidecar and
archive members, Manifest, Core Lock, Guide, managed files, canonical paths,
object hashes, active lock, CAS values, and atomic pointer bytes. They also:

- reject unknown or missing fields, duplicate JSON keys, non-canonical JSON,
  invalid Unicode, and invalid hashes/sizes;
- reject absolute, escaping, aliased, reserved-name, ADS, symlink, or reparse
  paths in the Package and required toolchain;
- reject missing, duplicate, unlisted, or extra managed toolchain files;
- hash and size-check every managed toolchain file and revalidate dependency
  metadata against the installed distributions;
- re-run complete validation from the immutable Registration during Locator reads.

Stable errors are:
`INPUT_INVALID`, `PATH_VIOLATION`, `OBJECT_MISSING`, `DUPLICATE`,
`IDENTITY_MISMATCH`, `HASH_MISMATCH`, `TAMPERED`, `ACTIVE_LOCK_BUSY`,
`ACTIVE_CAS_MISMATCH`, and `ATOMIC_WRITE_FAILED`.

## 5. Lifecycle and data protection

Registration creates an immutable content-addressed object only after validation,
using temporary bytes, flush/fsync, readback, and atomic publication. Existing
same-hash bytes may be reused; different bytes fail closed.

Activation takes the active lock, validates the current pointer and target
Registration, and atomically replaces the pointer only when the expected pointer
identity matches (or is `MISSING`). Recovery replaces only an explicitly
hash-locked broken pointer; a valid pointer is rejected by the recovery entry.
Deactivation/removal of an active pointer uses the same lock/CAS boundary and
leaves the Registration object and user DataRoot untouched until the Installer's
separate lifecycle operation is authorized.

Locator is read-only: it validates the fixed lock, active pointer, Registration,
PackageRoot, and toolchain, then returns the verified identity. It never repairs,
enumerates, downloads, launches, or chooses fallback. User files outside the
registry are not removed or rewritten by Registration/Activation/Locator.

## 6. Current product relation

R1 is `COMPLETE` and covers the final installed PackageRoot, private toolchain,
Manifest/Lock/binding, Shell lifecycle/release, and user-data protection. R2 is
`COMPLETE`: WorkBuddy `5.3.14` / Hy3 invoked the single Skill and Shell and returned
a concrete business reply plus LauncherReceipt. R2's
`INCOMPLETE / RESULT_POINTER_INVALID` only says that no video file was created;
video/result-pointer validation belongs to R3. R3 consumes a verified PackageRoot
through this unchanged Registration/Activation/Locator contract and does not add a
new registration protocol. R3 and the formal R4 closeout are `COMPLETE`; neither
changes this Registration/Activation/Locator contract.
