from datetime import datetime
import time
import requests
import selectorlib
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

connection = sqlite3.connect("data.db")
cursor = connection.cursor()


def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yml")
    value = extractor.extract(source)["test"]
    return value

def store(extracted):
    row = extracted
    current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    cursor.execute("INSERT INTO events VALUES(?,?)", (current_datetime, row))
    connection.commit()

def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    date, temp = row
    cursor.execute("SELECT * FROM events WHERE date=? AND temp=?",(date,temp))
    rows = cursor.fetchall()
    print(rows)
    return rows

if __name__ == "__main__":

    while True:
        scrapped = scrape(URL)
        extracted = extract(scrapped)
        print(extracted)
        store(extracted)


        time.sleep(2)  # wait for 1 minute before scraping again