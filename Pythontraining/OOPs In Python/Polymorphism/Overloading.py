# Example 1:
class Human:
    def sayhello(self, name=None):
        if name is not None:
            print("Hello" + name)
        else:
            print("Hello")


h = Human()
h.sayhello("john")
h.sayhello()


# Example 2:
class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a + b + c)


calobj = Calculation()
calobj.add()
calobj.add(10, 20)
calobj.add(100, 200, 300)
