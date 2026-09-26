# AgentShield Architecture

## Overview

AgentShield is designed as a security control plane for AI agents.

The platform separates:

1. Identity
2. Authorization
3. Security analysis
4. Execution
5. Audit
6. Observability

## High-Level Architecture

```text
                         USER
                           │
                           ▼
                    React Dashboard
                           │
                           ▼
                       FastAPI
                           │
                           ▼
                  Authentication
                           │
                           ▼
                       RBAC
                           │
                           ▼
                    Agent Runtime
                           │
                           ▼
                 Security Gateway
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        Normalizer      Threats       Risk
              │            │            │
              └────────────┼────────────┘
                           ▼
                     Policy Engine
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           ALLOW         BLOCK       APPROVAL
              │                          │
              │                     Human Review
              │                          │
              └──────────────┬───────────┘
                             ▼
                       Tool / MCP / API
                             │
                             ▼
                         Audit Log
                             │
                             ▼
                       PostgreSQL
```

## Core Principle

The security gateway must execute before the tool.

```text
Agent
  │
  ▼
Security Gateway
  │
  ├── BLOCK
  │
  ├── APPROVAL_REQUIRED
  │
  └── ALLOW
           │
           ▼
       Tool execution
```

A blocked action must never reach the underlying tool.

## Control Plane

The control plane contains:

* authentication
* authorization
* policies
* approvals
* configuration
* audit
* observability

## Execution Plane

The execution plane contains:

* agents
* tools
* MCP servers
* external APIs
* databases
* filesystem operations

AgentShield separates these concerns so that security policy is not implemented inside individual tools.
