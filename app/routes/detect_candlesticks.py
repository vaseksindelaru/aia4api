from fastapi import APIRouter
from app.detect_logicCandlesticks import detect_candlesticks

router = APIRouter()

@router.post("/detect_candlesticks/")
def detect(data: list):
    result = detect_candlesticks(data)
    return result.to_dict(orient='records')
