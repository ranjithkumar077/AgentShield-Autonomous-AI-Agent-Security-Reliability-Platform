"""Generate reports for the adversarial test suite.

Writes a JSON file with the raw results and a Markdown file summarising
pass/fail statistics and per‑case details.
"""

import json
from pathlib import Path

RESULT_DIR = (Path(__file__).resolve().parent / "results")


def write_report(report):
    # Ensure the results directory exists
    RESULT_DIR.mkdir(parents=True, exist_ok=True)

    json_path = RESULT_DIR / "adversarial_results.json"
    md_path = RESULT_DIR / "adversarial_report.md"

    # Write JSON report
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    # Build Markdown summary
    lines = [
        "# AgentShield Adversarial Test Report",
        "",
        "## Summary",
        "",
        f"- Total tests: {report['total']}",
        f"- Passed: {report['passed']}",
        f"- Failed: {report['failed']}",
        f"- Pass rate: {report['pass_rate']:.2%}",
        "",
        "## Test Results",
        "",
        "| ID | Category | Detected | Decision | Passed |",
        "|---|---|---|---|---|",
    ]
    for r in report["results"]:
        lines.append(
            f"| {r['id']} | {r['category']} | {r['detected']} | {r['decision']} | {r['passed']} |"
        )

    lines.extend(["", "## Failed Tests", ""])  # Section for failures
    failures = [r for r in report["results"] if not r["passed"]]
    if not failures:
        lines.append("No adversarial regression failures.")
    else:
        for f in failures:
            msgs = "; ".join(f["messages"])
            lines.append(f"- **{f['id']}**: {msgs}")

    md_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"JSON report: {json_path}")
    print(f"Markdown report: {md_path}")

if __name__ == "__main__":
    # When executed directly, expect a JSON report on stdin
    import sys
    data = json.load(sys.stdin)
    write_report(data)
