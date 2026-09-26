# API Reference

This document provides an overview of the REST API endpoints exposed by AgentShield.

## Authentication

All endpoints require a valid JWT token in the `Authorization: Bearer <token>` header.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check endpoint |
| GET | `/metrics` | Prometheus metrics |
| POST | `/evaluate` | Evaluate a tool request against security policies |
| GET | `/audit` | Retrieve audit logs |
| ... | ... | ... |

See the OpenAPI spec at `/openapi.json` for the full list.
