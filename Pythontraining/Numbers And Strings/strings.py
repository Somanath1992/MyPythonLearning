# immutable example
str1 = "welcome"
print(id(str1))
str1 = str1 + "to python"
print(id(str1))

# + and * operators with string - + is used for concatenation and * used for printing string multiple times
str2 = "welcome"
print(str2 + "programming")
print(str2 * 2)

# Slicing operators []
# starting index from 0
# ending index count will start from 1 to ending index
str3 = "welcome"
print(str3[1:3])
print(str3[:6])
print(str3[2:])
print(str3[1:-1])
print(str3[1:-2])

# ord() and chr() functions
# ord() will give ASCII number of character & chr() will give you ASCII char from number
print(ord('A'))
print(chr(65))

# max() min() & len() functions of string
# max will give max char, min will give min char & len will give number of charc in string
print(max("abc"))
print(min("abc"))
print(len("welcome"))

# in & not in operators
# this operators will returns true/ false
s = "welcome"
print("come" in s)
print("lome" in s)

print("come" not in s)
print("lome" not in s)

# String comparison
print("tim" == "tie")  # false
print("free" != "freedom")  # true
print("arrow" > "aron")  # true
print("right" >= "left")  # true
print("teeth" < "tee")  # false
print("yellow" <= "fellow")  # false
print("abc" > "")  # true

# Testing Strings True/False
s = "welcome to python"
print(s.isalnum())  # false
print("Welcome".isalpha())  # true

# Searching for substrings
str4 = "welcome to python"
print(s.endswith("thon"))  # true
print(s.startswith("good"))  # false
print(s.find("come"))  # 3 it will return position
print(s.find("become"))  # -1 not found
print(s.count("o"))  # 3 return count of o

# Converting String
s = "String in PYTHON"
print(s.capitalize())
print(s.title())
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.replace("in", "on"))

# Reverse a String
# method 1
a = "welcome"
rev_a = " "
for i in a:
    rev_a = i + rev_a
print("reversed string is:" + rev_a)
# method 2
b = "welcome"
rev_b = b[::-1]  # [0:7:-1]
print(rev_b)
