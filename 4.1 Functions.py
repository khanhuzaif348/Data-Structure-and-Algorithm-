# Fucntion   

# Introduction to Functions
#defining a function
#calling a function
#function with parameters
#default parameters
# Varible-length arguments
# Return Statement


# Introduction to Fucntions : A function is a block of reusable code that performs a specific task. Functions help in organizing code, improving readability, and reducing redundancy.  

# Defining a Function
def fucntion(parameters):
    """ Docstring: Describe what the function does """
    # Function body
    return result

# why use functions?
# 1. Code Reusability: Functions allow you to reuse code without rewriting it.
# 2. Modularity: Functions help break down complex problems into smaller, manageable parts.
# 3. Readability: Functions with descriptive names make code easier to understand.
# 4. Maintainability: Functions make it easier to update and maintain code.
# 5. Testing: Functions can be tested independently, making debugging easier.
#   return result
# --- IGNORE ---
# example function to check odd or even
def odd_even(num):
    """ This function shows the number is odd or even """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

#calling a function
print(odd_even(10))  # Output: Even
print(odd_even(7))   # Output: Odd  

## function with multiple  parameters
def add(a,b):
   # return "Your answer:"a+b




# positional Arguments 
def print_value(*args):
    for i in args:
        print(i)

print_value(1,3,4,5,6,"huzaif")


# Keywords Arguments 

def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

print_details(name="Huzaif",class="B.tech",Branch="C.S.E") 


#*args lets your function accept any number of positional arguments.

#Example:
def add(*args):
    print(args)

add(1, 2, 3, 4)

#Output:(1, 2, 3, 4)


#All values go into a tuple called args.

#application 

#When you don't know how many values user will pass
#Useful for mathematical functions, printing, aggregating values etc.

#  Example: Sum of unlimited numbers
def total(*nums):
    return sum(nums)

print(total(10, 20, 30, 40))  # 100


# **kwargs lets your function accept any number of keyword arguments.

#Example:
def student(**kwargs):
    print(kwargs)

student(name="Huzaif", age=22, city="Delhi")

#Output:{'name': 'Huzaif', 'age': 22, 'city': 'Delhi'}


# All keyword arguments go into a dictionary.

#Why use **kwargs?
#When you want flexible named parameters
#Useful in configurations, API calls, ML models, data preprocessing etc.



