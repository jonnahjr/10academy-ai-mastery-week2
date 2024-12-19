import pandas as pd

def user_engagement_analysis(data):
    # Group by user and calculate average engagement
    engagement_summary = data.groupby('user_id')['engagement_score'].mean()
    return engagement_summary
