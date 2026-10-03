class Smartphone:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display_info(self):
        print(f"Smartphone Brand: {self.brand},Price: {self.price}")

class Gaming_Phone(Smartphone):
    def __init__(self,brand,price,cooling_system):
        super().__init__(brand,price)
        self.cooling_system=cooling_system
    def display_gaming_phone(self):
        print(f"Cooling System: {self.cooling_system}")  

my_gaming_phone=Gaming_Phone("RedMagic",200000,"AquaCore")         
my_gaming_phone.display_info()
my_gaming_phone.display_gaming_phone()

