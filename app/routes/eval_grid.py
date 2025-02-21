from fastapi import APIRouter
from app.eval_logicGrid import grid_search

router = APIRouter()

@router.post("/eval_grid/")
def evaluate(data: dict):
    return grid_search(data['data'], data['volume_windows'], data['height_windows'])
