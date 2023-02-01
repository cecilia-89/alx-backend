#!/usr/bin/env python3
"""Sets up a basic flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """creates a home route"""
    return render_template('2-index.html')


class Config:
    """configures other languages in our app"""
    LANGUAGES = ["en", "fr"]


@babel.localselector
def get_locale():
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
