class Greeter:
    def say_hello(self,name1,name2=None):
        if name2!=None:
            print("Hello")
        else:
            print(f"Hello {name1}")


my_name= Greeter()
my_name.say_hello("Arham")
my_name.say_hello("Arham","Ayyash")
