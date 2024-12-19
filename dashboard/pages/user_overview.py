import streamlit as st
import pandas as pd

def display_user_overview():
    data = pd.read_csv('../../data/processed/user_data.csv')
    st.write(data.head())
