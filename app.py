from flask import Flask, render_template
from retrip_scraper import fetch_spots

app = Flask(__name__)

@app.route("/")
def index():
    results = fetch_spots()
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
