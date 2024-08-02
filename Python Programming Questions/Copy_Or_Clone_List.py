# Write a Program to Copy or Clone List
# Approach 1: Using Slicing technique
myList = [10, 15, 20, 25, 40]
myList_Copy = myList[:]
print(myList_Copy)

# Approach 2: Using extend method
myList1 = [10, 15, 20, 25, 40]
myList_Copy1 = []
myList_Copy1.extend(myList1)
print(myList_Copy1)

# Approach 3: Using list() method
myList2 = [10, 15, 20, 25, 40]
myList_Copy2 = list(myList2)
print(myList_Copy2)

# Approach 4: Using copy() method
myList3 = [10, 15, 20, 25, 40]
myList_Copy3 = myList3.copy()
print(myList_Copy3)

# Approach 5: Using List Comprehensive approach
myList4 = [10, 15, 20, 25, 40]
myList_Copy4 = [i for i in myList4]
print(myList_Copy4)
