import pandas as pd

def detect_candlesticks(data: list, volume_window=20, height_window=20):
    # Crear DataFrame desde lista de diccionarios
    df = pd.DataFrame(data)

    # Verificar que tenga las columnas necesarias
    if not {'high', 'low', 'volume'}.issubset(df.columns):
        raise ValueError("Los datos deben contener las columnas 'high', 'low', 'volume'.")

    # Calcular altura de la vela
    df['height'] = df['high'] - df['low']

    # Calcular SMA de volumen y altura
    df['volume_sma'] = df['volume'].rolling(window=volume_window).mean()
    df['height_sma'] = df['height'].rolling(window=height_window).mean()

    # Señal de detección
    df['signal'] = (df['volume'] > df['volume_sma']) & (df['height'] < df['height_sma'])

    # Filtrar resultados
    result = df[df['signal']].to_dict(orient='records')

    return result
