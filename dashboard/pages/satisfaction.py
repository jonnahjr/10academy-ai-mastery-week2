import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    # Replace this with actual data loading logic
    df = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Score': [85, 82, 88, 86, 89, 87]
    })
    return df

def show():
    st.title("Satisfaction Analysis")

    df = load_data()

    col1, col2, col3 = st.columns(3)
    col1.metric("Average Satisfaction Score", "8.5/10")
    col2.metric("Highly Satisfied Users", "65%")
    col3.metric("Satisfaction Trend", "↑ 5%")

    st.subheader("Satisfaction Score Trend")
    fig = px.line(df, x='Month', y='Score', title="Satisfaction Score Trend")
    st.plotly_chart(fig, use_container_width=True)

    # Add more satisfaction analysis visualizations here