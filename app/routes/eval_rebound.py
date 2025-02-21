# app/routes/eval_rebound.py

from fastapi import APIRouter
from app.eval_logicRebound import evaluar_rebote

router = APIRouter()

@router.post("/evaluation/rebound")
def evaluate_rebound(data: dict):
    return {'result': evaluar_rebote(data['data'], data['index'])}
