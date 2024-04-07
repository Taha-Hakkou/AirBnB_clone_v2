#!/usr/bin/python3
""" 7-states_list.py """
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """ remove current sqlalchemy session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ states list route """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    # python3 -m web_flask/7-states_list
    app.run(host="0.0.0.0", port=5000)
