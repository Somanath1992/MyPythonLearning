# Find out the given element is present in list or not

# Approach 1:
myList = [1, 2, 6, 3, 5, 4]
ele = 4
# ele = 100
flag = 0
for i in myList:
    if i == ele:
        print("Element Found")
        flag = 1
        break

if flag == 0:
    print("Element Not Found")

# Approach 2: Using in operator
myList1 = [2, 7, 8, 1, 0, 3]
ele_search = 0
# ele_search = 10
if ele_search in myList1:
    print("Element Found")
else:
    print("Element Not Found")
