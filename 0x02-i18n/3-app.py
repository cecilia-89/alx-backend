#!/usr/bin/env python3
"""Module: 2-app.py"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """configures other languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

def get_locale():
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index():
    """creates a home route"""
    return render_template('3-index.html')

babel = Babel(app, locale_selector=get_locale)

if __name__ == "__main__":
    app.run()
