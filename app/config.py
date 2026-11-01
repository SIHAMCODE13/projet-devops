"""Configuration de l'application, lue depuis les variables d'environnement."""

import os

SERVICE_NAME: str = os.getenv("SERVICE_NAME", "health-service")
SERVICE_VERSION: str = os.getenv("SERVICE_VERSION", "1.0.0")
