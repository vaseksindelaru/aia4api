import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

def prepare_data(data):
    """
    Prepara los datos para el entrenamiento del modelo de Gradient Boosting.
    """
    df = pd.DataFrame(data)
    df['Candle_Type'] = df['Candle_Type'].map({'Bullish': 1, 'Bearish': 0})
    features = df[['Candle_Type', 'VWAP']]
    label = df['Rebound_Success']
    return train_test_split(features, label, test_size=0.2, random_state=42)

def train_gradient_boosting(data):
    """
    Entrena un modelo de Gradient Boosting para predecir el éxito del rebote.
    """
    X_train, X_test, y_train, y_test = prepare_data(data)
    model = GradientBoostingClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return model, accuracy
