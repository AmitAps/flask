import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return  render_template ("index.html")

#first variable headline will exist in html file and the second headline will be exist in python file

@app.route("/more")
def more():
    return  render_template ("more.html")