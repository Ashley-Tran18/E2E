from base.base_test import BaseTest
from pages.products_page import ProductsPage
from utils.config_reader import ConfigReader
import allure
from time import sleep

@allure.story("Verify user can open Collection page after skipping login via cookies")
class TestProducts(BaseTest):
    def test_categories_page(self):
        
        "Step 1: Login to the website"
        product = ProductsPage(self.driver)
        product.get_cookie()

        "Step 2: Navigate to Products page"
        product.navigate_to_products_page()
        assert "products" in self.driver.current_url.lower()
        # self.driver.save_screenshot("navigate_to_products_page_success.png")
        print("✅ Navigate to Products Page successfully through menu")

        "Step 3: Create a new product"
        product.create_new_product()
        product.add_product_data_and_submit(ConfigReader.get_product_data)
        self.driver.save_screenshot("create_new_collections_success.png")

        """Verify the collection created successfully"""
        """Show toast message"""
        # collection.verify_collection_created_successfully()
        # self.driver.save_screenshot("created_collections_success.png")
        
        """Or redirect to edit page"""
        # collection.verify_redirect_to_collection_edit_page()
        # self.driver.save_screenshot("redirect_to_collections_edit__page_success.png")
        
        # "Step 4: Back to the Collection listing page"
        # collection.back_to_collection_page()
        # self.driver.save_screenshot("new_collections_display.png")

        # """Verify the newly collection added"""
        # collection.verify_new_collection_added(ConfigReader.get_collection_data)
        # sleep(2)

        # """Delete collection"""
        # sleep(2)
        # collection.del_collection()
        # self.driver.save_screenshot("deleted.png")
        
        
        
        
        

