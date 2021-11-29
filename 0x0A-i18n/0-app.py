#!/usr/bin/env python3
""" App module. """
from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """ / endpoint. """
    return render_template("0-index.html")
