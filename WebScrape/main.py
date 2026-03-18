import requests
import selectorlib
from send_email import send_email
import time
import sqlite3

# "INSERT INTO events VALUES ('Smashing Pumpkins','New York','2026.11.27')"
# "SELECT * FROM events WHERE date = '2026.07.24'"
# "DELETE FROM events WHERE band = 'Pearl Jam'"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

URL = "https://programmer100.pythonanywhere.com/tours/"

connection = sqlite3.connect('data.db')


def scrape(url):
    """Scrape the page source"""
    response = requests.get(url,headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    values = extractor.extract(source)["tours"]
    return values


def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)",row)
    connection.commit()


def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band,city,date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band =? AND city =? AND date =?",(band,city,date))
    rows = cursor.fetchall()
    return rows

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
               # send_email(message= "New Tour has been added")
        time.sleep(2)
