from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

my_cookie = {'name': 'cookie_policy',
             'value': '1'}

driver.get("https://labirint.ru/")  # переход на страницу
driver.add_cookie(my_cookie)  # добавление cookie

driver.refresh()  # обновление страницы
driver.delete_all_cookies()  # даление всех cookie
# Cookies можно удалять не полностью, но и по отдельности с помощью метода
# driver.delete_cookie()
# , если указать в параметрах метода имя переменной,
# в которой содержится нужное ключ — значение.

# cookies = driver.get_cookies() #переменная, в которую соберутся cookies
# print(cookies) #запрос на вывод данных в терминал

# Давайте обратимся к cookie с именем
# 'PHPSESSID'
# (в случайном порядке увидели и скопировали из терминала)
# с помощью метода get_cookie
cookie = driver.get_cookie('PHPSESSID')
# положили метод в переменную cookie
print(cookie)
# попросили вывести данных по этой cookie в терминал

driver.refresh()

sleep(10)
driver.quit()
