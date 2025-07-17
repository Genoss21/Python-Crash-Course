list = ['math', 'science', 2000, 2025];
print ("Value available in index 2 : ")
print(list[2])

# updating the value in index 2 
list[2] = 2022;
print("New value available at index 2 : ")
print(list[2])

tup1 = (12, 34.45);
tup2 = ('abc', 'xyz')

tup3 = tup1 + tup2;
print(tup3);

tup4 = ('physics', 'chemistry', 1997, 2000);
print (tup4);
del tup4;
print ("After deleting tup : ");
print (tup4);