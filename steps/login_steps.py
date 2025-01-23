from conftest import Navigation,LoginPage
import pytest
import allure
from config.config import UI_BASE_PAGE,UI_USERNAME,UI_PASSWORD

@allure.step(f"Navigate to {UI_BASE_PAGE} and login")
@pytest.fixture
def navigate_and_login(navigation_page:Navigation,login_page:LoginPage):
    assert navigation_page.go_to_end_point(UI_BASE_PAGE)
    assert login_page.login(username=UI_USERNAME,password=UI_PASSWORD)