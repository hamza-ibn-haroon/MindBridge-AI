from fastapi import APIRouter

from schemas.mood import MoodRequest, MoodResponse

from services.preprocessing.engine import preprocessor
from services.safety.engine import safety_engine
from services.intent.engine import intent_engine


router = APIRouter()


@router.post("/analyze", response_model=MoodResponse)
async def analyze_mood(request: MoodRequest):

    processed = preprocessor.preprocess(
        request.message
    )

    text = processed["normalized"]

    intent_result = intent_engine.detect(text)

    intent = intent_result["intent"]

    confidence = intent_result["confidence"]

    scores = {
        "stress": 0.0,
        "anxiety": 0.0,
        "sadness": 0.0,
        "motivation": 0.0,
    }

    if intent in {
        "stress",
        "academic_stress",
        "work_stress",
        "career_stress",
        "burnout",
    }:
        scores["stress"] = confidence

    if intent == "anxiety":
        scores["anxiety"] = confidence

    if intent in {
        "sadness",
        "loneliness",
    }:
        scores["sadness"] = confidence

    if intent == "low_motivation":
        scores["motivation"] = max(
            0.0,
            1.0 - confidence,
        )

    if intent == "unknown":
        primary_state = "unclear"
    else:
        primary_state = intent

    return MoodResponse(
        success=True,
        primary_state=primary_state,
        scores=scores,
        disclaimer=(
            "This is a rule-based conversational estimate "
            "and is not a clinical or medical assessment."
        ),
    )