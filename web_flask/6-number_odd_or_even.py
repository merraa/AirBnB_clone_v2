#!/usr/bin/python3
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    '''
    Hello route
    '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''
    HBNB route
    '''
    return 'HBNB:'


@app.route('/c/<text>')
def c_text(text):
    '''
    /c/<text> route
    '''
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    '''
    /python/<text> route
    '''
    return 'Python {}'.format(escape(text.replace('_', ' ')))


@app.route('/number/<n>')
def number_route(n):
    '''
    /number/<n> route
    '''
    return '{} is a number'.format(int(n))


@app.route('/number_template/<n>')
def number_template(n):
    '''
    /number_template/<n> route
    '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_or_odd(n):
    '''
    /number_odd_or_even/<n> route
    '''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
