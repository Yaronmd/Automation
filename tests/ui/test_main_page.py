import pytest
from pytest import fixture
import allure

from config.config import UI_BASE_PAGE,UI_PASSWORD,UI_USERNAME
from pages.base_pages.navigation import Navigation
from pages.login_page.login_page import LoginPage
from pages.main_page.main_page import MainPage

@pytest.fixture
def navigate(driver):
    naviagtion = Navigation(driver=driver)
    assert naviagtion.go_to_end_point(url=UI_BASE_PAGE)

@pytest.fixture
def login(driver,navigate):
    login_page = LoginPage(driver=driver)
    assert login_page.login(username=UI_USERNAME,password=UI_PASSWORD)

@allure.feature("Essential features")
@allure.title("Validate len of cards")
def test_validate_len_of_cards(driver,login):
    main_page = MainPage(driver=driver)
    list_of_cards = main_page.get_list_of_cards()
    assert len(list_of_cards) == 6

