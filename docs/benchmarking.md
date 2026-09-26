# Benchmarking

AgentShield includes a security evaluation framework.

## Categories

- Prompt injection
- Secret leakage
- Sensitive data
- Tool abuse
- MCP attacks
- Memory poisoning
- Policy decisions
- Authorization

## Metrics

The benchmark can measure:

- Accuracy
- Precision
- Recall
- F1
- False positive rate
- False negative rate
- Decision latency
- p50 latency
- p95 latency
- p99 latency

## Run

```bash
python -m benchmarks.run_benchmark
```

## Adversarial Testing

```bash
python -m adversarial.run
```

The objective is not only to demonstrate that AgentShield blocks known attacks, but also to measure false positives, false negatives, and performance.
