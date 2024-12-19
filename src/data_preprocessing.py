import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        
    def load_data(self, filepath):
        """Load data from CSV file"""
        return pd.read_csv(filepath)
        
    def handle_missing_values(self, df):
        """Handle missing values in the dataset"""
        # Replace missing values with mean for numeric columns
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
        
        # Replace missing values with mode for categorical columns
        categorical_columns = df.select_dtypes(exclude=[np.number]).columns
        df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])
        
        return df
        
    def remove_outliers(self, df, columns, threshold=3):
        """Remove outliers using Z-score method"""
        for column in columns:
            z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())
            df = df[z_scores < threshold]
        return df
        
    def normalize_features(self, df, columns):
        """Normalize features using StandardScaler"""
        df[columns] = self.scaler.fit_transform(df[columns])
        return df
        
    def reduce_dimensions(self, df, columns, n_components=2):
        """Perform PCA for dimensionality reduction"""
        pca = PCA(n_components=n_components)
        pca_result = pca.fit_transform(df[columns])
        return pd.DataFrame(
            data=pca_result,
            columns=[f'PC{i+1}' for i in range(n_components)]
        )