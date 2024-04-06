from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("http://www.uitestingplayground.com/ajax")

driver.implicitly_wait(20)

driver.get("http://www.uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

driver.quit()


driver.get("http://www.uitestingplayground.com/progressbar")
waiter = WebDriverWait(driver, 40, 0.1)
#  в переменной находится экземпляр с параметрами:
# 1 параметр - наш драйвер, 2 параметр - 40 секунд на ожидание

driver.find_element(By.CSS_SELECTOR, "#startButton").click()

waiter.until(EC.text_to_be_present_in_element((
    By.CSS_SELECTOR, "#progressBar"), "75%"))

driver.find_element(By.CSS_SELECTOR, "#stopButton").click()
print(driver.find_element(By.CSS_SELECTOR, "#result").text)

driver.quit()
