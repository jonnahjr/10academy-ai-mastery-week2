import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from pages.user_overview import display_user_overview
from pages.engagement import display_engagement
from pages.experience import display_experience
from pages.satisfaction import display_satisfaction

def main():
    st.title('User Engagement and Satisfaction Dashboard')

    # Sidebar navigation
    pages = {
        'User Overview': display_user_overview,
        'Engagement': display_engagement,
        'Experience': display_experience,
        'Satisfaction': display_satisfaction
    }

    page = st.sidebar.radio('Select a page', list(pages.keys()))
    pages[page]()  # Display the selected page

if __name__ == "__main__":
    main()
