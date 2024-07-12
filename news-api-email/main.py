import requests
from send_email import send_email

api_key = "9d67c2c60b464dfba5c4728fd0abc690"
topic = "tesla"
url = f"https://newsapi.org/v2/everything?q={topic}&fsortBy=published&apiKey=9d67c2c60b464dfba5c4728fd0abc690&language=en"

request = requests.get(url)
content = request.json()

body = "Subject: Today's news\n"
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body += article["title"] + "\n" \
            + article["description"] \
                + "\n" + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)
