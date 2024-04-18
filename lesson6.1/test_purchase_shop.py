from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re

total_in_cart = '$58.29'
product_buttons = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]


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

    for i in product_buttons:
        driver.find_element(
            By.CSS_SELECTOR, f"button[data-test='add-to-cart-{i}']").click()

    driver.find_element(
        By.CSS_SELECTOR, "a[data-test='shopping-cart-link']").click()

    driver.find_element(
        By.CSS_SELECTOR, "button[data-test='checkout']").click()

    driver.find_element(
        By.CSS_SELECTOR, "input[data-test='firstName']").send_keys("Ippolit")
    driver.find_element(
        By.CSS_SELECTOR, "input[data-test='lastName']").send_keys("Ippolitov")
    driver.find_element(
        By.CSS_SELECTOR, "input[data-test='postalCode']").send_keys("123567")

    driver.find_element(By.CSS_SELECTOR, "input[data-test='continue']").click()

    items_in_cart = driver.find_elements(
        By.CSS_SELECTOR, "div[data-test='inventory-item']")

    assert len(items_in_cart) == len(product_buttons)

    text = driver.find_element(
        By.CSS_SELECTOR, "div[data-test='total-label']").text

    driver.quit()

    result = re.search(r'\$([0-9]+\.[0-9]+)', text)

    assert result.group() == total_in_cart
