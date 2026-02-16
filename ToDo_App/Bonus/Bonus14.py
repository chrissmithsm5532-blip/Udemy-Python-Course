import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    #start camera
    camera_image = st.camera_input("Camera")

    if camera_image:
        #make pillow image
        img= Image.open(camera_image)
        #turn grey
        grey_img = img.convert("L")
        #display on webpage
        st.image(grey_img)