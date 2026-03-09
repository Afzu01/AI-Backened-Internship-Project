from pydantic import BaseModel, Field


class RecommendRequest(BaseModel):
    query: str = Field(..., min_length=2)
    top_k: int = Field(default=3, ge=1, le=10)


class EmbedRequest(BaseModel):
    text: str = Field(..., min_length=1)


class WebhookEvent(BaseModel):
    source: str
    event_type: str
    payload: dict
