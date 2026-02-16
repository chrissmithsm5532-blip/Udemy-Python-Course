import requests

API_KEY = "04c94b60172c4b8a89d30b73e79c438b"

url = ("https://newsapi.org/v2/everything?q=tesla&from=2026-01-16"
       "&sortBy=publishedAt&apiKey=04c94b60172c4b8a89d30b73e79c438b")

request = requests.get(url)

content= request.json()

print(content['articles'])

for article in content['articles']:
       print(article['title'])
       print(article['description'])