import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances

class SatisfactionAnalyzer:
    def __init__(self):
        self.scaler = StandardScaler()
        
    def calculate_satisfaction_scores(self, engagement_clusters, experience_clusters, user_data):
        """Calculate satisfaction scores based on engagement and experience"""
        # Calculate engagement score
        engagement_score = self._calculate_distance_score(
            user_data[['Session ID', 'Duration', 'Total DL + UL']],
            engagement_clusters.cluster_centers_[0]  # Least engaged cluster
        )
        
        # Calculate experience score
        experience_score = self._calculate_distance_score(
            user_data[['TCP Retransmission', 'RTT', 'Throughput']],
            experience_clusters.cluster_centers_[0]  # Worst experience cluster
        )
        
        # Calculate satisfaction score
        satisfaction_score = (engagement_score + experience_score) / 2
        
        return pd.DataFrame({
            'MSISDN': user_data['MSISDN'],
            'engagement_score': engagement_score,
            'experience_score': experience_score,
            'satisfaction_score': satisfaction_score
        })
        
    def _calculate_distance_score(self, data, cluster_center):
        """Calculate Euclidean distance based score"""
        distances = euclidean_distances(data, [cluster_center])
        return 1 / (1 + distances.flatten())  # Normalize to 0-1 range
        
    def cluster_satisfaction(self, scores, n_clusters=2):
        """Cluster users based on satisfaction scores"""
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(scores[['engagement_score', 'experience_score']])
        return clusters