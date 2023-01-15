#!/usr/bin/python3
"""Starts a Flask web application
"""
from flask import Flask

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        """Display 'Hello HBNB!'
        """
        return 'Hello HBNB!'

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """Display 'HBNB'
        """
        return 'HBNB'

    @app.route('/c/<text>', strict_slashes=False)
    def c(text):
        """Display “C ” followed by the value of
        the text variable (replace underscore _
        symbols with a space)
        """
        return 'C ' + text.replace('_', ' ')

    app.run('0.0.0.0')
