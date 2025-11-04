# pages/dashboard_page.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    # Locators
    dashboard_title = (By.XPATH, "//h1[text() = 'Dashboard']")

    # def get_dashboard_title(self):
    #     return self.get_text(self.dashboard_title)  


    # def is_on_dashboard(self):
    #     return "Dashboard" in self.get_dashboard_title()

    def is_on_dashboard(self):
        """Kiểm tra đang ở Dashboard thật"""
        try:
            text = self.get_text(self.dashboard_title)
            return "Dashboard" in text
        except:
            return False

    def get_welcome_message(self):
        return self.get_text(self.dashboard_title)