# Threat Model

This document outlines the potential threats against AgentShield and the mitigations applied.

## Threat Categories

- **Prompt Injection** – Malicious prompts that cause the LLM to generate unsafe actions.
- **Secret Leakage** – Accidental exposure of API keys, tokens, or private data.
- **Tool Abuse** – Using allowed tools to perform unintended operations.
- **MCP Attack** – Hijacking the Model‑Control‑Plane communication.
- **Memory Poisoning** – Writing malicious data into the agent's long‑term memory.

## Mitigations

| Threat | Mitigation |
|--------|------------|
| Prompt Injection | Input sanitization, LLM‑based threat detection, policy checks |
| Secret Leakage | Secret detection, redaction, audit logging |
| Tool Abuse | Action normalization, risk scoring, RBAC |
| MCP Attack | Secure gateway, authentication, request signing |
| Memory Poisoning | Write/Read checks, classification of memory trust levels |

For a deeper dive see the security model and the threat‑detection components.
