"""В файле объявите переменную  catalog
Переменная хранит в себе список ([]).
Наполните список пятью разными экземплярами класса Smartphone
Напишите цикл, который печатает весь каталог (список) в формате 
<марка> - <модель>. <номер телефона>
"""
from smartphone import Smartphone

smart_1 = Smartphone('Samsung','As2','+79217883456')
smart_2 = Smartphone('Samsung','Az3','+79217859780')
smart_3 = Smartphone('Samsung','OT','+79113483456')
smart_4 = Smartphone('Apple','SE','+79117893456')
smart_5 = Smartphone('Apple','Max 15','+79217883908')


catalog = [smart_1, smart_2, smart_3, smart_4, smart_5]


len_catalog = len(catalog) # подсчет длины списка

# цикл
if(len_catalog > 0): 
    for i in range(0, len_catalog):
     print(catalog[i].getInfoAboutSmartphone())
else:
   print("Error. The list of smartphones is empty")

