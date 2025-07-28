# object = A "bundle" of related attribute (variables) and methods (funtions)
#           Ex. Phone, Cup, Book
#           You need a "class" to create many objects

# class = (Bluepeint) used to design the structure and layout of na object

# this is a import class from car.py
from car import Car
        
car1 = Car("Mustang", 2024, "Black", False)
car2 = Car("Volvo", 2025, "Red", True)
car3 = Car("Lambo", 2026, "White", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.discribe()