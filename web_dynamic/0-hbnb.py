#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""

# Import necessary modules
from flask import Flask, render_template
from models import storage
import uuid

# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# Define functions
@app.teardown_appcontext
def teardown_db(exception):
    """
    After each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.route('/0-hbnb')
def hbnb_filters(the_id=None):
    """
    Handles request to custom template with states, cities & amenities
    """
    # Retrieve data from the storage
    state_objs = storage.all('State').values()
    states = dict([(state.name, state) for state in state_objs])
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([(user.id, "{} {}".format(user.first_name, user.last_name))
                  for user in storage.all('User').values()])

    # Render the template
    return render_template('0-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=states,
                           amens=amens,
                           places=places,
                           users=users)


# Main function
if __name__ == "__main__":
    """
    MAIN Flask App
    """
    app.run(host=host, port=port)
