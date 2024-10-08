#!/usr/bin/env python3
"""basic flask application"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """configuration class application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# initiate application obj with babel
app = Flask(__name__)
app.config.from_object(Config)
# Wrap the application with Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Gets locale from request object"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """renders a basic html template"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
