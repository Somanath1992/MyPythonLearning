# Example 1
print("This is starting point of the program")
print("Program in progress")
try:
    print(10 / 0)
except ZeroDivisionError:  # we can specify exception, it's not mandatory
    print("Exception occurred and handled")
print("Program completed")

# Example 2:    multiple except,else and finally block
try:
    num1, num2 = 10, 0
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Thrown ZeroDivisionError exception")
except SyntaxError:
    print("Thrown SyntaxError exception")
except:
    print("Exception handled")
else:
    print("No exception occurred")
finally:
    print("always execute")


# Example 3: creating/throwing user defined exception
def enter_age(num):
    if num < 0:
        raise ValueError("only integers are allowed")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


# enter_age(-1)
num = -1
try:
    enter_age(num)
except ValueError:
    print("value error exception occurred and handled")
print("program complete")
