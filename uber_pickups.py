import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber pickups in NYC")

DATE_COLUMN = "date/time"
DATA_URL = (
    "https://s3-us-west-2.amazonaws.com/"
    "streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)

import streamlit as st


# # bUILDING BLOCK FOR JSON LOTTIE
# import lottie
from streamlit-lottie import st_lottie
import requests, time

# -------------------------#
# bUILDING BLOCK FOR JSON LOTTIE
# url = requests.get(
#     "https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json")
# # Creating a blank dictionary to store JSON file,
# # as their structure is similar to Python Dictionary
# url_json = dict()

# if url.status_code == 200:
#     url_json = url.json()
# else:
#     print("Error in the URL")


# st.title("Adding Lottie Animation in Streamlit WebApp")

# st_lottie(url_json)

# -------------------------#
# # Lottie for delaying
# # Load the Lottie JSON data
# url = "https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json"
# response = requests.get(url)
# animation_data = response.json()

# # Title
# st.title("Adding Lottie Animation in Streamlit WebApp")

# # Introduce a delay before displaying the animation
# st.text("Loading animation...")
# st.empty()  # Add an empty widget to make a space for the animation
# time.sleep(3)  # Delay for 3 seconds

# # Display the Lottie animation
# st_lottie(animation_data)
# # -------------------------#


# Lottie animation with effect in js
custom_html2 = """
<div id="lottie-container"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.9.1/lottie.min.js"></script>
<script>
    // Load the Lottie animation
    var animation = lottie.loadAnimation({
      container: document.getElementById('lottie-container'),
      renderer: 'svg',
      loop: true,
      autoplay: false, // Set autoplay to false
      path: 'https://lottie.host/f4ab7b8d-3b5a-4b49-b140-7ffa213da26d/FujKaTQKG2.json'
    });

    // Define the scale factor
    var scaleFactor = 1;

    // Use setTimeout to delay the start of the animation by 3 seconds
    setTimeout(function() {
        // Play the animation after the delay
        animation.play();
        
        // Scale the animation over time for enlarging effect
        function scaleAnimation() {
            scaleFactor += 0.01; // Adjust the increment value as needed
            if (scaleFactor > 1.5) { // Adjust the maximum scale as needed
                scaleFactor = 1;
            }
            document.getElementById('lottie-container').style.transform = 'scale(' + scaleFactor + ')';
            requestAnimationFrame(scaleAnimation);
        }
        
        scaleAnimation();
    }, 3000); // 3000 milliseconds = 3 seconds
</script>
"""
st.components.v1.html(custom_html2, height=200)

# Define custom HTML
custom_html = """
<div style="background-color: lightblue; padding: 10px;">
    <h2>Custom Component</h2>
    <p>This is a custom HTML component!</p>
</div>
"""

# Embed custom HTML using st.components.v1.html
st.components.v1.html(custom_html, height=200)

custom_html2 = """
<div style="padding: 10px; border: 2px solid blue;">
    <h2>Styled Component</h2>
    <p style="color: red;">This component has custom styles!</p>
</div>
<script>
    // You can include custom JavaScript here
    console.log('Custom component loaded!');
</script>
"""

st.components.v1.html(custom_html2, height=200)


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text("Loading data...")
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)

st.subheader("Number of pickups by hour")
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider("hour", 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader("Map of all pickups at %s:00" % hour_to_filter)
st.map(filtered_data)
