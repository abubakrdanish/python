from datetime import datetime
import time
import requests
import selectorlib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# Initialize an empty DataFrame
df = pd.DataFrame(columns=["Time", "Extracted"])

def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yml")
    value = extractor.extract(source)["test"]
    return value

def store(extracted):
    global df
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("data.txt", "a") as file:
        file.write(formatted_now + "," + extracted + "\n")

    # Append the new data to the DataFrame
    new_row = pd.DataFrame({"Time": [formatted_now], "Extracted": [extracted]})
    df = pd.concat([df, new_row], ignore_index=True)

if __name__ == "__main__":
    st.title("Real-time Data Extraction and Visualization")

    plt.ion()  # Enable interactive mode

    while True:
        scrapped = scrape(URL)
        extracted = extract(scrapped)
        print(extracted)
        store(extracted)

        with open("data.txt", "r") as file:
            data = file.read()



        # Plot the data
        lines = data.split("\n")
        x = []
        y = []
        for line in lines:
            parts = line.split(",")
            if len(parts) > 1:
                x.append(parts[0])
                y.append(parts[1])
        plt.plot(x, y, 'bo-', linewidth=2, markersize=5)  # Plot the data with a blue line and markers
        plt.xlabel("Time")
        plt.ylabel("Extracted")
        plt.title("Real-time Data Extraction and Visualization")
        st.pyplot(plt)  # Display the plot in Streamlit
        plt.clf()  # Clear the plot for the next iteration

        time.sleep(2)
        plt.clf()
        plt.close()