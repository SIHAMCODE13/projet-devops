from fastapi import FastAPI
from app.routers.health import router as health_router

app = FastAPI(
    title="Health Service",
    version="1.0.0"
)

app.include_router(health_router, prefix="/api")
