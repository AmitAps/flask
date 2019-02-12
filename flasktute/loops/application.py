import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    names = ["Amit", "Julie","Aps","Ankit"]
    return  render_template ("index.html",names=names)

#first variable headline will exist in html file and the second headline will be exist in python file
