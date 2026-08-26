---
name: golden-key-openmontage
description: Send an ordinary user's literal request through the installed Golden Key OpenMontage WorkBuddy entry.
---

# Golden Key OpenMontage WorkBuddy entry

WorkBuddy remains the sole Agent and the sole user conversation entry. Send the
user's literal message to the installed fixed entry and return its receipt.

The fixed entry owns package lookup, release binding, validation, lifecycle
state, and receipt delivery. Do not ask the user or model for commands, JSON,
paths, hashes, environment names, evidence records, or internal controls. Do
not create another Agent, Skill, router, MCP surface, retry/replay path,
Provider choice, renderer choice, media workflow, consent decision, or recovery
decision. Those decisions remain outside this Shell adapter.

GOLDEN_KEY_WORKBUDDY_SKILL_IDENTITY=<installer:skill_identity>
GOLDEN_KEY_WORKBUDDY_RELEASE_IDENTITY=<installer:release_identity>
