# Observability

AgentShield exports Prometheus metrics for request rates, latency, and security decisions.

## Metrics

- `agentshield_requests_total` – Counter for total incoming requests.
- `agentshield_request_duration_seconds` – Histogram of request latency.
- `agentshield_decisions_total{decision="allow"}` – Counter for decisions of each type.
- `agentshield_llm_usage_total` – Counter for LLM tokens used.

## Setup

The FastAPI app mounts `/metrics` automatically when `prometheus_client` is installed.

```python
from prometheus_client import make_asgi_app
app.mount("/metrics", make_asgi_app())
```

Grafana dashboards can be built on top of these metrics.
