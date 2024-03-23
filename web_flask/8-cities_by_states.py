#!/usr/bin/python3
""" 8-cities_by_states.py """
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def remove_session():
    """ remove session """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ cities by states route """
    states = storage.all()
    remove_session()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    # python3 -m web_flask/8-cities_by_states
    app.run(host="0.0.0.0", port=5000)
