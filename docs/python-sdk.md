# Python SDK

## Installation

```bash
pip install agentshield
```

## Usage

```python
from agentshield import SecurityGateway

gateway = SecurityGateway()

result = gateway.evaluate(
    tool="database",
    operation="read",
    resource="users",
    scope="development",
    text="",
)

print(result.decision)  # ALLOW, BLOCK, or APPROVAL_REQUIRED
print(result.risk_score)
print(result.threats)
```

### Advanced Usage

```python
# Specify additional parameters
result = gateway.evaluate(
    tool="api",
    operation="call",
    resource="payment",
    scope="production",
    parameters={"amount": 100, "currency": "USD"},
    text="Process payment",
)
```

The SDK abstracts the HTTP calls to the FastAPI backend and provides typed response objects.
