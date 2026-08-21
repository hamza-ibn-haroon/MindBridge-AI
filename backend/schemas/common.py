from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class APIResponse(BaseModel):
    success: bool = True
    message: Optional[str] = None


class EntityData(BaseModel):
    topic: Optional[str] = None
    trigger: Optional[str] = None
    entities: Dict[str, Any] = Field(default_factory=dict)


class RecommendationResponse(BaseModel):
    recommendations: List[str] = Field(default_factory=list)