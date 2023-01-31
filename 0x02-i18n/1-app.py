#!/usr/bin/env python3
"""Sets up a basic flask app"""

from flask_babel import Babel
from flask import Flask

app = Flask(__name__)
babel = Babel(app)


class Config:
    """configures other languages in our app"""
    LANGUAGES = ["en", "fr"]
