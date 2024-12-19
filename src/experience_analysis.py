import pandas as pd

def analyze_user_experience(data):
    # Calculate average experience score by user
    experience_summary = data.groupby('user_id')['experience_score'].mean()
    return experience_summary
