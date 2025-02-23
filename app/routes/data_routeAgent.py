from fastapi import APIRouter, HTTPException
from app.agents.data_agent import DataAgent

router = APIRouter()
agent = DataAgent()

@router.post("/data-agent/analyze")
def analyze_data(data: list):
    try:
        clustered_data = agent.analyze_data(data)
        agent.save_data(clustered_data)
        return clustered_data.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))