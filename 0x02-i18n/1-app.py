#!/usr/bin/env python3
"""A Basic flask application"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Application configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)
# Wrap the application with Babel
babel = Babel(app)


@app.route('/')
def index():
    """Renders a basic html template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
