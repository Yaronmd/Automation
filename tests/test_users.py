import pytest
from api_tests.request_helper import Request
from selenium.webdriver.common.by import By

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
    driver.get("https://www.google.com")

    # Find the search box and input "Selenium"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium")
    search_box.submit()

    # Assert that the title contains the word "Selenium"
    assert "Selenium" in driver.title