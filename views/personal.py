import streamlit as st
from PIL import Image

def personal():
    """
    Personal introudction page.
    
    Displays:
    - Tehcnical background
    - Personal background
    """
    col1, col2 = st.columns([3, 1])

    # techincal background - writing
    with col1:
        st.header("🛠️ The Technical Side")
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Education📚")
        st.write(
            f"""
            My data science journey began in 2016 as an undergrad at the University of Wisconsin - La Crosse. While I was there
            I received a **Master's degree in Applied Statistics**, as well as a **Bachelor's degree in Statistics**.
            """
        )
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Professional Experience💼")
        st.write(f"""
            After graduating I began working an internship as a **data scientist at U.S. Geological Survey**. I learned and
            grew alot here, as I got to apply some of the skills that I learned in school for the first time. I was involved with several
            projects that were centered around datasets for invasive and endangered species. I even got to **co-author a [paper](https://www.usgs.gov/software/indiana-mussel-metabolomics-data-analysis)**!
            """
        )
        st.write(f"""
            My internship concluded in the summer of 2022 and I moved back to my hometown of Milwaukee, Wisconsin, where I accepted a position
            as a data scientist at Elutions. I've been fortunate to work on 
            some really cool projects while working here, including:
            - **Building, optimizing, and deploying models** to optimize industrial machine performance.  
            - Developing and maintaining **pipelines** to support machine learning models.  
            - Analyzing machine failure data to **predict future failures**.       
            """
        )

    # techincal background - images
    with col2:
        grad_image = Image.open("img/personal/diploma.png")
        target_size = (200, 150) 
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        grad_image = grad_image.resize(target_size)
        st.image(grad_image)

        usgs_image = Image.open("img/personal/USGS_DS.jpg")
        target_size = (200, 150) 
        usgs_image = usgs_image.resize(target_size)
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image(usgs_image)

        elutions_image = Image.open("img/personal/elutions.png")
        target_size = (200, 40) 
        elutions_image = elutions_image.resize(target_size)
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image(elutions_image)

    # personal background
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.header("🏕️ Beyond the Data - Away From My Desk")

    # fitness writing
    st.subheader("Fitness🏃‍♂️")
    st.write(
        f"""
        On a day to day basis, I really enjoy staying active and exercising. When the weather permits, I enjoy going
        for a run outside. I'm not an avid runner by any means, but I do really enjoy it. I try to push myself to run a half marathon at 
        least once a summer. Occasionally I'll shoot some hoops with friends and play some pickup basketball. I fear my best days are behind me,
        but it's still fun! I also enjoy playing frisbee golf - and recently got into real golf.
        """)
    st.write(
        f"""
        I also really enjoy riding my bike. There's actually a trail that runs from right by my apartment to my work - which
        I find pretty amazing! It's about a 14 mile trip one way, so I definitely can't do it everyday. But I try to do it every 
        so often. It helps that there's a coffee shop on the way!
        """)
    st.write(
        f"""
        Unfortunately, living in Wisconsin, I can't always be outside. We have some pretty cold days here. So for all other days, I like to
        go to the gym and lift weights. The current gym I'm at has a really nice sauna and cold plunge that I've been trying to
        use more.
        """)
    st.markdown("<br>", unsafe_allow_html=True)

    # fitness pictures
    image_info = [
        ("img/personal/basketball.jpg", "Intramural champs baby!"),
        ("img/personal/half_marathon.jpeg", "Half Marathon 2023!"),
        ("img/personal/bike_ride.jpg", "Views from my bike ride to work")
    ]
    target_size = (200, 270)
    images = [(Image.open(path).resize(target_size), caption) for path, caption in image_info]
    with st.container():
        cols = st.columns(3)
        for col, (img, caption) in zip(cols, images):
            with col:
                st.image(img, caption=caption)

    # outdoor writing
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Outdoors🏞️")
    st.write(
        f"""
        My (maybe unrealistic) goal is to spend as much time outside as I do at my desk. My favorite thing to do on a warm 
        Wisconsin weekend is to go camping. I love being out in nature and away from the city. It's probably my favorite hobby. 
        It's very refreshing to unplug and step away for the weekend.
        """)
    st.write(
        f"""
        I've been to several state parks in Wisconsin, but my favorite spot will always be the Porcupine Mountains in the 
        Upper Peninsula of Michigan. Each of the last three summers I've been able to get up there and make a 4 day weekend out of it.
        And I have plans to return this September!
        """
    )
    st.markdown("<br>", unsafe_allow_html=True)
    
    # outdoor pictures
    image_info = [
        ("img/personal/porkies1.heic", "Presque Isle Falls, Michigan"),
        ("img/personal/porkies2.jpg", "The usual setup! Big ole tent + screent tent"),
        ("img/personal/porkies3.jpg", "Saw my first ever wild bear in 2024!")
    ]
    target_size = (200, 270)
    images = [(Image.open(path).resize(target_size), caption) for path, caption in image_info]
    with st.container():
        cols = st.columns(3)
        for col, (img, caption) in zip(cols, images):
            with col:
                st.image(img, caption=caption)

    # concerts + live events
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Live Events🎤")
    st.write(
        f"""
        I frequently chase my favorite bands and try to get out to as many concerts as possible. In the last year (2024-2025),
        I've been able to see:
        - Billy Strings (2x)
        - Sturgill Simpson
        - Tyler Childers
        - Goose

        And a lot more! I really enjoy folksy/bluegrass music, but I'm pretty open to any genre.
        """
    )

    st.write(
        f"""
        I also am a pretty avid sports fan - Wisconsin sports in particular. Growing up in Milwaukee, it's always been pretty easy
        to hit a handful of Bucks and Brewers game each summer. I'd say my favorite sports are football and basketball, and I also really
        enjoy mixed martial arts. Go Packers!
        """
    )
    st.markdown("<br>", unsafe_allow_html=True)
    
    # live event pictures
    image_info = [
        ("img/personal/red_rocks.heic", "Tyler Childers @ Red Rocks"),
        ("img/personal/tuck.jpeg", "Bark at the Park with Tucker"),
        ("img/personal/pack.heic", "LAMBEAU FIELD")
    ]
    target_size = (200, 270)
    images = [(Image.open(path).resize(target_size), caption) for path, caption in image_info]
    with st.container():
        cols = st.columns(3)
        for col, (img, caption) in zip(cols, images):
            with col:
                st.image(img, caption=caption)