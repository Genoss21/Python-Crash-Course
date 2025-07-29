# Nested class = A class defined within another class 
#                class Outer
#                   class Inner:

# Benefits: Allows you to logically group classes that are closely related 
#           Encapsulate private details that arent relevant outside of the outer class 
#           keeps the namespace clean; reduces the possibility of naming conflicts

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
            
        def get_details(self):
            return f"{self.name} {self.position}"
    
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
    
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
    
    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company1 = Company("TSGI")
company2 = Company("Denso")

company1.add_employee("Fritz", "CEO")
company1.add_employee("Jerome", "IT head")
company1.add_employee("Tobes", "Presedent")

company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", "assistant")

for employee in company1.list_employees():
    print(employee)
    
for employee in company2.list_employees():
    print(employee)
# print(company.company_name)