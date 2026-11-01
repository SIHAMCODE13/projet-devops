"""Point d'entrée de l'application FastAPI."""

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator

from app.config import SERVICE_NAME, SERVICE_VERSION
from app.routers.health import router as health_router
from app.services.health_service import get_health_status

# Chemins absolus : l'application fonctionne quel que soit le dossier de lancement
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title=SERVICE_NAME, version=SERVICE_VERSION)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# API : GET /api/health
app.include_router(health_router, prefix="/api")

# Monitoring Prometheus : métriques exposées sur GET /metrics
Instrumentator(excluded_handlers=["/metrics", "/static.*"]).instrument(app).expose(
    app, include_in_schema=False
)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def dashboard(request: Request):
    """Page d'accueil : dashboard de l'état du service."""
    return templates.TemplateResponse(
        request, "index.html", {**get_health_status(), "service_name": SERVICE_NAME}
    )
