from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture(autouse= True, scope='class')
def setup(request):
  driver = webdriver.Chrome()
  driver.get("https://ecommerce.artoftesting.com/")
  driver.maximize_window()
  driver.implicitly_wait(5)
  request.cls.driver = driver
  yield
  driver.quit()
