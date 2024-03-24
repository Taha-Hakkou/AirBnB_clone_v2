#!/usr/bin/python3
""" 10-hbnb_filters.py """
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """ remove current sqlalchemy session """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ hbnb filters route """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    # python3 -m web_flask/10-hbnb_filters
    app.run(host="0.0.0.0", port=5000)
