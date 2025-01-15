from pages.base_pages.base_page import SeleniumBasePage
from pages.base_pages.element_actions import ElementActions
from selenium.webdriver.common.by import By


class CartPage(SeleniumBasePage):

    __checkout_button_path = (By.CSS_SELECTOR,"[data-test='checkout']")
    __back_to_shopping_path = (By.CSS_SELECTOR,"[data-test='continue-shopping']")
    __page_labels = ("Your Cart","QTY","Description","Continue Shopping","Checkout")

    def __init__(self, driver):
        super().__init__(driver)
        self.element_actions = ElementActions(driver)

    def validate_page_labels(self):
        for label in self.__page_labels:
            if not  self.get_element(by_locator=(f"//*[.='{label}']")):
                self.logger.error(f"Failed to find label:'{label}' in cart page")
                return False 
            return True

    def validate_inventory_item_name(self,name:str):
        if self.get_element((By.XPATH,f"//*[@data-test='inventory-item-name' and .()='{name}']")):
            return True
        return False
    
    def validate_inventory_item_desc(self,desc:str):
        if self.get_element((By.XPATH,f"//*[@data-test='inventory-item-desc' and .()='{desc}']")):
            return True
        return False
    
    def validate_inventory_item_price(self,price:str):
        if self.get_element((By.XPATH,f"//*[@data-test='inventory-item-price' and .()='{price}']")):
            return True
        return False
    
    def valdiate_item_quantity_by_name(self,name,number:int=1):
        path = (By.XPATH,f"//*[.='{name}']//ancestor::div[@data-test='inventory-item']//*[@data-test='item-quantity' and .='{number}']")
        if self.get_element(path):
            return True
        return False
    
    @staticmethod
    def _common_get_remove_path_by_name(name:str):
        inventory_name = name.lower()
        inventory_name = inventory_name.replace(" ","-")
        return (By.XPATH,f"//button[@data-test='remove-to-cart-{inventory_name}']")
     
    def validate_remove_button_exist(self,name):
        if self.get_element(by_locator=self._common_get_remove_path_by_name(name=name)):
           return True
        return False
    
    def click_remove_item_from_cart_by_name(self,name:str):
       if self.element_actions.click_presence_of_element_located(self._common_get_remove_path_by_name(name)):
          return True
       self.logger.error("Failed to click on 'remove to card' for inventory name: {inventory_name}")
       return False

    
    def click_checkout(self):
        if self.element_actions.click_presence_of_element_located(self.__checkout_button_path):
            return True
        return False
    
    def click_back_to_shopping(self):
        if self.element_actions.click_presence_of_element_located(self.__back_to_shopping_path):
            return True
        return False
    
    def validate_inevtory_add_to_carts_with_all_info(self,inevtory:dict):
        if self.valdiate_item_quantity_by_name(inevtory.get("name")) and \
        self.validate_inventory_item_desc(inevtory.get("desc")) and \
        self.validate_inventory_item_price(inevtory.get("price")) and \
        self.valdiate_item_quantity_by_name(inevtory.get("name")):
            self.logger.info("Success to validate inventory information in cart")
            return True
        return False
    
    def validate_list_of_inventories(self,inventories:list[dict]):
        for inventory in inventories:
            if not self.validate_inevtory_add_to_carts_with_all_info(inventory):
                return False
        return True
                

    

    