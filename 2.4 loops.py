# Loops 
# Loops are used to execute a block of code repeatedly until a certain condition is met.    
# Python has two types of loops: for loops and while loops. 
# For Loops
      # Iterover a range
      # Iterative over a string
# While Loops
# loops control statements
    # break
    # continue
    # pass
# nested loops
# Practical Example and common errors


# For Loop - Iterating over a range
for i in range(5): # range strarts from 0 to 4
    print("Iteration:", i)  
print()  # Print a newline for better readability   
# For Loop - Iterating over a string
for char in "Hello":
    print("Character:", char)
print()  # Print a newline for better readability
# While Loop -  While loop continues as long as the condition is True . 
count = 0
while count < 5:
    print("Count:", count)
    count += 1
print()  # Print a newline for better readability               

# Loop Control Statements
# Break Statement - Exits the loop when count reaches 3
for i in range(10):
    if i ==3:
        break 
    print("Break Example - i:", i)
print()  # Print a newline for better readability



for i in range(5):
    if i%2:
        continue  # Skip the rest of the loop when i is 2
    print("Continue Example - i:", i)


#pass
for i in range(5):
    if i == 2:
        pass  # Placeholder, does nothing
    print("Pass Example - i:", i)

# Nested Loops  
for i in range(3):
    for j in range(2):
        print(f"Nested Loop - i: {i}, j: {j}")



# practical Example : - 
#sum of the first n natural numbers using a loop

## while loop
n = 10
sum_n = 0
i = 1
while i <= n:
    sum_n += i
    i += 1  
print("Sum of first", n, "natural numbers using while loop is:", sum_n)  

## for loop
n = 10  
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print("Sum of first", n, "natural numbers using for loop is:", sum_n)

# Prime or not 
num =  2
for i in range(2,num):
     if num % i == 0:
        print("Not prime")
        break
else:
    print(i)
    print("Prime")
    print()  # Print a newline for better readability


# find prime with given range
# find all prime numbers in a given range

for num in range(2,100):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num, "is a prime number") 
print()  # Print a newline for better readability
# Common Errors
# Infinite Loop Example (uncomment to test)
# count = 0
# while count < 5:
#    print("Infinite Loop Example - Count:", count)
#   
#   
# # Logical Error Example
# sum_n = 0 
# for i in range(1, 10):  # Should be range(1, 11) to include 10
#    sum_n += i 
# print("Logical Error Example - Sum of first 10 natural numbers is:", sum_n)    
 


