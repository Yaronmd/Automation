import allure
from steps.login_steps import navigate_and_login
from steps.main_page_steps import get_inventory_cards
import pytest



@allure.feature("Test main page as cards")
@pytest.mark.parametrize("expcted_len_of_cards, ", [6])
def test_validate_len_of_cards(navigate_and_login,main_page,expcted_len_of_cards):
    list_of_cards =  get_inventory_cards(main_page=main_page)
    assert len(list_of_cards) == expcted_len_of_cards, f"Expected  cards, but got {len(list_of_cards)}"