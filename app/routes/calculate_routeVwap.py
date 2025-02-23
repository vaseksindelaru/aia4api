from fastapi import APIRouter
from app.logic.calculate_logicVwap import calculate_vwap

router = APIRouter()

@router.post("/calculate_vwap/")
def calc_vwap(data: list):
    return calculate_vwap(data)