from flask import Flask, render_template, request
import json

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
