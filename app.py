from flask import Flask, render_template
import sqlite3

connection = sqlite3.connect("files.db")

cursor = connection.cursor()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

app.run(host="0.0.0.0", port=3000)