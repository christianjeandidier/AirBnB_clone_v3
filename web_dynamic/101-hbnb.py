#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid

# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

# Teardown database
@app.teardown_appcontext
def teardown_db(exception):
    """Close SQLAlchemy Session after each request"""
    storage.close()

# Route for hbnb_filters
@app.route('/101-hbnb')
def hbnb_filters():
    """Handles request to custom template with states, cities, and amenities"""
    states = storage.all('State').values()
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = {user.id: f"{user.first_name} {user.last_name}" for user in storage.all('User').values()}
    return render_template('101-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=states,
                           amens=amens,
                           places=places,
                           users=users)

# Main Flask app
if __name__ == "__main__":
    app.run(host=host, port=port)
