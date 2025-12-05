# IMporting Modules in python : Modules and Package
''' In Python,modules and packages help organize and reuse code .
Here's comprehensive guide on how to import them'''

import math 
math.sqrt(16)# return 4
from math import sqrt ,pi
print(sqrt(16))
print(sqrt(25))
print(pi)


from package import addition
a  = addition(1,3)
print(a)