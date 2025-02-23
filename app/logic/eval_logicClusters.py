import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def evaluate_clusters(data, max_clusters=5):  # Cambio de optimize_clusters a evaluate_clusters
    df = pd.DataFrame(data)
    X = df[list(df.columns)]
    
    inertias = []
    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)
    
    diffs = np.diff(inertias)
    diffs2 = np.diff(diffs)
    optimal_k = np.argmax(diffs2) + 2
    optimal_k = max(optimal_k, 2)
    
    return {
        "optimal_clusters": int(optimal_k),
        "inertias": inertias
    }