# Introduction to Operators
#Arithmetic Operators
        # Addition
        # Subtraction
        # Multiplication
        # Division
        #floor Division
        #modulus
        #exponentiation

# 3. Comparison Operators
#          # Equal to
#         # Not equal to
#        # Greater than
#       # Less than
#      # Greater than or equal to
#     # Less than or equal to
# 4. Logical Operators
#        # and
#      # or
#    # not
# 5. Practical Examples and common Errors 
# 
 # Arithmetic Operators
 # Addition
a = 10
b = 5
addition = a + b
Subtraction = a - b
Multiplication = a * b
Division = a / b
floor_division = a // b
print("Addition:", addition)  # Output: 15
print("Subtraction:", Subtraction)  # Output: 5
print("Multiplication:", Multiplication)  # Output: 50  
print("Division:", Division)  # Output: 2.0
print("Floor Division:", floor_division)  # Output: 2
print("Modulus:", a % b)  # Output: 0
print("Exponentiation:", a ** b)  # Output: 100000  000
print()
print()

#comparison Operators
# == Equal to
x = 10
y = 5
print("Is x equal to y?", x == y)  # Output: False
str1 = "hello"
str2 = "hello"  
str1 == str2

print("Is str1 equal to str2?", str1 == str2)  # Output: True
# != Not equal to
print("Is x not equal to y?", x != y)  # Output: True
print("Is str1 not equal to str2?", str1 != str2)  # Output: False

# > Greater than
print("Is x greater than y?", x > y)  # Output: True
print("Is y greater than x?", y > x)  # Output: False
# < Less than
print("Is x less than y?", x < y)  # Output: False
print("Is y less than x?", y < x)  # Output: True
# >= Greater than or equal to
print("Is x greater than or equal to y?", x >= y)  # Output:
print("Is y greater than or equal to x?", y >= x)  # Output: False
# <= Less than or equal to
print("Is x less than or equal to y?", x <= y)  # Output: False
print("Is y less than or equal to x?", y <= x)  # Output: True
print()
print()


# Logical Operators
# and
a = True    
b = False
print("a and b:", a and b)  # Output: False
print("a and a:", a and a)  # Output: True  
# or
print("a or b:", a or b)  # Output: True
print("b or b:", b or b)  # Output: False
# not
print("not a:", not a)  # Output: False 
print("not b:", not b)  # Output: True
print()


# simple Calculator using Arithmetic Operators
#take 2 input from user and perform basic arithmetic operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponentiation:", num1 ** num2)
print()
# Common Errors
# Division by zero error
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.") 
# Type error
try:
    result = 10 + "5"   
except TypeError:
    print("Error: Cannot add a number and a string.")




    
