# class variable = Shared among all instance of a class
#                  Defined outside the constructor
#                  Allow you to share data among all objects created from that class

class Student:
    # class that is defined outside the constructor
    class_year = 2025
    num_students = 0
    
    # self refers to the object with working with
    # this is a constructor
    def __init__(self, name, age):
        # This is instance variables
        self.name = name
        self.age = age
        # instead of self use the class name called Student
        Student.num_students += 1

student1 = Student("Bob", 30)
student2 = Student("Pat", 35)
student3 = Student("Ward", 55)
student4 = Student("Andy", 25)

# print(student1.name)
# print(student1.age)
# print(Student.class_year)

print(f"My graduating class of {Student.class_year} has {Student.num_students}")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)