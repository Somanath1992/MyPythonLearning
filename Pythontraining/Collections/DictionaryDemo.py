# Example 1: Create dictionary
mydic = {"brand": "Hyundai",
         "model": "i10",
         "year": 2020}
print(mydic)

# Example 2: Accessing elements from dictionary
mydic1 = {"brand": "Hyundai",
          "model": "i10",
          "year": 2020}
print(mydic1["brand"])

# using get function
print(mydic1.get("model"))

# Example 3: change values in dictionary
mydic2 = {"brand": "Hyundai",
          "model": "i10",
          "year": 2020}
mydic2["year"] = 2021
print(mydic2)

# Example 4: Reading elements from dictionary using loop
mydic3 = {"brand": "Hyundai",
          "model": "i10",
          "year": 2020}
for i in mydic3:
    print(i)  # will print only keys

for i in mydic3:
    print(mydic3[i])  # will print only values

for i in mydic3.values():
    print(i)  # will print only values

for x, y in mydic3.items():
    print(x, y)  # will print all keys and values from dictionaries

# Example 5: check keys is exist in dictionary or not
mydic4 = {"brand": "Hyundai",
          "model": "i10",
          "year": 2020}
if "model" in mydic4:
    print("exist")
else:
    print("not exist")

print("year" in mydic4)

# Example 6: Find length of dictionary
mydic5 = {"brand": "Hyundai",
          "model": "i10",
          "year": 2020}
print(len(mydic5))

# Example 6: Adding elements in dictionary
mydic6 = {"brand": "Hyundai",
          "model": "i10",
          "year": 2020}
mydic6["color"] = "red"
print(mydic6)

# Example 7: remove element from dictionary
mydic7 = {"brand": "Hyundai",
          "model": "i10",
          "year": 2020}
mydic7.pop("model")
print(mydic7)

del mydic7["brand"]
print(mydic7)
#del mydic7
# print(mydic7)  #NameError: name 'mydic7' is not defined. Did you mean: 'mydic'?

mydic7.clear()
print(mydic7)

# Example 8: Copy dictionary
# without using copy function
mydic8 = {"brand": "Hyundai",
          "model": "i10",
          "year": 2020}
mydic9 = mydic8
print(mydic9)

# Using copy function
mydic10 = {"brand": "Hyundai",
           "model": "i10",
           "year": 2020}
mydic11 = mydic10.copy()
print(mydic11)
