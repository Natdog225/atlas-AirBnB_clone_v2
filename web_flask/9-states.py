#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays 'C ' followed by the value of the text variable
                 (replace underscore _ symbols with a space )
    /python/(<text>): Displays 'Python ' followed by the value of the text
                 variable with default value of 'is cool'
    /number/<n>: Displays 'n is a number' only if n is an integer
    /number_template/<n>: Displays an HTML page only if n is an integer
    /number_odd_or_even/<n>: Displays an HTML page only if n is an integer
    /states_list: Displays an HTML page with a list of all State objects
    /cities_by_states: Displays an HTML page with a list of cities by states
    /states: Displays an HTML page with a list of all State objects
    /states/<id>: Displays an HTML page with the details of a State object,
                   or "Not found!" if no match.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C ' followed by the value of the text variable."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python ' followed by the value of the text variable."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if n is an integer."""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page only if n is an integer."""
    return render_template('6-number_odd_or_even.html', n=n)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of cities by states."""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all State objects."""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with the details of a State object."""
    states = storage.all(State)
    state = states.get("State.{}".format(id))
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def close_session(exception):
    """Removes the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
