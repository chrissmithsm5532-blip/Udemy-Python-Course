import requests
import selectorlib
from datetime import datetime


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

URL = "https://programmer100.pythonanywhere.com"


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
    with open("temp.txt", "a") as file:
        now = datetime.now()
        file.write(now.strftime("%Y-%m-%d %H:%M:%S, ") + extracted + "\n")


def read():
    with open("data.txt", "r") as file:
        return file.read()



if __name__ == "__main__":
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        content= read()
        store(extracted)

