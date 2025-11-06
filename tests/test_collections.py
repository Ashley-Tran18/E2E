from base.base_test import BaseTest
from pages.collections_page import CollectionsPage
from utils.config_reader import ConfigReader
from pages.login_page import LoginPage
import allure
from time import sleep

@allure.story("Verify user can open Collection page after skipping login via cookies")
class TestCollection(BaseTest):
    def test_collection_page(self):
        
        collection = CollectionsPage(self.driver)
        collection.get_cookie()
        
        # Navigate to Collection page
        collection.navigate_to_collections_page()
        assert "collection" in self.driver.current_url.lower()
        # self.driver.save_screenshot("navigate_to_collections_page_success.png")
        print("✅ Navigate to Collection Page successfully through menu")

        collection.create_new_collection()
        collection.add_collection_data_and_submit(ConfigReader.get_collection_data)
        # collection.verify_created_collection_succefully()
        # collection.verify_collection_edit_page_display()

        is_created = False
        if collection.is_created():
            self.driver.save_screenshot("Created collection successfully.png")
            print("✅ Create a new Collection Page successfully")
            is_created = True
            
        else:
            self.driver.save_screenshot("Created collection failed.png")
            print("✅ Create a new Collection Page failed")
            
        assert is_created