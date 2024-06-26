#!/usr/bin/python3
""" 9-states.py """
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """ remove current sqlalchemy session """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ states route """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route("/states/<uuid:id>", strict_slashes=False)
def state(id):
    """ state route """
    state = storage.all(State).get(f'State.{id}')
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    # python3 -m web_flask/9-states
    app.run(host="0.0.0.0", port=5000)
