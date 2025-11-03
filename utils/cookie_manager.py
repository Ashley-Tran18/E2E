# import json
# import os

# class CookieManager:
#     COOKIE_PATH = os.path.join("utils", "cookies.json")

#     @staticmethod
#     def save_cookies(driver):
#         """Lưu cookies hiện tại của trình duyệt sau khi login thành công"""
#         cookies = driver.get_cookies()
#         with open(CookieManager.COOKIE_PATH, "w") as f:
#             json.dump(cookies, f)
#         print("💾 Cookies saved to cookies.json")

#     @staticmethod
#     def load_cookies(driver, base_url):
#         """Load cookies từ file để bỏ qua login"""
#         if not os.path.exists(CookieManager.COOKIE_PATH):
#             print("⚠️ cookies.json not found")
#             return False

#         with open(CookieManager.COOKIE_PATH, "r") as f:
#             cookies = json.load(f)

#         driver.get(base_url)
#         for cookie in cookies:
#             # Selenium không chấp nhận sameSite
#             cookie.pop("sameSite", None)
#             driver.add_cookie(cookie)

#         print("✅ Cookies loaded into browser")
#         return True


# import json
# import os

# class CookieManager:
#     COOKIE_FILE = "cookies.json"

#     @staticmethod
#     def save_cookies(driver):
#         cookies = driver.get_cookies()
#         with open(CookieManager.COOKIE_FILE, "w") as f:
#             json.dump(cookies, f)
#         print("✅ Cookies saved to file")

#     @staticmethod
#     def load_cookies(driver, base_url):
#         if not os.path.exists(CookieManager.COOKIE_FILE):
#             print("⚠️ No cookie file found")
#             return []   # ← Trả về list rỗng, không phải True/False

#         with open(CookieManager.COOKIE_FILE, "r") as f:
#             cookies = json.load(f)

#         driver.get(base_url)  # mở trước để set cookies
#         for cookie in cookies:
#             # Selenium không cho thêm "sameSite" hoặc "secure" đôi khi
#             cookie.pop("sameSite", None)
#             cookie.pop("secure", None)
#             try:
#                 driver.add_cookie(cookie)
#             except Exception as e:
#                 print(f"⚠️ Failed to add cookie: {e}")

#         print("✅ Cookies loaded into browser")
#         return cookies  # ← Trả về danh sách cookies

import json
import os

class CookieManager:
    COOKIE_FILE = "cookies.json"

    @staticmethod
    def save_cookies(driver):
        cookies = driver.get_cookies()
        with open(CookieManager.COOKIE_FILE, "w") as f:
            json.dump(cookies, f)
        print("✅ Cookies saved to file")

    @staticmethod
    def load_cookies(driver, base_url):
        """Load cookies từ file và add vào browser"""
        if not os.path.exists(CookieManager.COOKIE_FILE):
            print("⚠️ No cookie file found")
            return []

        with open(CookieManager.COOKIE_FILE, "r") as f:
            cookies = json.load(f)

        driver.get(base_url)
        for cookie in cookies:
            cookie.pop("sameSite", None)
            cookie.pop("secure", None)
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"⚠️ Failed to add cookie: {e}")

        print("✅ Cookies loaded into browser")
        return cookies
