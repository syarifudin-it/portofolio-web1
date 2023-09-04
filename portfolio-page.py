#  pip install requests streamlit streamlit_lottie bokeh==2.4.1
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from bokeh.models.widgets import Div


st.set_page_config(
    page_title="🚀 Syarifudin's Portfolio Page 🚀",
    page_icon=":boy:",
    layout="wide",
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#  To get rid of the Streamlit branding stuff
local_css("css/styles.css")

#  Anchor
st.title("#")  # This anchor is needed for the page to start at the top when it is called.

# --- INTRO ---
with st.container():
    col1, col2 = st.columns((2, 1))
    with col1:
        st.title("Welcome to my Portfolio Page!")
        st.subheader("Hi, I am Syarifudin 🤗")
        st.subheader(
            """
            I'm a Indonesian-based *IT Specialist | Network Engineer* who specializes in the broad fields of *Network Engieerng* and *Data Scientist*.
            """
        )
        st.write("""""")
        st.subheader(
            """
            This page is actually made with Python :snake: and the associated Streamlit library. Even though the purpose of this library is mainly data science, this page is made to showcase that even with no knowledge of Web Development you can make a nice looking portfolio page with pure Python code.
            """
        )
    with col2:
        st_lottie(
            load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_bniew9j6.json"),
            height=500,
        )


# --- ABOUT ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st_lottie(
            load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_dh764zdr.json"),
            height=500,
        )
    with col2:
        st.header("About")
        st.write(
            """
            I have been IT professionally since 2014, starting with IT Technical Support on IT Consultant 🐱‍👤
            
            Short facts & milestones:
            - Certified MTCNA - Mikrotik Academy
            - Certified Junior Network Administrator - BNSP
            - Training CCNA 200-301 ID-Networkers
            - Training Digital Talent Schoolarship Kominfo - CCNA Netwok Engineer
            - Training/Bootcamp Machine Learning dan AI DQLab 2023
            - Bachelor's degree. Informatics Engineering (STT PELITA BANGSA)
            - 8+ years of professional experience in IT Specialist | Network Engineer
            - Enthusiasm for Network Engineering, Data Engineering, Automating Things, Data Scientist, Futsal, and fast food 🍕🍟🥓🍔🥯🍨🍫
            If you are interested in building something together, have questions/suggestions about my code or just wanna connect, feel free to get in touch with me! 
            """
        )


# --- TECH STACK / SKILLS ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Tech Stack / Skills")
        st.write(
            """
            Languages
            - Python, HTML, CSS, PHP, Google Collab
            Frameworks
            - Bootstrap, Codeigniter
            Databases
            - MySQL, PostgreSQL
            Hosting & Cloud
            - Azure, Admin Office365, Exchange Online, Streamlit Cloud 😉
            Miscellaneous
            - Github
            Network
            - Cisco, Mikrotik, Palo Alto, FortiNet, Sophos, Ruckus, Cambium, Huawei
            Server
            - Zimbra Mail, Active Directory Windows, File Server Windows, FTP, Web Server, NAS, Veeam Backup, Vsphere VM
             """
        )

    with col2:
        st_lottie(
            load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ba013t74.json"),
            height=500,
        )


# --- PORTFOLIO ---
with st.container():
    st.write("---")
    st.header("Portfolio")
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('MachineLearningDasboard.jpg')
        st.subheader("Machine Learning Dashboard")
        st.write("This app predicts the Heart Disease")
        if st.button('Enter App', key="https://heart-disease-dashboard-project-jctb3carhy6y6kbihlhi7x.streamlit.app"):
            js = "window.open('https://heart-disease-dashboard-project-jctb3carhy6y6kbihlhi7x.streamlit.app')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="ews_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/syarifudin-it/heart-disease-dashboard-project')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col2:
        st.image('portofolioweb.jpg')
        st.subheader("Portfolio Website made with Streamlit")
        st.write("Portfolio Website made with Python/Streamlit.")
        if st.button('Enter App', key="https://portofolio-web1-q2ydirwj4qqz7xjj64o8nt.streamlit.app/"):
            st.write('You are already on the streamlit portfolio website 😃')
        if st.button('Github', key="spw_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/syarifudin-it/portofolio-web1')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col3:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Setup Access Point Ubuquity and Controller In linux server")
        st.write("Setup and configuration management wireless ubiquity on Campus STT Pelita")
        if st.button('Enter App', key="ccw_enter"):
            js = "window.open('https://crypto-watchlist-rather-to.herokuapp.com/')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="ccw_github"):
            st.write('Github opens in new browser tab')
           js = "window.open('https://github.com/ratherUsefulCode/')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)


with st.container():
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("QR Codes Reader and Generator")
        st.write("Create and/or read every QR code.")
        if st.button('Enter App', key="qrc_enter"):
            st.write('Web Application opens in new browser tab')
        if st.button('Github', key="qrc_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/ratherUsefulCode/github-email-exposer')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col5:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Github E-Mail Exposer")
        st.write("Expose all E-Mail addresses contributing to a given Github account.")
        if st.button('Enter App', key="gee_enter"):
            js = "window.open('https://github.com/ratherUsefulCode/github-email-exposer')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.write('Web Application opens in new browser tab')
            st.bokeh_chart(div)
        if st.button('Github', key="gee_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/ratherUsefulCode/github-email-exposer')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col6:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Portfolio Website made with Bootstrap")
        st.write("Portfolio Website made with HTML/Bootstrap.")
        if st.button('Enter App'):
            js = "window.open('https://rather.to')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
            st.write('Web Application opens in new browser tab')
        if st.button('Github', key="bpw_github"):
            js = "window.open('https://github.com/ratherUsefulCode/rather-to')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)


# --- CONTACT ---
with st.container():
    st.write("---")
    st.markdown("<h2 style='text-align: center;'>Contact</h2>", unsafe_allow_html=True)
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col2:
        contact_form = """
        <form action="https://formsubmit.co/805cc992f02da35ae356f2451ece18be" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)


with st.container():
    for i in range(8):
        st.write("##")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write(
            """
            Feel free to copy this page 👍
            """
        )
    with col2:
        st.markdown("<p style='text-align: right;'>Made in 2023 with ❤, 🐍 and Streamlit</p>", unsafe_allow_html=True)
    st.write("---")

