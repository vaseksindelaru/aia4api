# app/main.py

from fastapi import FastAPI
from app.routes import detection, eval_grid, eval_rebound

app = FastAPI()

app.include_router(detection.router)
app.include_router(eval_grid.router)
app.include_router(eval_rebound.router)
