list1 = ['physics', 'Biology', 'chemistry', 'maths']
print ("list before sort:", list1)
list1.sort()
print ("list after sort : ", list1)

list2 = [10,16, 9, 24, 5]
print ("list before sort", list2)
list2.sort()
print ("list after sort : ", list2)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Sorting in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc) 

list3 = ['Physics', 'biology', 'Biomechanics', 'psychology']
print ("list before sort", list3)
list3.sort(key=str.lower)
print ("list after sort : ", list3)

def myfunction(x):
   return x%10
list4 = [17, 23, 46, 51, 90]
print ("list before sort", list4)
list4.sort(key=myfunction)
print ("list after sort : ", list4)