# models.py
"""Threat models used by the threat detection subsystem."""

from dataclasses import dataclass
from enum import Enum
from typing import List


class ThreatType(str, Enum):
    PROMPT_INJECTION = "PROMPT_INJECTION"
    SECRET_LEAKAGE = "SECRET_LEAKAGE"
    SENSITIVE_DATA = "SENSITIVE_DATA"
    TOOL_ABUSE = "TOOL_ABUSE"


@dataclass
class ThreatResult:
    threat_type: ThreatType
    detected: bool
    score: int
    reason: str
    matches: List[str]

    def to_dict(self) -> dict:
        return {
            "threat_type": self.threat_type.value,
            "detected": self.detected,
            "score": self.score,
            "reason": self.reason,
            "matches": self.matches,
        }
