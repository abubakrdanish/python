from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dictionary data from the CSV file
df = pd.read_csv("dictionary.csv")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def get_definition(word):
    definition = df.loc[df["word"] == word]['definition'].squeeze()
    result_dictionary = {'word': word, 'definition': definition}
    return result_dictionary




if __name__ == "__main__":
    app.run(debug=True)
