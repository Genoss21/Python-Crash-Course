import array as arr 

# creating array
orgnlArray = arr.array('i', [10,5,15,6,75,80,1])
print("Original array: ", orgnlArray)

# converting into list
sortedList = orgnlArray.tolist()

# sorting the list
sortedList.sort()

# creating array from sorted list
sortedArray = arr.array('i', sortedList)
print("Array after sorting: ", sortedArray)