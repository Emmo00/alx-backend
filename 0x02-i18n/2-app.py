#!/usr/bin/env python3
"""flask app
"""
from typing import List

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


class Config:
    """config object
    """
    LANGUAGES: List[str] = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config())


@app.route('/')
def index() -> None:
    """index page
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
