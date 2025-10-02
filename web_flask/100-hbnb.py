#!/usr/bin/python3
"""
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    """displays html page for states, cities and their amenities"""
    data = {
        "states": storage.all('State').values(),
        "cities": storage.all('City').values(),
        "places": storage.all('Place').values(),
        "amenities": storage.all('Amenity').values()
    }

    return render_template('100-hbnb.html', models=data)


@app.teardown_appcontext
def remove_session(self):
    """close the db"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
