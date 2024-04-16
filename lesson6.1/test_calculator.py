import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.parametrize(
        'spinner_timer, first_num, second_num, operator, result',
        [(45, 7, 8, '+', 15)])
def test_caculator_spinner_time(spinner_timer, first_num,
                                second_num, operator, result):

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    driver.maximize_window()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.CSS_SELECTOR, "input#delay")
    delay_input.clear()
    delay_input.send_keys(spinner_timer)

    driver.find_element(
        By.XPATH, "//div[@class='top']/span[text()='C']").click()

    driver.find_element(
        By.XPATH, f"//div[@class='keys']/span[text()='{first_num}']").click()
    driver.find_element(
        By.XPATH, f"//div[@class='keys']/span[text()='{operator}']").click()
    driver.find_element(
        By.XPATH, f"//div[@class='keys']/span[text()='{second_num}']").click()
    driver.find_element(
        By.XPATH, "//div[@class='keys']/span[text()='=']").click()

    start_time = time.time()

    waiter = WebDriverWait(driver, spinner_timer + 5)

    waiter.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, "div.screen"), f'{result}'))

    end_time = time.time()

    result_time = round(end_time - start_time)

    assert result_time == spinner_timer

    driver.quit()
