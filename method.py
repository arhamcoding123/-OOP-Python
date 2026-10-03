class Animal:
    def make_sound(self):
        print("Animals makes different sounds")



class Dog(Animal):
    def make_sound(self):
        print("Dogs says: WOOF WOOF!!!")        



class Cat(Animal):
    def make_sound(self):
        print("Cats says: Meow Meow!!!")   


my_dog=Dog()
my_dog.make_sound()

my_cat=Cat()
my_cat.make_sound()