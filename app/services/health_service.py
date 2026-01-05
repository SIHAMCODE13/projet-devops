from app.config import SERVICE_NAME, SERVICE_VERSION

def get_health_status():
    return {
        "status": "UP",
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION
    }
