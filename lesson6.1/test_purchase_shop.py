from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re


def test_total_in_cart():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(
        By.CSS_SELECTOR, "input#user-name").send_keys("standard_user")
    driver.find_element(
        By.CSS_SELECTOR, "input#password").send_keys("secret_sauce")
    driver.find_element(
        By.CSS_SELECTOR, "input#login-button").click()

    driver.find_element(
        By.CSS_SELECTOR,
        "button[data-test='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element(
        By.CSS_SELECTOR,
        "button[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    driver.find_element(
        By.CSS_SELECTOR,
        "button[data-test='add-to-cart-sauce-labs-onesie']").click()

    driver.find_element(
        By.CSS_SELECTOR,
        "a[data-test='shopping-cart-link']").click()

    driver.find_element(
        By.CSS_SELECTOR,
        "button[data-test='checkout']").click()

    driver.find_element(
        By.CSS_SELECTOR,
        "input[data-test='firstName']").send_keys("Ippolit")
    driver.find_element(
        By.CSS_SELECTOR,
        "input[data-test='lastName']").send_keys("Ippolitov")
    driver.find_element(
        By.CSS_SELECTOR,
        "input[data-test='postalCode']").send_keys("123567")

    driver.find_element(
        By.CSS_SELECTOR,
        "input[data-test='continue']").click()

    text = driver.find_element(
        By.XPATH, "//div[@data-test='total-label']").text

    result = re.search(r'\$([0-9]+\.[0-9]+)', text)
    print(result.group())

    assert result.group() == '$58.29'
