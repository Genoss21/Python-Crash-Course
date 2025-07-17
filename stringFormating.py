name ="Tutorialspoint"
print("Welcome to %s!" % name)

str = "Welcome to {}"
print(str.format("Tutorialspoint"))

item1_price = 2500
item2_price = 300
total = f'Total: {item1_price + item2_price}'
print(total)

from string import Template

# Defining template string
str = "Hello and Welcome to $name !"

# Create Tempalte object
templateObj = Template(str)

# now provide the values
new_str = templateObj.substitute(name="Tutorialspoint")
print(new_str)