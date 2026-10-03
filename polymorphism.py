class Dog:
    def make_sound(self):
        return "Woof Woof!"

class Cat:
    def make_sound(self):
        return "Meow Meow!"

def animal_party(animal_object):
    print(animal_object.make_sound())

my_dog=Dog()
my_cat=Cat()

print("Dog Says:")
animal_party(my_dog)

print("Cat Says:")
animal_party(my_cat)