import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    
    # Handle missing values
    data.fillna(data.mean(), inplace=True)
    
    # Standardize numerical features
    # aa
    scaler = StandardScaler()
    data[['engagement_score', 'experience_score']] = scaler.fit_transform(data[['engagement_score', 'experience_score']])
    
    return data
