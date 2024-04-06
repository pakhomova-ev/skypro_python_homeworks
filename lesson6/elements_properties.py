from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=ChromeService(
#     ChromeDriverManager().install()))


# driver.get("https://ya.ru")

# usd = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]')
# txt = usd.text #в переменную с методом text соберется информация об элементе

# # #После сокращения:
# # txt = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').text

# # print(txt)

# print(txt) #запрос выведет информацию из переменной в терминал

# driver.quit() #закрываем драйвер

# =============Method tag

# tag = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').tag_name
# собираем информацию о теге в переменную

# print(tag) #выводим информацию из переменной в терминал

# driver.quit()

# Id
# id = driver.find_element(By.CSS_SELECTOR,
#                          'a[title="USD MOEX"]').id
# собираем информацию об идентификаторе

# print(id)  #выводим информацию из переменной в терминал

# driver.quit()

# Благодаря методу is_displayed мы можем отслеживать
# видимость элементов на странице.

# driver = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install()))

# driver.get("http://uitestingplayground.com/visibility")
# is_displayed = driver.find_element(
#     By.CSS_SELECTOR, "#transparentButton").is_displayed()

# print(is_displayed)

# driver.find_element(By.CSS_SELECTOR, "#hideButton").click() #нажатие на Hide
# # Opacity 0 окажется скрытой
# sleep(2)

# #еще раз проверим видимость Opacity 0:
# is_displayed = driver.find_element(
#     By.CSS_SELECTOR, "#transparentButton").is_displayed()

# print(is_displayed) #еще раз выводим статус видимости Opacity 0

# sleep(2)

# driver.quit()

# Метод  is_enabled — проверяет, доступен ли элемент
# интерфейса для взаимодействия
# (обычно это кнопки, ссылки и другие интерактивные элементы).

# driver = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://demoqa.com/radio-button")
# is_enabled = driver.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled()
# print(is_enabled)

# is_enabled = driver.find_element(By.CSS_SELECTOR, "#noRadio").is_enabled()
# print(is_enabled)

# driver.quit()

# is_selected проверяет, выбирается элемент или нет: например,
# стоит ли галочка в чекбоксе.

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/checkboxes")

is_selected1 = driver.find_element(
    By.CSS_SELECTOR, "input[type='checkbox']:nth-child(1)").is_selected()
print(is_selected1)

is_selected2 = driver.find_element(
    By.CSS_SELECTOR, "input[type='checkbox']:nth-child(3)").is_selected()
print(is_selected2)

driver.quit()
