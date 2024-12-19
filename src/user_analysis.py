import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

class UserAnalyzer:
    def __init__(self):
        self.kmeans = None
        
    def get_top_handsets(self, df, n=10):
        """Get top n handsets"""
        return df['Handset Type'].value_counts().head(n)
        
    def get_top_manufacturers(self, df, n=3):
        """Get top n manufacturers"""
        return df['Handset Manufacturer'].value_counts().head(n)
        
    def get_top_handsets_per_manufacturer(self, df, manufacturer, n=5):
        """Get top n handsets for a specific manufacturer"""
        return df[df['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(n)
        
    def aggregate_user_metrics(self, df):
        """Aggregate metrics per user"""
        return df.groupby('MSISDN').agg({
            'Session ID': 'count',
            'Duration': 'sum',
            'Total DL': 'sum',
            'Total UL': 'sum'
        }).reset_index()
        
    def cluster_users(self, df, n_clusters=3):
        """Cluster users based on their metrics"""
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = self.kmeans.fit_predict(df)
        return clusters