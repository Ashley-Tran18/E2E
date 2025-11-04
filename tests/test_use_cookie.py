# tests/test_use_cookies.py
import pytest
from base.base_test import BaseTest
from pages.cookie_page import CookiePage
from utils.config_reader import ConfigReader

@pytest.mark.usefixtures("setup")
class TestUseCookies(BaseTest):

    def test_open_site_with_cookies(self):
        """Mở site bằng cookies đã lưu (bỏ qua login form)"""
        base_url = ConfigReader.get_base_url()
        cookie_page = CookiePage(self.driver, base_url)

        # Load cookies và mở trang
        cookie_page.open_with_cookies()

        # Kiểm tra login thành công
        assert cookie_page.is_logged_in(), "❌ Login bằng cookies thất bại!"
        print("🎉 Đăng nhập bằng cookies thành công!")
