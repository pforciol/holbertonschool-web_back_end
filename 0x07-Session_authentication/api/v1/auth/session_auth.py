#!/usr/bin/env python3
""" SessionAuth module
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
            Creates a Session based on user_id

            Args:
                user_id: the id of the user

            Returns:
                The Session ID or None
        """
        if user_id and type(user_id) is str:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            Retrieve an User id based on a Session ID

            Args:
                session_id: the id of the session

            Returns:
                The User ID or None
        """
        if session_id and type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        """
            Retrieve a User

            Args:
                request: the request

            Returns:
                A User instance based on a cookie value
        """
        id = self.user_id_for_session_id(self.session_cookie(request))
        if id:
            return User.get(id)

    def destroy_session(self, request=None) -> bool:
        """
            Deletes a Session

            Args:
                request: the request

            Returns:
                True or False
        """
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                if self.user_id_for_session_id(session_id):
                    del self.user_id_by_session_id[session_id]
                    return True
        return False
