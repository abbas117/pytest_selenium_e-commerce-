from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
  def __init__(self, driver):
    self.driver = driver
    self.username_locator = (By.ID,'uname')
    self.password_locator = (By.ID,'pass')
    self.login_locator = (By.XPATH, '//button[@class="Login_btn__pALc8"]')

  def clear_username(self):
    self.driver.find_element(*self.username_locator).clear()

  def enter_username(self,username):
    self.driver.find_element(*self.username_locator).send_keys(username)

  def clear_password(self):
    self.driver.find_element(*self.password_locator).clear()

  def enter_password(self,passowrd):
    self.driver.find_element(*self.password_locator).send_keys(passowrd)
    time.sleep(2)

  def click_login(self):
    self.driver.find_element(*self.login_locator).click()

    
