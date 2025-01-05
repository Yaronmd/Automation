from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from pages.base_pages.base_page import SeleniumBasePage

class InputActions(SeleniumBasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)  # Call the BasePage constructor

    def send_keys(self, by_locator: tuple, keys: str, timeout: int = 10, hide_keys: bool = False) -> bool:
        """
        Sends keys to an input field located by the given locator.
        Args:
            by_locator (tuple): Locator for the input field (e.g., (By.ID, "username")).
            keys (str): The string to type into the field.
            timeout (int): Maximum wait time for the field to be ready.
            hide_keys (bool): If True, hides the keys in logs.
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            element = self._wait_for(EC.presence_of_element_located, by_locator, timeout)
            element.click()  # Focus on the element
            element.clear()  # Clear existing content
            element.send_keys(keys)  # Send the desired keys
            self.logger.info(
                f"Success: Sent keys {'***hidden***' if hide_keys else keys} to {by_locator}"
            )
            return True
        except Exception as e:
            self.logger.error(f"Failed to send keys to {by_locator}. Exception: {e}")
            return False