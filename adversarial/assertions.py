"""Security assertions for adversarial test results.

Provides simple helpers that produce an :class:`AssertionResult` indicating whether a
security detector behaved as expected.
"""

from dataclasses import dataclass


@dataclass
class AssertionResult:
    """Result of a single assertion.

    * ``passed`` – ``True`` when the observed value matches the expectation.
    * ``message`` – Human‑readable description used in the report.
    """

    passed: bool
    message: str


def assert_detected(detected: bool, case_id: str) -> AssertionResult:
    """Assert that a threat was detected.

    Parameters
    ----------
    detected:
        The boolean returned by the security engine.
    case_id:
        Identifier of the adversarial case (used for the message).
    """
    if detected:
        return AssertionResult(True, f"{case_id}: threat detected")
    return AssertionResult(False, f"{case_id}: threat MISSED")


def assert_decision(actual: str, expected: str, case_id: str) -> AssertionResult:
    """Assert that the decision matches the expected decision.

    Parameters
    ----------
    actual:
        Decision returned by the gateway (e.g., ``"BLOCK"``).
    expected:
        Expected decision for this test case.
    case_id:
        Identifier of the adversarial case.
    """
    if actual == expected:
        return AssertionResult(True, f"{case_id}: {actual} == {expected}")
    return AssertionResult(False, f"{case_id}: {actual} != {expected}")
