# Approach 1: Without using temporary Variable
def swap_two_numbers(num1, num2):
    print("numbers before swapping:", num1, num2)
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print("numbers after swapping:", num1, num2)


swap_two_numbers(3, 4)

# Approach 2: Without using temporary Variable
num3 = input("enter value of num3:")
num4 = input("enter value of num4:")
print("Value of num3 & num4 before swapping:", num3, num4)
num3, num4 = num4, num3
print("Value of num3 & num4 after swapping:", num3, num4)

# Approach 3:Using temporary Variable
num5 = input("enter value of num5:")
num6 = input("enter value of num6:")
print("Value of num5 & num6 before swapping:", num5, num6)
temp = num5
num5 = num6
num6 = temp
print("Value of num5 & num6 after swapping:", num5, num6)
