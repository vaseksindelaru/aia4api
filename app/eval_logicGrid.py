from .detect_logicCandlesticks import detect_candlesticks
import pandas as pd

def grid_search(data, volume_windows, height_windows):
    best_score = -1
    best_params = {}

    for vw in volume_windows:
        for hw in height_windows:
            filtered_data = detect_candlesticks(data)
            score = len(filtered_data) / len(data)
            if score > best_score:
                best_score = score
                best_params = {'volume_window': vw, 'height_window': hw}
    
    return {'best_params': best_params, 'score': best_score}
