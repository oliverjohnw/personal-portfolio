import streamlit as st

def about_me_page():
    """
    About me page.
    """
    st.header("🛠️ The Technical Side")
    st.write(
        f"""
        My data science journey began in 2016 as an undergrad at the University of Wisconsin - La Crosse. While I was there
        I received a Master's degree in Applied Statistics, as well as a Bachelor's degree in Statistics.

        After graduating I began working an internship as a data scientist at [U.S. Geological Survey](https://www.usgs.gov/). I learned and
        grew alot here, as I got to apply some of the skills that I learned in school for the first time. I was involved with several
        projects that were centered around datasets for invasive and endangered species. I even got to co-author a paper!

        My internship concluded in the summer of 2022 and I moved back to my hometown of Milwaukee, Wisconsin, where I accepted a position
        as a data scientist at [Elutions](https://www.elutions.com/). I've been fortunate to work on 
        some really cool projects while working here, including:

        - Building, optimizing, and deploying models to optimize industrial machine performance.  
        - Developing and maintaining pipelines to support machine learning models.  
        - Analyzing machine failure data to predict future failures.  
        """
    )
    st.write(f"\n\n")


    st.header("🏕️ Beyond Data (Away From My Desk)")
    st.write(
        ""
    )