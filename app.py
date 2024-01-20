import os
import subprocess
from flask import Flask, render_template, request
import json

# Check if data.json exists and is not empty
if not os.path.exists("data.json") or os.path.getsize("data.json") == 0:
    # Call generate_data.py
    subprocess.call(["python", "generate_data.py"])

# Load the data
with open("data.json", "r") as f:
    results = json.load(f)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    q = request.args.get("q")
    filtered_results = [
        result for result in results if q.lower() in result["title"].lower()
    ]

    return render_template("search_result.html", results=filtered_results)
