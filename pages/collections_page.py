from selenium.webdriver.common.by import By
from base.base_page import BasePage
from base.base_locator import BaseLocator
from utils.config_reader import ConfigReader
from pages.login_page import LoginPage
from time import sleep

class CollectionsPage(BasePage, BaseLocator):
    def __init__(self, driver):
        super().__init__(driver)
        BaseLocator.__init__(self, driver)

    def get_cookie(self):
        "Step 1: Login to the website"
        login_page = LoginPage(self.driver) 
        login_page.login(*ConfigReader.get_email_password()) 

    def navigate_to_collections_page(self):
        "Step 2: Navigate to Collections page"
        self.wait_and_click(self.collections_menu)

    def create_new_collection(self):
        "Step 3: Create a new Collection"
        self.wait_and_click(self.new_collections_btn)    

    def add_collection_data_and_submit(self, collection_data):
        "Step 4: Add collection data & submit"
        collection_data = ConfigReader.get_collection_data()
        collection_name = collection_data['collection_name']
        collection_code = collection_data['collection_code']
        collection_des = collection_data['collection_des']
        
        self.send_keys(self.collection_name_input, collection_name)
        self.send_keys(self.collection_code_input, collection_code)
        self.wait_and_click(self.collection_des_type)
        self.send_keys(self.collection_des_input, collection_des)
        # sleep(2)
        self.wait_and_click(self.add_collection_btn)
    
    # def verify_created_collection_succefully(self):
    #     "Verify collection is created successfully"
    #     try:
    #         self.presence_of_element(self.collection_created_msg)
    #         return True
    #     except:
    #         return False

    # def verify_collection_edit_page_display(self):
    #     "Verify collection is created successfully"
    #     try:
    #         self.wait_for_element_visible(self.collection_edit_header)
    #         return True
    #     except:
    #         return False
        
    def is_created(self):
        "Verify created successfully"
        try:
            self.wait_for_element_visible(self.collection_edit_header)
            return True
        except:
            return False
        
    


    # def verify_collection_created_successfully(self):
    #     return self.get_text(self.collection_created_msg)



