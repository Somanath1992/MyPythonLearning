# How to clear List / Elements in List
# Approach 1: Using Clear Method
myList = [1, 2, 6, 3, 5, 4]
print("My List Before Clearing", myList)
myList.clear()
print("My List After Clearing", myList)

# Approach 2 : Initializing List with No Value
myList1 = [1, 2, 6, 3, 5, 4]
print("My List Before Clearing", myList1)
myList1 = []
print("My List Before Clearing", myList1)

# Approach 3 : Using "*= 0" this method removes all elements from list and makes it empty
myList2 = [1, 2, 6, 3, 5, 4]
print("My List Before Clearing", myList2)
myList2 *= 0
print("My List Before Clearing", myList2)

# Approach 4 : Using del() method
myList3 = [1, 2, 6, 3, 5, 4]
print("My List Before Clearing", myList3)
del myList3[:]  # we can specify starting index and ending index,starting index start from 0 and ending index from 1
print("My List After Clearing", myList3)
