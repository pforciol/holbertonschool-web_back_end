#!/usr/bin/env python3
""" Auth module. """
import requests
URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """ Register the user with the given email and password """
    task_name = "Register user:"
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(f"{URL}/users", data=data)
    assert response.status_code == 200, f"{task_name} test failed"
    print(f"{task_name} test passed")


def log_in_wrong_password(email: str, password: str) -> None:
    """ Log in with a wrong password """
    task_name = "Log in wrong password:"
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(f"{URL}/sessions", data=data)
    assert response.status_code == 401, f"{task_name} test failed"
    print(f"{task_name} test passed")


def log_in(email: str, password: str) -> str:
    """ Log in with the right password """
    task_name = "Log in right password:"
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(f"{URL}/sessions", data=data)
    assert response.status_code == 200, f"{task_name} test failed"
    print(f"{task_name} test passed")
    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """ Check if user is logged, must fail """
    task_name = "Profile unlogged:"
    cookies = {
        "session_id": "no_session_id"
    }
    response = requests.get(f"{URL}/profile", cookies=cookies)
    assert response.status_code == 403, f"{task_name} test failed"
    print(f"{task_name} test passed")


def profile_logged(session_id: str) -> None:
    """ Check if user is logged, must work """
    task_name = "Profile logged:"
    cookies = {
        "session_id": session_id
    }
    response = requests.get(f"{URL}/profile", cookies=cookies)
    assert response.status_code == 200, f"{task_name} test failed"
    print(f"{task_name} test passed")


def log_out(session_id: str) -> None:
    """ Log out the user """
    task_name = "Log out user:"
    cookies = {
        "session_id": session_id
    }
    response = requests.delete(f"{URL}/sessions", cookies=cookies)
    assert response.status_code == 200, f"{task_name} test failed"
    print(f"{task_name} test passed")


def reset_password_token(email: str) -> str:
    """ Reset the password of a user with a token """
    task_name = "Reset password with token:"
    data = {
        "email": email
    }
    response = requests.post(f"{URL}/reset_password", data=data)
    assert response.status_code == 200, f"{task_name} test failed"
    print(f"{task_name} test passed")
    return response.json().get("reset_token")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Update the password according the token """
    task_name = "Update password:"
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    response = requests.put(f"{URL}/reset_password", data=data)
    assert response.status_code == 200, f"{task_name} test failed"
    print(f"{task_name} test passed")


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
