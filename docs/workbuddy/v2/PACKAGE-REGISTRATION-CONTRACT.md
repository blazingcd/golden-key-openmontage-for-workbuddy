# OpenMontage Package Registration and Locator Contract

状态：`STAGE_2_PASS_ACCEPTED / STABLE_CONTRACT`

## 1. Scope

This contract binds one explicitly supplied, already-installed, versioned OpenMontage Package to immutable local identity records and locates the single active Package. It does not install, download, execute, repair, or select a Package; it does not run the OpenMontage Agent.

The four public entries are:

```python
register_package(data_root, release_archive, release_sha256_sidecar, package_root, package_python)
activate_package(data_root, expected_active_pointer_sha256_or_missing, registration_sha256)
recover_active_package(data_root, expected_broken_pointer_sha256, replacement_registration_sha256)
locate_active_package(data_root)
```

`register_package` validates and writes an immutable registration but never activates it. `activate_package` performs an explicit CAS selection. `recover_active_package` replaces only an explicitly hash-locked broken pointer and rejects a valid pointer. `locate_active_package` is read-only and performs full identity revalidation; it never repairs, enumerates fallback objects, launches a process, accesses a network, or writes.

## 2. Identifiers and authority

```text
registration schema: golden-key-workbuddy-openmontage-package-registration-v1
registration owner: golden-key-workbuddy-shell-v2
active pointer schema: golden-key-workbuddy-active-openmontage-package-v1
active lock schema: golden-key-workbuddy-active-package-lock-v1
manifest schema: golden-key-workbuddy-portable-bundle-v1
lock schema: integer 2
manifest path: BUNDLE-MANIFEST.json
lock path: GOLDEN_KEY_WORKBUDDY_CORE.lock.json
guide path: AGENT_GUIDE.md
bundled Python path: bootstrap/python/python.exe
```

Manifest authority must be exactly:

```json
{"invocation_model":"direct_agent","nested_agent_host_allowed":false}
```

Lock authority must be exactly:

```json
{"consumer":"workbuddy","consumer_direct_official_sync_allowed":false,"invocation_model":"direct_agent","nested_agent_host_allowed":false,"official_openmontage_role":"reviewed_upstream_baseline_only","source":"golden-key-core"}
```

The external wire fields `core.contract_id`, `core.tag`, `core.source_commit`, `core.file_count`, `managed_core`, `golden-key-core`, `golden-key-workbuddy-callable-core-v1`, and `GOLDEN_KEY_WORKBUDDY_CORE.lock.json` retain their literal meanings. They do not mean the Golden Key SaaS Core. SaaS Core is outside this contract and outside Stage 2.

## 3. Registration identity

A Package Registration contains only these required root fields and rejects missing or unknown fields:

```text
schema_version, owner, contract_id, openmontage_release,
openmontage_commit, authority, release, package_root,
package_python, manifest, lock, guide
```

Nested shapes are also closed:

- `authority`: exact `manifest` and `lock` objects above.
- `release`: ZIP basename, archive SHA-256, and exact `.zip.sha256` sidecar basename.
- `package_python`: fixed relative path, canonical absolute path, SHA-256, positive size, version, fixed source `python.org_windows_embeddable_x64`, and source archive SHA-256.
- `manifest`: fixed relative/absolute path, schema, SHA-256, and positive size.
- `lock`: fixed relative/absolute path, integer schema 2, SHA-256, positive size, and bundle SHA-256.
- `guide`: fixed relative/absolute path, SHA-256, and positive size.

Strings are Unicode NFC and must not contain surrogate code points. SHA-256 is lowercase 64-hex; commit is lowercase 40-hex; sizes are JSON integers. Canonical object bytes are UTF-8 without BOM, sorted keys, compact separators, and exactly one trailing LF. The SHA-256 of those complete canonical bytes is the `registration_sha256` and object filename; it is not duplicated inside the object.

## 4. Validation chain

Registration accepts only explicit absolute existing paths and never expands `~`, searches a drive, consults environment defaults, or guesses the newest Package. It validates:

- the Release ZIP actual SHA against the sidecar, including an optional exact archive basename;
- exactly one safe Manifest and Lock archive member, byte-identical to the installed files;
- Manifest/Lock schema, closed authority shapes, and matching contract/release/commit identities;
- Lock bundle digest, unique safe inventory paths, Manifest `managed_core` ownership, file count, SHA, size, and every installed managed file;
- the fixed non-empty Guide through Manifest, Lock, registration identity, and installed bytes;
- the fixed bundled private Python declared by Manifest, including runtime role, owner, metadata, SHA, size, and canonical PackageRoot path;
- canonical PackageRoot and fixed child paths that do not escape through traversal, symlink/reparse resolution, Windows aliases, ADS, reserved device names, trailing dots, or trailing spaces.

Every later activation, recovery, and locate operation reloads the content-addressed object and revalidates its canonical bytes, filename hash, paths, Manifest, Lock, Guide, Python, and managed files. A lifecycle component may reclaim the Release archive after registration; Locator revalidates the frozen local identity and does not claim to re-fetch or revalidate a remote Release.

## 5. Storage, lock, CAS, and recovery

```text
<DataRoot>/State/PackageRegistration/v1/objects/<registration_sha256>.json
<DataRoot>/State/PackageRegistration/v1/active.json
<DataRoot>/State/PackageRegistration/v1/active.lock
```

Registration objects are content-addressed and immutable. Publication uses a same-directory temporary file, flush, `fsync`, readback, and atomic publication. Existing identical bytes are idempotent; conflicting bytes at the same hash path fail closed.

`active.lock` has fixed canonical identity bytes and persists as the lock identity file. It is created only when an empty registry is initialized; if registrations or a pointer exist, a missing or changed lock is tampering. Activation and recovery share a process guard and a kernel-level exclusive byte-0 lock, use one monotonic 5-second deadline with 0.05-second retries, re-read the lock in the critical section, and always release/close in `finally`.

Inside the same critical section, a writer reads the raw active pointer, compares its caller-supplied SHA-256 or literal `MISSING`, fully revalidates the explicit target registration, writes/flushes/`fsync`s/reads back a same-directory temporary pointer, rechecks raw pointer bytes, and uses `os.replace`. A stale expected value cannot overwrite another writer. Failure before replacement preserves the old pointer; Locator never reads temporary files.

Recovery requires the exact SHA-256 of an existing damaged pointer and an explicit fully valid replacement registration SHA. It never creates a registration, chooses a fallback, accepts a missing pointer, or replaces a valid pointer. Rollback is explicit activation of a named older valid registration; there is no time-based or directory-based selection.

## 6. Fail-closed errors

Stable error codes are:

```text
INPUT_INVALID
PATH_VIOLATION
OBJECT_MISSING
DUPLICATE
IDENTITY_MISMATCH
HASH_MISMATCH
TAMPERED
ACTIVE_LOCK_BUSY
ACTIVE_CAS_MISMATCH
ATOMIC_WRITE_FAILED
```

Missing objects, unknown or missing fields, duplicate JSON keys or inventory/archive paths, non-finite JSON, surrogate/NFC violations, tampered bytes, identity drift, unsafe paths, hash/size mismatch, lock damage, stale CAS, and atomic-write failures all reject without guessing or silently repairing. Even a registry with exactly one object is not a substitute for a missing active pointer.

## 7. Future consumers and message boundary

A future Launcher may only read the immutable mapping returned by `locate_active_package` to bind the exact PackageRoot, bundled Python, Guide, Manifest, Lock, Release, authority, and commit. This document does not implement or authorize the Launcher, Runtime preparation, WorkBuddy entry, or status/result relay.

The verified external Package Guide may be read only after successful Registration/Locator identity validation and only by the correct downstream session consumer. The Shell must not interpret that Guide as permission to direct production.

`user_message` remains the user's literal business request, materials, facts, authorizations, and desired result. Package identity, paths, Python, cwd, commands, retries, stop conditions, and evidence collection remain separate `executor_controls`; the two must never be concatenated.

## 8. Implementation evidence

`golden_key_openmontage_workbuddy/package_registration.py` is the accepted implementation. `tests/workbuddy/test_package_registration.py` is the implementation evidence for closed schemas, Release/Manifest/Lock/Python/Guide identity, canonical encoding, path safety, missing/duplicate/surrogate/tamper/drift/hash failures, immutable publication, active lock/CAS concurrency, recovery, rollback, and read-only Locator behavior.

That test evidence does not prove installation, Runtime, Launcher, real WorkBuddy, OpenMontage production, Provider, SaaS, network, media, or business E2E.
