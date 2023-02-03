#!/usr/bin/env python3
"""Module: 5-app.py"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from datetime import datetime
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """configures other languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
#babel = Babel(app)
app.config.from_object(Config)


#@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    has_locale = request.args.to_dict().get("locale")
    if has_locale in app.config['LANGUAGES']:
        return has_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


#@babel.timezoneselector
def get_timezone():
    """determines the timezone"""

    has_timezone = request.args.to_dict()
    user_timezone = g.user

    for i in [has_timezone, user_timezone]:
        try:
            time_zone = i.get('timezone')
            pytz.timezone(time_zone).zone
            return time_zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']

Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/', strict_slashes=False)
def index():
    """creates a home route"""
    return render_template('index.html')


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
    zone = get_timezone()

    format = "%b-%d-%Y %H:%M:%S %p"
    now_utc = datetime.now(pytz.timezone('UTC'))
    diff_utc = now_utc.astimezone(pytz.timezone(zone))
    g.timezone = diff_utc.strftime(format)


if __name__ == "__main__":
    app.run()
