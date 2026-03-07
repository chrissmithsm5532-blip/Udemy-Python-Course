import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Happiness")

x_data = st.selectbox("Select data for x axis",
                     ("GDP","Happiness","Generosity"))

y_data = st.selectbox("Select data for y axis",
                     ("GDP","Happiness","Generosity"))

x_data_label = x_data
y_data_label = y_data

st.subheader(f"{x_data} Vs {y_data}")

x_data = x_data.lower()
y_data = y_data.lower()

df =pd.read_csv("happy.csv")

figure = px.scatter(x = df[f"{x_data}"],y=df[f"{y_data}"],labels= {"x":f"{x_data_label}","y":f"{y_data_label}"})
st.plotly_chart(figure)

