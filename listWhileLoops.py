my_list = [1, 2, 3, 4, 5]
index = 0 

while index < len(my_list):
    print(my_list[index])
    index += 1
    
lst = [25, 67, 23, 12, 100]
indices = range(len(lst))
for i in indices:
    print("lst[{}]: ".format(i), lst[i])
    
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print (squared_numbers)

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
   print(index, fruit)