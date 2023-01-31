#!/usr/bin/env python3
"""Sets up a basic flask app"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """creates a home route"""
    return render_template('0-index.html')


class Config:
    """configures other languages in our app"""
    LANGUAGES = ["en", "fr"]


if __name__ == "__main__":
    app.run()
