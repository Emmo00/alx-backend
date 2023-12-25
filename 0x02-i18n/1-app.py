#!/usr/bin/env python3
"""flask app
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """config object
    """
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config())


@app.route('/')
def index() -> None:
    """index page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
