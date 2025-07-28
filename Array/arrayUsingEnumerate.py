import array as arr 

# creating array
numericArray = arr.array('i', [111,211,311,411,511])

# use of enumarate funtion
for loc, val in enumerate(numericArray):
    print(f"Index: {loc}, value: {val}")