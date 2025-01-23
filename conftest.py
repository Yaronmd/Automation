from helper.logger import logger
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from webdriver_manager.chrome import ChromeDriverManager

from pages.base_pages.navigation import Navigation
from pages.cart_page.cart_page import CartPage
from pages.cart_page.checkout_page import CheckoutPage
from pages.login_page.login_page import LoginPage
from pages.main_page.main_page import MainPage



@pytest.fixture
def navigation_page(driver)->Navigation:
    """
    Fixture for initializing the Navigation page object.

    Args:
        driver: The WebDriver instance used for interacting with the browser.

    Returns:
        Navigation: An instance of the Navigation page object.
    """
    return Navigation(driver=driver)

@pytest.fixture
def login_page(driver)->LoginPage:
    """
    Fixture for initializing the Login page object.

    Args:
        driver: The WebDriver instance used for interacting with the browser.

    Returns:
        LoginPage: An instance of the Login page object.
    """
    return LoginPage(driver=driver)

@pytest.fixture
def main_page(driver):
    """
    Fixture for initializing the Main page object.

    Args:
        driver: The WebDriver instance used for interacting with the browser.

    Returns:
        MainPage: An instance of the Main page object.
    """
    return MainPage(driver=driver)

@pytest.fixture
def cart_page(driver)->CartPage:
    """
    Fixture for initializing the Cart page object.

    Args:
        driver: The WebDriver instance used for interacting with the browser.

    Returns:
        CartPage: An instance of the Cart page object.
    """
    return CartPage(driver)

@pytest.fixture
def checkout_page(driver)->CheckoutPage:
    """
    Fixture for initializing the Checkout page object.

    Args:
        driver: The WebDriver instance used for interacting with the browser.

    Returns:
        CheckoutPage: An instance of the Checkout page object.
    """
    return CheckoutPage(driver)    

@pytest.fixture(scope="function")
def driver() -> WebDriver:
    """
    Fixture to initialize the WebDriver and connect it to the Selenium Hub.
    """
    # Set the desired capabilities for the driver (you can change this based on the browser you're using)
    options = Options()
    options.add_argument("--start-maximized")
    capabilities = options.to_capabilities()
    capabilities['platformName'] = 'LINUX'
    # Set the remote WebDriver to the Selenium Hub
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',  # Hub URL from the Docker Compose file
        options = options
    )
    
    yield driver

    driver.quit()
