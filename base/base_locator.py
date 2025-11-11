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

        
        # Categories Page Locators
        
        # Products Page Locators
        self.products_menu = (By.XPATH, "//li[@class='root-nav-item nav-item']//a[@href='https://e2e.evershop.app/admin/products']")
        self.new_product_btn = (By.XPATH, "//div[@class = 'flex justify-end space-x-2 items-center']//span[text() = 'New Product']")
        self.product_name_input = (By.XPATH, "//div[@class = 'card-session-content pt-lg']//input[@id = 'field-name']")
        self.product_sku_input = (By.XPATH, "//div[@class = 'card-session-content pt-lg']//input[@id = 'field-sku']")
        self.product_price_input = (By.XPATH, "//div[@class = 'card-session-content pt-lg']//input[@id='field-price']")
        self.product_weight_input = (By.XPATH, "//div[@class = 'card-session-content pt-lg']//input[@id='field-weight']")
        self.select_product_category = (By.XPATH, "//div[@class = 'mt-4 relative']//a[@class = 'text-interactive']")
        self.product_des_type = (By.XPATH, "//div[contains(@class , 'row-templates')]//a[3]")
        self.product_available_block = (By.XPATH, "//div[@class = 'column p-3 md:col-span-1']")
        self.product_des_type_plus_1 = (By.XPATH, "//div[@class = 'column p-3 md:col-span-1']//div[@class = 'ce-toolbar__plus']")
        self.product_des_quote_select = (By.XPATH, "//div[@class='column p-3 md:col-span-1']//div[text() = 'Quote']")
        self.product_quote_input = (By.XPATH, "//div[@class =  'column p-3 md:col-span-1']//div[@class = 'cdx-input cdx-quote__text']")
        self.product_quote_caption_input = (By.XPATH, "//div[@class =  'column p-3 md:col-span-1']//div[@class = 'cdx-input cdx-quote__caption']")
        self.product_des_type_plus_2 = (By.XPATH, "//div[@class = 'column p-3 md:col-span-2']//div[@class = 'ce-toolbar__plus']")
        self.product_des_rawhtml_select = (By.XPATH, "//div[@class='column p-3 md:col-span-2']//div[text() = 'Raw HTML']")
        self.product_rawhtml_input = (By.XPATH, "//div[@class='column p-3 md:col-span-2']//div[@class = 'cdx-block ce-rawtool']")
        self.product_upload_image = (By.XPATH, "//div[@class = 'uploader grid-item']//div[@class = 'uploader-icon']")
        self.product_url_key_input = (By.XPATH, "//div[@class = 'card-session-content pt-lg']//input[@id = 'field-url_key']")
        self.product_meta_title_input = (By.XPATH, "//div[@class = 'card-session-content pt-lg']//input[@id = 'field-meta_title']")
        self.product_meta_des_input = (By.XPATH, "//div[@class = 'card-session-content pt-lg']//div[@class = 'form-field undefined']//textarea")
        self.product_quantity_input = (By.XPATH, "//div[@class = 'card-session-content pt-lg']//input[@id = 'field-qty']")
        self.product_des_input = (By.XPATH, "//div[contains(@class, 'row grid')]//div[@class = 'ce-paragraph cdx-block']")
        self.product_color_list = (By.XPATH, "//tr//select[@id = 'field-attributes.1.value']")
        self.add_product_btn = (By.XPATH, "//div[@class = 'form-submit-button flex border-t border-divider mt-4 pt-4 justify-between']//button[@class = 'button primary']")
        

        self.cancel_btn = (By.XPATH, "//div[@class = 'form-submit-button flex border-t border-divider mt-4 pt-4 justify-between']//button[@class = 'button danger outline']")
        self.collection_created_msg = (By.XPATH, "//div[contains(@class, 'Toastify__toast-container')]//div[text()= 'Collection created successfully!']")
        self.collection_edit_header = (By.XPATH, "//h1[@class = 'page-heading-title']")
        self.edit_collection_back_btn = (By.XPATH, "//div[contains(@class, 'flex justify-start')]//span[@class = 'flex items-center justify-center']")
        self.collection_table = (By.XPATH, "//tbody/tr/td[3]//a")
        self.collection_rows = (By.XPATH, "//tbody/tr")
        self.collection_cell = (By.XPATH, "//./td[3]")
        self.collection_checkbox = (By.XPATH, "//./td[1]//input[@type='checkbox']")
        self.collection_del_btn = (By.XPATH, "//div[contains(@class, 'border border-divider')]//span[text()= 'Delete']")
        self.collection_confirm_del_btn = (By.XPATH, "//div[contains(@class, 'flex justify-end space-x-2')]//button[@class = 'button critical']//span[text() = 'Delete']")

        











