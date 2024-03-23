#!/usr/bin/python3
""" 4-number_route.py """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """ hello route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """ hbnb route """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ c route """
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """ python route """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """ number route """
    return f"{n} is a number"


if __name__ == '__main__':
    # python3 -m web_flask/4-number_route
    app.run(host="0.0.0.0", port=5000)
