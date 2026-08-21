import uuid

from fastapi import APIRouter, HTTPException

from schemas.chat import ChatRequest, ChatResponse

from services.preprocessing.engine import preprocessor
from services.safety.engine import safety_engine
from services.intent.engine import intent_engine
from services.entity.engine import entity_engine
from services.context.engine import context_engine
from services.response.engine import response_engine
from services.recommendation.engine import recommendation_engine


router = APIRouter()


@router.post("/message", response_model=ChatResponse)
async def chat_message(request: ChatRequest):

    if not request.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty.",
        )

    # ---------------------------------------------
    # Session
    # ---------------------------------------------

    session_id = request.session_id or str(uuid.uuid4())

    # ---------------------------------------------
    # Preprocessing
    # ---------------------------------------------

    processed = preprocessor.preprocess(
        request.message
    )

    normalized_text = processed["normalized"]

    # ---------------------------------------------
    # Context - user message
    # ---------------------------------------------

    context_engine.add_user_message(
        session_id,
        request.message,
    )

    # ---------------------------------------------
    # Safety
    # ---------------------------------------------

    safety = safety_engine.analyze(
        normalized_text
    )

    safety_level = safety["level"]

    # ---------------------------------------------
    # Intent
    # ---------------------------------------------

    intent_result = intent_engine.detect(
        normalized_text
    )

    intent = intent_result["intent"]

    confidence = intent_result["confidence"]

    # ---------------------------------------------
    # Entity
    # ---------------------------------------------

    entities = entity_engine.extract(
        normalized_text
    )

    # ---------------------------------------------
    # Context update
    # ---------------------------------------------

    context_engine.update(
        session_id=session_id,
        intent=intent,
        entities=entities,
        safety_level=safety_level,
    )

    # ---------------------------------------------
    # Response
    # ---------------------------------------------

    response_result = response_engine.generate(
        intent=intent,
        safety_level=safety_level,
        safety_response=safety.get("response"),
    )

    response_text = response_result["response"]

    # ---------------------------------------------
    # Recommendations
    # ---------------------------------------------

    recommendations = recommendation_engine.get(
        intent=intent,
        entities=entities,
    )

    # ---------------------------------------------
    # Context - assistant response
    # ---------------------------------------------

    context_engine.add_assistant_message(
        session_id,
        response_text,
    )

    # ---------------------------------------------
    # Final JSON
    # ---------------------------------------------

    return ChatResponse(
        success=True,
        session_id=session_id,
        intent=intent,
        confidence=confidence,
        safety_level=safety_level,
        entities=entities,
        matched_keywords=intent_result[
            "matched_keywords"
        ],
        matched_phrases=intent_result[
            "matched_phrases"
        ],
        response_type=response_result["type"],
        response=response_text,
        recommendations=recommendations,
    )