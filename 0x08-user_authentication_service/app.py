#!/usr/bin/env python3
""" App module. """
from flask import Flask, abort
from flask.globals import request
from flask.helpers import make_response
from flask.json import jsonify

from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def welcome():
    """ / GET endpoint. """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """ /users POST endpoint. """
    email = request.form['email']
    passw = request.form['password']
    try:
        user = AUTH.register_user(email, passw)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """ /sessions POST endpoint. """
    email = request.form['email']
    passw = request.form['password']

    if not AUTH.valid_login(email, passw):
        abort(401)

    session_id = AUTH.create_session(email)
    resp = make_response({"email": email, "message": "logged in"})
    resp.set_cookie("session_id", session_id)

    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
