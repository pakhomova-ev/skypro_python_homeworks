"""В отдельном файле создайте класс Address
Класс должен содержать в себе поля:
«индекс»,
«город»,
«улица»,
«дом»,
«квартира»."""

class Address:
    
    def __init__(self, address_index, address_city, address_street, address_building, address_apartment):
        self.index = address_index
        self.city = address_city
        self.street = address_street
        self.building = address_building
        self.apartment = address_apartment
