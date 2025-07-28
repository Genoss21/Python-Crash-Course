import array as arr 

# Creating array
numericArray = arr.array('i', [88,99,77,55,33])

print("Original array:", numericArray)
revArray = numericArray[::-1]
print("Reversed array: ", revArray)