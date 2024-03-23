#!/usr/bin/python3
""" 7-states_list.py """
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def remove_session():
    """ remove session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ states list route """
    states = storage.all()
    remove_session()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    # python3 -m web_flask/7-states_list
    app.run(host="0.0.0.0", port=5000)
