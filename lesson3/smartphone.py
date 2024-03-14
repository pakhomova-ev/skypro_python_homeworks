"""Объявите в классе конструктор.
Конструктор должен принимать на вход следующие параметры:
марка телефона,
модель телефона,
абонентский номер (+79…)."""


class Smartphone:

    def __init__(self, smartphone_brand, smartphone_model,
                 smartphone_user_number):
        self.smartphone_brand = smartphone_brand
        self.smartphone_model = smartphone_model
        self.smartphone_user_number = smartphone_user_number

    def getInfoAboutSmartphone(self):
        return (f"{self.smartphone_brand} - {self.smartphone_model}. {self.smartphone_user_number}")