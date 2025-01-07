
from pages.base_pages.element_actions import ElementActions
from pages.base_pages.element_input_actions import InputActions
from selenium.webdriver.common.by import By

from pages.base_pages.base_page import SeleniumBasePage
from pages.main_page.inventory_card_page import InventoryCardPage
import random
class MainPage(SeleniumBasePage):
    # Locators
    LIST_OF_CARDS = (By.XPATH, "//*[@data-test='inventory-list']//div[@class='inventory_item']")


    def __init__(self, driver):
        super().__init__(driver)
        self.inventory_card_page=InventoryCardPage(driver)

    def get_list_of_cards(self):
        elements = self.get_elements(by_locator=self.LIST_OF_CARDS)
        return elements
    
    def get_inventory_list_contant(self):
        cards = []
        list_of_cards = self.get_list_of_cards()
        for index in range(1,len(list_of_cards)-1):
            card = self.inventory_card_page.get_inventory_item(by_index=index)
            if not card:
                self.logger.error(f"Failed to find card contant for card number:{index}")
                return False
            cards.append(card)
        self.logger.info(f"cards contant: {cards}")
        return cards
    
    def add_to_card_random_inventory(self,cards):
        if not cards:
            return False
        card = random.choice(cards)
        inventory_name = card.get("name")
        if self.inventory_card_page.click_add_to_cart_by_name(inventory_name):
            self.logger.info(f"Sucess to add '{inventory_name}' to cart")
            return card
        return False

    
        

        
        