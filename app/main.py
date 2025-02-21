from fastapi import FastAPI
from app.routes import calculate_vwap, detect_candlesticks, detect_rebound, eval_GB, eval_grid




app = FastAPI()

# Registrar las rutas
app.include_router(calculate_vwap.router)
app.include_router(detect_candlesticks.router)
app.include_router(detect_rebound.router)
app.include_router(eval_GB.router)
app.include_router(eval_grid.router)
