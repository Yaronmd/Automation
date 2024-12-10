import pytest
from api_tests.request_helper import Request

users_requests = Request(endpoint="/users")

def test_get_users():
    assert users_requests.make_get_request().status_code == 200


def test_set_user():
    post_data = {
        "firstname": "yaron",
        "lastname": "mordechai",
        "email":"yaronmord@gmail.com"

    }
    response = users_requests.make_post_request(data=post_data)
    assert response.status_code == 201
    print(response.json())
   