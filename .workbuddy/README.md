# WorkBuddy project configuration

This directory is a consumer-owned placeholder for the WorkBuddy integration.

- The current path is **Skill-first**: import `workbuddy-skill/golden-key-openmontage` and let WorkBuddy remain the only Agent.
- No active repository-level `mcp.json` is shipped before W4 packaging. The W2 real WorkBuddy comparison passed and fixed MCP as **optional**: the direct CLI remains the canonical fallback, while local stdio MCP adds structured Schema discovery and avoids shell command construction.
- WorkBuddy owns the conversation-model configuration. Golden Key production Provider references are generated separately under `D:/WorkBuddyData/Config`; this directory never stores credential values.
- Direct CLI long tasks use `golden-key-workbuddy task submit/status/run/cancel/recover` and persist under `D:/WorkBuddyData/Jobs`. Queued tasks can be cancelled; running blocking Tools are explicitly not claimed cancelable, and interrupted tasks are failed without automatic retry.
- Run `golden-key-workbuddy doctor --data-root D:\WorkBuddyData --create-dirs` before later adapter work.

Current status is Pre-Alpha. This directory is not evidence that installation or real WorkBuddy acceptance has passed.
