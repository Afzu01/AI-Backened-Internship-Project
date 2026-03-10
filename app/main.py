from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.schemas import EmbedRequest, RecommendRequest, WebhookEvent
from app.services import CatalogService

app = FastAPI(title="AI Backend Internship Project API", version="1.0.0")
service = CatalogService()
UI_FILE = Path(__file__).resolve().parent.parent / "ui" / "index.html"


@app.get("/")
def root() -> dict:
    return {"message": "API is running", "docs": "/docs", "ui": "/ui"}


@app.get("/ui")
def ui() -> FileResponse:
    return FileResponse(UI_FILE)


@app.post("/recommend")
def recommend(payload: RecommendRequest) -> dict:
    items = service.recommend(payload.query, payload.top_k)
    return {"query": payload.query, "results": items}


@app.post("/embed")
def embed(payload: EmbedRequest) -> dict:
    vector = service.embed(payload.text)
    return {
        "text": payload.text,
        "dimensions": len(vector),
        "preview": vector[:10],
    }


@app.post("/webhooks/events")
def webhook(event: WebhookEvent) -> dict:
    return {
        "status": "received",
        "source": event.source,
        "event_type": event.event_type,
        "payload_keys": list(event.payload.keys()),
    }
