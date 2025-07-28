# Find the largest number in an array

import array as arr 
a = arr.array('i', [10,5,6,7,50,69])
print(a)
largest = a[0]
for i in range(1, len(a)):
    if a[i]>largest:
        largest=a[i]
print ("Largest number: ", largest)