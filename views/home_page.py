import streamlit as st
from PIL import Image

def home_page():
    """
    Home page layout.
    
    Displays:
    - Intro statement
    - Page description
    - Image of me
    """
    with st.container():
        col1, col2 = st.columns([3, 1])

        # writing (intro statement + page description)
        with col1:
            st.title("Welcome to My Portfolio 👋")
            st.write("Hello! I'm John, a data scientist currently located in Milwaukee, Wisconsin.")
            st.markdown("<br>", unsafe_allow_html=True)
            st.header("📄 Page Description")
            st.write("""This is my personal portfolio page where I put pretty much everything - 
                     including my resume, personal projects, and much more. Feel free to explore my work and connect if you'd like! 
                     """)
            st.write("""The sidebar on the left will take you to wherever you'd like. You can navigate between my personal introduction,
                     resume, projects, and contact information all over there. 😊
                     """)

        # image
        with col2:
            image = Image.open("img/home_page/me.png")
            resized_image = image.resize((800, 600)) 
            st.markdown("<br><br><br>", unsafe_allow_html=True)
            st.image(resized_image, caption="Welcome to my page!", use_container_width=True)