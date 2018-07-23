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
# will need to add in authentication button for each channel
# - social media - 
@app.route("/stats/facebook")
def test():
    r = requests.get("https://facebook.com")
    return r.text

@app.route("/stats/twitter")
def test1():
    r = requests.get("https://twitter.com")
    return r.text

@app.route("/stats/pinterest")
def test2():
    r = requests.get("https://pinterest.com")
    return r.text

@app.route("/stats/youtube")
def test3():
    r = requests.get("https://youtube.com")
    return r.text

# - analytics channels - adwords, analytics, etc


if __name__ == "__main__":
    app.run()
