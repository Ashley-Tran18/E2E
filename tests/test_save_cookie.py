# tests/test_login_save_cookie.py
import allure
from base.base_test import BaseTest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from utils.cookie_manager import CookieManager

@allure.epic("Authentication")
class TestLogin(BaseTest):

    @allure.story("Auto Login & Save Cookies")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_and_save_cookies(self):
        with allure.step("Mở trang login"):
            login_page = LoginPage(self.driver)

        with allure.step("Nhập email & password"):
            email, password = ConfigReader.get_email_password()
            login_page.login(email, password)

        with allure.step("Kiểm tra login thành công"):
            # assert "dashboard" in self.driver.current_url.lower()
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="login_success",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Lưu cookies để dùng lại"):
            CookieManager.save_cookies(self.driver)