from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "UP"
    assert data["service"]
    assert data["version"]
    assert data["uptime_seconds"] >= 0
    assert "timestamp" in data


def test_dashboard_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Health Service Dashboard" in response.text
    assert "UP" in response.text


def test_static_files_are_served():
    assert client.get("/static/css/style.css").status_code == 200
    assert client.get("/static/js/script.js").status_code == 200


def test_metrics_endpoint():
    client.get("/api/health")  # génère au moins une métrique
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "http_requests_total" in response.text


def test_unknown_route_returns_404():
    assert client.get("/does-not-exist").status_code == 404
