"""В классе должно быть 4 поля:
to_address (тип данных Address);
from_address (тип данных Address);
cost (тип данных число);
track(тип данных строка)."""

class Mailing:
     
    def __init__(self,to_address,from_address,track,cost):
            self.to_address = to_address
            self.from_address = from_address
            self.track = track
            self.cost = cost


    def getInfoAboutMailing(self):
          print((f"Отправление {self.track} из {self.from_address.index}, {self.from_address.city},\
 {self.from_address.street}, {self.from_address.building} - {self.from_address.apartment} в\
 {self.to_address.index}, {self.to_address.city}, {self.to_address.street},\
 {self.to_address.building} - {self.to_address.apartment}. Стоимость {self.cost} рублей."))
                    