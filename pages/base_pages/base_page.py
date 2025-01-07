
import time
from helper.logger import logger
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class SeleniumBasePage:

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.logger = logger
    
    def _wait_for(self, condition, locator: tuple, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(condition(locator))
        except Exception as e:
            self.logger.error(f"Wait failed for locator {locator}. Exception: {e}")
            raise

        
        
    def validate_title(self,title:str)->bool:
        if title in self.driver.title:
            self.logger.info(f"Success validate title:'{title}'")
            return True
        self.logger.error(f"Failed to validate title:'{title}'")
        return False
    
    def get_element(self,by_locator:tuple,timeout:int=10):
        try:
            element = self._wait_for(condition=EC.presence_of_element_located,locator=by_locator,timeout=timeout)
            self.logger.info(f"Success get element for locator:{by_locator}")
            return element
        except Exception as e:
            self.logger.error(f"Failed to validate to get elemnt for locator:{by_locator}, exception:{type(e).__name__}")
            return False
        
    def get_elements(self,by_locator:tuple,timeout:int=10):
        try:
            elements = self._wait_for(condition=EC.presence_of_all_elements_located,locator=by_locator,timeout=timeout)
            return elements
        except Exception as e:
            logger.error(f"Failed to validate to get elements for locator:{by_locator}, exception:{type(e).__name__}")
            return None

    def get_list_of_text(self,by_locator:tuple,timeout:int=10):
            elements = self.get_elements(by_locator=by_locator,timeout=timeout)
            if not elements:
                return None
            list_of_text = []
            for elem in elements:
                if elem.text:
                    list_of_text.append(elem.text)
            self.logger.info(f"Success to get list of text for locator:{by_locator}, texts:{list_of_text}")
            return list_of_text
    
    def get_element_text(self,by_locator:tuple,timeout:int=10):
        element = self.get_element(by_locator=by_locator,timeout=timeout)
        if not element:
            return None
        text = element.text
        self.logger.info(f"Success to get elemnt text for locator:{by_locator}, text:{text}")
        return text
    
    def get_attribute_of_element(self,by_locator:tuple,attribute:str,timeout:int=10):
        element = self.get_element(by_locator=by_locator,timeout=timeout)
        if not element:
            return None
        return element.get_attribute(attribute)
        


