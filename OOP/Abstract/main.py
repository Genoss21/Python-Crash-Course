# Abstract class: A class that connot be instantiated on its own; Meant to be subclassed.
#                 They can contain abstract methods, which are declared but have no implementation
#                 Abstract classes benefits:
#                 1. Prevents instantiation of the classes itself
#                 2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod

# Parent class
class Vehicle(ABC):
    
    # Note that the methods here should be also seen in the child class
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    
# Child class
class Car(Vehicle):
    
    def go(self):
        print("You are driving the car")
    
    def stop(self):
        print("You are stopping the car")
        
class Motorcycle(Vehicle):
    
    def go(self):
        print("You are riding the motorcycle")
    
    def stop(self):
        print("You are stopping the motorcycle")
        
class Boat(Vehicle):
    
    def go(self):
        print("You are sailing with boat")
    
    def stop(self):
        print("You are anchor the boat")    


car = Car()
motorcycle = Motorcycle()

car.go()
car.stop()