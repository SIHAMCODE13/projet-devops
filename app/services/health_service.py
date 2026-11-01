"""Logique métier du health-check."""

import time
from datetime import UTC, datetime

from app.config import SERVICE_NAME, SERVICE_VERSION

# Instant de démarrage du service (horloge monotone, insensible aux changements d'heure)
_STARTED_AT = time.monotonic()


def get_health_status() -> dict:
    """Retourne l'état courant du service."""
    return {
        "status": "UP",
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
        "uptime_seconds": round(time.monotonic() - _STARTED_AT, 2),
        "timestamp": datetime.now(UTC).isoformat(),
    }
