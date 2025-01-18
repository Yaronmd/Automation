import pytest
from api_tests.request_helper import Request
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
users_requests = Request(endpoint="/users")

def test_get_users():
    response = users_requests.make_get_request()
    assert response.status_code == 200
    print(response.json())

def test_get_user_by_id():
    response = users_requests.make_get_request(by_id="2")
    assert response.status_code == 200
    print(response.json())

def test_set_user():
    post_data = {
        "firstname": "yaron",
        "lastname": "mordechai",
        "email":"yaronmord@gmail.com"

    }
    response = users_requests.make_post_request(data=post_data)
    assert response.status_code == 201
    print(response.json())

def test_delete_user():
    response = users_requests.make_delete_request(identifier="1")
    assert response.status_code == 200  # Or 200 based on API documentation
    print("Delete operation successful.")