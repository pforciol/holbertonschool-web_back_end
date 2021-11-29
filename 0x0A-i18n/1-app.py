#!/usr/bin/env python3
""" App module. """
from flask import Flask
from flask.templating import render_template
from flask_babel import Babel

app = Flask(__name__)


class Config():
    """ Config class. """
    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def hello_world():
    """ / endpoint. """
    return render_template("1-index.html")
