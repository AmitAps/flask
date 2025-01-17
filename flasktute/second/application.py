from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World"


@app.route("/amit")
def amit():
    return "Hello, Amit"


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}</h1>"