from selenium.webdriver.common.by import By
from utils.config_reader import ConfigReader

class BaseLocator:
    def __init__(self, driver):
        self.driver = driver    
        self.timeout = ConfigReader.get_timeout()
        
        # Login Page Locators
        self.email_input = (By.XPATH, "//div[@class = 'form-field']//input[@id = 'field-email']")
        self.password_input = (By.XPATH, "//div[@class = 'form-field']//input[@id = 'field-password']")
        self.login_btn = (By.XPATH, "//div[@class = 'form-submit-button flex border-t border-divider mt-4 pt-4 justify-between']//button")
        self.dashboard_header = (By.XPATH, "//h1[@class = 'page-heading-title']")
        self.login_error_message = (By.XPATH, "//div[@class = 'Toastify']//div[@class = 'Toastify__toast-body']")

        # Collections Page Locators
        self.admin_nav = (By.XPATH, "//div[@class = 'admin-navigation']")
        self.collections_menu = (By.XPATH, "//li[@class='root-nav-item nav-item']//a[@href='https://e2e.evershop.app/admin/collections']")
        self.new_collections_btn = (By.XPATH, "//div[@class = 'flex justify-end space-x-2 items-center']//span[text() = 'New Collection']")
        self.collection_name_input = (By.XPATH, "//div[@class = 'card-session-content pt-lg']//input[@id = 'field-name']")
        self.collection_code_input = (By.XPATH, "//div[@class = 'card-session-content pt-lg']//input[@id = 'field-code']")
        self.collection_des_type = (By.XPATH, "//div[contains(@class , 'row-templates')]//a[1]")
        self.collection_des_input = (By.XPATH, "//div[contains(@class, 'row grid')]//div[@class = 'ce-paragraph cdx-block']")
        self.cancel_btn = (By.XPATH, "//div[@class = 'form-submit-button flex border-t border-divider mt-4 pt-4 justify-between']//button[@class = 'button danger outline']")
        self.add_collection_btn = (By.XPATH, "//div[@class = 'form-submit-button flex border-t border-divider mt-4 pt-4 justify-between']//button[@class = 'button primary']")
        self.collection_created_msg = (By.XPATH, "//div[contains(@class, 'Toastify__toast-container')]//div[text()= 'Collection created successfully!']")
        self.collection_edit_header = (By.XPATH, "//h1[@class = 'page-heading-title']")
        self.edit_collection_back_btn = (By.XPATH, "//div[contains(@class, 'flex justify-start')]//span[@class = 'flex items-center justify-center']")
        self.collection_table = (By.XPATH, "//tbody/tr/td[3]//a")
        self.collection_rows = (By.XPATH, "//tbody/tr")
        self.collection_cell = (By.XPATH, "//./td[3]")
        self.collection_checkbox = (By.XPATH, "//./td[1]//input[@type='checkbox']")
        self.collection_del_btn = (By.XPATH, "//div[contains(@class, 'border border-divider')]//span[text()= 'Delete']")
        self.collection_confirm_del_btn = (By.XPATH, "//div[contains(@class, 'flex justify-end space-x-2')]//button[@class = 'button critical']//span[text() = 'Delete']")

        











