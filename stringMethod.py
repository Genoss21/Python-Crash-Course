# Case Conversion Methods
s = "Hello World"
print(s.upper())        # HELLO WORLD
print(s.lower())        # hello world
print(s.title())        # Hello World
print(s.capitalize())   # Hello world
print(s.swapcase())     # hELLO wORLD

# Alignment Methods
print(s.center(20, '*'))    # ****Hello World*****
print(s.ljust(20, '-'))     # Hello World---------
print(s.rjust(20, '-'))     # ---------Hello World
print(s.zfill(20))          # 0000000000Hello World

# Split and Join Methods
csv = "apple,banana,cherry"
print(csv.split(','))           # ['apple', 'banana', 'cherry']
words = ['Python', 'is', 'fun']
print(' '.join(words))          # Python is fun
print(s.split())                # ['Hello', 'World']
print("line1\nline2".splitlines())  # ['line1', 'line2']
print("   hello   ".strip())    # hello
print("   hello   ".lstrip())   # hello   
print("   hello   ".rstrip())   #    hello

# Boolean String Methods
print(s.isalpha())      # False (space included)
print("Hello".isalpha())# True
print("123".isdigit())  # True
print("hello".islower())# True
print("HELLO".isupper())# True
print("Hello".istitle())# True
print("   ".isspace())  # True
print("hello123".isalnum()) # True

# Find and Replace Methods
print(s.find("World"))      # 6
print(s.rfind("l"))         # 9
print(s.index("World"))     # 6
print(s.replace("World", "Universe")) # Hello Universe
print(s.count("l"))         # 3