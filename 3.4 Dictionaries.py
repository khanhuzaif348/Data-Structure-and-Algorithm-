# Introduction of Dictionaries in Python
# A dictionary is a collection of key-value pairs, where each key is unique.
# Dictionaries are mutable, meaning they can be changed after their creation.

#creating a dictionary
#accessing values in a dictionary
# Modifying values in a dictionary
# Dictioanary methods
# Iterating over a dictionary
# Nested dictionaries
# Dictionary comprehensions
# Practical examples of dictionaries and common errors






# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(type(my_dict))  # Output: <class 'dict'>  
# How create empty dictionary
empty_dict = {}
empty_dict2 = dict() 




# Accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 30

# Accessing values using get method with default value
print(my_dict.get("age"))  # Output: age value
# Default if key not found
print(my_dict.get("Last_name", "Not Found"))  # Output: Not Found

#modifying dictionary Elements -  Adding or Updating Key-Value Pairs
my_dict["age"] = 31  # Update existing key 
my_dict["profession"] = "Engineer"  # Add new key-value pair
print(my_dict)
# Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'profession': 'Engineer'}
# Removing Key-Value Pairs
del my_dict["city"]  # Remove key-value pair by key
removed_value = my_dict.pop("profession")  # Remove and return value
print(my_dict)
print("Removed:", removed_value) 
#dictionary Methods
# Getting all keys
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age'])
# Getting all values
values = my_dict.values()
print(values)  # Output: dict_values(['Alice', 31])
# Getting all key-value pairs
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 31)])
# Checking if a key exists
has_name = "name" in my_dict
print(has_name)  # Output: True
# Getting the number of key-value pairs                                     
length = len(my_dict)
#shallow copy vs deep copy
student_copy = my_dict.copy()  # Shallow copy -  it allocate the diffenrent memory
print(student_copy)



## Iterate over Dictionarys
for key, value in my_dict.items():
    print(f"{key}: {value}")    



## Nested Dictionaries
nested_dict = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}   
print(nested_dict["student1"]["name"])  # Output: Alice
print(nested_dict["student2"]["age"])   # Output: 22
# Adding a new nested dictionary
nested_dict["student3"] = {"name": "Charlie", "age": 23}
print(nested_dict)
# Output: {'student1': {'name': 'Alice', 'age': 20}, 'student2': {'name': 'Bob', 'age': 22}, 'student3': {'name': 'Charlie', 'age': 23}}
print(length)  # Output: 2
print(nested_dict)
# Output: {'student1': {'name': 'Alice', 'age': 20}, 'student2': {'name': 'Bob', 'age': 22}}

# dictionary Comprehensions
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# Filtering a dictionary
filtered_dict = {k: v for k, v in squared_dict.items() if v % 2 == 0}
print(filtered_dict)  # Output: {0: 0, 2: 4, 4: 16}


 # practical Example 
# USe a Dictionaries to count the frequency of elements in list 
numbers  =  [1,1,2,2,2,3,4,4,5,5,5]
freq = {}
for  number in numbers:
    if number in freq:
        freq[number] += 1
    else: 
        freq[number] = 1
print(freq)  # Output: {1: 2, 2: 3, 3: 1, 4: 2, 5: 3}
