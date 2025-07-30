# Static methods = A method taht belong to a clas rather than any object that class (instance)
#                  Usually used for general utlity functions

# Instance methods = Best for operation on intances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    
    # Objects from this class
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    # Get_info is a instance method 
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Fritz", "Manager")
employee2 = Employee("Jerome", "CEO")
employee3 = Employee("Tobes", "President")

        
print(Employee.is_valid_position("Cook"))

print (employee1.get_info())
print (employee2.get_info())
print (employee3.get_info())