#!/usr/bin/env python3
"""7-app"""
from flask import Flask, g, request, render_template
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    g.user = get_user()


@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale:
        return locale
    if g.user and g.user['locale']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone)
        except UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone']:
        try:
            return pytz.timezone(g.user['timezone'])
        except UnknownTimeZoneError:
            pass
    return pytz.timezone('UTC')


@app.route('/')
def index():
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run()
