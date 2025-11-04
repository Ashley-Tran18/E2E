# tests/test_dashboard.py
from utils.cookie_manager import CookieManager
from base.base_test import BaseTest
from base.base_page import BasePage
from pages.dashboard_page import DashboardPage
from time import sleep

class TestDashboard(BaseTest):
    
    def test_dashboard_without_login(self):
        print(" Bước 1: Load cookies...")
        CookieManager.load_cookies(self.driver, "https://e2e.evershop.app/")

        print(" Bước 2: In cookies để kiểm tra...")
        cookies = self.driver.get_cookies()
        for c in cookies:
            print(f"  {c['name']} = {c['value'][:30]}...")

        print(" Bước 3: Vào thẳng trang Admin...")
        self.driver.get("https://e2e.evershop.app/admin")
        sleep(3)

        print(" Bước 4: Kiểm tra Dashboard...")
        dashboard = DashboardPage(self.driver)
        assert dashboard.is_on_dashboard(), " Không vào được Dashboard – bị redirect login!"

        welcome = dashboard.get_welcome_message()
        print(f" CHÀO MỪNG: {welcome}")
        print(" TEST PASS – ĐÃ LOGIN BẰNG COOKIES! 🚀")