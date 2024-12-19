import streamlit as st
import pandas as pd

def display_experience():
    data = pd.read_csv('../../data/processed/user_data.csv')
    experience_summary = data.groupby('user_id')['experience_score'].mean()
    st.write(experience_summary)
