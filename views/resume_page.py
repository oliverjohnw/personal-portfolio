import streamlit as st

def resume_page():
    """
    Resume page layout.
    """
    st.title("Resume")
    st.download_button(label="GitHub Pages Resume", 
                   data="", 
                   file_name="", 
                   mime=None, 
                   on_click=lambda: st.markdown("[Click here](https://oliverjohnw.github.io/digital-cv)", unsafe_allow_html=True))

    # Add PDF Download Button
    pdf_path = "docs/John Oliver Resume - Data Scientist.pdf"  # Replace with actual file path
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(label="Download Resume (PDF)", 
                        data=pdf_bytes, 
                        file_name="John_Oliver_Resume.pdf", 
                        mime="application/pdf")





    # st.title("John Oliver")
    # st.write("_Data Scientist based out of Milwaukee, Wisconsin_")

    # st.markdown("[Email](mailto:johnoliver616@yahoo.com) / [GitHub](https://github.com/oliverjohnw) / [LinkedIn](https://www.linkedin.com/in/john-oliver-76508519a/)")

    # st.header("Technical Experience")

    # st.subheader("Data Scientist @ [Elutions](https://www.elutions.com/)")
    # st.write("**June 2022 - Present**")
    # st.write("_Description: Data scientist involved in the creation and continuous deployment of live models._")
    # st.markdown("""
    # - Developed and deployed **LightGBM** and **XGBoost** models to optimize industrial machine performance across several manufacturing clients.
    # - Led end-to-end data science workflows, including data acquisition, exploratory data analysis (EDA), data cleansing, model development, and live deployment in production environments.
    # - Developed reusable data science pipelines with **ZenML** to streamline data preprocessing, cleansing, and model construction, significantly reducing project turnaround time for new clients.
    # - Conducted **survival analysis** on maintenance datasets to model machine asset lifecycles, providing data-driven recommendations for preventative maintenance scheduling.
    # """)

    # st.subheader("Data Science Intern @ [U.S. Geological Survey](https://www.usgs.gov/)")
    # st.write("**June 2021 - June 2022**")
    # st.write("_Description: Applied multivariate statistics and machine learning on projects focused on natural resources and invasive or endangered species._")
    # st.markdown("""
    # - Analyzed demographic patterns of endangered mussel populations using supervised and unsupervised machine learning techniques, including **Non-Metric Multidimensional Scaling (NMDS)**, **Principal Component Analysis (PCA)**, and **distance-based Redundancy Analysis (db-RDA)**.
    # - Co-authored a peer-reviewed paper investigating the impact of distance/dissimilarity metrics on **clustering**, **ordination**, and **canonical multivariate techniques** on metabolomic datasets.
    # - Conducted statistical consulting and model implementation to evaluate agreement statistics for invasive Silver Carp aging techniques using **Linear Mixed Models** in **lme4**.
    # """)

    # st.subheader("Mathematical Tutor @ [University of Wisconsin La-Crosse](https://www.uwlax.edu/)")
    # st.write("**September 2019 - December 2021**")
    # st.markdown("""
    # - Provided tutoring support for collegiate-level mathematics courses, including **Algebra**, **Calculus**, and **Linear Algebra**, improving students' comprehension and performance.
    # - Adapted to individual learning styles while ensuring concepts were effectively understood.
    # """)

    # st.header("Education")

    # st.subheader("Master of Science in Applied Statistics")
    # st.write("[University of Wisconsin La Crosse](https://www.uwlax.edu/grad/statistics/) - La Crosse, Wisconsin")
    # st.write("Spring 2020 - Fall 2021")
    # st.markdown("**Master's Project:** [Bayesian Hyperparameter Tuning in Classification of NBA Game Outcomes](https://github.com/oliverjohnw/nba-grad-project)")

    # st.subheader("Bachelor of Science in Statistics")
    # st.write("[University of Wisconsin La Crosse](http://catalog.uwlax.edu/undergraduate/mathematics/statistics-bs/) - La Crosse, Wisconsin")
    # st.write("Fall 2016 - Spring 2020")

    # st.header("Projects")

    # st.subheader("NFL Game Prediction Dashboard")
    # st.write("Constructed a model that predicts the outcome of games in the NFL. Built an interactive dashboard to visualize predictions, team data, statistics, and key game factors.")
    # st.markdown("* [Dashboard](https://johns-nfl-dashboard.streamlit.app/)")
    # st.markdown("* [GitHub](https://github.com/oliverjohnw/nfl-dashboard)")

    # st.subheader("Spotify Song Recommender")
    # st.write("Designed and implemented a music recommendation system that suggests similar songs based on user input from Spotify.")
    # st.markdown("* [GitHub](https://github.com/oliverjohnw/spotify-recommendations)")
