#!/usr/bin/env python3
""" Auth module. """
from typing import Union
from db import DB
from user import User
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """ Hash the password passed in input. """
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Generate a uuid. """
    return str(uuid.uuid4())


class Auth:
    """ Auth class to interact with the authentication database. """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Add a user to the DataBase. """
        try:
            self._db.find_user_by(email=email)
        except Exception:
            return self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """ Chek if the request has correct credentials. """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(str.encode(password), user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """ Create a session related to a user. """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ Get a user from his login session. """
        if session_id:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except Exception:
                return None
        return None

    def destroy_session(self, user_id: int) -> None:
        """ Destroy a user login session. """
        if user_id:
            self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """ Generate a reset token for the user. """
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return str(token)
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update the password with a token. """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            self._db.update_user(user.id,
                                 hashed_password=_hash_password(password),
                                 reset_token=None)
        except Exception:
            raise ValueError
        return None
