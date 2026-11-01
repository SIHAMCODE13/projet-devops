"""Routes liées à la santé du service."""

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.health_service import get_health_status

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    uptime_seconds: float
    timestamp: str


@router.get("/health", response_model=HealthResponse, summary="État du service")
def health() -> dict:
    return get_health_status()
