#!/usr/bin/python3
""" 6-number_odd_or_even.py """
from flask import Flask, render_template
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ number template """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ number odd or even """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    # python3 -m web_flask/6-number_odd_or_even
    app.run(host="0.0.0.0", port=5000)
