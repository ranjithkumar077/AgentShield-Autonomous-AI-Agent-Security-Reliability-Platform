# run_benchmark.py
"""Entry point to execute the AgentShield benchmark suite.

This script ties together the benchmark runner and the reporting utilities.
It can be invoked directly:

    python -m benchmarks.run_benchmark

The script will:
  1. Execute all benchmark tests via `benchmarks.runner.run_all()`.
  2. Generate a concise JSON‑compatible report using `benchmarks.report.generate_report`.
  3. Print the report to stdout.
"""

from benchmarks.runner import run_all
from benchmarks.report import generate_report

def main() -> None:
    """Run the full benchmark suite and output a summary report."""
    results = run_all()
    summary = generate_report(results)
    print(summary)

if __name__ == "__main__":
    main()
