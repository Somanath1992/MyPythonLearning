# Example 1: Create set
myset = {"apple", "banana", "cherry"}
print(myset)

# Example 2: Accessing elements from set
myset1 = {"apple", "banana", "cherry"}
for i in myset1:
    print(i)

# Example 3: Checking value exist in set or not
myset2 = {"apple", "banana", "cherry"}
print("banana" in myset2)
print("banana1" in myset2)

# Example 4: Add new elements in set
# add()-add single element & update() function-add multiple elements
myset3 = {"apple", "banana", "cherry"}
myset3.add("orange")
print(myset3)

# using update() function
myset4 = {"apple", "banana", "cherry"}
myset4.update(["mango", "berry"])
print(myset4)

# Example 5: find length of set
myset5 = {"apple", "banana", "cherry"}
print(len(myset5))

# Example 6: remove elements from set- remove(). discard()
myset6 = {"apple", "banana", "cherry"}
myset6.remove("apple")  # index will not work in set
print(myset6)
# myset6.remove("berry")  # KeyError: 'berry' as this value is not available in set

# discard()
myset7 = {"apple", "banana", "cherry"}
myset7.discard("banana")
print(myset7)
myset7.discard("berry")  # will not give any error , this difference between remove() & discard()
print(myset7)

# Example 7: clear all elements from set
myset8 = {"apple", "banana", "cherry"}
myset8.clear()
print(myset8)  # print empty set , variable is still available

del myset8
# print(myset8) #NameError: name 'myset8' is not defined. Did you mean: 'myset'? it will completely delete data with varible

# Example 8: join two sets - union ()
myset9 = {"apple", "banana", "cherry"}
myset10 = {1, 2, 3}
myset11 = myset9.union(myset10)
print(myset11)

# using update function
myset12 = {"apple", "banana", "cherry"}
myset13 = {1, 2, 3}
myset12.update(myset13)
print(myset12)
