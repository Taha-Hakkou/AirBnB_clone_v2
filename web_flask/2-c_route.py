#!/usr/bin/python3
""" 2-c_route.py """
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


if __name__ == '__main__':
    # python3 -m web_flask/2-c_route
    app.run(host="0.0.0.0", port=5000)
