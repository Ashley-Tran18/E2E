import json
import os
from utils.config_reader import ConfigReader

class CookieManager:
    COOKIE_PATH = os.path.join("utils", "cookies.json")

    @staticmethod
    def save_cookies(driver):
        """Lưu cookies hiện tại của trình duyệt sau khi login thành công"""
        cookies = driver.get_cookies()
        with open(CookieManager.COOKIE_PATH, "w", encoding="utf-8") as f:
            json.dump(cookies, f, indent=2, ensure_ascii=False)
        print("💾 Cookies saved to cookies.json")

    @staticmethod
    def load_cookies(driver, base_url):
        """Load cookies từ file để bỏ qua login"""
        if not os.path.exists(CookieManager.COOKIE_PATH):
            print("⚠️ cookies.json not found")
            return False

        with open(CookieManager.COOKIE_PATH, "r", encoding="utf-8") as f:
            cookies = json.load(f)

        # Phải mở domain trước mới add được cookie
        base_url = ConfigReader.get_base_url()
        driver.get(base_url)

        for cookie in cookies:
            # Selenium không chấp nhận sameSite và đôi khi lỗi expiry float
            cookie.pop("sameSite", None)

            # Chỉ giữ các field hợp lệ
            cookie_data = {
                k: cookie[k] for k in cookie.keys() & {
                    "name", "value", "domain", "path", "secure", "httpOnly"
                }
            }

            if "expiry" in cookie:
                try:
                    cookie_data["expiry"] = int(cookie["expiry"])
                except Exception:
                    pass

            try:
                driver.add_cookie(cookie_data)
            except Exception as e:
                print(f"[!] Cannot add cookie {cookie.get('name')}: {e}")

        print("✅ Cookies loaded into browser")
        return True
