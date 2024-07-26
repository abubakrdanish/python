import streamlit as st
import requests

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
request = requests.get(url)
content = request.json()


if request.status_code == 200:
    st.title(content["title"])
    st.image(content["hdurl"])
    
    st.markdown("<br>", unsafe_allow_html=True)  # Add a line break
    st.markdown(f"<b>{content['explanation']}</b>", unsafe_allow_html=True)
else:
    st.write("Failed to retrieve image")
