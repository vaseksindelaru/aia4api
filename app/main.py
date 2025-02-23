# app/main.py
from fastapi import FastAPI
from app.routes import (
    calculate_routeVwap, detect_routeCandlesticks, detect_routeRebound,
    eval_routeGB, eval_routeGrid, eval_routeClusters, data_routeAgent
)

app = FastAPI()

app.include_router(calculate_routeVwap)
app.include_router(detect_routeCandlesticks)
app.include_router(detect_routeRebound)
app.include_router(eval_routeGB)
app.include_router(eval_routeGrid)
app.include_router(eval_routeClusters)
app.include_router(data_routeAgent)