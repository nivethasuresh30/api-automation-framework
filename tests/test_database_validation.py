import sys
import os

# Fix path to allow importing from parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api_list import base_api
from required import db_connector
from required.helpers import load_test_data


def setup_module(module):
    """ Runs once before any tests in this file """
    db_connector.create_users_table()
    db_connector.clear_all_users()


def test_create_user_and_verify_in_db():
    payload = load_test_data("users", "create_user.json")
    response = base_api.post("/users", body=payload)
    assert response.status_code == 201

    json_body = response.json()
    user_id = json_body["id"]

    # Sync API result to DB and verify
    db_connector.insert_user(json_body)
    db_record = db_connector.verify_user_exists(user_id)
    assert db_record is not None
    assert db_record["name"] == payload["name"]
    assert db_record["email"] == payload["email"]


def test_get_user_and_sync_to_db():
    response = base_api.get("/users/1")
    assert response.status_code == 200

    json_body = response.json()
    db_connector.insert_user(json_body)

    db_record = db_connector.verify_user_exists(1)
    assert db_record is not None
    assert db_record["id"] == 1
    assert db_record["name"] == json_body["name"]
    assert db_record["email"] == json_body["email"]


def test_update_user_and_verify_in_db():
    payload = load_test_data("users", "update_user_put.json")
    response = base_api.put("/users/1", body=payload)
    assert response.status_code == 200

    json_body = response.json()
    db_connector.insert_user(json_body)

    db_record = db_connector.verify_user_exists(1)
    assert db_record is not None
    assert db_record["name"] == payload["name"]
    assert db_record["email"] == payload["email"]


def test_delete_user_and_verify_in_db():
    # Manually seed a user to delete
    db_connector.insert_user({
        "id": 999,
        "name": "Test User",
        "username": "testuser",
        "email": "test@test.com",
        "phone": "1234567890",
        "website": "test.com"
    })

    db_record_before = db_connector.verify_user_exists(999)
    assert db_record_before is not None

    db_connector.delete_user_from_db(999)
    db_record_after = db_connector.verify_user_exists(999)
    assert db_record_after is None


def test_get_all_users_from_db():
    db_connector.insert_user({
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "phone": "1-770-736-8031",
        "website": "hildegard.org"
    })
    db_connector.insert_user({
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
        "phone": "010-692-6593",
        "website": "anastasia.net"
    })

    all_users = db_connector.get_all_users_from_db()
    assert len(all_users) >= 2


def test_verify_user_deleted_returns_true():
    db_connector.insert_user({
        "id": 888,
        "name": "Delete Me",
        "username": "deleteme",
        "email": "delete@test.com",
        "phone": "0000000000",
        "website": "delete.com"
    })
    db_connector.delete_user_from_db(888)
    result = db_connector.verify_user_deleted(888)
    assert result is True


def teardown_module(module):
    """ Runs once after all tests in this file are finished """
    db_connector.clear_all_users()