from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.data_agent import DataAgent

router = APIRouter()
agent = DataAgent()

class DataAgentRequest(BaseModel):
    open: float
    close: float
    high: float
    low: float
    volume: float

@router.post("/data-agent/analyze")
def analyze_data(data: list[DataAgentRequest]):
    try:
        clustered_data = agent.analyze_data([item.model_dump() for item in data])  # Cambio de dict() a model_dump()
        agent.save_data(clustered_data)
        return clustered_data.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))