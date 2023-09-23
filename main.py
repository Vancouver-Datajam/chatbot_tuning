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



# Define the pages in the app
PAGES = {
    "Uber Pickups": show_uber_pickups,
    "Chatbot": show_chatbot
}

# Set the initial page
if 'page' not in st.session_state:
    st.session_state.page = "Initial"

# Create buttons for navigation
if st.session_state.page == "Initial":
    if st.button('Go to Chatbot'):
        st.session_state.page = "Chatbot"
    elif st.button('Go to Uber Pickups'):
        st.session_state.page = "Uber Pickups"
elif st.session_state.page in PAGES:
    PAGES[st.session_state.page]()
