from fastapi import APIRouter
from app.logic.detect_logicCandlesticks import detect_candlesticks

router = APIRouter()

@router.post("/detect_candlesticks/")
def detect_candles(data: list):
    return detect_candlesticks(data)