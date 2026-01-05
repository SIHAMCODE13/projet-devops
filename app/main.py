from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Health Service", version="1.0.0")

@app.get("/api/health")
def health():
    return {"status": "UP", "service": "health-service", "version": "1.0.0"}

# Monitoring Prometheus
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)
