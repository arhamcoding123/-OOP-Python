class Vehicle:
    def speed_limit(self):
        print("A normal vehicle has a max speed of 100 km/h.")



class SportsCar(Vehicle):
    def speed_limit(self):
        print("A sports car has a max speed of 350 km/h.")        

my_sports_car=SportsCar()
my_sports_car.speed_limit()