import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Temperature/date")

with open ("temp.txt","r") as file:
    content = file.read()

df = pd.read_csv("temp.txt")

figure = px.line(df, x="date", y="temperature")

st.plotly_chart(figure)