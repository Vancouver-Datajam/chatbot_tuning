import streamlit as st

def show():
    
    st.title('Chatbot Page')
    
    # Your existing code for chatbot.py

    if st.button('Go to Back'):
            st.session_state.page = "Uber Pickups"