#!/usr/bin/env python3
""" Auth module
"""
from flask.json import jsonify
from api.v1.views import app_views
from os import getenv
from flask import request, abort
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login_user() -> str:
    """ POST /api/v1/auth_session/login
    """
    email = request.form.get('email', default=None)
    passw = request.form.get('password', default=None)

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not passw:
        return jsonify({"error": "password missing"}), 400
    if email and type(email) is str:
        if passw and type(passw) is str:
            usr = User.search({"email": email})
            if usr:
                if len(usr):
                    usr = usr[0]
                    if not usr.is_valid_password(passw):
                        return jsonify({"error": "wrong password"}), 401
                    else:
                        from api.v1.app import auth
                        session_id = auth.create_session(usr.id)
                        user = jsonify(usr.to_json())
                        user.set_cookie(getenv("SESSION_NAME"), session_id)
                        return user
            else:
                return jsonify({"error": "no user found for this email"}), \
                    404
    return None


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout_user() -> str:
    """ DELETE /api/v1/auth_session/logout
    """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
