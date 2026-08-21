from fastapi import APIRouter
from pydantic import BaseModel

from services.preprocessing.engine import preprocessor
from services.intent.engine import intent_engine
from services.entity.engine import entity_engine
from services.recommendation.engine import (
    recommendation_engine,
)


router = APIRouter()


class RecommendationRequest(BaseModel):

    message: str

    intent: str | None = None

    session_id: str | None = None


@router.post("/get")
async def get_recommendations(
    request: RecommendationRequest,
):

    processed = preprocessor.preprocess(
        request.message
    )

    text = processed["normalized"]

    if request.intent:

        intent = request.intent

    else:

        intent_result = intent_engine.detect(text)

        intent = intent_result["intent"]

    entities = entity_engine.extract(text)

    recommendations = recommendation_engine.get(
        intent=intent,
        entities=entities,
    )

    return {
        "success": True,
        "intent": intent,
        "entities": entities,
        "recommendations": recommendations,
    }