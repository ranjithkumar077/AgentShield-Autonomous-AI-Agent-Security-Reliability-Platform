# report.py
"""Generate a summary report for benchmark results.

The report aggregates accuracy, precision/recall/F1, latency statistics, and token usage.
It prints a human‑readable JSON summary to stdout.
"""

import json
from typing import List, Dict, Any

from .metrics import accuracy, precision_recall_f1, latency_stats, token_usage


def generate_report(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Compute aggregated metrics from a list of individual test results.

    Each result dict is expected to contain the keys:
        - "correct": bool indicating if the decision matches expectation
        - "latency_ms": float latency in milliseconds
        - "tokens": dict with "prompt_tokens" and "completion_tokens"
    """
    predictions = [r["correct"] for r in results]
    references = [True] * len(predictions)  # all expected to be correct for accuracy
    acc = accuracy(predictions, references)
    # Compute counts for precision/recall/f1 (treat correct as true positive)
    tp = sum(predictions)
    fp = len(predictions) - tp
    fn = 0  # since reference is always True in this simple benchmark
    prf = precision_recall_f1(tp, fp, fn)
    lat_stats = latency_stats([r["latency_ms"] for r in results])
    token_stats = token_usage([r["tokens"] for r in results])
    report = {
        "accuracy": acc,
        "precision": prf["precision"],
        "recall": prf["recall"],
        "f1": prf["f1"],
        "latency": lat_stats,
        "tokens": token_stats,
        "total_tests": len(results),
        "passed": tp,
        "failed": fp,
    }
    return report


def main():
    # Placeholder: read results from stdin JSON array
    import sys
    data = json.load(sys.stdin)
    report = generate_report(data)
    json.dump(report, sys.stdout, indent=2)

if __name__ == "__main__":
    main()
