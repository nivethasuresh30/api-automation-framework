# import sys
# import os
#
# # Adds the parent directory to the system path
# # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api_list import base_api

def test_delete_user_returns_200():
    response = base_api.delete("/users/1")
    assert response.status_code == 200

def test_delete_user_response_is_empty():
    response = base_api.delete("/users/1")
    json_body = response.json()
    # Some APIs return an empty dict, others return None/null
    assert json_body == {}

def test_delete_nonexistent_user_returns_200_or_404():
    response = base_api.delete("/users/9999")
    assert response.status_code in [200, 404]