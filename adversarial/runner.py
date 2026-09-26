"""Adversarial runner that loads cases, evaluates them against the security gateway, and returns results.

It relies on the existing ThreatAggregator from the backend security package.
"""

import json
import sys
import time
from pathlib import Path

# Ensure backend is on sys.path
ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from app.security.threats.aggregator import ThreatAggregator
from .assertions import assert_detected, assert_decision

CASE_DIR = Path(__file__).resolve().parent / "cases"

class AdversarialRunner:
    def __init__(self):
        self.threats = ThreatAggregator()

    def load_cases(self):
        cases = []
        for file_path in sorted(CASE_DIR.glob("*.jsonl")):
            with file_path.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    item = json.loads(line)
                    # Preserve source filename for reporting
                    item["_source"] = file_path.name
                    cases.append(item)
        return cases

    def evaluate(self, case):
        text = case.get("text", "")
        tool = case.get("tool", "unknown")
        operation = case.get("operation", "read")
        start = time.perf_counter()
        threats = self.threats.analyze(
            text=text,
            tool=tool,
            operation=operation,
            parameters={},
        )
        detected = any(t.detected for t in threats)
        score = max((t.score for t in threats if t.detected), default=0)
        decision = (
            "BLOCK" if score >= 90 else ("APPROVAL_REQUIRED" if detected else "ALLOW")
        )
        latency_ms = (time.perf_counter() - start) * 1000
        expected_detected = case.get("expected_detected")
        expected_decision = case.get("expected_decision")
        assertions = []
        if expected_detected is not None:
            assertions.append(assert_detected(detected, case["id"]))
        if expected_decision:
            assertions.append(assert_decision(decision, expected_decision, case["id"]))
        passed = all(a.passed for a in assertions)
        return {
            "id": case["id"],
            "category": case["category"],
            "source": case["_source"],
            "detected": detected,
            "threat_score": score,
            "decision": decision,
            "expected_detected": expected_detected,
            "expected_decision": expected_decision,
            "passed": passed,
            "latency_ms": round(latency_ms, 4),
            "messages": [a.message for a in assertions],
        }

    def run(self):
        cases = self.load_cases()
        results = [self.evaluate(c) for c in cases]
        passed = sum(r["passed"] for r in results)
        failed = len(results) - passed
        return {
            "total": len(results),
            "passed": passed,
            "failed": failed,
            "pass_rate": (passed / len(results) if results else 0),
            "results": results,
        }

if __name__ == "__main__":
    runner = AdversarialRunner()
    report = runner.run()
    print(json.dumps(report, indent=2))
