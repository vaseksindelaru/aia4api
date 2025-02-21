from fastapi import APIRouter
from app.detect_logicRebound import evaluar_rebote

router = APIRouter()

@router.post("/detect_rebound/")
def evaluate_rebound(data: dict):
    return {'result': evaluar_rebote(data['data'], data['index'])}
