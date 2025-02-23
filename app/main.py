from fastapi import FastAPI
from app.routes import (
    calculate_routeVwap, detect_routeCandlesticks, detect_routeRebound, eval_routeClusters,
    eval_routeGB, eval_routeGrid, data_routeAgent
)

app = FastAPI()

app.include_router(calculate_routeVwap.router)
app.include_router(detect_routeCandlesticks.router)
app.include_router(detect_routeRebound.router)
app.include_router(eval_routeGB.router)
app.include_router(eval_routeGrid.router)
app.include_router(eval_routeClusters.router)
app.include_router(data_routeAgent.router)