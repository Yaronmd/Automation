from pages.base_pages.base_page import SeleniumBasePage
from selenium.webdriver.common.by import By

from pages.base_pages.element_actions import ElementActions

class InventoryCardPage(SeleniumBasePage):
    INVENTORY_NAME_PATH = "//*[@data-test='inventory-item-name']"
    INVENTORY_DESC_PATH = "//*[@data-test='inventory-item-desc']"
    INVENTORY_PRICE_PATH = "//*[@data-test='inventory-item-price']"
    INVENTORY_IMAGE_PATH = "//*[@class='inventory_item_img']//a//img"

    def __init__(self, driver):
        super().__init__(driver)
        self.element_actions = ElementActions(driver)

    
    def get_inventory_item_name(self,by_index:str):
        """
        Retrieve the name of an inventory item by its index.

        Args:
            by_index (str): The index of the inventory item.

        Returns:
            str or None: The name of the inventory item if found, otherwise None.
        """
        inventory_name_locator_path = (By.XPATH,f"({self.INVENTORY_NAME_PATH})[{by_index}]")
        element_text = self.get_element_text(by_locator=inventory_name_locator_path)
        if not element_text:
          return None
        return element_text
    
    def get_inventory_item_desc(self,by_index:str):
        """
        Retrieve the description of an inventory item by its index.

        Args:
            by_index (str): The index of the inventory item.

        Returns:
            str or None: The description of the inventory item if found, otherwise None.
        """
        inventory_desc_locator_path = (By.XPATH,f"({self.INVENTORY_DESC_PATH})[{by_index}]")
        element_text = self.get_element_text(by_locator=inventory_desc_locator_path)
        if not element_text:
          return None
        return element_text

    def get_inventory_item_price(self,by_index:str):
        """
        Retrieve the price of an inventory item by its index.

        Args:
            by_index (str): The index of the inventory item.

        Returns:
            str or None: The price of the inventory item if found, otherwise None.
        """
        inventory_price_locator_path = (By.XPATH,f"({self.INVENTORY_PRICE_PATH})[{by_index}]")
        element_text = self.get_element_text(by_locator=inventory_price_locator_path)
        if not element_text:
          return None
        return element_text
    
    def get_inventory_item_image(self,by_index:str):
       """
        Retrieve the image URL of an inventory item by its index.

        Args:
            by_index (str): The index of the inventory item.

        Returns:
            str or None: The URL of the inventory item's image if found, otherwise None.
        """
       inventory_image_locator_path = (By.XPATH,f"({self.INVENTORY_IMAGE_PATH})[{by_index}]")
       src = self.get_attribute_of_element(by_locator=inventory_image_locator_path,attribute="src")
       if not src:
          return None
       return src
    
    def get_inventory_item(self,by_index:str):
       """
        Retrieve all details (name, description, price, and image) of an inventory item by its index.

        Args:
            by_index (str): The index of the inventory item.

        Returns:
            dict or None: A dictionary containing the item's details if all are found, otherwise None.
        """
       name = self.get_inventory_item_name(by_index)
       desc = self.get_inventory_item_desc(by_index)
       price = self.get_inventory_item_price(by_index)
       image = self.get_inventory_item_image(by_index)
       if name and desc and price and image:
          return {"name":name,"desc":desc,"price":price,"image":image}
       return None
    
    def click_add_to_cart_by_name(self,inventory_name:str):
       """
        Click the "Add to Cart" button for an inventory item based on its name.

        Args:
            inventory_name (str): The name of the inventory item.

        Returns:
            bool: True if the button was clicked successfully, otherwise False.
        """
       inventory_name = inventory_name.lower()
       inventory_name = inventory_name.replace(" ","-")
       inventory_add_card_locator_path = (By.XPATH,f"//button[@data-test='add-to-cart-{inventory_name}']")
       if self.element_actions.click_presence_of_element_located(inventory_add_card_locator_path):
          return True
       self.logger.error("Failed to click on 'add to card' for inventory name: {inventory_name}")
       return False