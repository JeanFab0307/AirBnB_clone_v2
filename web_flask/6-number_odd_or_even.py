#!/usr/bin/python3
"""starts a flask web app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    newText = text.replace('_', ' ')
    return 'C {}'.format(newText)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text=None):
    if text is None:
        newText = 'is cool'
    else:
        newText = text.replace('_', ' ')
    return 'Python {}'.format(newText)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    return render_template('5-number.html', Number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', Number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
