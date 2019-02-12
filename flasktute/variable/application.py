from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    headline = "Hello,World"
    return  render_template ("index.html", headline=headline)

#first variable headline will exist in html file and the second headline will be exist in python file
@app.route("/bye")
def bye():
    headline = "Good Bye"
    return  render_template ("index.html", headline=headline)
