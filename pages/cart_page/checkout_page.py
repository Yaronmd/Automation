from pages.base_pages.base_page import SeleniumBasePage
from pages.base_pages.element_actions import ElementActions
from pages.base_pages.element_input_actions import InputActions
from selenium.webdriver.common.by import By


class CheckoutPage(SeleniumBasePage):
     
     first_name_locator_path = (By.CSS_SELECTOR,"[data-test='firstName']")
     last_name_locator_path = (By.CSS_SELECTOR,"[data-test='lastName']")
     postal_loctor_path = (By.CSS_SELECTOR,"[data-test='postalCode']")
     button_error_locator_path = (By.CSS_SELECTOR,"[data-test='error']")
     continue_button_locator_path = (By.CSS_SELECTOR,"[data-test='continue']")

     def __init__(self, driver):
        super().__init__(driver)
        self.element_actions = ElementActions(driver)
        self.element_inputs = InputActions(driver)

     def set_first_name(self,first_name:str):
        """
        Set the first name in the checkout form.

        Args:
            first_name (str): The first name to input.

        Returns:
            bool: True if the first name was successfully set, False otherwise.
        """
        if self.element_inputs.send_keys(by_locator=self.first_name_locator_path,keys=first_name):
            self.logger.info("Success to set first name")
            return True
        self.logger.error("Failed to set first name")
        return False
     def set_last_name(self,last_name:str):
        """
        Set the last name in the checkout form.

        Args:
            last_name (str): The last name to input.

        Returns:
            bool: True if the last name was successfully set, False otherwise.
        """
        if self.element_inputs.send_keys(by_locator=self.last_name_locator_path,keys=last_name):
            self.logger.info("Success to set last name")
            return True
        self.logger.error("Failed to set last name")
        return False
     def set_postal(self,postal:str):
        """
        Set the postal code in the checkout form.

        Args:
            postal (str): The postal code to input.

        Returns:
            bool: True if the postal code was successfully set, False otherwise.
        """
        if self.element_inputs.send_keys(by_locator=self.postal_loctor_path,keys=postal):
            self.logger.info("Success to set postal")
            return True
        self.logger.error("Failed to set postale")
        return False
     
     def set_form(self,first_name:str,last_name:str,postal:str):
         """
        Set the entire form with first name, last name, and postal code.

        Args:
            first_name (str): The first name to input.
            last_name (str): The last name to input.
            postal (str): The postal code to input.

        Returns:
            bool: True if the form was successfully filled, False otherwise.
        """
         if self.set_first_name(first_name=first_name) and self.set_last_name(last_name=last_name) and self.set_postal(postal=postal):
             self.logger.info("Success to set form")
             return True
         self.logger.error("Failed to set form")
         return False
     
     def validate_missing_field_message(self,field_name:str):
         """
        Validate the error message for a missing field.

        Args:
            field_name (str): The name of the missing field.

        Returns:
            bool: True if the error message matches the expected text, False otherwise.
        """
         error_message = f"Error: {field_name.title()} is required"
         message = self.get_element_text(by_locator=self.button_error_locator_path,as_visibility=True,timeout=20)
         if not message:
             self.logger.error(f"Got empty message for {field_name}")
         if message and message == error_message:
             return True
         self.logger.error(f"Failed to find error message: {error_message}")
         return False
     
     def click_continue(self):
         """
        Click the 'Continue' button on the checkout page.

        Returns:
            bool: True if the button was successfully clicked, False otherwise.
        """
         if self.element_actions.click_presence_of_element_located(locator=self.continue_button_locator_path):
             self.logger.info("Success to click continue button")
             return True
         self.logger.error("Failed to click continue button")
         return False

