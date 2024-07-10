# Swap any element in list based on position
# Approach 1:
my_list = [4, 1, 8, 3]
print(my_list)
pos1, pos2 = 1, 3
my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]
print(my_list)

# Approach 2: Using built in function pop()
my_list1 = [81, 36, 28, 45]
loc1, loc2 = 1, 3
first_ele = my_list1.pop(loc1)  # 36
second_ele = my_list1.pop(loc2 - 1)  # 81,28,45
my_list1.insert(loc1, second_ele)
my_list1.insert(loc2, first_ele)
print(my_list1)

# Approach 3: Using tuple variable
my_list2 = [21, 48, 69, 93]
# interchange / swap position of 48 & 93
post1, post2 = 1, 3
get = (my_list2[post1], my_list2[post2])
my_list2[post2], my_list2[post1] = get
print(my_list2)
