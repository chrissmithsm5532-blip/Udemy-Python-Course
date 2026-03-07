import streamlit as st

st.title("Weather Forecast for Next days")
place = st.text_input("Place: ")
days = st.slider("ForeCast", 1, 5,
                 help="Select the number of Forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
