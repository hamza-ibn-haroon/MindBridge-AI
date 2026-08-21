from typing import Dict

from pydantic import BaseModel, Field


class MoodRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
    )

    session_id: str | None = None


class MoodResponse(BaseModel):
    success: bool = True

    primary_state: str

    scores: Dict[str, float]

    disclaimer: str