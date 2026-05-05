import sys
import os
import json
from api_list import base_api

# Adds the parent directory to the system path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def load_test_data(filename):
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'inputs', 'users'))
    file_path = os.path.join(base_path, filename)
    with open(file_path, 'r') as f:
        return json.load(f)

def test_put_user_returns_200():
    payload = load_test_data("update_user_put.json")
    response = base_api.put("/users/1", body=payload)
    assert response.status_code == 200

def test_put_user_returns_updated_name():
    payload = load_test_data("update_user_put.json")
    response = base_api.put("/users/1", body=payload)
    json_body = response.json()
    assert json_body["name"] == payload["name"]

def test_put_user_returns_updated_email():
    payload = load_test_data("update_user_put.json")
    response = base_api.put("/users/1", body=payload)
    json_body = response.json()
    assert json_body["email"] == payload["email"]

def test_patch_user_returns_200():
    payload = load_test_data("update_user_patch.json")
    response = base_api.patch("/users/1", body=payload)
    assert response.status_code == 200

def test_patch_user_returns_updated_name():
    payload = load_test_data("update_user_patch.json")
    response = base_api.patch("/users/1", body=payload)
    json_body = response.json()
    assert json_body["name"] == payload["name"]

def test_patch_user_returns_updated_email():
    payload = load_test_data("update_user_patch.json")
    response = base_api.patch("/users/1", body=payload)
    json_body = response.json()
    assert json_body["email"] == payload["email"]

def test_put_nonexistent_user_returns_500_or_404():
    payload = load_test_data("update_user_put.json")
    response = base_api.put("/users/9999", body=payload)
    assert response.status_code in [404, 500]