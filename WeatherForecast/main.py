import streamlit as st
import plotly.express as px
from pandas.core.resample import get_resampler

from backend import getData
from plotly.graph_objs.surface.contours import y

st.title("Weather Forecast for Next days")
place = st.text_input("Place: ")
days = st.slider("ForeCast", 1, 5,
                 help="Select the number of Forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

d,t = getData(place,days,option)



figure = px.line(x = d,y=t,labels= {"x":"Date","y":"Temperature (C)"})
st.plotly_chart(figure)