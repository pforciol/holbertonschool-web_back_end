#!/usr/bin/env python3
""" App module. """
from flask import Flask, abort, redirect
from flask.globals import request
from flask.helpers import make_response, url_for
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


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ /sessions DELETE endpoint. """
    user = AUTH.get_user_from_session_id(request.cookies["session_id"])
    if user:
        AUTH.destroy_session(user.id)
        return redirect(url_for('welcome'))
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """ /profile GET endpoint. """
    user = AUTH.get_user_from_session_id(request.cookies["session_id"])
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """ /reset_password POST endpoint. """
    email = request.form['email']
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """ /reset_password PUT endpoint. """
    email = request.form['email']
    reset_token = request.form['reset_token']
    new_password = request.form['new_password']
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
