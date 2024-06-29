# Program to find of factorial(!) of number
# Factorial of a non-negative integer is the multiplication of all positive integers smaller than or equal to n
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

