import streamlit as st
import pandas as pd

def display_satisfaction():
    data = pd.read_csv('../../data/processed/user_data.csv')
    st.write(data[['user_id', 'satisfaction']])
