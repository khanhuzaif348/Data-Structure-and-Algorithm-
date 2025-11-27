# Introduction of Conditional Statements

# Conditional statements allow us to execute certain blocks of code based on specific conditions.
# The most common conditional statements in Python are 'if', 'elif', and 'else'.
# Example of using conditional statements:

# If statement
#else statement
#elif statement
# Nested if statements
#practiceExample    
#common Errors and Best Practices



# If statement
age  = 20:
if age >= 18:
    print("You are an adult.")


# Else statement
# age  = 16
if age >= 18:
    print("You are an adult.")  
else:
    print("You are a minor.")   


# Elif statement
## Elif statement is used to check multiple conditions.
age = 65
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# Nested conditional  statements  
# Nested if statements are if statements placed inside another if statement.
# Example of nested if statements:
num =  int(input("Enter a number: "))
if num>=0:
    print("The number is positive.")
    if num%2==0:
        print("The number is even.")
    else:
        print("The number is odd. ")

#Practice Example -  check a year is leap year or not
num = int(input("input the  year"))

if num%4==0:
    if num%100==0:
        if num%400==0:
            print("This is leap year")
        else:
            print("This is not leap year3")
    else:
        print("This is a leeap year2")
else :
    print("This is Not a Leap year1")
    

