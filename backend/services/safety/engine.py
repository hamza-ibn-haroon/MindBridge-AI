from .rules import (
    CONCERN_PATTERNS,
    HIGH_RISK_PATTERNS,
    SAFETY_RESPONSES,
)


class SafetyEngine:

    def _contains_pattern(
        self,
        text: str,
        patterns: list[str],
    ) -> list[str]:

        matches = []

        for pattern in patterns:
            if pattern.lower() in text.lower():
                matches.append(pattern)

        return matches

    def analyze(self, text: str) -> dict:

        normalized = text.lower().strip()

        high_risk = self._contains_pattern(
            normalized,
            HIGH_RISK_PATTERNS,
        )

        if high_risk:
            return {
                "level": "high_risk",
                "matched_patterns": high_risk,
                "response": SAFETY_RESPONSES["high_risk"],
            }

        concern = self._contains_pattern(
            normalized,
            CONCERN_PATTERNS,
        )

        if concern:
            return {
                "level": "concern",
                "matched_patterns": concern,
                "response": SAFETY_RESPONSES["concern"],
            }

        return {
            "level": "normal",
            "matched_patterns": [],
            "response": None,
        }


safety_engine = SafetyEngine()