from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def test_caculator_spinner_time():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    driver.maximize_window()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    driver.find_element(
        By.CSS_SELECTOR, "input#delay").clear()
    driver.find_element(
        By.CSS_SELECTOR, "input#delay").send_keys(45)

    print(driver.find_element(
        By.CSS_SELECTOR, "input#delay")
        .get_attribute("value"))

    driver.find_element(
        By.XPATH, "//div[@class='top']/span[text()='C']").click()

    driver.find_element(
        By.XPATH, "//div[@class='keys']/span[text()='7']").click()
    driver.find_element(
        By.XPATH, "//div[@class='keys']/span[text()='+']").click()
    driver.find_element(
        By.XPATH, "//div[@class='keys']/span[text()='8']").click()
    driver.find_element(
        By.XPATH, "//div[@class='keys']/span[text()='=']").click()

    start_time = time.time()
    print(f'start time {start_time}')

    waiter = WebDriverWait(driver, 50)

    waiter.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, "div.screen"), "15"))

    end_time = time.time()
    print(f'end time {end_time}')
    result = round(end_time - start_time)
    print(result)

    assert result == 45

    driver.quit()
