import allure

@allure.step("Fill out the checkout form")
def fill_checkout_form(checkout_page, first_name, last_name, postal_code):
    assert checkout_page.set_form(first_name=first_name, last_name=last_name, postal=postal_code), "Failed to set checkout form"

@allure.step("Continue checkout process")
def continue_checkout(checkout_page):
    assert checkout_page.click_continue(), "Failed to continue checkout"
