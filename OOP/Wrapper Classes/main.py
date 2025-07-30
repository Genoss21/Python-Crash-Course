# Decorator = A function that extends the behavior of another function 
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

# This is the decorator and it is a function
def add_sprinkles(function):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        function(*args, **kwargs)
    return wrapper

def add_fudge(function):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        function(*args, **kwargs)
    return wrapper

# This is the base function
@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} Ice cream")

get_ice_cream("vanilla")