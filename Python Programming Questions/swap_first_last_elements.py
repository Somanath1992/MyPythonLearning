# Swap First and Last Element from List
# Approach 1: Using Temporary Variable
my_list = [12, 4, 65, 8, 34]
size = len(my_list)
temp = my_list[0]
my_list[0] = my_list[size - 1]
my_list[size - 1] = temp
print("List After Swapping:", my_list)

# Approach 2:
my_list1 = [4, 6, 9, 1, 7]
my_list1[0], my_list1[-1] = my_list1[-1], my_list1[0]
print("List After Swapping:", my_list1)

# Approach 3: Using Tuple
my_list2 = [1, 2, 3, 4]
get = (my_list2[-1], my_list2[0])  # packing
my_list2[0], my_list2[-1] = get  # Unpacking
print("List After Swapping:", my_list2)

# Approach 4: Using * operand
my_list3 = [1, 2, 3, 4, 8]
start, *middle, end = my_list3
my_list3 = [end, *middle, start]
print("List After Swapping:", my_list3)

# Approach 5: Using Pop()
my_list4 = [7, 6, 8, 4]
first = my_list4.pop(0)
last = my_list4.pop(-1)
my_list4.insert(0, last)
my_list4.append(first)
print("List After Swapping:", my_list4)
