from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="User's message",
    )

    session_id: Optional[str] = Field(
        default=None,
        description="Temporary conversation session ID",
    )


class ChatResponse(BaseModel):
    success: bool = True

    session_id: str

    intent: str

    confidence: float

    safety_level: str

    entities: Dict[str, Any] = Field(default_factory=dict)

    matched_keywords: List[str] = Field(default_factory=list)

    matched_phrases: List[str] = Field(default_factory=list)

    response_type: str

    response: str

    recommendations: List[str] = Field(default_factory=list)