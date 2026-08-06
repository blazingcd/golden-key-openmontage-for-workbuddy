# WorkBuddy project configuration

This directory is a consumer-owned placeholder for the WorkBuddy integration.

- The current path is **Skill-first**: import `workbuddy-skill/golden-key-openmontage` and let WorkBuddy remain the only Agent.
- No active `mcp.json` is shipped in W1. The **MCP decision Gate** in W2 compares direct local execution with a deterministic local stdio adapter before MCP is made default, optional, or omitted.
- WorkBuddy owns the conversation-model configuration. Golden Key production Provider references are generated separately under `D:/WorkBuddyData/Config`; this directory never stores credential values.
- Direct CLI long tasks use `golden-key-workbuddy task submit/status/run/cancel/recover` and persist under `D:/WorkBuddyData/Jobs`. Queued tasks can be cancelled; running blocking Tools are explicitly not claimed cancelable, and interrupted tasks are failed without automatic retry.
- Run `golden-key-workbuddy doctor --data-root D:\WorkBuddyData --create-dirs` before later adapter work.

Current status is Pre-Alpha. This directory is not evidence that installation or real WorkBuddy acceptance has passed.
