from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    ALLOW = "ALLOW"
    BLOCK = "BLOCK"
    APPROVAL_REQUIRED = "APPROVAL_REQUIRED"


@dataclass
class SecurityDecision:
    tool: str
    operation: str
    resource: str
    scope: str
    risk_score: int
    decision: Decision
    reason: str
