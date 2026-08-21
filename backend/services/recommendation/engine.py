from .recommendations import RECOMMENDATIONS


class RecommendationEngine:

    def get(
        self,
        intent: str,
        entities: dict | None = None,
    ) -> list[str]:

        recommendations = RECOMMENDATIONS.get(
            intent,
            RECOMMENDATIONS["unknown"],
        )

        return recommendations[:4]


recommendation_engine = RecommendationEngine()