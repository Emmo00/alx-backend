#!/usr/bin/env python3
"""flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """index page
    """
    return render_template('0-index.html')


app.run('0.0.0.0', 5000, debug=True)
