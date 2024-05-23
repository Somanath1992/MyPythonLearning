# Example 1:
class MyClass:
    def myfun(self):
        pass

    def display(self):
        print("hello")


# We can access methods in class by directly using class name.method name
# Here MyClass() is a object of MyClass
MyClass().myfun()
MyClass().display()

# We can also create variable of object as below & access methods in class:
mc1 = MyClass()
mc1.myfun()
mc1.display()


# Example 2:
class MyClass1:
    def m1(self):
        print("this is instance method")

    @staticmethod
    def m2(num):  # self in instance and static method are different as in static it will consider as parameter
        print(num)


mc2 = MyClass1()
mc2.m1()
mc2.m2(100)  # this is not recommended as this method is static, and we can directly access using class name

MyClass1.m2(10)  # this is recommended for static method


# Example 3:

class MyClass2:
    a, b = 10, 20  # class variables

    def add(self):
        print(self.a + self.b)

    def mul(self):
        print(self.a * self.b)


mc2 = MyClass2()
mc2.add()
mc2.mul()

# Example 4:
i, j = 15, 25  # global variables


class MyClass3:
    a, b = 10, 20  # class variables

    def add(self, x, y):
        print(x + y)  # local variables
        print(self.a + self.b)
        print(i + j)


mc3 = MyClass3()
mc3.add(2, 3)

# Example 5:
c, d = 15, 25  # global variables


class MyClass4:
    c, d = 10, 20  # class variables

    def add1(self, c, d):
        print(c + d)  # local variables
        print(self.c + self.d)  # class variables
        print(globals()['c'] + globals()['d'])  # global variables


mc4 = MyClass4()
mc4.add1(1, 2)


# Example 6: One class can have multiple objects
class MyClass5:
    def display(self, name):
        print("this is display method")
        print(name)


obj1 = MyClass5()
obj1.display("john")

obj2 = MyClass5()
obj2.display("scott")


# Example 7:
class MyClass6:
    def __init__(self):
        print("this is constructor")

    def m3(self):
        print("hello")

    def m4(self, p, q):
        return p + q


mc6 = MyClass6()  # invoke constructor automatically
mc6.m3()
print(mc6.m4(10, 20))


# Example 8: Parametrized constructor
class MyClass7:
    name = "Tim"

    def __init__(self, name):
        print(name)
        print(self.name)


mc7 = MyClass7("David")


# Example 9: Scenario: Create Employee class, define constructor which will accept parameters, create method and
# print values of contractor in method
class Employee:
    def __init__(self, EmpId, EmpName, EmpSalary):
        self.EmpId = EmpId
        self.EmpName = EmpName
        self.EmpSalary = EmpSalary

    def employee_data(self):
        print(self.EmpId, self.EmpName, self.EmpSalary)


emp = Employee(100, "Ray", 20000)
emp.employee_data()


# Example 10:
class Employee1:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def __str__(self):  # String constructor
        return self.ename


emp1 = Employee1(102, "Riya", 45000)
print(emp1)
