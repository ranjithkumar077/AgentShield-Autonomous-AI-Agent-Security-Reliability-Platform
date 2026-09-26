# Security Model

AgentShield uses multiple independent security layers.

## Layer 1 — Authentication

Determines who is making the request.

```text
JWT
```

## Layer 2 — Authorization

Determines whether the authenticated principal has permission.

```text
viewer
operator
security_admin
system_admin
```

## Layer 3 — Action Normalization

Converts different tool formats into a common representation.

```text
ToolAction
├── tool
├── operation
├── resource
├── scope
├── parameters
└── text
```

## Layer 4 — Threat Detection

Detects:

* prompt injection
* secrets
* sensitive information
* tool abuse
* MCP attacks
* memory poisoning

## Layer 5 — Risk Engine

Calculates a risk score.

Example:

```text
database read       → 10
database insert     → 60
database delete     → 90
database drop       → 100
```

## Layer 6 — Policy Engine

Maps actions to security decisions.

```text
ALLOW
BLOCK
APPROVAL_REQUIRED
```

## Layer 7 — Human Approval

Sensitive but potentially legitimate actions can require human review.

## Layer 8 — Audit

Security decisions are recorded for investigation and compliance.

## Layer 9 — Observability

Metrics and tracing provide operational visibility.

## Defense in Depth

No single detector should be treated as the complete security boundary.

```text
Authentication
      +
Authorization
      +
Threat Detection
      +
Risk
      +
Policy
      +
Approval
      +
Audit
```

Together these provide defense in depth.
