from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Перейдите на сайт
# Дождитесь загрузки всех картинок.
# Получите значение атрибута src у 3-й картинки
# Выведите значение в консоль

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 10)

waiter.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, 'img#landscape')))

print(driver.find_element(By.CSS_SELECTOR, "img#award").get_attribute("src"))

driver.quit()
