# Find out maximum and minimum number from Array / List
arr = [1, 2, 3, 4, 5]
# Approach 1: using built in methods
print(max(arr))
print(min(arr))
# Approach 2: Using Logic, compare each number with each other
arr1 = [20, 15, 46, 51]
# Find Max Number
maximum = arr[0]
length_arr = len(arr1)
for i in range(1, length_arr):
    if arr1[i] > maximum:
        maximum = arr1[i]
print(maximum)
# Find Min Number
minimum = arr1[0]
for j in range(1, length_arr):
    if arr1[j] < minimum:
        minimum = arr1[j]
print(minimum)
