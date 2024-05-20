# Example 1:
def func(i, j):
    print(i, j)


func(10, 20)  # positional arguments
func(j=30, i=25)  # keyword arguments


# Example 2: default values to positional arguments
def func1(a, b=10):
    print(a, b)


func1(100, 200)
func1(200)


# Example 3: keyword arguments
def greetings(name, greetmsg):
    print(greetmsg + " " + name)


greetings(name="John", greetmsg="Hello")
greetings(greetmsg="Hello", name="John")


# Example 4:
def func2(a, b, c):
    print(a, b, c)


func2(10, 20, 30)  # positional parameters
func2(a=10, b=20, c=30)  # keyword parameters
func2(b=20, a=10, c=30)  # keyword parameters
func2(10, 20, c=30)  # combination of positional & keyword parameters
func2(10, b=20, c=30)  # combination of positional & keyword parameters


# func2(10, b=20, 30)     # positional argument must appear before any keyword arguments (will give syntax error)
# func2(10, 30, b=30)       # will give run time error -TypeError: func2() got multiple values for argument 'b'


# Example 5: function can return multiple values
def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a


print(largest(100, 200))
print(largest(20, 10))

res = largest(30, 40)
print(res)
print(type(res))    # tuple

