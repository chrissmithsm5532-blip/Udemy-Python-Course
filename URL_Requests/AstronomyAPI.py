import requests
import streamlit as st

API_KEY = "QSEJh9qgKMGkHSr7hrvbGfVupZwOsUvF7FIEBOGh"

#get
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"


request = requests.get(url)

data = request.json()

description = data["explanation"]

hdurl = data["hdurl"]

image_filepath = "image.png"
response2 = requests.get(hdurl)

with open(image_filepath, "wb") as file:
    file.write(response2.content)


st.title("Astronomy API")
st.image(image_filepath)
st.write(description)

