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
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    has_locale = request.args.to_dict().get("locale")
    if has_locale in app.config['LANGUAGES']:
        return has_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """creates a home route"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
