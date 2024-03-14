"""В файле объявите класс User
- Объявите в классе конструктор.
- Конструктор должен принимать на вход 2 параметра:
first_name — имя.
last_name — фамилия.
Помните, что все методы класса, включая конструктор,
принимают первым параметром
self
- Создайте в классе 3 метода, которые печатают:
имя,
фамилию,
имя и фамилию.
"""


class User:
    def __init__(self, first_name, last_name):
        print(f'Создан User - {first_name} {last_name}')
        self.user_first_name = first_name
        self.user_last_name = last_name

    def getFirstName(self):
        print(f'Меня зовут {self.user_first_name}')

    def getLastName(self):
        print(f'Моя фамилия {self.user_last_name}')

    def getFullName(self):
        print(f'Мое полное имя {self.user_first_name} {self.user_last_name}')
