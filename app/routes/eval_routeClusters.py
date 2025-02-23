from fastapi import APIRouter
from pydantic import BaseModel
from app.logic.eval_logicClusters import evaluate_clusters  

router = APIRouter()

class OptimizeClustersRequest(BaseModel):
    data: list
    max_clusters: int = 5

@router.post("/optimize_clusters/")
def optimize_clusters_endpoint(request: OptimizeClustersRequest):
    result = evaluate_clusters(request.data, request.max_clusters)
    return result