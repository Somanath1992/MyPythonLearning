import sys

sys.path.append("C:/Users/Admin/PycharmProjects/MySeleniumLearning/Pythontraining/Packages In Python/emp_package")
# Approach 1
import emp_module

empobj = emp_module.Employee(100, "john", 20000)
empobj.displayemp()

sys.path.append("C:/Users/Admin/PycharmProjects/MySeleniumLearning/Pythontraining/Packages In Python/stu_package")
# Approach 1
import stu_module

stuobj = stu_module.Student(210, "scott", 'B')
stuobj.displaystu()

# Approach 2
from emp_module import *

obj1 = Employee(301, "Dev", 14000)
obj1.displayemp()

from stu_module import *
obj2 = Student(401,"Ben",'C')
obj2.displaystu()
