
from base.base_test import BaseTest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from utils.cookie_manager import CookieManager
import allure

class TestLogin(BaseTest):
    @allure.story("Successful login with valid admin credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    
    def test_save_cookie(self):
        login_page = LoginPage(self.driver) 
        login_page.login(*ConfigReader.get_email_password()) 
        self.driver.save_screenshot("login_success.png")

        # Save cookies
        # CookieManager.save_cookies(self.driver)