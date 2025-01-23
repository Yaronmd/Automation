import allure
from conftest import MainPage,CartPage
@allure.step("Open the shopping cart")
def open_cart(main_page:MainPage):
    assert main_page.click_on_shopping_cart(), "Failed to open the shopping cart"

@allure.step("Validate cart contents")
def validate_cart_contents(cart_page:CartPage, expected_items):
    assert cart_page.validate_multiple_inventories(expected_items), "Cart contents do not match"

@allure.step("Click checkout")
def click_checkout(cart_page:CartPage):
    assert cart_page.click_checkout()