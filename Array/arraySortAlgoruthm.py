import array as arr 

a = arr.array('i', [10,2,16,68,9,1,86])
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if(a[i]) > a[j]:
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
print(a)