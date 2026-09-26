# AgentShield
[![CI](https://github.com/ranjithkumar077/AgentShield/actions/workflows/ci.yml/badge.svg)](https://github.com/ranjithkumar077/AgentShield/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
> AI Agent Security, Policy Enforcement & Observability Platform

AgentShield is an open-source security gateway for AI agents.

It sits between an AI agent and the tools it wants to use and evaluates every sensitive action before execution.

```text
User
 │
 ▼
AI Agent
 │
 ▼
AgentShield
 ├── Authentication
 ├── Authorization
 ├── Action Normalization
 ├── Threat Detection
 ├── Risk Engine
 ├── Policy Engine
 ├── Human Approval
 ├── Audit Logging
 └── Observability
 │
 ▼
Tool / API / MCP Server
```

## Why AgentShield?

AI agents can:

* access databases
* modify files
* call APIs
* execute commands
* interact with MCP servers
* read and write memory
* use external services

Traditional application security does not always understand these agent-specific actions.

AgentShield provides a security control layer between the agent and its tools.

## Core Security Model

AgentShield follows:

```text
Tool Request
     │
     ▼
Authentication
     │
     ▼
Authorization
     │
     ▼
Action Normalization
     │
     ▼
Threat Detection
     │
     ▼
Risk Scoring
     │
     ▼
Policy Evaluation
     │
 ┌───┼───────────────┐
 ▼   ▼               ▼
ALLOW BLOCK   APPROVAL_REQUIRED
     │
     ▼
Execution
     │
     ▼
Audit + Observability
```

## Security Decisions

### ALLOW

The operation satisfies the configured security policy.

### BLOCK

The operation is considered unsafe and must not execute.

### APPROVAL_REQUIRED

The operation may be legitimate but requires human authorization before execution.

## Threat Detection

AgentShield detects:

* Prompt injection
* Secret leakage
* Sensitive data exposure
* Tool abuse
* MCP attacks
* Memory poisoning
* Suspicious tool arguments

## MCP Security

AgentShield can act as a security gateway between MCP clients and MCP servers.

```text
MCP Client
    │
    ▼
AgentShield MCP Gateway
    │
    ├── Threat Detection
    ├── Risk Analysis
    ├── Policy
    ├── Approval
    └── Audit
    │
    ▼
MCP Server
```

## Secure Agent Memory

AgentShield also protects agent memory against poisoning and unauthorized access.

Memory is classified as:

```text
UNTRUSTED
REVIEW_REQUIRED
TRUSTED
```

Untrusted or review-required memory is not automatically trusted as model context.

## Python SDK

Install:

```bash
pip install agentshield
```

Example:

```python
from agentshield import SecurityGateway

gateway = SecurityGateway()

result = gateway.evaluate(
    tool="database",
    operation="delete",
    resource="users",
)

print(result.decision)
```

## Dashboard

AgentShield includes a React dashboard for:

* Security events
* Risk levels
* Approval workflows
* Agent activity
* Observability
* Security metrics

## Technology

### Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic

### Frontend

* React
* Vite

### AI

* NVIDIA NIM
* OpenAI-compatible LLM gateway

### Security

* Prompt injection detection
* Secret detection
* Policy enforcement
* RBAC
* MCP security
* Secure memory

### Infrastructure

* Docker
* Docker Compose
* GitHub Actions
* Render

## Development

Clone:

```bash
git clone https://github.com/ranjithkumar077/AgentShield.git
cd AgentShield
```

Backend:

```bash
cd backend
python -m venv venv
```

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

## Testing

```bash
pytest -v
```

Security benchmark:

```bash
python -m benchmarks.run_benchmark
```

Adversarial tests:

```bash
python -m adversarial.run
```

Performance benchmark:

```bash
python -m performance.benchmark
```

## Security Philosophy

AgentShield does not depend on an LLM for every security decision.

Deterministic security rules handle obvious cases.

```text
Safe       → ALLOW
Dangerous  → BLOCK
Ambiguous  → APPROVAL_REQUIRED
```

LLM analysis can be used for ambiguous cases, but deterministic controls remain the foundation.

## Project Status

AgentShield is an active open-source project under development.

Current capabilities include:

* Security gateway
* Threat detection
* Agent runtime
* LLM gateway
* Database persistence
* Human approval
* React dashboard
* Observability
* MCP security
* Secure agent memory
* Benchmarking
* Adversarial testing
* Performance testing
* Docker
* CI/CD
* Production deployment
* RBAC
* Python SDK

## License

MIT

[![CI](https://github.com/ranjithkumar077/AgentShield/actions/workflows/ci.yml/badge.svg)](https://github.com/ranjithkumar077/AgentShield/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Roadmap

### Completed

- [x] Security gateway
- [x] Risk engine
- [x] Policy engine
- [x] Threat detection
- [x] Agent runtime
- [x] LLM gateway
- [x] PostgreSQL support
- [x] Human approval
- [x] React dashboard
- [x] Observability
- [x] MCP security
- [x] Secure memory
- [x] Benchmarking
- [x] Adversarial testing
- [x] Performance testing
- [x] Docker
- [x] CI/CD
- [x] Production deployment
- [x] Production security hardening
- [x] RBAC
- [x] Python SDK

### Planned

- [ ] Public package release
- [ ] Advanced policy editor
- [ ] External identity providers
- [ ] Distributed security event processing
- [ ] Additional agent frameworks
- [ ] Extended attack datasets
