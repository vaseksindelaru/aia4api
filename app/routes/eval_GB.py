from fastapi import APIRouter
from app.eval_logicGB import train_gradient_boosting

router = APIRouter()

@router.post("/eval_GB/")
def train(data: list):
    model, accuracy = train_gradient_boosting(data)
    return {"accuracy": accuracy}
