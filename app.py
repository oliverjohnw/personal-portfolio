import streamlit as st

# local imports
from views import home_page, resume_page, projects_page, contact_page

def main():

    # page settings
    st.set_page_config(page_title="My Portfolio", layout="wide")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Resume", "Projects", "Contact"])

    # page selections
    if page == "Home":
        home_page()
    elif page == "Resume":
        resume_page()
    elif page == "Projects":
        projects_page()
    elif page == "Contact":
        contact_page()

if __name__ == "__main__":
    main()