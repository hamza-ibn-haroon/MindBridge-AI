from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.context.engine import context_engine


router = APIRouter()


class InsightsRequest(BaseModel):

    session_id: str


@router.post("/analyze")
async def analyze_insights(
    request: InsightsRequest,
):

    context = context_engine.get_context(
        request.session_id
    )

    if not context["messages"]:

        raise HTTPException(
            status_code=404,
            detail="No conversation found for this session.",
        )

    return {
        "success": True,
        "session_id": request.session_id,
        "current_intent": context["last_intent"],
        "dominant_topic": (
            context["last_entities"].get("topic")
        ),
        "trigger": (
            context["last_entities"].get("trigger")
        ),
        "recent_messages": len(
            context["messages"]
        ),
        "safety_level": context[
            "last_safety_level"
        ],
        "suggested_action": (
            "Focus on one small practical step "
            "related to your current concern."
        ),
    }