import streamlit as st
from landing import show as show_uber_pickups
from chatbot import show as show_chatbot
from streamlit_lottie import st_lottie
import requests

# Load background image at the very beginning
background_image = "https://cdn.statically.io/img/www.techfinitive.com/wp-content/uploads/2023/05/can-ai-save-the-environment.jpg?quality=90&f=auto"
background = f"""
    <style>
    .stApp {{
        background-image: url({background_image});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
"""
st.markdown(background, unsafe_allow_html=True)

# Styling the welcome message
welcome_message = """
    <style>
        .welcome-message {
            font-size: 32px;  # Equivalent to h2
            font-weight: bold;
            color: #ffffff;  # Dark grey color
            text-align: center;
            padding: 20px;
            margin-top: 20px;
        }
    </style>
    <div class="welcome-message">
        Welcome to Our Chat Bot 
        <p> Vancouver Datajam 2023
    </div>
"""
st.markdown(welcome_message, unsafe_allow_html=True)

# Animated button style
animated_button_style = """
    <style>
        .stButton>button {
            display: inline-block;
            font-size: 20px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            outline: none;
            color: #fff;
            background-color: #4CAF50;
            border: none;
            border-radius: 15px;
            box-shadow: 0 9px #999;
            padding: 10px 24px;
            margin: 2px;
        }
        
        .stButton>button:hover {background-color: #3e8e41;}
        
        .stButton>button:active {
            background-color: #3e8e41;
            box-shadow: 0 5px #666;
            transform: translateY(4px);
        }
    </style>
"""
st.markdown(animated_button_style, unsafe_allow_html=True)


# Define the pages in the app
PAGES = {"Uber Pickups": show_uber_pickups, "Chatbot": show_chatbot}

# Set the initial page
if "page" not in st.session_state:
    st.session_state.page = "Initial"

# Create buttons for navigation
if st.session_state.page == "Initial":
    if st.button("Go to Chatbot"):
        st.session_state.page = "Chatbot"
    elif st.button("Go to Data Set?? "):
        st.session_state.page = "Uber Pickups"
elif st.session_state.page in PAGES:
    PAGES[st.session_state.page]()

# Load Lottie animation JSON
lottie_url = "https://lottie.host/89731dff-bbb7-4a88-9baf-b04089f686c3/4YDO2zKY4U.json"
lottie_json = requests.get(lottie_url).json()

# Display the Lottie animation at the end
# custom_html2 = """
# <div id="lottie-container" overflow-y:auto style="height:15vh;"></div>
# <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.9.1/lottie.min.js"></script>
# <script>
#     // Load the Lottie animation
#     var animation = lottie.loadAnimation({
#     container: document.getElementById('lottie-container'),
#     renderer: 'svg',
#     loop: true,
#     autoplay: false, // Set autoplay to false
#     path: 'https://lottie.host/f4ab7b8d-3b5a-4b49-b140-7ffa213da26d/FujKaTQKG2.json'
#     });

#     // Define the scale factor
#     var scaleFactor = 1;

#     // Use setTimeout to delay the start of the animation by 3 seconds
#     setTimeout(function() {
#         // Play the animation after the delay
#         animation.play();
        
#         // Scale the animation over time for enlarging effect
#         function scaleAnimation() {
#             scaleFactor += 0.01; // Adjust the increment value as needed
#             if (scaleFactor > 1.5) { // Adjust the maximum scale as needed
#                 scaleFactor = 1;
#             }
#             document.getElementById('lottie-container').style.transform = 'scale(' + scaleFactor + ')';
#             requestAnimationFrame(scaleAnimation);
#         }
        
#         scaleAnimation();
#     }, 1000); // 3000 milliseconds = 3 seconds
# </script>
# """
#st.components.v1.html(custom_html2, height=1000)
