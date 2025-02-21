from fastapi import APIRouter
from app.calculate_logicVwap import calculate_vwap

router = APIRouter()

@router.post("/calculate_vwap/")
def vwap(data: list):
    result = calculate_vwap(data)
    return result.to_dict(orient='records')
