# from selenium import webdriver
# from utils.config_reader import ConfigReader
# from utils.cookie_manager import CookieManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import pytest
# import allure


# class BaseTest:
#     @pytest.fixture(autouse=True)
#     def setup(self,request):
#         options = Options()
        
#         options.add_argument("--incognito")
#         prefs = {
#             "credentials_enable_service": False,         # Tắt dịch vụ lưu mật khẩu
#             "profile.password_manager_enabled": False    # Tắt gợi ý lưu mật khẩu
#         }
#         options.add_experimental_option("prefs", prefs)
        
#         # options.add_argument('--headless')
#         # options.add_argument('--no-sandbox')
#         # options.add_argument('--disable-dev-shm-usage')
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
#         base_url = ConfigReader.get_base_url()
#         self.driver.get(base_url)
#         self.driver.maximize_window()

#         # Load cookies nếu có — tự động bỏ qua login
#         cookies_loaded = CookieManager.load_cookies(self.driver, base_url)
#         if cookies_loaded:
#             print("✅ Cookies found → Skip login")
#             self.driver.refresh()
#         else:
#             print("⚠️ No cookies found → Manual login required first time")
        
#         # Cho phép các class test kế thừa sử dụng driver
#         request.cls.driver = self.driver
#         yield
#         self.driver.quit()
        

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from utils.config_reader import ConfigReader
# from utils.cookie_manager import CookieManager  # file bạn dùng để save/load cookies


# class BaseTest:
#     @pytest.fixture(autouse=True)
#     def setup(self, request):
#         options = Options()
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         self.driver.maximize_window()
#         request.cls.driver = self.driver

#         base_url = ConfigReader.get_base_url()
#         self.driver.get(base_url)

#         # 🧠 Load cookies nếu có
#         cookies = CookieManager.load_cookies(self.driver, base_url)
#         if cookies:
#             for cookie in cookies:
#                 # Selenium yêu cầu vào đúng domain trước khi add_cookie
#                 self.driver.add_cookie(cookie)
#             print("✅ Cookies loaded into browser")
#             # Sau khi add cookies xong, reload lại base_url để tự login
#             self.driver.get(base_url)
#         else:
#             print("⚠️ No cookies found, will need manual login first")

#         yield
#         self.driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.config_reader import ConfigReader
from utils.cookie_manager import CookieManager


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        """Khởi tạo trình duyệt và tự động load cookies nếu có"""
        options = Options()

        # Tuỳ chọn bảo mật & tiện ích
        options.add_argument("--incognito")
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)

        # Mở Chrome
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.maximize_window()
        request.cls.driver = self.driver

        # Mở trang chính
        base_url = ConfigReader.get_base_url()
        self.driver.get(base_url)

        # 🧠 Tự động load cookies nếu có để skip login
        cookies = CookieManager.load_cookies(self.driver, base_url)
        if cookies:
            print("✅ Cookies found → Skip login")
            self.driver.refresh()
        else:
            print("⚠️ No cookies found → Please login manually, then run CookieManager.save_cookies() once")

        yield
        self.driver.quit()
