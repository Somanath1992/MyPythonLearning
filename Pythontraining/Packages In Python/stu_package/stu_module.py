class Student:
    def __init__(self, stuid, stuname, grade):
        self.stuid = stuid
        self.stuname = stuname
        self.grade = grade

    def displaystu(self):
        print(self.stuid, self.stuname, self.grade)
