#!/usr/bin/python3
"""Starts a Flask web application
"""
from flask import Flask
from flask import render_template, url_for
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

if __name__ == '__main__':
    app = Flask(__name__, static_url_path='')

    @app.route('/', strict_slashes=False)
    def index():
        """Display 'Hello HBNB!'
        """
        return 'Hello HBNB!'

    @app.route('/c/<text>', strict_slashes=False)
    def c(text):
        """Display “C ” followed by the value of
        the text variable (replace underscore _
        symbols with a space)
        """
        return 'C ' + text.replace('_', ' ')

    @app.route('/python/')
    @app.route('/python/<text>', strict_slashes=False)
    def python(text="is cool"):
        """Display “Python ”, followed by the value of
        the text variable (replace underscore _
        symbols with a space )
        """
        return 'Python ' + text.replace('_', ' ')

    @app.route('/number/<int:n>', strict_slashes=False)
    def number(n):
        """Display “n is a number” only if n is an integer
        """
        return str(n) + ' is a number'

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_template(n):
        """Display a HTML page only if n is an integer
        """
        return render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def number_odd_or_even(n):
        """Display a HTML page only if n is an integer
        """
        parity = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', n=n, parity=parity)

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        """Display a HTML page of the States
        """
        states = storage.all(State).values()
        return render_template('7-states_list.html', states=states)

    @app.route('/cities_by_states', strict_slashes=False)
    def cities_by_states():
        """Display a HTML page of the States and the
        Cities by State
        """
        states = storage.all(State).values()
        cities = list()

        for state in states:
            for city in state.cities:
                cities.append(city)

        return render_template('8-cities_by_states.html',
                               states=states, state_cities=cities)

    @app.route('/states', strict_slashes=False)
    def states():
        """Display a HTML page of all States
        """
        states = storage.all(State).values()
        return render_template('7-states_list.html', states=states)

    @app.route('/states/<id>', strict_slashes=False)
    def get_state_by_uuid(id):
        """Display a HTML page of a State and their cities
        """
        states = storage.all(State).values()

        for state in states:
            if id == state.id:
                return render_template('9-states.html',
                                       state=state, state_cities=state.cities)

        return render_template('9-states.html', not_found=True)

    @app.route('/hbnb_filters', strict_slashes=False)
    def hbnb_filters():
        states = storage.all(State).values()
        amenities = storage.all(Amenity).values()
        cities = list()

        for state in states:
            for city in state.cities:
                cities.append(city)

        return render_template('10-hbnb_filters.html',
                               states=states, state_cities=cities,
                               amenities=amenities)

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        states = storage.all(State).values()
        amenities = storage.all(Amenity).values()
        places = storage.all(Place).values()
        users = storage.all(User).values()
        cities = list()
        owners = list()

        for state in states:
            for city in state.cities:
                cities.append(city)

        for place in places:
            for user in users:
                if place.user_id == user.id:
                    owners.append(user)

        return render_template('100-hbnb.html',
                               states=states, state_cities=cities,
                               amenities=amenities, places=places,
                               owners=owners)

    @app.teardown_appcontext
    def teardown_db(error):
        """Closes the database again at the end of the request.
        """
        storage.close()

    app.run('0.0.0.0')
