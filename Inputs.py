#input() = A Funtction that prompts the user to enter a data
#           returns the entered data as a string

name = input("What is your name?: ")
age = input("How old are you?: ")

#need to be type cast cause age is save as string alternative way is you can do this 
# age = int(input("How old are you?: "))
age = int(age)
age = age + 1 

#insert "f" if you want to insert variable like so
print(f"welcome {name}!")
print("Happy Birthday!")
print(f"You are {age} years old!")


