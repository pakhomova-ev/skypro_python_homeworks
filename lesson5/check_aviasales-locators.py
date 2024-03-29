from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# Локатор логотипа (html-елемент, содержащий в себе значок и слово "авиасейлс")
# <div>a.s__IfjHnfURFBTIihipyW2z>

# driver.get("https://www.aviasales.ru/")
# sleep(3)

# locator_logo_main_page = 'div>a.s__IfjHnfURFBTIihipyW2z'
# logo_main_page = driver.find_element(By.CSS_SELECTOR, locator_logo_main_page)
# print(logo_main_page.get_attribute("href"))

# driver.quit()

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.aviasales.ru/")
sleep(3)
# Локатор поля Откуда - <input#avia_form_origin-input>
locator_input_from = 'input#avia_form_origin-input'

is_form_visible = driver.find_element(
    By.CSS_SELECTOR, locator_input_from).is_displayed()
input_from_find_element = driver.find_element(
    By.CSS_SELECTOR, locator_input_from)
if (is_form_visible is True):
    input_from_find_element.click()
    input_from_find_element.send_keys("Moscow")
    input_from_find_element.send_keys(Keys.ENTER)

print(input_from_find_element.get_attribute("value"))
sleep(2)

# Локатор поля Куда - <input#avia_form_destination-input>
locator_input_to = 'input#avia_form_destination-input'
input_to = driver.find_element(
    By.CSS_SELECTOR, locator_input_to)
input_to.click()
input_to.send_keys("Абакан")
print(input_to.get_attribute("value"))
sleep(2)

# Локатор поля Когда - <button[data-test-id="start-date-field"]>
locator_date_from = 'button[data-test-id="start-date-field'
date_from = driver.find_element(
    By.CSS_SELECTOR, locator_date_from)
date_from.click()

locator_date_from_day = 'div.s__ta_SSbfNo_PsQ7Rdf70_\
                         [data-test-id="date-04.04.2024"]'
date_from_from_day = driver.find_element(
    By.CSS_SELECTOR, locator_date_from_day)
date_from_from_day.click()

sleep(3)
