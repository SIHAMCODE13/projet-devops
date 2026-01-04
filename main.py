import os
from fastapi import FastAPI

app = FastAPI()

SERVICE_NAME = os.getenv("SERVICE_NAME", "health-service")
SERVICE_VERSION = os.getenv("SERVICE_VERSION", "1.0.0")

@app.get("/")
def root():
    return {"message": "Hello DevOps"}

@app.get("/api/health")
def health():
    return {
        "status": "UP",
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION
    }
