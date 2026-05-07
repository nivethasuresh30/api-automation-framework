import os
import json
from api_list import base_api

# def load_test_data(filename):
#     # Fixed 'file' to '__file__' and aligned the logic
#     base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'inputs', 'users'))
#     file_path = os.path.join(base_path, filename)
#     with open(file_path, 'r') as f:
#         return json.load(f)

def load_test_data(filename):

    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'inputs', 'users'))
    file_path = os.path.join(base_path, filename)
    print(f"\nLooking for file at: {file_path}")
    with open(file_path, 'r') as f:
        return json.load(f)

def test_create_user_returns_201():
    payload = load_test_data("create_user.json")
    response = base_api.post("/users", body=payload)
    assert response.status_code == 201

def test_create_user_returns_correct_name():
    payload = load_test_data("create_user.json")
    response = base_api.post("/users", body=payload)
    json_body = response.json()
    assert json_body["name"] == payload["name"]

def test_create_user_returns_correct_email():
    payload = load_test_data("create_user.json")
    response = base_api.post("/users", body=payload)
    json_body = response.json()
    assert json_body["email"] == payload["email"]

def test_create_user_returns_id():
    payload = load_test_data("create_user.json")
    response = base_api.post("/users", body=payload)
    json_body = response.json()
    assert "id" in json_body
    assert json_body["id"] is not None

def test_create_user_response_has_correct_structure():
    payload = load_test_data("create_user.json")
    response = base_api.post("/users", body=payload)
    json_body = response.json()
    assert "id" in json_body
    assert "name" in json_body
    assert "email" in json_body

