import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine

# Function to connect to the PostgreSQL database
def connect_to_db():
    engine = create_engine('postgresql://username:password@localhost/dbname')
    return engine.connect()

# Load data from the database
def load_data():
    conn = connect_to_db()
    query = "SELECT * FROM xdr_data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Handle missing values
def handle_missing_values(df):
    df.fillna(df.mean(), inplace=True)
    return df

# Identify and treat outliers (for simplicity, using Z-Score)
def handle_outliers(df):
    from scipy import stats
    z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
    df = df[(z_scores < 3).all(axis=1)]  # Remove outliers
    return df

# Normalize data for modeling
def normalize_data(df):
    scaler = StandardScaler()
    numerical_columns = df.select_dtypes(include=[np.number]).columns
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
    return df

# Preprocessing pipeline
def preprocess_data():
    df = load_data()
    df = handle_missing_values(df)
    df = handle_outliers(df)
    df = normalize_data(df)
    return df
