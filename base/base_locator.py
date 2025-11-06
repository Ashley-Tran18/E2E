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
        # self.collection_created_msg = (By.XPATH, "//div[contains(@class, 'Toastify__toast-container')]//div[@class = 'Toastify__toast-body']")
        self.collection_created_msg = (By.XPATH, "//div[contains(@class, 'Toastify__toast-container')]//div[text()= 'Collection created successfully!']")
        
        self.collection_edit_header = (By.XPATH, "//h1[@class = 'page-heading-title']")