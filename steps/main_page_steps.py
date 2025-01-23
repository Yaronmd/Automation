from conftest import MainPage
import pytest
import allure


@allure.step("Get list of inventory cards")
def get_inventory_cards(main_page:MainPage):
    cards = main_page.get_inventory_list_contant()
    assert cards, "No inventory cards found"
    return cards

@allure.step("Add a random card to the cart")
def add_random_card_to_cart(main_page:MainPage, cards):
    selected_card = main_page.add_to_card_random_inventory(cards)
    assert selected_card, "Failed to add a card to the cart"
    return selected_card

@allure.step("Validate cart badge number")
def validate_cart_badge(main_page:MainPage, expected_number):
    assert main_page.validate_badge_cart_number(expected_number), f"Expected cart badge to show {expected_number}"
