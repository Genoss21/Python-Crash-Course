# Examples for all list methods in Python

# 1. append()
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # ['apple', 'banana', 'cherry']

# 2. extend()
fruits.extend(['date', 'elderberry'])
print(fruits)  # ['apple', 'banana', 'cherry', 'date', 'elderberry']

# 3. insert()
fruits.insert(1, 'blueberry')
print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

# 4. remove()
fruits.remove('banana')
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

# 5. pop()
popped = fruits.pop()
print(popped)  # 'elderberry'
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']

# 6. clear()
fruits.clear()
print(fruits)  # []

# 7. index()
numbers = [10, 20, 30, 20]
idx = numbers.index(20)
print(idx)  # 1

# 8. count()
cnt = numbers.count(20)
print(cnt)  # 2

# 9. sort()
numbers.sort()
print(numbers)  # [10, 20, 20, 30]

# 10. reverse()
numbers.reverse()
print(numbers)  # [30, 20, 20, 10]

# 11. copy()
numbers_copy = numbers.copy()
print(numbers_copy)  # [30, 20, 20, 10]