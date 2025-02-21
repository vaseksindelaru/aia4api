from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_detect_candlesticks():
    response = client.post("/detect_candlesticks/", json=[
        {"open": 100, "close": 105, "high": 110, "low": 95, "volume": 1000},
        {"open": 102, "close": 99, "high": 108, "low": 97, "volume": 800}
    ])
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # La respuesta debe ser una lista

def test_eval_grid_search():
    response = client.post("/evaluation/grid-search", json={
        "data": [
            {"open": 100, "close": 105, "high": 110, "low": 95, "volume": 1000},
            {"open": 102, "close": 99, "high": 108, "low": 97, "volume": 800}
        ],
        "volume_windows": [3, 5],
        "height_windows": [3, 5]
    })
    assert response.status_code == 200
    assert "best_params" in response.json()

def test_eval_rebound():
    response = client.post("/evaluation/rebound", json={
        "data": [
            {"open": 100, "close": 105, "high": 110, "low": 95, "volume": 1000},
            {"open": 102, "close": 99, "high": 108, "low": 97, "volume": 800},
            {"open": 98, "close": 106, "high": 109, "low": 96, "volume": 900}
        ],
        "index": 0
    })
    assert response.status_code == 200
    assert "result" in response.json()
    assert response.json()["result"] in [0, 1]  # Debe devolver 0 o 1

def test_train_gradient_boosting():
    response = client.post("/train_GB/", json={
        "data": [
            {"Candle_Type": 1, "VWAP": 103, "Rebound_Success": 1},
            {"Candle_Type": 0, "VWAP": 99, "Rebound_Success": 0},
            {"Candle_Type": 1, "VWAP": 107, "Rebound_Success": 1}
        ]
    })
    assert response.status_code == 200
    assert "accuracy" in response.json()
