from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_timer(self, sec):
        timer_input = self._driver.find_element(By.CSS_SELECTOR, "input#delay")
        timer_input.clear()
        timer_input.send_keys(sec)

    def get_calculated_value(self, spinner_time, result_operation):
        WebDriverWait(self._driver, spinner_time + 5).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, "div.screen"), f'{result_operation}'))
        calculate_value = self._driver.find_element(
            By.CSS_SELECTOR, "div.screen").text
        return int(calculate_value)

    def set_num(self, num):
        self._driver.find_element(
            By.XPATH, f"//div[@class='keys']/span[text()='{num}']").click()

    def set_operant(self, operator):
        self._driver.find_element(
            By.XPATH, f"//div[@class='keys']/span[text()='{operator}']").click()
