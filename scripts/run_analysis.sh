#!/bin/bash
# Run data preprocessing
python3 src/data_preprocessing.py

# Run clustering analysis
python3 src/engagement_clustering.py

# Run experience analysis
python3 src/experience_analysis.py

# Run satisfaction model training
python3 src/satisfaction_model.py

# Run user analysis
python3 src/user_analysis.py
