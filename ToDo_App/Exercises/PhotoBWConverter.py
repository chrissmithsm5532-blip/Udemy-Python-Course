import streamlit as st
from PIL import Image

with st.expander("Start Camera"):

    uploaded_image = st.file_uploader("Upload Image")
if uploaded_image:
    img = Image.open(uploaded_image)
    grey_img = img.convert("L")
    st.image(grey_img)