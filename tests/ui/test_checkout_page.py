import allure
from steps.login_steps import navigate_and_login
from steps.main_page_steps import get_inventory_cards, add_random_card_to_cart, validate_cart_badge
from steps.cart_steps import open_cart, validate_cart_contents,click_checkout
from steps.checkout_steps import fill_checkout_form, continue_checkout,validate_missing_field
import pytest


@pytest.mark.parametrize("first_name, last_name, postal_code, missing_field", [
    ("", "Mordechai", "1234","First Name"),
    ("John", "", "5678","Last Name"),
    ("Jane", "Smith", "","Postal Code")
])    
@allure.feature("Test Checkout page error messages")
def test_end_to_end_flow(navigate_and_login, main_page, cart_page, checkout_page,first_name,last_name,postal_code,missing_field):
   

    # Step 2: Get inventory cards
    cards = get_inventory_cards(main_page)
    
    # Step 3: Add a random card to the cart
    selected_card = add_random_card_to_cart(main_page, cards)
    validate_cart_badge(main_page, 1)
    
    # Step 4: Validate cart contents
    open_cart(main_page)
    validate_cart_contents(cart_page, [selected_card])
    
    click_checkout(cart_page)
    # Step 5: Checkout
    fill_checkout_form(checkout_page, first_name=first_name, last_name=last_name, postal_code=postal_code)
    continue_checkout(checkout_page)
    validate_missing_field(checkout_page,missing_field)