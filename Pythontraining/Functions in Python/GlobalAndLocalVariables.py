# Example1:
global_var = 20  # global variable


def func():
    local_var = 10  # local variable
    print(local_var)
    print(global_var)


func()
# print(local_var) # invalid because local_var is local variable of func()
print(global_var)  # valid because global_var is global variable

# Example 2:
xy = 100  # global variable


def cool():
    xy = 200  # local variable
    print(xy)


cool()

# Example 3:
xy1 = 100  # global variable


def cool1():
    global xy1
    xy1 = 200  # global variable
    print(xy1)


cool1()  # 200
print(xy1)

# Example 4:
x = 100  # global variable


def cool2():
    global x
    x = 500
    print(x)


# cool2()  # 500
print(x)  # 100


# Example 5:
# We can declare global variable inside the function as well using global keyword
def cool3():
    global x1
    x1 = 300
    print(x1)


cool3()
print(x1)

