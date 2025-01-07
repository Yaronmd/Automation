
from pages.base_pages.element_actions import ElementActions
from pages.base_pages.element_input_actions import InputActions
from selenium.webdriver.common.by import By

from pages.base_pages.base_page import SeleniumBasePage

class LoginPage(SeleniumBasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.input_actions = InputActions(driver)
        self.element_actions = ElementActions(driver)

    def enter_username(self, username: str) -> bool:
        self.logger.info(f"set user name:{username}")
        return self.input_actions.send_keys(self.USERNAME_INPUT, username)

    def enter_password(self, password: str) -> bool:
        self.logger.info(f"set password")
        return self.input_actions.send_keys(self.PASSWORD_INPUT, password, hide_keys=True)

    def click_login(self) -> bool:
        self.logger.info(f"click login")
        return self.element_actions.click_presence_of_element_located(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> bool:
        if not self.enter_username(username):
            return False
        if not self.enter_password(password):
            return False
        return self.click_login()