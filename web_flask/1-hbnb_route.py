#!/usr/bin/python3
""" 1-hbnb_route.py """
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


if __name__ == '__main__':
    # python3 -m web_flask/1-hbnb_route
    app.run(host="0.0.0.0", port=5000)
