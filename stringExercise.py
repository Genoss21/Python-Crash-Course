mystr = "The quick brown fox jump over the brown fence"
vowels ="aeiou"
count = 0

for x in mystr:
    if x.lower() in vowels: count+=1
print("Number of Vowels:", count)

mystr1 = '10101'

def strtoint(mystr1):
   for x in mystr1:
      if x not in '01': return "Error. String with non-binary characters"
   num = int(mystr1, 2)
   return num
print ("binary:{} integer: {}".format(mystr1,strtoint(mystr1)))

digits = [str(x) for x in range(10)]
mystr3 = 'He12llo, Py00th55on!'
chars = []
for x in mystr3:
   if x not in digits:
      chars.append(x)
newstr = ''.join(chars)
print (newstr)