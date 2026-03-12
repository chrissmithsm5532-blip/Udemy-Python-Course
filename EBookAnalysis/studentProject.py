import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

# backend

analyzer = SentimentIntensityAnalyzer()

initial_value =21

file_location = f"diary/2023-10-{initial_value}.txt"

dates=[]
review_pos=[]
review_neg=[]


for i in range(7):

    with open (file_location) as file:
        entry = file.read()
        scores = analyzer.polarity_scores(entry)
        review_neg.append(scores['neg'])
        review_pos.append(scores['pos'])
        dates.append("Oct " + str(initial_value))
        initial_value = initial_value + 1
        file_location = f"diary/2023-10-{initial_value}.txt"

print(dates,review_pos,review_neg)

#front end
st.title("Diary Tone")

st.header("Positivity")

#postive chart

pos_data = {
    "2023 date": dates,
    "Positivity": review_pos
}

fig = px.line(pos_data, x="2023 date", y="Positivity", title="Simple Plotly Line Chart")

st.plotly_chart(fig)

#negative chart

st.header("Negativity")

neg_data = {
    "2023 date": dates,
    "Negativity": review_neg
}

fig = px.line(neg_data, x="2023 date", y="Negativity", title="Simple Plotly Line Chart",)

st.plotly_chart(fig)



