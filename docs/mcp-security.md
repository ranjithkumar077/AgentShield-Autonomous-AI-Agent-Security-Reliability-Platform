# MCP Security

AgentShield can protect MCP tool calls.

## Flow

```text
MCP Client
    │
    ▼
AgentShield
    │
    ├── Authenticate
    ├── Authorize
    ├── Normalize
    ├── Detect threats
    ├── Calculate risk
    ├── Apply policy
    └── Request approval
    │
    ▼
MCP Server
```

## Tool Classification

Examples:

```text
search_*    → search
get_*       → read
list_*      → read
create_*    → create
update_*    → update
delete_*    → delete
execute_*   → execute
```

Unknown operations should not automatically receive unrestricted access.

## Security Requirement

An MCP tool call must not be forwarded until AgentShield has completed its security evaluation.
