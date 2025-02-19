from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.detection_logic import detect_candlesticks

app = FastAPI()

class Candlestick(BaseModel):
    high: float
    low: float
    volume: float

@app.post("/detect/")
def detect(data: List[Candlestick], volume_window: int = 20, height_window: int = 20):
    try:
        # Convertir entrada a diccionarios para pasar a la lógica
        data_dicts = [item.dict() for item in data]
        result = detect_candlesticks(data_dicts, volume_window, height_window)
        return {"detected_candlesticks": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
