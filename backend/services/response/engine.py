from .responses import RESPONSES


class ResponseEngine:

    def generate(
        self,
        intent: str,
        safety_level: str,
        safety_response: str | None = None,
    ) -> dict:

        if safety_level == "high_risk":
            return {
                "type": "safety",
                "response": safety_response,
            }

        if safety_level == "concern" and safety_response:
            return {
                "type": "supportive",
                "response": safety_response,
            }

        responses = RESPONSES.get(
            intent,
            RESPONSES["unknown"],
        )

        # Simple deterministic rotation.
        # No AI/LLM involved.
        response = responses[0]

        return {
            "type": "supportive",
            "response": response,
        }


response_engine = ResponseEngine()