#!/usr/bin/python3
""" 100-hbnb.py """
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def remove_session():
    """ remove session """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb route """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


if __name__ == '__main__':
    # python3 -m web_flask/100-hbnb
    app.run(host="0.0.0.0", port=5000)
