#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template
from models import storage
import uuid

# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

# Teardown function
@app.teardown_appcontext
def teardown_db(exception):
    """
    After each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()

# Route for rendering the custom template
@app.route('/1-hbnb')
def hbnb_filters(the_id=None):
    """
    Handles request to custom template with states, cities & amenities
    """
    # Retrieve data from the storage
    state_objs = storage.all('State').values()
    states = {state.name: state for state in state_objs}
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = {user.id: "{} {}".format(user.first_name, user.last_name)
             for user in storage.all('User').values()}

    # Render the template
    return render_template('1-hbnb.html',
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
