import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    #new_year = True
    #text = "Yes" if new_year else "No" and just pass the text
    return  render_template ("index.html",new_year=new_year)

#first variable headline will exist in html file and the second headline will be exist in python file
