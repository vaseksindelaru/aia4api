from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_detect():
    response = client.post("/detection/", json={"data": [...]})
    assert response.status_code == 200
    assert response.json() == {...}

def test_evaluate():
    response = client.post("/evaluation/grid-search", json={"data": [...], "volume_windows": [...], "height_windows": [...]})
    assert response.status_code == 200
    assert response.json() == {...}

def test_evaluate_rebound():
    response = client.post("/evaluation/rebound", json={"data": [...], "index": 0})
    assert response.status_code == 200
    assert response.json() == {"result": ...}
