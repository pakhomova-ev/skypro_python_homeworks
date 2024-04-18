from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Перейдите на страницу http://uitestingplayground.com/ajax
# Нажмите на синюю кнопку
# Получите текст из зеленой плашки
# Выведите его в консоль (Data loaded with AJAX get request)

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

waiter = WebDriverWait(driver, 20)
driver.get(
    "http://uitestingplayground.com/ajax")

driver.find_element(By.ID, "ajaxButton").click()
waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.bg-success')))

print(driver.find_element(By.CSS_SELECTOR, 'p.bg-success').text)

driver.quit()
