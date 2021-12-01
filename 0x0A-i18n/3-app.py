#!/usr/bin/env python3
""" App module. """
from flask import Flask, request
from flask.templating import render_template
from flask_babel import Babel
app = Flask(__name__)


class Config():
    """ Config class. """
    LANGUAGES = ["en", "fr"]

    Babel.default_locale = "fr"
    Babel.default_timezone = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Determines the best match with our supported language. """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello_world():
    """ / endpoint. """
    return render_template("3-index.html")
