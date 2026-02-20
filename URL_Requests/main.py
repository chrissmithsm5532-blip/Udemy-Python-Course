import requests`
from send_email import send_email

API_KEY = "04c94b60172c4b8a89d30b73e79c438b"
topic = "tesla"

url = (f"https://newsapi.org/v2/everything?q={topic}&from=2026-01-16"
       "&sortBy=publishedAt&apiKey=04c94b60172c4b8a89d30b73e79c438b&language=en")

request = requests.get(url)

content= request.json()

print(content['articles'])

message = ""

for article in content['articles'][:20]:
       message = message + (f"Title:         {article['title']}\nDescription:"
                            f"   {article['description']}\n"
                            + f"{article["url"]}\n\n")
message = "Subject: Today's News" + "\n" + message
message = message.encode("utf-8")
send_email(message)