#!/usr/bin/env python3
"""Module: 2-app.py"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, lazy_gettext as _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)
babel = Babel(app)


class Config:
    """configures other languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
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
    return render_template('5-index.html')


def get_user():
    """returns a logged in user"""
    has_user = request.args.to_dict().get("login_as")
    if has_user is not None:
        return users.get(int(has_user))


@app.before_request
def before_request():
    """executes before all other functions"""
    user = get_user()
    g.user = user


if __name__ == "__main__":
    app.run()
