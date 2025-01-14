
from pages.base_pages.element_actions import ElementActions
from pages.base_pages.element_input_actions import InputActions
from selenium.webdriver.common.by import By

from pages.base_pages.base_page import SeleniumBasePage
from pages.main_page.inventory_card_page import InventoryCardPage
import random
class MainPage(SeleniumBasePage):
    # Locators
    list_of_cards_path = (By.XPATH, "//*[@data-test='inventory-list']//div[@class='inventory_item']")
    cart_button_path = (By.CSS_SELECTOR,"[data-test='shopping-cart-link']")
    badge_cart_numer_path = (By.CSS_SELECTOR,"[data-test='shopping-cart-badge']")

    def __init__(self, driver):
        super().__init__(driver)
        self.inventory_card_page=InventoryCardPage(driver)
        self.element_actions = ElementActions(driver)
        

    def get_list_of_cards(self):
        elements = self.get_elements(by_locator=self.list_of_cards_path)
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
    
    def click_on_shopping_cart(self):
        if not self.element_actions.click_presence_of_element_located(locator=self.cart_button_path):
            self.logger.error("Failed to click on shopping cart")
            return False
        self.logger.info("Suceess to click on shopping cart")
        return True

    def validate_badge_cart_number(self,len_added_to_card:int):
        text =  self.get_element_text(by_locator=self.badge_cart_numer_path)
        if not text:
            return False
        if len_added_to_card == int(text):
            self.logger.info(f"Suceess to validate badge cart number is equal to: {len_added_to_card}")
            return True
        self.logger.info("Failed to validate badge cart number is equal to: {len_added_to_card}")
        return False



    
        

        
        