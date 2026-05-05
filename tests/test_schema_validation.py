# import sys
# import os

# Adds the parent directory to the system path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api_list import base_api
from required.helpers import validate_schema

def test_get_all_users_schema():
    response = base_api.get("/users")
    assert response.status_code == 200
    validate_schema(response.json(), "users_list_schema.json")

def test_get_single_user_schema():
    response = base_api.get("/users/1")
    assert response.status_code == 200
    validate_schema(response.json(), "user_schema.json")

def test_get_user_2_schema():
    response = base_api.get("/users/2")
    assert response.status_code == 200
    validate_schema(response.json(), "user_schema.json")

def test_get_user_3_schema():
    response = base_api.get("/users/3")
    assert response.status_code == 200
    validate_schema(response.json(), "user_schema.json")

def test_create_user_response_schema():
    from required.helpers import load_test_data
    payload = load_test_data("users", "create_user.json")
    response = base_api.post("/users", body=payload)
    assert response.status_code == 201
    validate_schema(response.json(), "create_user_response_schema.json")

def test_update_user_response_schema():
    from required.helpers import load_test_data
    payload = load_test_data("users", "update_user_put.json")
    response = base_api.put("/users/1", body=payload)
    assert response.status_code == 200
    validate_schema(response.json(), "user_schema.json")