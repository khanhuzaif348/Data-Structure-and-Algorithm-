#Tuple -  Is immutable data structure in python 
# create by using parenthesis ()
# Tuples are ordered collection of items

# Introduction of tuples
# creating a tuples
# Accessing TupleElements 
# Tuple Operations
#Immutability of Tuples
# Tuple Methods
# Tuple Packing and Unpacking
# Nested Tuples
# Tuple Comprehensions
# Advantages and Use Cases of Tuples
#Practical Examples



# Introduction of tuples
my_tuple = (1, 2, 3, "Hello", 4.5)
print(type(my_tuple))  # Output: <class 'tuple'>    
# How create empty tuple
empty_tuple = ()
empty_tuple2 = tuple()
print(type(empty_tuple))  # Output: <class 'tuple'>
print(type(empty_tuple2))  # Output: <class 'tuple'>
# Accessing Tuple Elements
print(my_tuple[0])  # Output: 1 --> indexing 
pint(my_tuple[0:3])  #Slicing --> Output: (1, 2, 3)

# Tuple Operations

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)
# Repetition
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

## Immutability of Tuples

# Tuples are immutable, meaning their elements cannot be changed after creation.
# The following line would raise an error:  
# my_tuple[0] = 10  # This will raise a TypeError   
# Tuple Methods -  count() and index()
my_tuple = (1, 2, 3, 2, 4, 2)
count_of_2 = my_tuple.count(2)  
print(count_of_2)  # Output: 3
index_of_3 = my_tuple.index(3)
print(index_of_3)  # Output: 2

# Tuple Packing and Unpacking --> 
# defination: Packing is the process of combining multiple values into a single tuple, 
# while unpacking is the process of extracting individual values from a tuple into separate variables.
# Packing and Unpacking Example 
packed_tuple = 1, "Hello", 3.5  # Packing
print(packed_tuple)  # Output: (1, 'Hello', 3.5)
a, b, c = packed_tuple  # Unpacking 
print(a)  # Output: 1
print(b)  # Output: Hello  

# Unpacking with * operator
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)    # Output: 5



# Nested Tuples
nested_tuple = (1, (2, 3), (4, (5, 6)))
print(nested_tuple[1])        # Output: (2, 3)
print(nested_tuple[2][1])     # Output: (5, 6)
print(nested_tuple[2][1][0])  # Output: 5
# Tuple Comprehensions
squared_tuple = tuple(x**2 for x in range(5))
print(squared_tuple)  # Output: (0, 1, 4, 9, 16)
# Advantages and Use Cases of Tuples
# 1. Data Integrity
# 2. Performance
# 3. Dictionary Keys
# 4. Multiple Return Values
# Practical Examples
# Example 1: Using Tuples as Dictionary Keys
location_coords = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
    (41.8781, -87.6298): "Chicago"
}
print(location_coords[(40.7128, -74.0060)])  # Output: New York
















