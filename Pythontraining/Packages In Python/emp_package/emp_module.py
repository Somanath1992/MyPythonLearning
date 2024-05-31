class Employee:
    def __init__(self, empid, empname, sal):
        self.empid = empid
        self.empname = empname
        self.sal = sal

    def displayemp(self):
        print(self.empid, self.empname, self.sal)
