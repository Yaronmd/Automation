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


@pytest.fixture
def main_page(driver, login):
    """
    Initialize and return the MainPage object after login.
    """
    return MainPage(driver=driver)

@allure.title("Validate len of cards")
def test_validate_len_of_cards(main_page:MainPage):
    list_of_cards = main_page.get_list_of_cards()
    assert len(list_of_cards) == 6


@pytest.fixture
def cards(main_page: MainPage):
    """
    Fixture to validate the content of cards on the main page.
    """
    cards = main_page.get_inventory_list_contant()
    assert cards, "Cards content should not be empty"
    return cards

@pytest.fixture
def selected_card(main_page: MainPage, cards):
    """
    Fixture to select and add a random card to the cart.
    """
    selected_card = main_page.add_to_card_random_inventory(cards)
    assert selected_card, "A card should be successfully added to the cart"
    return selected_card

@allure.title("Validate cards content, select one, and add to cart")
def test_validate_cards_contant(selected_card):
    """
    Test to validate the card content and ensure one card is selected and added to the cart.
    """
    assert selected_card, "The selected card should be returned by the fixture"