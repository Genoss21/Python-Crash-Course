a = [10, 5, 15, 4, 6, 20, 9]
print(a)
 
max = a[0]
 
for i in range(1, len(a)):
    if a[i] > max:
        max = a[i]
 
print("Largest:", max)