# policy_engine.py
"""Policy engine that loads security policies from YAML and evaluates requests.

The policies are defined in `backend/app/config/default.yaml`. Each entry contains
`tool`, `operation`, `resource`, `scope`, `risk_score`, `decision`, and `reason`.

The engine looks for the most specific matching policy (exact match on all four
fields). If none is found, it falls back to a default "allow" with low risk.
"""

import os
import yaml
from pathlib import Path
from typing import List, Dict

from .decision import SecurityDecision


class PolicyEngine:
    """Load policies from a YAML file and evaluate incoming requests.

    Example usage:
        engine = PolicyEngine()
        decision = engine.evaluate(
            tool="database",
            operation="delete",
            resource="users",
            scope="production",
        )
    """

    def __init__(self, config_path: str | os.PathLike | None = None):
        # Resolve default path relative to project root
        if config_path is None:
            base_dir = Path(__file__).resolve().parents[3]  # backend/app
            config_path = base_dir / "config" / "default.yaml"
        self.config_path = Path(config_path)
        self.policies = self._load_policies()

    def _load_policies(self) -> List[Dict]:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Policy file not found: {self.config_path}")
        with open(self.config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data.get("policies", [])

    def evaluate(
        self,
        tool: str,
        operation: str,
        resource: str,
        scope: str,
    ) -> SecurityDecision:
        """Return a :class:`SecurityDecision` based on the loaded policies.

        The first policy that matches **all** four fields is returned. If no
        policy matches, a permissive decision with low risk is produced.
        """
        for pol in self.policies:
            if (
                pol.get("tool") == tool
                and pol.get("operation") == operation
                and pol.get("resource") == resource
                and pol.get("scope") == scope
            ):
                return SecurityDecision(
                    tool=tool,
                    operation=operation,
                    resource=resource,
                    scope=scope,
                    risk_score=pol.get("risk_score", 0),
                    decision=pol.get("decision", "allow"),
                    reason=pol.get("reason", "matched policy"),
                )
        # Default permissive policy
        return SecurityDecision(
            tool=tool,
            operation=operation,
            resource=resource,
            scope=scope,
            risk_score=0,
            decision="allow",
            reason="no matching policy, default allow",
        )
