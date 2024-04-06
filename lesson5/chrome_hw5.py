from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

# 01.01 Клик по кнопке
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(3)

buttonAddElement = driver.find_element(
    By.CSS_SELECTOR, 'button[onclick="addElement()"]')
for i in range(5):
    buttonAddElement.click()
sleep(3)

buttonDeleteElement = 'div#elements>button.added-manually'
elementsButton = driver.find_elements(By.CSS_SELECTOR, buttonDeleteElement)
print(f'01.01 Клик по кнопке. Chrome_Кнопок в списке - {len(elementsButton)}')


# 02.01 Клик по кнопке без ID

# Open new tab for next task
driver.switch_to.new_window('tab')

driver.get("http://uitestingplayground.com/dynamicid")
sleep(5)
buttonDynamicId = driver.find_element(
    By.CSS_SELECTOR, 'button.btn.btn-primary')
for i in range(3):
    buttonDynamicId.click()
    sleep(3)

    print("02.01 Клик по кнопке без ID. ButtonDynamicId - " +
          driver.find_element(By.CSS_SELECTOR, buttonDynamicId)
          .get_attribute("id"))
    driver.refresh()

    sleep(3)

# 03.01 Клик по кнопке с CSS-классом

# Open new tab for next task
driver.switch_to.new_window('tab')

driver.get("http://uitestingplayground.com/classattr")

buttonDynamicId = driver.find_element(
    By.CSS_SELECTOR, 'button.btn-primary')
sleep(5)
for i in range(3):
    buttonDynamicId.click()
    sleep(3)
    alert = driver.switch_to.alert
    alert.accept()
    sleep(3)

# 04.01 Модальное окно

# Open new tab for next task
driver.switch_to.new_window('tab')

driver.get("https://the-internet.herokuapp.com/entry_ad")
sleep(3)
closeTheModalWindow = driver.find_element(
    By.CSS_SELECTOR,
    "div#modal div.modal-footer>p").click()
sleep(2)

# 05.02 Поле ввода

# Open new tab for next task
driver.switch_to.new_window('tab')

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(3)

input_text = driver.find_element(By.CSS_SELECTOR,
                                 'div.example>input[type="number"]')

input_text.send_keys(1000)
sleep(3)
input_text.clear()
sleep(3)

input_text.send_keys(999)
sleep(3)

# 06.02 Форма авторизации

# Open new tab for next task
driver.switch_to.new_window('tab')

driver.get("http://the-internet.herokuapp.com/login")
sleep(3)
input_username = "div.large-6>input#username"
driver.find_element(By.CSS_SELECTOR, input_username).send_keys("tomsmith")

input_password = "div.large-6>input#password"
driver.find_element(By.CSS_SELECTOR, input_password).send_keys(
    "SuperSecretPassword!")

button_login = 'button[type="submit"]'
driver.find_element(By.CSS_SELECTOR, button_login).click()
sleep(3)

driver.quit()
