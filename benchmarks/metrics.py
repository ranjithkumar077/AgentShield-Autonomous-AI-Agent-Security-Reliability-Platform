# metrics.py
"""Utility functions for evaluating benchmark results.

Provides simple metric calculations such as accuracy, recall, precision,
latency statistics, and token usage aggregation. Designed to be framework-
agnostic so it can be reused across different LLM providers.
"""

from typing import List, Dict, Any

def accuracy(predictions: List[Any], references: List[Any]) -> float:
    """Return the fraction of predictions that exactly match the references."""
    if not predictions:
        return 0.0
    correct = sum(p == r for p, r in zip(predictions, references))
    return correct / len(predictions)

def precision_recall_f1(true_positives: int, false_positives: int, false_negatives: int) -> Dict[str, float]:
    """Calculate precision, recall, and F1 score from counts."""
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) else 0.0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) else 0.0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0.0
    return {"precision": precision, "recall": recall, "f1": f1}

def latency_stats(latencies_ms: List[float]) -> Dict[str, float]:
    """Return basic latency statistics (mean, median, p95)."""
    if not latencies_ms:
        return {"mean": 0.0, "median": 0.0, "p95": 0.0}
    sorted_lat = sorted(latencies_ms)
    n = len(latencies_ms)
    mean = sum(latencies_ms) / n
    median = sorted_lat[n // 2] if n % 2 == 1 else (sorted_lat[n // 2 - 1] + sorted_lat[n // 2]) / 2
    p95 = sorted_lat[int(0.95 * n) - 1]
    return {"mean": mean, "median": median, "p95": p95}

def token_usage(stats: List[Dict[str, int]]) -> Dict[str, int]:
    """Aggregate token usage across a list of request statistics.

    Each dict is expected to contain ``'prompt_tokens'`` and ``'completion_tokens'``.
    """
    total_prompt = sum(s.get("prompt_tokens", 0) for s in stats)
    total_completion = sum(s.get("completion_tokens", 0) for s in stats)
    return {"prompt_tokens": total_prompt, "completion_tokens": total_completion, "total_tokens": total_prompt + total_completion}

__all__ = ["accuracy", "precision_recall_f1", "latency_stats", "token_usage"]
