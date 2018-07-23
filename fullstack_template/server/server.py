from flask import Flask, render_template
import requests

app = Flask(__name__, static_folder="../static/dist",
template_folder="../static")

#possible login feature
@app.route("/")
def index():
    return render_template("index.html")

#possible favorites dashboard - save your favorite graphs here
@app.route("/dashboard")
def hello():
    return "Hello World!"

#each channel should have their own statistics
@app.route("/stats")
def test():
    r = requests.get("https://google.com")
    return r.text

if __name__ == "__main__":
    app.run()
