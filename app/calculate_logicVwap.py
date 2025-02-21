import pandas as pd

def calculate_vwap(data):
    """
    Calcula el VWAP para los datos proporcionados.
    """
    df = pd.DataFrame(data)
    df['VWAP'] = (df['close'] * df['volume']).cumsum() / df['volume'].cumsum()
    return df
