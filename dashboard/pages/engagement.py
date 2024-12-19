import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def display_engagement():
    data = pd.read_csv('../../data/processed/user_data.csv')
    st.subheader('User Engagement Distribution')
    sns.histplot(data['engagement_score'], kde=True)
    plt.title('User Engagement Distribution')
    st.pyplot()
