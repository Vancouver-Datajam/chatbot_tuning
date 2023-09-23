import streamlit as st
from uber_pickups import show as show_uber_pickups
from chatbot import show as show_chatbot

# # Check if the 'page' attribute is in session_state
# if 'page' not in st.session_state:
#     st.session_state.page = "Uber Pickups"

# # Display the selected page
# if st.session_state.page == "Uber Pickups":
#     show_uber_pickups()
# elif st.session_state.page == "Chatbot":
#     show_chatbot()

from streamlit_lottie import st_lottie
import requests

page_bg_img = """
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Define parallax scrolling effect using HTML and CSS
parallax_effect_html = """
<div style="position: width:100vw; background-attachment: fixed; background-image: url('https://cdn4.vectorstock.com/i/1000x1000/47/93/desert-parallax-background-vector-10204793.jpg'); height: 100vh; w; background-position: center; background-repeat: no-repeat; background-size: cover;">
    <div style="height: 75vh;"></div>
    <div style="text-align: center;">
        <!-- You can place content here like headings or buttons -->
    </div>
</div>
"""

# Load Lottie animation JSON
lottie_url = "https://lottie.host/89731dff-bbb7-4a88-9baf-b04089f686c3/4YDO2zKY4U.json"
lottie_json = requests.get(lottie_url).json()

# Display the parallax section
st.components.v1.html(parallax_effect_html, height=1920, width=1080, scrolling=True)

# Define the pages in the app
PAGES = {"Uber Pickups": show_uber_pickups, "Chatbot": show_chatbot}

# Set the initial page
if "page" not in st.session_state:
    st.session_state.page = "Initial"

# Create buttons for navigation
if st.session_state.page == "Initial":
    if st.button("Go to Chatbot"):
        st.session_state.page = "Chatbot"
    elif st.button("Go to Uber Pickups"):
        st.session_state.page = "Uber Pickups"
elif st.session_state.page in PAGES:
    PAGES[st.session_state.page]()

# Display the Lottie animation at the end
st_lottie(lottie_json, width=200, height=200)
