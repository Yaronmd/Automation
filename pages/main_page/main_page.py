
from pages.base_pages.element_actions import ElementActions
from pages.base_pages.element_input_actions import InputActions
from selenium.webdriver.common.by import By

from pages.base_pages.base_page import SeleniumBasePage

class MainPage(SeleniumBasePage):
    # Locators
    LIST_OF_CARDS = (By.XPATH, "//*[@data-test='inventory-list']//div[@class='inventory_item']")


    def __init__(self, driver):
        super().__init__(driver)
        

    def get_list_of_cards(self):
        elements = self.get_elements(by_locator=self.LIST_OF_CARDS)
        return elements
        