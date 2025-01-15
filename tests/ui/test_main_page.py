import pytest
import allure
from config.config import UI_BASE_PAGE, UI_PASSWORD, UI_USERNAME
from pages.base_pages.navigation import Navigation
from pages.login_page.login_page import LoginPage
from pages.main_page.main_page import MainPage

# Fixtures
@pytest.fixture
def navigate(driver):
    navigation = Navigation(driver=driver)
    assert navigation.go_to_end_point(url=UI_BASE_PAGE)

@pytest.fixture
def login(driver, navigate):
    login_page = LoginPage(driver=driver)
    assert login_page.login(username=UI_USERNAME, password=UI_PASSWORD)

@pytest.fixture
def main_page(driver, login):
    return MainPage(driver=driver)

@pytest.fixture
def get_list_of_cards(main_page: MainPage):
    with allure.step("Get list of cards"):
        cards = main_page.get_inventory_list_contant()
        assert cards, "Cards content should not be empty"
        return cards

@pytest.fixture(scope="module")
def selected_cards_fixture():
    return []

# Helper Functions
@allure.step("Select a random card")
def select_random_card(main_page: MainPage, cards, selected_cards_fixture):
    selected_card = main_page.add_to_card_random_inventory(cards)
    assert selected_card, "A card should be successfully added to the cart"
    selected_cards_fixture.append(selected_card)
    return selected_card

@allure.step("Validate shopping cart badge")
def validate_card_add_to_cart_icon(main_page: MainPage, selected_cards_fixture):
    assert main_page.validate_badge_cart_number(len(selected_cards_fixture))

@allure.step("Click on the shopping cart")
def click_shopping_cart(main_page: MainPage):
    assert main_page.click_on_shopping_cart()

# Tests

def test_validate_len_of_cards(main_page: MainPage):
    with allure.step("Validate the length of the list of cards"):
        list_of_cards = main_page.get_list_of_cards()
        assert len(list_of_cards) == 6, f"Expected 6 cards, but got {len(list_of_cards)}"

def test_add_to_cart_and_validate(main_page, get_list_of_cards, selected_cards_fixture):
    cards = get_list_of_cards
    select_random_card(main_page=main_page, cards=cards, selected_cards_fixture=selected_cards_fixture)
    validate_card_add_to_cart_icon(main_page=main_page, selected_cards_fixture=selected_cards_fixture)
    click_shopping_cart(main_page=main_page)
    
