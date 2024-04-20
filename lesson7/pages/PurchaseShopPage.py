from selenium.webdriver.common.by import By
import re


class PurchasePage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def login_shop(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "input#user-name").send_keys("standard_user")
        self._driver.find_element(
            By.CSS_SELECTOR, "input#password").send_keys("secret_sauce")
        self._driver.find_element(
            By.CSS_SELECTOR, "input#login-button").click()

    def add_items_to_cart(self, list):
        for item in list:
            self._driver.find_element(
                By.CSS_SELECTOR,
                f"button[data-test='add-to-cart-{item}']").click()

        self._driver.find_element(
            By.CSS_SELECTOR, "a[data-test='shopping-cart-link']").click()

    def open_cart(self):
        self._driver.get('https://www.saucedemo.com/cart.html')
        self._driver.find_element(
            By.CSS_SELECTOR, "button[data-test='checkout']").click()

    def fill_info_form(self, first_name, last_name, postal_code):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[data-test='firstName']"
            ).send_keys(first_name)
        self._driver.find_element(
            By.CSS_SELECTOR, "input[data-test='lastName']"
            ).send_keys(last_name)
        self._driver.find_element(
            By.CSS_SELECTOR, "input[data-test='postalCode']"
            ).send_keys(postal_code)

        self._driver.find_element(By.CSS_SELECTOR,
                                  "input[data-test='continue']").click()

    def get_total_amount_in_cart(self):
        total_amount = self._driver.find_element(
            By.CSS_SELECTOR, "div[data-test='total-label']").text
        result = re.search(r'\$([0-9]+\.[0-9]+)', total_amount)

        return result.group()
