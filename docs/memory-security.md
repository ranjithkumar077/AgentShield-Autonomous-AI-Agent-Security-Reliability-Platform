# Memory Security

## Secure Agent Memory

AgentShield treats long‑term agent memory as a security boundary.

### Threat

A malicious actor could write dangerous instructions into memory which would later be injected into the model context.

### Protection Layers

1. **Write Check** – Incoming memory writes are scanned by the threat detector. Suspicious content is marked `REVIEW_REQUIRED`.
2. **Read Check** – When memory is retrieved for model context, only entries marked `TRUSTED` are included automatically. `REVIEW_REQUIRED` entries require explicit approval.
3. **Delete Check** – Deleting memory entries also goes through authorization and audit.

### Trust Levels

| Level | Description |
|---|---|
| `UNTRUSTED` | New memory writes. Must be evaluated before use. |
| `REVIEW_REQUIRED` | Potentially dangerous; requires human review before being promoted. |
| `TRUSTED` | Cleared by policy and can be safely used in model context |

### API Endpoints

- `POST /api/memory` – Write memory (subject to write check)
- `GET /api/memory?agent_id=<id>` – List memory (filter by trust level)
- `DELETE /api/memory/{id}` – Delete memory (authorization required)

### Best Practices

- Keep sensitive secrets out of memory; use secure credential stores.
- Regularly audit `REVIEW_REQUIRED` entries.
- Apply role‑based access control to memory operations.
