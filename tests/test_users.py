import pytest
from api_tests.request_helper import Request


def test_get_users():
    req = Request(endpoint="/users")
    assert req.make_get_request().status_code == 200