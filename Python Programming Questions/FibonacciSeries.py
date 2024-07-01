# Fibonacci Series: Is a sequence of numbers where each number is the sum of the two preceding ones
# 0 1 1 2 3 5 8 13 21 34 ....
num1 = 0
num2 = 1
print(num1, num2, end=' ')
# end=' ' is just used for formatting purpose to print output in one line
for i in range(2, 10):
    add = num1 + num2
    print(add, end=' ')
    num1 = num2
    num2 = add
