# Program to find of factorial(!) of number
# Factorial of a non-negative integer is the multiplication of all positive integers smaller than or equal to n
# Approach 1: Using Looping Statement
def factorial_num(num):
    factorial = 1
    if num < 0:
        print("Negative numbers does not have factorial")
    elif num == 0:
        print("Factorial number of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)


number = int(input("Enter number to find factorial:"))
factorial_num(number)


# Approach 2: Using recursive(function calls itself) function
def fact_num(num1):
    if num1 == 0 or num1 == 1:
        return 1
    else:
        return num1 * fact_num(num1 - 1)


number_1 = int(input("Enter number to find factorial:"))
print("The factorial of ", number_1, "is", fact_num(number_1))


# Approach 3: Using Ternary Operator (if else in single line)
def fact_number(num2):
    return 1 if num2 == 0 or num2 == 1 else num2 * fact_number(num2 - 1)


number_2 = int(input("Enter number to find factorial:"))
print("The factorial of", number_2, "is", fact_num(number_2))
