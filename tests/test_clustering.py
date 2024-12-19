import pytest
from src.engagement_clustering import cluster_engagement

def test_cluster_engagement():
    data = pd.read_csv('../data/raw/user_data.csv')
    clustered_data = cluster_engagement(data, n_clusters=3)
    assert clustered_data['engagement_cluster'].nunique() == 3  # Ensure 3 clusters
