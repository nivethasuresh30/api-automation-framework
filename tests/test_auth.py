# import sys
# import os

# Adds the parent directory to the system path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api_list import base_api

def test_get_all_users_returns_200():
    response = base_api.get("/users")
    assert response.status_code == 200

def test_get_all_users_returns_list():
    response = base_api.get("/users")
    json_body = response.json()
    assert isinstance(json_body, list)
    assert len(json_body) > 0

def test_get_single_user_returns_200():
    response = base_api.get("/users/1")
    assert response.status_code == 200

def test_get_single_user_has_correct_id():
    response = base_api.get("/users/1")
    json_body = response.json()
    assert json_body["id"] == 1

def test_get_single_user_has_name():
    response = base_api.get("/users/1")
    json_body = response.json()
    assert "name" in json_body
    assert json_body["name"] is not None

def test_get_nonexistent_user_returns_404():
    response = base_api.get("/users/9999")
    assert response.status_code == 404


def test_get_users_with_session(api_session, base_url):
    # Uses the base_url and session fixtures automatically
    response = api_session.get(f"{base_url}/users")

    # Assertions
    assert response.status_code == 200
    assert isinstance(response.json(), list)