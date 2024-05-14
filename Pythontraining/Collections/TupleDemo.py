# Example 1: Creating Tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple)

# creating empty tuple
mytuple1 = ()
print(mytuple1)
# Example 2: Access tuple elements
mytuple2 = ("apple", "banana", "cherry")
print(mytuple2[1])  # index starts from 0
print(mytuple2[-1])

# Example 3: Range of indexes
mytuple3 = ("apple", "banana", "cherry", "berry", "melon", "mango", "kiwi")
print(mytuple3[2:5])
print(mytuple3[-4:-1])

# Example4: change items from tuple
# We can not change because it is immutable
# but there is a workaround convert tuple-> list (modify) -> tuple
mytuple4 = ("apple", "banana", "cherry")
mylist = list(mytuple4)
mylist[0] = "orange"
mytuple4 = tuple(mylist)
print(mytuple4)

# Example 5: Reading tuple elements using loop
mytuple5 = ("apple", "banana", "cherry")
for i in mytuple5:
    print(i)

# Example 6: Check if element exists:
mytuple6 = ("apple", "banana", "cherry")
if "banana" in mytuple6:
    print("Yes, banana is present")
else:
    print("No, banana is not present")

# Example 7 : Length of tuple
mytuple7 = ("apple", "banana", "cherry")
print(len(mytuple7))

# Example 8: Add elements into tuple
# No we can not add because it is immutable
mytuple8 = ("apple", "banana", "cherry")
#mytuple8[0] = "orange"          # TypeError: 'tuple' object does not support item assignment

print(mytuple7)

# Example 9: Copy tuple
mytuple9 = ("apple", "banana", "cherry")
mytuple10 = mytuple9
print(mytuple10)

# Example 10 : Removing element from tuple
# No we can not remove because it is immutable
mytuple11 = ("apple", "banana", "cherry")
#mytuple11.remove("apple") # invalid statement
#del mytuple11
# print(mytuple11) #NameError: name 'mytuple11' is not defined. Did you mean: 'mytuple1'?

# Example 11: joining / combining tuple
mytuple12 = ("apple", "banana", "cherry")
mytuple13 = (10, 20, 30)
mytuple14 = mytuple12 + mytuple13
print(mytuple14)

# Example 12: compare tuples
tuple1 = (10, 20, 30)
tuple2 = (10, 20, 30)
if tuple1 == tuple2:
    print("tuples are equal")
else:
    print("tuples are not equal")
