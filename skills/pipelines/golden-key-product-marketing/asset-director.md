# Asset Director — Golden Key Product Marketing

Build the schema-valid `asset_manifest` from approved scene and proposal artifacts. Every
existing asset records provenance and exact source ranges in metadata; every generated asset
records provider/model when bound, prompt, negative prompt, reference frame, protected
elements, seed when available, cost, disclosure, acceptance, and fallback.

Do not execute a generation slot simply because intake or benchmark metadata mentions it.
Generate only approved capability demands that solve a named shot problem. Sample expensive,
identity-sensitive, logo/text-sensitive, or service-representation-sensitive work before
batch generation.

Resolve narration/source speech, subtitles, BGM, natural sound, SFX, fonts, and overlays as
one approved audio/text asset system. Unavailable providers create an explicit fallback or
blocker; they do not erase a content decision.

Generated outputs later enter `asset_manifest.metadata.generated_assets` with request/receipt
references, output path/hash, lineage, review status, and the scene/shot they satisfy.

Resolve every selected `source_asset_ref` to its exact existing `source_path`, source hash,
source range, and persisted audio-analysis evidence through the supplied material query result
or snapshot. An asset ID without this mapping is not executable. Request a missing mapping
through the material-query contract once; never invent it.
