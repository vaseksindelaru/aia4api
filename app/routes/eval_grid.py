# app/routes/eval_grid.py

from fastapi import APIRouter
from app.eval_logicGrid import grid_search

router = APIRouter()

@router.post("/evaluation/grid-search")
def evaluate(data: dict):
    return grid_search(data['data'], data['volume_windows'], data['height_windows'])
