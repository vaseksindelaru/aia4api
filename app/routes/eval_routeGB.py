from fastapi import APIRouter
from app.logic.eval_logicGB import train_gradient_boosting

router = APIRouter()

@router.post("/train_GB/")
def train_gb(data: list):
    result = train_gradient_boosting(data)
    return {"accuracy": result["accuracy"]}