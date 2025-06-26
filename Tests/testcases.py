from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Test_loginpage import LoginPage
from BaseClass.baseclass import BaseClass
from pages.test_addtocart import Addtocart
from pages.test_checkout import Checkout_class

# @pytest.mark.usefixtures("setup")
class TestLogin(BaseClass):
    @pytest.mark.parametrize("username , password",[("auth_user","auth_password")])
    def test_login_valid(self, username, password):
        lp = LoginPage(self.driver)
        lp.clear_username()
        lp.enter_username(username)
        lp.clear_password()
        lp.enter_password(password)
        lp.click_login()

    def test_add_to_cart(self):
        ac = Addtocart(self.driver)
        ac.click_add_to_cart()
        ac.cartbtn()

    def test_checkout_btn(self):
        cb = Checkout_class(self.driver)
        cb.click_checkout()
        cb.verify_success_message()
        cb.click_logout()