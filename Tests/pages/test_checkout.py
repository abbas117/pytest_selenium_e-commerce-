from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checkout_class:
  def __init__(self, driver):
    self.driver = driver 
    self.checkout_locator = (By.XPATH, '//button[text() = "Checkout"]')
    self.success_message_locator = (By.XPATH,"//span[text()= 'Thank you For Shopping With Us']")
    self.logout_locator = (By.XPATH,"//span[text()= 'Logout']")

  def click_checkout(self):
      self.driver.find_element(*self.checkout_locator).click()
      time.sleep(2)
      
  def verify_success_message(self):
    message = self.driver.find_element(*self.success_message_locator).text
    print(message)

  def click_logout(self):
    self.driver.find_element(*self.logout_locator).click()
    time.sleep(2)
    



