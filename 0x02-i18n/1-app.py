#!/usr/bin/env python3
"""Sets up a basic flask app"""

from flask import request
from flask_babel import Babel
app = __import__('0-app').app

babel = Babel(app)

class Config:
    """configures other languages in our app"""
    LANGUAGES = ["en", "fr"]

