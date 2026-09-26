# Configuration

This guide explains how to configure AgentShield via environment variables and the `config.yaml` file.

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `AGENTSHIELD_PORT` | Port the FastAPI server listens on. | `8000` |
| `AGENTSHIELD_LOG_LEVEL` | Logging verbosity (`debug`, `info`, `warning`, `error`). | `info` |
| `AGENTSHIELD_DB_URL` | PostgreSQL connection string. | `postgresql://user:pass@localhost/agentshield` |
| `AGENTSHIELD_JWT_SECRET` | Secret key for signing JWTs. | *required* |
| `AGENTSHIELD_RISK_THRESHOLD` | Numeric risk score above which actions require approval. | `70` |

## `config.yaml`

```yaml
logging:
  level: info
  format: "% (asctime)s - %(name)s - %(level)s - %(message)s"

security:
  jwt_secret: "<replace-with-secure-secret>"
  risk_threshold: 70

postgres:
  url: "postgresql://user:pass@localhost/agentshield"

observability:
  prometheus_endpoint: "/metrics"
```

The file is loaded at startup; values from environment variables override the YAML.
