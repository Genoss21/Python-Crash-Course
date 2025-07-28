import array as arr 

# creating array
a = arr.array('i', [96,26,45,36,88,82])

# checking the length
l = len(a)

# loop variable
idx = 0

# while loop
while idx < l:
    print (a[idx])
    # incrementing while loop
    idx+=1