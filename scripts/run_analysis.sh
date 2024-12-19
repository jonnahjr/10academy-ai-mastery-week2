#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Preprocess data
python src/data_preprocessing.py

# Run clustering
python src/engagement_clustering.py

# Train and evaluate model
python src/satisfaction_model.py
