string = "hello world"
uppercase_letters = [char.upper() for char in string if
                     char.isalpha()]
print(uppercase_letters)

# lambda example
original_list = [1, 2, 3, 4, 5]
doubled_list = [(lambda x: x * 2)(x) for x in original_list]
print(doubled_list)

# nested loop example
list1=[1,2,3]
list2=[4,5,6]
Comblst=[(x,y) for x in list1 for y in list2]
print(Comblst)

# Conditionals in Python List Comprehension
list3=[x for x in range(1,21) if x%2==0]
print(list3)

# Example Using For Loop
chars=[]
for ch in 'TutorialsPoint':
   if ch not in 'aeiou':
      chars.append(ch)
print (chars)

# Example Using List Comprehension
chars1 = [ char1 for char1 in 'TutorialsPoint' if char1 not in 'aeiou']
print (chars1)