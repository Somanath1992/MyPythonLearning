# Single Inheritance
# Example 1:
class A:
    def m1(self):
        print("this is m1 method from class A")


class B(A):
    def m2(self):
        print("this is m2 method from class B")


bobj = B()
bobj.m1()  # class A method
bobj.m2()  # class B method


# Example 2:
class C:
    x, y = 10, 20

    def add(self):
        print(self.x + self.y)


class D(C):
    a, b = 200, 100

    def sub(self):
        print(self.a - self.b)


dobj = D()
dobj.add()
dobj.sub()
