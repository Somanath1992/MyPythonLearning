# Approach 1
import animal
import bird
animal.fly()
animal.color()
bird.fly()
bird.color()


# Approach 2
from animal import *
fly()
color()
# if we import both modules at a time and try to call functions , it will call functions from latest implemented module
# so in this case import first module call functions then import another module and call functions
from bird import *
fly()
color()
