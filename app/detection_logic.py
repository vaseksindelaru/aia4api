import pandas as pd


def detect_candlesticks(data, volume_window=5, height_window=5):
    df = pd.DataFrame(data)
    df['Total_Height'] = df['high'] - df['low']
    df['Volume_SMA'] = df['volume'].rolling(window=volume_window).mean()
    df['Total_Height_SMA'] = df['Total_Height'].rolling(window=height_window).mean()
    df['High_Volume'] = df['volume'] > df['Volume_SMA']
    df['Small_Body'] = df['Total_Height'] < df['Total_Height_SMA']
    df_filtered = df[df['High_Volume'] & df['Small_Body']].copy()
    return df_filtered.to_dict(orient='records')