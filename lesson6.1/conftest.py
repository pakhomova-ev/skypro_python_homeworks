import pytest
from selenium import webdriver


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()    
    driver.maximize_window()
    yield driver
    driver.quit()