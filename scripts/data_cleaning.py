import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

class EngagementAnalyzer:
    def __init__(self):
        self.scaler = StandardScaler()
        
    def calculate_engagement_metrics(self, df):
        """Calculate engagement metrics per user"""
        engagement_metrics = df.groupby('MSISDN').agg({
            'Session ID': 'count',  # frequency
            'Duration': 'sum',      # duration
            'Total DL + UL': 'sum'  # traffic
        }).reset_index()
        
        return engagement_metrics
        
    def normalize_metrics(self, df):
        """Normalize engagement metrics"""
        columns_to_normalize = ['Session ID', 'Duration', 'Total DL + UL']
        df[columns_to_normalize] = self.scaler.fit_transform(df[columns_to_normalize])
        return df
        
    def cluster_users(self, df, n_clusters=3):
        """Cluster users based on engagement metrics"""
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(df)
        return clusters
        
    def get_top_users_per_metric(self, df, metric, n=10):
        """Get top n users for a specific metric"""
        return df.nlargest(n, metric)