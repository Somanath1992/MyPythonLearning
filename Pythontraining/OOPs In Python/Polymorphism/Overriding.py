# Example 1: Calling parent class method in child class using super()
class A:
    def m1(self):
        print("This is m1 method from class A")


class B(A):
    def m1(self):  # overriding
        print("This is m1 method from class B")
        super().m1()  # Accessing super class /parent class method in class B


bobj = B()
bobj.m1()


# Example 2: Accessing parent class variables in child class
class C:
    a, b = 10, 20


class D(C):
    i, j = 100, 200

    def m2(self, x, y):
        print(x + y)
        print(self.i + self.j)
        print(self.a + self.b)


dobj = D()
dobj.m2(1000, 2000)


# Example 3: Overriding variables
class Parent:
    name = "scott"


class Child(Parent):
    name = "John"  # overriding the variable value


cld = Child()
print(cld.name)


# Example 4: Overriding methods
class Bank:
    def rate_of_interest(self):
        return 0


class ABank(Bank):
    def rate_of_interest(self):
        return 10


class BBank(Bank):
    def rate_of_interest(self):
        return 12


abank = ABank()
print(abank.rate_of_interest())

bbank = BBank()
print(bbank.rate_of_interest())

