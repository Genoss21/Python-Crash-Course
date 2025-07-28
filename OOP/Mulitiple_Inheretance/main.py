# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

#Multilevel inheritance = inherit from a parent which inherits from another parent
#                         C(B) <- B(A) <- A

# Grand Parent classes (A)
class Animal:
    
    def __init__(self, name):
        self.name = name     
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# Parent classes (B)
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

# Children classes (C)
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# With multiple parent
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
rabbit.sleep()
