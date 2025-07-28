# Inheretance = Allows a class to inherit attributes and methos from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
        
# The class Dog will inherit all the attributes and method from the parent called Animal
class Dog(Animal):
    def speak(self):
        print ("Woof!")

# The class Dog will inherit all the attributes and method from the parent called Animal
class Cat(Animal):
    def speak(self):
        print ("Meow!")
# The class Dog will inherit all the attributes and method from the parent called Animal
class Mouse(Animal):
    def speak(self):
        print ("Squeek!")

dog = Dog("Coffee")
cat = Cat("Maeven")
mouse = Mouse("Mite")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()