import array as arr 
a = arr.array('i', [1,2,3,4,5,6])
b = arr.array('i', [7,8,9])

# Using append
a.append(10)

# Using insert
a.insert(1,20)

# Using extend
a.extend(b)

print(a)

