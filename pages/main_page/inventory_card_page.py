from pages.base_pages.base_page import SeleniumBasePage
from selenium.webdriver.common.by import By

from pages.base_pages.element_actions import ElementActions

class InventoryCardPage(SeleniumBasePage):
    INVENTORY_NAME_PATH = "//*[@data-test='inventory-item-name']"
    INVENTORY_DESC_PATH = "//*[@data-test='inventory-item-desc']"
    INVENTORY_PRICE_PATH = "//*[@data-test='inventory-item-price']"
    INVENTORY_IMAGE_PATH = "//*[@class='inventory_item_img']//a"

    def __init__(self, driver):
        super().__init__(driver)
        self.element_actions = ElementActions(driver)

    
    def get_inventory_item_name(self,by_index:str):
        INVENTORY_NAME_LOCATOR_PATH = (By.XPATH,f"({self.INVENTORY_NAME_PATH})[{by_index}]")
        element_text = self.get_element_text(by_locator=INVENTORY_NAME_LOCATOR_PATH)
        if not element_text:
          return None
        return element_text
    
    def get_inventory_item_desc(self,by_index:str):
        INVENTORY_DESC_LOCATOR_PATH = (By.XPATH,f"({self.INVENTORY_DESC_PATH})[{by_index}]")
        element_text = self.get_element_text(by_locator=INVENTORY_DESC_LOCATOR_PATH)
        if not element_text:
          return None
        return element_text

    def get_inventory_item_price(self,by_index:str):
        INVENTORY_PRICE_LOCATOR_PATH = (By.XPATH,f"({self.INVENTORY_PRICE_PATH})[{by_index}]")
        element_text = self.get_element_text(by_locator=INVENTORY_PRICE_LOCATOR_PATH)
        if not element_text:
          return None
        return element_text
    def get_inventory_item_image(self,by_index:str):
       INVENTORY_IMAGE_LOCATOR_PATH = (By.XPATH,f"({self.INVENTORY_IMAGE_PATH})[{by_index}]")
       src = self.get_attribute_of_element("src")
       if not src:
          return None
       return src
    
    def get_inventory_item(self,by_index:str):
       name = self.get_inventory_item_name(by_index)
       desc = self.get_inventory_item_desc(by_index)
       price = self.get_inventory_item_price(by_index)
       image = self.get_inventory_item_image(by_index)
       if name and desc and price and image:
          return {"name":name,"desc":desc,"price":price,"image":image}
       return None
    
    def click_add_to_cart_by_name(self,inventory_name:str):
       inventory_name = inventory_name.lower()
       inventory_name = inventory_name.replace(" ","-")
       INVENTORY_ADD_CARD_LOCATOR_PATH = (By.XPATH,f"//button[@data-test='add-to-cart-{inventory_name}']")
       if self.element_actions.click_presence_of_element_located(INVENTORY_ADD_CARD_LOCATOR_PATH):
          return True
       return False