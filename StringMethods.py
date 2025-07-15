name = input("Enter your full name: ")
phone_number = input("Enter your phone number #: ")

# to know the lenght of the string
# result = len(name)

# This will find the first occurance of the space or any letter iside the find("")
# and .rfind("") for the last occurance
# result = name.find(" ")

# name = name.capitalize()
# # Make all letters uppercase
# name = name.upper()

# # Make all the letter lowercase
# name = name.lower()

# This will check if the string contains all only digit 
# and the output will be true and false
# result = name.isdigit()

# # This will check if the string contains all only letters 
# # and the output will be true and false
# result = name.isalpha()

# count will count how many characters are there in the string
# result = phone_number.count("-")

# This will repalce the - with space
phone_number = phone_number.replace("-", " ")

print(phone_number)

# Important note if you want to see all the methods for string
# just type "print(help(str))"