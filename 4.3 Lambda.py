# Introdunction of Lambda - 
'''
 Lambda function known as Anonymous Function and define by lambda Keyword , they can have any number of arguments but only one expression 
 . They commonly used for short operations or as arguments to higher-order functions.
 '''
 #syntax -  
lambda arguments: expression

def add(a,b):
    return a+b

# smiler   with ther help of lambda function
addition =  lambda a,b : a+b  
addition(3,5)  

#map() function
# map function are used to applies on all item on data 
# and its return object ( an iterator). useful transform data in list comprehensively

def mul(x):
    return x**2
numbers=[1,2,3,4,5]
list(map(mul,numbers))   
# Lambda with map() function
numbers = [1, 2, 3, 4, 5,6 ]
square_num = list(map(lambda x: x**2, numbers))


print(squared)  # Output: [1, 4, 9, 16, 25]
# map function are used to apply opearation on data 
# Lambda with filter() function




# the filter() function in python 
''' The  filter function constructs an iterator  from elements of an
function return true. It is used to filter out item from a lsit  absed on conditions. 
'''
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]
# 