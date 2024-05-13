# Example 1: How to create list
mylist1 = [10, 20, 30, 40, 50]
mylist2 = ["apple", "banana", "cherry"]
mylist3 = ["apple", 10, "banana", 20]
mylist = list()

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist)

# Example 2: Accessing elements from the list
a = ["apple", "banana", "cherry"]  # index starts from 0

print(a[0])
print(a[2])
print(a[-1])  # we can pass negative values as well, -1 will be considered as last value from list
print(a[-2])

# Example 3: Range of indexes
mylist4 = ["apple", "banana", "cherry", "orange", "kiwi", "mango", "melon"]
print(mylist4[2:5])
print(mylist4[-4:-1])

# Example 4: Changing element value
mylist5 = ["apple", "banana", "cherry"]
print(mylist5)
mylist5[0] = "berry"
print(mylist5)

# Example 5: read elements using loop
mylist6 = ["apple", "banana", "cherry"]
for i in mylist6:
    print(i)

# Example 6: Check element exist in list or not
mylist7 = ["apple", "banana", "cherry"]
if "apple" in mylist7:
    print("yes, apple  is present")
else:
    print("No, apple is not present")

# Example 7: Length of List
mylist8 = ["apple", "banana", "cherry"]
print(len(mylist8))

# Example 8: Add elements in list append() & insert()
mylist9 = ["apple", "banana", "cherry"]
# append()
mylist9.append("orange")
print(mylist9)
# insert()
mylist9.insert(1, "berry")
print(mylist9)

# Example 9: Remove element from list
# pop() function
mylist10 = ["apple", "banana", "cherry"]
mylist10.pop(1)
print(mylist10)

# del keyword
mylist11 = ["apple", "banana", "cherry"]
del mylist11[2]
print(mylist11)

# clear() function
mylist12 = ["apple", "banana", "cherry"]
mylist12.clear()
print(mylist12)

# Example 10: Copy list
# list()
mylist13 = ["apple", "banana", "cherry"]
mylist14 = list(mylist13)
print(mylist13)
print(mylist14)

# Copy()
mylist15 = ["apple", "banana", "cherry"]
mylist16 = mylist15.copy()
print(mylist15)
print(mylist16)

# Example 11: Combine / Join lists
# using + operator
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# using loop statement
list4 = ['a', 'b', 'c']
list5 = [1, 2, 3]
for i in list5:
    list4.append(i)
print(list4)

# using extend() function
list6 = ['a', 'b', 'c']
list7 = [1, 2, 3]
list6.extend(list7)
print(list6)
