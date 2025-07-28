import array as arr 
a = arr.array('i',[10,5,46,8,78,91])
b = arr.array('i')

for i in range(len(a)-1,-1,-1):
    b.append(a[i])
    
print(a)
print(b)