from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import requests
from app.logic.calculate_logicVwap import calculate_vwap
from app.logic.detect_logicCandlesticks import detect_candlesticks
from app.logic.detect_logicRebound import evaluar_rebote

engine = create_engine('sqlite:///market_data_dynamic.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class DataAgent:
    def __init__(self, max_clusters=5):
        self.max_clusters = max_clusters
        self.features = ['Candle_Type', 'VWAP', 'Spread']
        self.tables = {}

    def analyze_data(self, data):
        try:
            df = pd.DataFrame(calculate_vwap(data))
            df['Spread'] = df['high'] - df['low']
            candlesticks = detect_candlesticks(df)
            df_filtered = pd.DataFrame(candlesticks)
            if df_filtered.empty:
                return pd.DataFrame(columns=self.features + ['Rebound_Success', 'Cluster'])  # Devolver DataFrame vacío si no hay candlesticks
            df_filtered['Candle_Type'] = np.where(df_filtered['close'] > df_filtered['open'], 'Bullish', 'Bearish')
            df_filtered['Rebound_Success'] = [evaluar_rebote(df, i) for i in range(len(df_filtered))]
            X = df_filtered[self.features]
            
            try:
                response = requests.post(
                    "http://localhost:8000/optimize_clusters/",
                    json={"data": X.to_dict(orient='records'), "max_clusters": self.max_clusters},
                    timeout=5
                )
                response.raise_for_status()
                optimal_k = response.json()["optimal_clusters"]
            except requests.RequestException as e:
                print(f"Error al contactar optimize_clusters: {e}. Usando fallback.")
                optimal_k = min(self.max_clusters, X.shape[0]) or 1  # Asegurar al menos 1 clúster

            self.model = KMeans(n_clusters=optimal_k, random_state=42)
            self.model.fit(X)
            df_filtered['Cluster'] = self.model.labels_
            return df_filtered
        except Exception as e:
            print(f"Error en analyze_data: {e}")
            raise

    def define_table(self, cluster_id, features):
        class DynamicTable(Base):
            __tablename__ = f'cluster_{cluster_id}_data'
            id = Column(Integer, primary_key=True)
            strategy_id = Column(Integer, ForeignKey('strategies.id'))
        for feature in features:
            if feature == 'Candle_Type':
                setattr(DynamicTable, feature, Column(Integer))
            elif feature == 'Rebound_Success':
                setattr(DynamicTable, feature, Column(Integer))
            else:
                setattr(DynamicTable, feature, Column(Float))
        self.tables[cluster_id] = DynamicTable
        return DynamicTable

    def create_tables(self):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def save_data(self, clustered_data):
        for cluster_id in clustered_data['Cluster'].unique():
            cluster_data = clustered_data[clustered_data['Cluster'] == cluster_id]
            if cluster_id not in self.tables:
                self.define_table(cluster_id, self.features + ['Rebound_Success'])
                self.create_tables()
            TableClass = self.tables[cluster_id]
            for _, row in cluster_data.iterrows():
                row_data = {key: row[key] for key in self.features + ['Rebound_Success']}
                if 'Candle_Type' in row_data:
                    row_data['Candle_Type'] = 1 if row_data['Candle_Type'] == 'Bullish' else 0
                entry = TableClass(**row_data)
                session.add(entry)
        session.commit()

class Strategy(Base):
    __tablename__ = 'strategies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    params = Column(String)