#Introduction of List 
# A list is a collection which is ordered and changeable(Mutable). 
# In Python, lists are written with square brackets[ ].

# Creating a list
#accessing elements of a list
#MOdifying elements of a list
#List methods
#slicing lists
#looping through a list(Iterate over list)
#list comprehension
#nesting lists
#Practical examples of lists



# Creating a list
my_list = []
type(my_list)  # Output: <class 'list'>
mixed_list = [1, "Hello", 3.14, True]
print(mixed_list)  # Output: [1, 'Hello', 3.14, True]

# Accessing elements of a list [Indexing]
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruit[-1])  # Output: cherry
print(fruits[-2])  # Output: banana
print(fruits[0:2])  # Output: ['apple', 'banana']


# Modifying elements of a list
fruits[1] = "blueberry" # Changing 'banana' to 'blueberry'
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
fruits.append("date") # listName.append(value) -  added last position
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']
# Insert at specific position
fruits.insert(1, "banana") # listName.insert(index, value)
print(fruits)  # Output: ['apple', 'banana', 'blueberry', 'cherry', 'date']
# Remove an item    
fruits.remove("cherry") # listName.remove(value)
print(fruits)  # Output: ['apple', 'banana', 'blueberry', 'date']
# Pop an item   
popped_fruit = fruits.pop() # listName.pop() - removes last item
print(popped_fruit)  # Output: date
print(fruits)  # Output: ['apple', 'banana', 'blueberry']
# Clear the list
fruits.clear() # listName.clear()
print(fruits)  # Output: [] 
# Re-creating the list for further examples
fruits = ["apple", "banana", "blueberry", "cherry", "date"]
# Slicing lists
print(fruits[1:4])  # Output: ['banana', 'blueberry', 'cherry']
print(fruits[:3])   # Output: ['apple', 'banana', 'blueberry']
print(fruits[2:])   # Output: ['blueberry', 'cherry', 'date']
print(fruits[-3:-1])  # Output: ['blueberry', 'cherry'] 

# Looping through a list (Iterate over list)
for fruit in fruits:
    print(fruit)    
# Output:
# apple
# banana    
# blueberry
# cherry
# date  
# List comprehension - concise way to create lists
#syntax : [expression for item in iterable if condition]
squared_numbers = [x**2 for x in range(5)]
print(squared_numbers)  # Output: [0, 1, 4, 9, 16]
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]  
# Nesting lists     use of nested lists to represent matrices or grids
lst1 = [1, 2, 3,4]
lst2 = [5, 6, 7,8]
pair = [[i,j] for i in lst1 for j in lst2]
print(pair)
# Output: [[1, 5], [1, 6], [1, 7], [1, 8], [2, 5], [2, 6], [2, 7], [2, 8], [3, 5], [3, 6], [3, 7], [3, 8], [4, 5], [4, 6], [4, 7], [4, 8]]
# list comprehension with function calls
word = ["hello", "world"   ]
length = [len(w) for w in word]
print(lengths)  # Output:   [5, 5]
# Practical examples of lists
# Example 1: Storing student names
students = ["Alice", "Bob", "Charlie"]
# Example 2: Shopping cart items
shopping_cart = ["milk", "bread", "eggs"]
# Example 3: To-do list
todo_list = ["finish homework", "clean room", "call mom"]
# Example 4: Storing temperatures
temperatures = [72.5, 75.0, 78.3, 80.1]
# Example 5: Storing coordinates
coordinates = [(10, 20), (30, 40), (50, 60)]
# Example 6: Matrix representation
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing an element in the matrix
element = matrix[1][2]  # Output: 6
print(element)
# Example 7: Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
# Example 8: Combining two lists into a list of tuples
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
combined = list(zip(list1, list2))
print(combined)  # Output: [('a', 1), ('b', 2), ('c', 3)]
# Example 9: Flattening a nested list
nested_list = [[1, 2], [3, 4], [5]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5]
# Example 10: Finding the maximum value in a list   
values = [10, 20, 5, 30, 15]
max_value = max(values) 
print(max_value)  # Output: 30  
# Example 11: Counting occurrences of an item in a list
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
blue_count = colors.count("blue")
print(blue_count)  # Output: 3
# Example 12: Sorting a list
unsorted_list = [5, 2, 9, 1, 5, 6]
sorted_list = sorted(unsorted_list)
print(sorted_list)  # Output: [1, 2, 5, 5, 6, 9]
# Example 13: Reversing a list
original_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original_list))
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
# Example 14: Merging two lists
list_a = [1, 2, 3]
list_b = [4, 5, 6]
merged_list = list_a + list_b
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]
# Example 15: Finding the index of an item in a list
animals = ["cat", "dog", "rabbit", "dog"]
dog_index = animals.index("dog")
print(dog_index)  # Output: 1
