#!/usr/bin/env python3
""" encrypt_password module """

import bcrypt


def hash_password(password: str) -> bytes:
    """

        Args:
            password: the password to encrypt

        Returns:
            A salted and hashed password.

    """
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """

        Args:
            hashed_password: the hashed password
            password: the password to encrypt

        Returns:
            True if password is valid, False else.

    """
    return bcrypt.checkpw(str.encode(password), hashed_password)
