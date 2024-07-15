import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

uploaded_image = st.file_uploader("Upload Image")

if camera_image:
    # Read the image from the camera input
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img, caption="Grayscale Camera Image")
elif uploaded_image:
    # Read the image from the file uploader
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img, caption="Grayscale Uploaded Image")
