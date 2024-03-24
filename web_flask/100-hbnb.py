#!/usr/bin/python3
""" 100-hbnb.py """
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """ remove session """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb route """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


if __name__ == '__main__':
    # python3 -m web_flask/100-hbnb
    app.run(host="0.0.0.0", port=5000)
