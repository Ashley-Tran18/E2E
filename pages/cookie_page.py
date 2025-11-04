from selenium.webdriver.common.by import By
from base.base_page import BasePage  
from utils.config_reader import ConfigReader
import json
import os
import time
from selenium.common.exceptions import NoSuchElementException

class CookiePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = ConfigReader.get_base_url()
        # self.title = (By.XPATH, "//h1[text() = 'Dashboard']")

    def open_with_cookies(self):
        print("🚀 Opening site using saved cookies...")

        cookie_file = os.path.join(os.getcwd(), "utils", "cookies.json")
        if not os.path.exists(cookie_file):
            print("⚠️ cookies.json not found!")
            return

        # 1️⃣ Mở trang đúng domain trước
        self.driver.get(self.base_url)
        time.sleep(1)

        # 2️⃣ Load cookie từ file
        with open(cookie_file, "r", encoding="utf-8") as f:
            cookies = json.load(f)

        for cookie in cookies:
            cookie.pop("sameSite", None)
            cookie.pop("expiry", None)

            # Nếu web là HTTPS mà cookie có secure=false, sửa lại cho an toàn
            if self.base_url.startswith("https://"):
                cookie["secure"] = True

            try:
                self.driver.add_cookie(cookie)
                print(f"🍪 Added cookie: {cookie['name']}")
            except Exception as e:
                print(f"⚠️ Cannot add cookie {cookie.get('name')}: {e}")

        print("✅ Cookies loaded into browser")
        self.driver.refresh()
        time.sleep(2)

    def is_logged_in(self):
        """Kiểm tra login thành công: tìm avatar hoặc logout button"""
        try:
            # Thay selector này cho đúng trang web của bạn
            # Ví dụ: avatar ở góc phải hoặc 'Logout' trong menu
            self.driver.find_element(By.XPATH, "//h1[text() = 'Dashboard']")
            print("✅ Logged in successfully using cookies!")
            return True
        except NoSuchElementException:
            print("❌ Not logged in (no avatar/logout element found).")
            return False
