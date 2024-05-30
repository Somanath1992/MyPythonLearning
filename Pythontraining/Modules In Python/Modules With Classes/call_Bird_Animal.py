# Approach 1:
import animal1
import bird1
obj1 = animal1.Animal()
obj1.display()
obj2 = bird1.Bird()
obj2.display()

# Approach 2
from animal1 import Animal
from bird1 import Bird
obj3 = Animal()
obj3.display()
obj4 = Bird()
obj4.display()

