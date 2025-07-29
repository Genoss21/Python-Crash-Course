# Aggregation = A relationship where one object contains reference to other INDEPENDENT objects
#               "has-a" relationship

# Composition = The composed object directly owns its components, which cannot exist independently
#               "owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size
        
# Now the car owns an engine and owns 4 wheels 
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        # Composition comes in 
        # Call the engine constractor
        self.engine = Engine(horse_power)
        # This list comprehension will give us 4 wheel objects
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
    
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"
      
# If we delete this the engine and the wheels will not exsist  
car1 = Car("Ford", "Mustang", 500, 18)
car2 = Car("Ford", "Raptor", 700, 20)

print(car1.display_car())
print(car2.display_car())