#!/usr/bin/env python3
"""Sets up a basic flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    """creates a home route"""
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run()
