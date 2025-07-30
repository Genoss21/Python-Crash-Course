from abc import ABCMeta, abstractstaticmethod

class Person( metaclass= ABCMeta):
    
    @abstractstaticmethod
    def print_data():
        """ Implement in child class """
        
class PersonSingleton(Person):
    
    __instance = None
    
    @staticmethod
    def get_intancte():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantaited more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
    
    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")
        
p = PersonSingleton("Fritz", 25) 
print(p)
p.print_data()
    