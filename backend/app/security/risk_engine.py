from dataclasses import dataclass
from enum import Enum

from app.security.decision import Decision, SecurityDecision


class RiskEngine:
    """Simple rule‑based risk engine.

    In later versions this will be replaced by a more sophisticated
    pipeline (prompt‑injection detector, secret scanner, policy engine, …).
    """

    def evaluate(self, action) -> SecurityDecision:
        """Return a :class:`SecurityDecision` for a given ToolAction.

        Parameters
        ----------
        action: ToolAction
            An object containing tool, operation, resource, scope, and parameters.
        """
        tool = action.tool
        operation = action.operation
        resource = action.resource
        scope = action.scope

        tool_lower = tool.lower()
        operation_lower = operation.lower()
        resource_lower = resource.lower()
        scope_lower = scope.lower()

        # Dangerous database operations
        if "delete" in operation_lower or "drop" in operation_lower:
            return SecurityDecision(
                tool=tool,
                operation=operation,
                resource=resource,
                scope=scope,
                risk_score=95,
                decision=Decision.BLOCK,
                reason="Destructive database operation detected",
            )

        # Shell / terminal execution – requires human approval
        if "shell" in tool_lower or "terminal" in tool_lower:
            return SecurityDecision(
                tool=tool,
                operation=operation,
                resource=resource,
                scope=scope,
                risk_score=85,
                decision=Decision.APPROVAL_REQUIRED,
                reason="Shell execution requires human approval",
            )

        # File deletion
        if "remove" in operation_lower or "delete" in operation_lower:
            # Note: we already caught database deletes above; this is for generic file ops
            return SecurityDecision(
                tool=tool,
                operation=operation,
                resource=resource,
                scope=scope,
                risk_score=90,
                decision=Decision.BLOCK,
                reason="File deletion detected",
            )

        # Low‑risk read / search operations
        if "search" in operation_lower or "read" in operation_lower:
            return SecurityDecision(
                tool=tool,
                operation=operation,
                resource=resource,
                scope=scope,
                risk_score=10,
                decision=Decision.ALLOW,
                reason="Low‑risk read operation",
            )

        # Default – allow but with modest risk score
        return SecurityDecision(
            tool=tool,
            operation=operation,
            resource=resource,
            scope=scope,
            risk_score=30,
            decision=Decision.ALLOW,
            reason="No high‑risk behavior detected",
        )
