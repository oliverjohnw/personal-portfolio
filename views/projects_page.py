import streamlit as st

def projects_page():
    """
    Project page layout.
    """
    st.title("Projects")
    st.write("### NFL Betting Dashboard")
    st.write("An interactive dashboard to visualize NFL data and assist with betting decisions.")
    st.link_button("View on GitHub", "https://github.com/your-github/nfl-dashboard")
    st.write("### Survival Analysis Tool")
    st.write("A tool to predict asset failures using Weibull analysis.")
    st.link_button("View on GitHub", "https://github.com/your-github/survival-analysis")
