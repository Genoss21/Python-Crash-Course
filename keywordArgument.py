def printinfo (name, age ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print("Age: ", age)
    return

# Now you can call printinfo function
# by positional arguments
printinfo ("Fritz", 29)

# by keyword arguments 
printinfo(name="miki", age = 30)

def division(num, den):
   quotient = num/den
   print ("num:{} den:{} quotient:{}".format(num, den, quotient))

division(10,5)
division(5,10)