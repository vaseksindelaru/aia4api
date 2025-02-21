# app/routes/detection.py

from fastapi import APIRouter
from app.detection_logic import detect_candlesticks

router = APIRouter()

@router.post("/detection/")
def detect(data: list):
    return detect_candlesticks(data)
