import requests
import selectorlib
from datetime import datetime
import sqlite3
from datetime import datetime
import streamlit as st
import plotly.express as px



HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

URL = "https://programmer100.pythonanywhere.com"

connection = sqlite3.connect('temp.db')


def scrape(url):
    """Scrape the page source"""
    response = requests.get(url,headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("temp.yaml")
    values = extractor.extract(source)["temp"]
    return values


def store(extracted):
       cursor = connection.cursor()
       date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       cursor.execute("INSERT INTO Temperatures VALUES(?,?)", (date_now,extracted))
       connection.commit()


def read_dates():
    cursor = connection.cursor()
    cursor.execute("SELECT date FROM Temperatures")
    dates = cursor.fetchall()
    dates = [(t[0]) for t in dates]
    #datetime.strptime("2026-03-18 15:39:45", "%Y-%m-%d %H:%M:%S")
    dates = [datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in dates]
    print(dates)
    return dates

def read_temperatures():
    cursor = connection.cursor()
    cursor.execute("SELECT temperature FROM Temperatures")
    temperatures = cursor.fetchall()
    temperatures = [int(t[0]) for t in temperatures]
    print(temperatures)
    return temperatures

if __name__ == "__main__":
        scraped = scrape(URL)
        extracted = extract(scraped)
        store(extracted)
        dates = read_dates()
        temps = read_temperatures()
        st.title("Temperature/date")
        figure = px.line(
            x=dates,
            y=temps,
            labels={"x": "Date", "y": "Temperature"},
            title="Temperature Over Time"
        )

        st.plotly_chart(figure)




