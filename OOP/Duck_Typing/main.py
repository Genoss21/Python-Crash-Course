class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")
        
class Cat(Animal):
    def speak(self):
        print("Meow!")
        
class Car:
    
    alive = False
    
    def speak(self):
        print("HONK!")
        
animals = [Dog(), Cat(), Car()]

# For every animal in animals
for animal in animals:
    # Use the speak method 
    animal.speak()
    print(animal.alive)