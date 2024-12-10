
import time
from helper.logger import logger
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class SeleniumBasePage:

    def __init__(self,driver:WebDriver):
        self.driver = driver
    
    
    def go_to_end_point(self,end_point:str)->bool:
        try:
            self.driver.get(end_point)
            return True
        except Exception as e:
            logger.error(f"Failed go to end point:{end_point}, exception:{e}")
            return False
        
    def perform_click(self,by_locator:tuple,timeout:int=10)->bool:
        try:
            element = WebDriverWait(driver=self.driver,timeout=timeout).until(EC.presence_of_element_located(by_locator))
            element.click()
            logger.info(f"Success to click,locator:{by_locator}")
            return True
        except Exception as e:
            logger.error(f"Failed to click by presence_of_element_located, locator:{by_locator}, timeout:{timeout}, expection:{type(e).__name__}")
            return False
        
    def send_keys(self,by_locator:tuple,keys:str,timeout:int=10,hide_keys:bool=False)->bool:
        try:
            element = WebDriverWait(driver=self.driver,timeout=timeout).until(EC.presence_of_element_located(by_locator))
            element.clear()
            element.send_keys(keys)
            logger.info(f"Success to send keys:{'secret keys' if hide_keys else keys} for locator:{by_locator}")
            return True
        except Exception as e:
            logger.error(f"Failed to send keys by presence_of_element_located, locator:{by_locator}, timeout:{timeout}, expection:{type(e).__name__}")
            return False
        
    def validate_title(self,title:str,wait_before_action:int)->bool:
        if wait_before_action > 0:
            time.sleep(wait_before_action)
        if title in self.driver.title:
            logger.info(f"Success validate title:'{title}'")
            return True
        logger.error(f"Failed to validate title:'{title}'")
        return False