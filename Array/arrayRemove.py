import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# before removing array
print("Before removing: ", numericArray)

# removing array
# numericArray.remove(311)
numericArray.pop(3)

# after removing array
print ("Affter removing: ", numericArray)