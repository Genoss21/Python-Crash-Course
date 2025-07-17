# Two lists to be joined
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']

# Joining the lists
joined_list = L1 + L2

# Printing the joined list
print("Joined List:", joined_list)

# Join Lists Using List Comprehension

joined_list1 = [item for sublist in [L1, L2] for item in sublist] 
# Printing the joined list
print("Joined List:", joined_list1)

# Join Lists Using append() Function
list1 = ['Fruit', 'Number', 'Animal']

# List from which elements will be appended
list2 = ['Apple', 5, 'Dog']

# Joining the list using append() function
for element in list2:
    list1.append(element)
# Printing the joined list
print("Joined List", list1)

# Join Lists Using extend() Function
# List to be extended
list3 = [10, 15, 20]
# List to be added
list4 = [25, 30, 35]
# Joining the lists using the extend() function
list3.extend(list4)
# Printing the extended list
print("Extended List:", list1)
