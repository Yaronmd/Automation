from selenium.webdriver.support import expected_conditions as EC
from helper.logger import logger
from pages.base_pages.base_page import SeleniumBasePage
from selenium.webdriver.remote.webdriver import WebDriver

class ElementActions(SeleniumBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)  # Call the BasePage constructor

    def click_element_to_be_clickable(self, locator: tuple, timeout: int = 10) -> bool:
        try:
            element = self._wait_for(EC.element_to_be_clickable, locator, timeout)
            element.click()
            return True
        except Exception as e:
            self.logger.error(f"Failed to click on element {locator}. Exception: {e}")
            return False
        
    def click_presence_of_element_located(self, locator: tuple, timeout: int = 10) -> bool:
        try:
            element = self._wait_for(EC.presence_of_element_located, locator, timeout)
            element.click()
            return True
        except Exception as e:
            self.logger.error(f"Failed to click on element {locator}. Exception: {e}")
            return False