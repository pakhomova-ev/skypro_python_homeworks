import pytest
from selenium import webdriver
import allure

@allure.step("open browser")
@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()    
    driver.maximize_window()
    yield driver
    driver.quit()