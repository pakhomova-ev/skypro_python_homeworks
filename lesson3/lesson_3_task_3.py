"""Импортируйте классы Address и Mailing
-В файле создайте экземпляр класса Mailing
- Заполните поля класса адресами (to_address и from_address),
трек-номером (track) и стоимостью (cost).
Распечатайте в консоль отправление в формате:
Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира>
в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.
Все данные должны получаться из экземпляра
Mailing"""

from address import Address
from mailing import Mailing

to_address = Address('1345678', 'Pskov', 'Drom', 34, 456)
from_address = Address('13678', 'Moscow', 'WRT', 1, 14)

mail1 = Mailing(to_address, from_address, '345 6677 344', 4567)

mail1.getInfoAboutMailing()
