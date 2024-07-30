#!/usr/bin/env python3
"""Application configuration class"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale():
    """Gets locale from request object"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders a basic html template"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
