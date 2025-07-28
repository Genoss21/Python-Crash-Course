# super() = Function used in a child class to call methods from a parent class (Superclass).
#           Allows you to extend the functionality of the inhereted methods

# Parent class
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

# Child class
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    # This is called method overriding
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        # if you want to use the method on the parents class, use the super() method
        super().describe()
        
        
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
        
    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        # if you want to use the method on the parents class, use the super() method
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.radius = width
        self.height = height
        
    # This is called method overriding
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.width * self.height / 2}cm^2")
        # if you want to use the method on the parents class, use the super() method
        super().describe()
        
circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)

# print(square.color)
# print(square.is_filled)
# print(f"{square.width}cm")

square.describe()