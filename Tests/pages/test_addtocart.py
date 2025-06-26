from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Test_loginpage import LoginPage
from BaseClass.baseclass import BaseClass

class Addtocart:
    def __init__(self, driver):
        self.driver = driver
        self.product_locator = (By.XPATH, "//div[@class='Products_item__Za1Q4']")
        self.title_locator = (By.XPATH, ".//div[@class='Products_title__7ggYL']")
        self.addtocart_locator = (By.XPATH, ".//button[text()='Add To Cart']")
        self.cartbtn_locator = (By.XPATH, "//div[@class='Header_detailCart__SrHWm']")

    def click_add_to_cart(self):
        target_products = ["To Kill a Mockingbird", "War and Peace", "The Great Gatsby"]

        total_products = len(self.driver.find_elements(*self.product_locator))
        print(f"Total products found: {total_products}")

        for i in range(total_products):
            # 🔄 Re-fetch products every loop to avoid stale element
            products = self.driver.find_elements(*self.product_locator)
            product = products[i]

            title = product.find_element(*self.title_locator).text
            print(f"Found product: {title}")

            if title in target_products:
                addtocart_btn = product.find_element(*self.addtocart_locator)
                addtocart_btn.click()
                print(f"✅ Added '{title}' to cart")
        time.sleep(2)
        
    def cartbtn(self):
        self.driver.find_element(*self.cartbtn_locator).click()
        time.sleep(2)