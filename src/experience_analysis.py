import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

class ExperienceAnalyzer:
    def __init__(self):
        self.kmeans = None
        
    def aggregate_experience_metrics(self, df):
        """Aggregate experience metrics per user"""
        experience_metrics = df.groupby('MSISDN').agg({
            'TCP Retransmission': 'mean',
            'RTT': 'mean',
            'Throughput': 'mean'
        }).reset_index()
        
        return experience_metrics
        
    def get_metric_statistics(self, df, metric, n=10):
        """Get top, bottom and most frequent values for a metric"""
        return {
            'top': df[metric].nlargest(n),
            'bottom': df[metric].nsmallest(n),
            'most_frequent': df[metric].value_counts().head(n)
        }
        
    def analyze_throughput_by_handset(self, df):
        """Analyze throughput distribution per handset type"""
        return df.groupby('Handset Type')['Throughput'].agg(['mean', 'std', 'count'])
        
    def cluster_users(self, df, n_clusters=3):
        """Cluster users based on experience metrics"""
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = self.kmeans.fit_predict(df)
        return clusters