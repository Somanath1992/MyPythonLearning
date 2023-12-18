# Example1: Print a person is eligible for vote or not
age = 20
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")

# Example 2 : Using True and False instead of passing expression
if True:
    print("True condition")
else:
    print("False Condition")

#Example 3 : Using 1 & 0
if 1:
    print("True condition")
else:
    print("False Condition")

# Example 4 : Find a given number is even or odd
num = 10
if num % 2 == 0:
    print("Given number is Even")
else:
    print("Given number is odd")

''' Example 5 : if else in single line (ternary operator) 
(The ternary conditional operator simply allows testing a condition in a single line replacing 
the multiline if-else making the code compact.) '''
num1 = 15
print("Given number is Even") if num1 % 2 == 0 else print("Given number is odd")

# Example 6: if else -Multiple Statements in Single Line
num2 = 5
{print("hello"),print("python")} if num2 >= 10 else{print("hi"),print("java")}

