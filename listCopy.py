import copy

# Orginal list
original_list = [[1, 2, 3], [4, 5, 6], [7,8,9]]

# Creating a shallow copy
shallow_copy_list = copy.copy(original_list)

# Modifying an element in the shallow copied list
shallow_copy_list[0][0] = 100

# Print both lists
print("Original List:", original_list)
print("Shallow Copied list:", shallow_copy_list)

# Example of deep copy 

#Original list
original_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Create a deep copy 
deep_copied_list = copy.deepcopy(original_list1)

# Modifying an element in the deep copied list
deep_copied_list[0][0] = 100

# Printing both lists
print("Original List:", original_list1)
print("Deep Copied List:", deep_copied_list)

# Copying List Using Slice Notation
# [start:end:step]

# Original list
original_list2 = [1, 2, 3, 4, 5]
#Copying the list using slice notation
copied_list = original_list2[1:4]

# Modifying the copied list
copied_list[0] = 100

print("Original List:", original_list2)
print("Copied List:", copied_list)

original_list3 = [1, 2, 3, 4, 5]
# Copying the list using the copy() function
copied_list = copy.copy(original_list3)
print("Copied List:", copied_list)