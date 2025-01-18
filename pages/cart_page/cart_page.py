from pages.base_pages.base_page import SeleniumBasePage
from pages.base_pages.element_actions import ElementActions
from selenium.webdriver.common.by import By


class CartPage(SeleniumBasePage):
    __checkout_button_path = (By.CSS_SELECTOR, "[data-test='checkout']")
    __back_to_shopping_path = (By.CSS_SELECTOR, "[data-test='continue-shopping']")
    __page_labels = ("Your Cart", "QTY", "Description", "Continue Shopping", "Checkout")

    def __init__(self, driver):
        super().__init__(driver)
        self.element_actions = ElementActions(driver)


    def are_page_labels_present(self):
        """Check if all expected labels are present on the page."""
        for label in self.__page_labels:
            if not self.get_element((By.XPATH, f"//*[.='{label}']")):
                self.logger.error(f"Label '{label}' not found on the cart page.")
                return False
            self.logger.info(f"Label '{label}' found on the cart page.")
        return True

    def is_inventory_item_present(self, name: str):
        """Check if an inventory item with a specific name exists."""
        element = self.get_element((By.XPATH, f"//*[@data-test='inventory-item-name' and .='{name}']"))
        if element:
            self.logger.info(f"Inventory item with name '{name}' is present.")
            return True
        self.logger.warning(f"Inventory item with name '{name}' is not found.")
        return False

    def get_inventory_item_text(self, data_test: str):
        """Get text for an inventory item based on a data-test attribute."""
        text = self.get_element_text((By.XPATH, f"//*[@data-test='{data_test}']"))
        if text:
            self.logger.info(f"Retrieved text for '{data_test}': {text}")
        else:
            self.logger.warning(f"Failed to retrieve text for '{data_test}'.")
        return text

    def get_remove_button_path_by_name(self, name: str):
        """Construct the XPath for the remove button of an inventory item."""
        inventory_name = name.lower().replace(" ", "-")
        path = (By.XPATH, f"//button[@data-test='remove-to-cart-{inventory_name}']")
        self.logger.debug(f"Generated XPath for remove button: {path}")
        return path

    def is_remove_button_present(self, name: str):
        """Check if the remove button for an item exists."""
        element = self.get_element(self.get_remove_button_path_by_name(name))
        if element:
            self.logger.info(f"Remove button for '{name}' is present.")
            return True
        self.logger.warning(f"Remove button for '{name}' is not found.")
        return False

    def click_remove_button_by_name(self, name: str):
        """Click the remove button for an item."""
        path = self.get_remove_button_path_by_name(name)
        if self.element_actions.click_presence_of_element_located(path):
            self.logger.info(f"Clicked on remove button for '{name}'.")
            return True
        self.logger.error(f"Failed to click on remove button for '{name}'.")
        return False

    def click_checkout(self):
        """Click the checkout button."""
        if self.element_actions.click_presence_of_element_located(self.__checkout_button_path):
            self.logger.info("Clicked on the checkout button.")
            return True
        self.logger.error("Failed to click on the checkout button.")
        return False

    def click_back_to_shopping(self):
        """Click the back to shopping button."""
        if self.element_actions.click_presence_of_element_located(self.__back_to_shopping_path):
            self.logger.info("Clicked on the back to shopping button.")
            return True
        self.logger.error("Failed to click on the back to shopping button.")
        return False

    def validate_inventory_details(self, inventory: dict):
        """Validate the details of an inventory item."""
        name = inventory.get("name")
        desc = inventory.get("desc")
        price = inventory.get("price")
        quantity = inventory.get("quantity", 1)

        name_valid = self.is_inventory_item_present(name)
        desc_valid = self.get_inventory_item_text("inventory-item-desc") == desc
        price_valid = self.get_inventory_item_text("inventory-item-price") == price
        quantity_valid = self.get_element(
            (By.XPATH, f"//*[.='{name}']//ancestor::div[@data-test='inventory-item']"
                       f"//*[@data-test='item-quantity' and .='{quantity}']")
        ) is not None

        if name_valid and desc_valid and price_valid and quantity_valid:
            self.logger.info(f"Inventory '{name}' details validated successfully.")
            return True

        self.logger.error(f"Failed to validate inventory details for '{name}'.")
        return False

    def validate_multiple_inventories(self, inventories: list[dict]):
        """Validate a list of inventory items."""
        for inventory in inventories:
            if not self.validate_inventory_details(inventory):
                self.logger.error(f"Validation failed for one or more inventory items: {inventory}")
                return False
        self.logger.info("All inventories validated successfully.")
        return True


    

    