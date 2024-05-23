# Multilevel Inheritance
class A:
    x, y = 10, 20

    def add(self):
        print(self.x + self.y)


class B(A):
    a, b = 200, 100

    def sub(self):
        print(self.a - self.b)


class C(B):
    i, j = 5, 2

    def mul(self):
        print(self.i * self.j)


cobj = C()
cobj.add()
cobj.sub()
cobj.mul()
