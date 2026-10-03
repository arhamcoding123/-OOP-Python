class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display_info(self):
        print(f"Car Brand: {self.brand},Color: {self.color}")

class ElectricCar(Car):
    def __init__(self,brand,color,battery_capacity):
        super().__init__(brand,color)
        self.battery_capacity=battery_capacity
    def display_elc_car(self):
        print(f"Battery Capacity: {self.battery_capacity}")  

my_ev=ElectricCar("Tesla","Red",85)         
my_ev.display_info()
my_ev.display_elc_car()

