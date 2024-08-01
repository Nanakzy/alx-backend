#!/usr/bin/env python3
"""
This module defines a basic Flask application with Babel for internationalization.
It includes routes, configurations, and user management with mock data.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

class Config:
    """
    Config class for Flask app configuration.
    
    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for Babel.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

def get_user():
    """
    Retrieves the user dictionary based on the login_as URL parameter.

    Returns:
        dict or None: The user dictionary if the user is found, otherwise None.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    """
    Sets the global user before each request.
    """
    g.user = get_user()

@babel.localeselector
def get_locale():
    """
    Determines the best match for supported languages based on URL parameter,
    user settings, or request headers.

    Returns:
        str: The best matched locale.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    Renders the index template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run()
