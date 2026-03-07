import streamlit as st
import plotly.express as px
from pandas.core.resample import get_resampler

from backend import get_data
from plotly.graph_objs.surface.contours import y

# add UI
st.title("Weather Forecast for Next days")
place = st.text_input("Place: ")
days = st.slider("ForeCast", 1, 5,
                 help="Select the number of Forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

#get Temperature/Sky data
if place:
    try:
        filtered_data = get_data(place,days)
        if option == "Temperature":
            #plot Temperature Data
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            corrected_temp = [t / 10 for t in temperatures]
            figure = px.line(x = dates, y= corrected_temp, labels= {"x":"Date","y":"Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            #Display Sky data
            image_list = []
            for condition in sky_conditions:
                image_list.append(f"images/{condition}.png")
            st.image(image_list,width=115)
    except KeyError:
            st.write("That place does not exist")



