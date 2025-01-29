import streamlit as st

def resume_page():
    """
    Resume page layout.
    """
    st.title("My Resume")
    st.write("### Experience")
    st.write("- Built and deployed machine learning models for multiple clients.")
    st.write("- Developed survival analysis models to predict asset failures.")
    st.write("### Skills")
    st.write("- Python, SQL, Machine Learning, Data Visualization, Streamlit")
    # with open("assets/resume.pdf", "rb") as file:
    #     st.download_button("Download Resume", file, "resume.pdf")
