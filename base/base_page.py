from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import ConfigReader

class BasePage:
    def __init__(self, driver):
        self.driver = driver    
        self.timeout = ConfigReader.get_timeout()
     
    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*locator)
        )

    def click(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)
    
    def get_text(self, locator):
        return self.find_element(locator).text
    
    def wait_for_element_visible(self, locator, timeout=None):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_and_click(self, locator, timeout = None):
        timeout = timeout or self.timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.click()

    def wait_and_find_element(self, locator):
        # chờ element hiển thị rồi trả về element
        return self.wait_for_element_visible(locator)
