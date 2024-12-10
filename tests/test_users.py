import pytest
from api_tests.request_helper import Request
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pages.base_page import SeleniumBasePage
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

def test_google(driver):
    # Navigate to Google
    base_page = SeleniumBasePage(driver=driver)
    base_page.go_to_end_point("https://www.google.com")
    base_page.send_keys(by_locator=(By.NAME,"q"),keys="Selenium"+Keys.ENTER)
    assert base_page.validate_title("Selenium",wait_before_action=5)
