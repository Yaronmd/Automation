from helper.logger import logger
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver() -> WebDriver:
    """
    Fixture to initialize the WebDriver and connect it to the Selenium Hub.
    """
    # Set the desired capabilities for the driver (you can change this based on the browser you're using)
    options = Options()
    capabilities = options.to_capabilities()
    capabilities['platformName'] = 'LINUX'
    # Set the remote WebDriver to the Selenium Hub
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',  # Hub URL from the Docker Compose file
        options = options
    )
    
    yield driver

    driver.quit()
