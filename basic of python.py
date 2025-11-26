
# Basic of Python Programming Language

# Syntax  -  Set of rule to write code 
print("Hello, World!")  # This is a simple print statement
# Indentation - Python uses indentation to define blocks of code
if True:
    print("This is indented correctly.")        
# Comments - Use '#' for single-line comments
# This is a comment
"""
This is a multi-line comment
or docstring.
"""
'''
This is another way to write multi-line comments.
''' 
# Variables - Used to store data
x = 10          # Integer       
y = 3.14        # Float
name = "Alice"  # String
is_active = True  # Boolean
# Data Types - Different types of data
print(type(x))          # <class 'int'> 
print(type(y))          # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_active))  # <class 'bool'>
# Primetive Data Types - int, float, str, bool
a = 5               # Integer   
b = 2.5             # Float
c = "Hello"        # String 
d = False          # Boolean
# Non-Primetive Data Types - list, tuple, set, dict
# List - Ordered, mutable collection    
my_list = [1, 2, 3, "four", 5.0]
print(my_list)  # [1, 2, 3, 'four', 5.0]
# Tuple - Ordered, immutable collection
my_tuple = (1, 2, 3, "four", 5.0)
print(my_tuple)  # (1, 2, 3, 'four', 5.0)
# Set - Unordered, mutable collection of unique elements    
my_set = {1, 2, 3, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}
# Dictionary - Key-value pairs
my_dict = {"name": "Alice", "age": 25, "is_student": False}
print(my_dict)  # {'name': 'Alice', 'age': 25, 'is_student': False}
# Type Conversion - Converting one data type to another
num_str = "100"
#type Interference
variable = 10       # Initially an integer
variable = "Now I'm a string"  # Now a string   
num_int = int(num_str)  # Convert string to integer
print(num_int)  # 100   
num_float = float(num_int)  # Convert integer to float
print(num_float)  # 100.0


# code example of Indentation
if True:
    print("Indentation is important in Python!")    
    if False:
        print("This won't be printed.")
    print("This will be printed.")
    print("End of the code example.")   
    print("This is the end of the code example.")
     # HOw many time print statement is indented that many time it will be executed



