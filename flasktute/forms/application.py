from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/")
def index():
    return  render_template ("index.html")

#first variable headline will exist in html file and the second headline will be exist in python file

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form Instead!! This method is not allowed"
    else:
        name = request.form.get("something").capitalize()
        return  render_template ("hello.html", name=name)