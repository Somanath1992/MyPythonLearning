import sys

sys.path.append("C:/Users/Admin/PycharmProjects/MySeleniumLearning/Pythontraining/Packages In Python/Package2")
sys.path.append("C:/Users/Admin/PycharmProjects/MySeleniumLearning/Pythontraining/Packages In Python/Package2/Package3")
# Approach 1
import module3
import module4

module3.display()
module4.show()

# Approach2
from module3 import *
from module4 import *
display()
show()
