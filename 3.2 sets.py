#Introduction of sets in Python
#Sets are unordered collections of unique elements in Python. 
# They are useful for storing multiple items in a single variable without duplicates. 
# Sets support various operations like union, intersection, and difference.


# Creating a set --> curly braces {}
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set) 

# Basic set opearations
# Adding an element to a set
my_set.add(6)
print("Set after adding 6:", my_set)    
# Removing an element from a set
my_set.remove(3)
print("Set after removing 3:", my_set)
# Remove element using discard (no error if element not found)
my_set.discard(10)  # No error if 10 is not present 
print("Set after discarding 10 (not present):", my_set)


# pop method removes and returns an arbitrary element from the set - FIFO operation 
removed_element = my_set.pop()
print("Removed element using pop():", removed_element)
print("Set after pop():", my_set)  

# Checking membership
print("Is 4 in the set?", 4 in my_set)

# Set operations
set_a = {1, 2, 3}   
set_b = {3, 4, 5}

#Union of two sets -- combines all unique elements from both sets 
union_set = set_a.union(set_b)      
print("Union of set_a and set_b:", union_set)

# Intersection of two sets -- elements common to both sets
intersection_set = set_a.intersection(set_b)    
print("Intersection of set_a and set_b:", intersection_set)



# Difference of two sets -- elements in set_a but not in set_b
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b (set_a - set_b):", difference_set) 

# Symmetric Difference -- elements in either set_a or set_b but not in both
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference of set_a and set_b:", symmetric_difference_set)



# Sets methods
## is subset
subset_result = {1, 2}.issubset(set_a)
print("Is {1, 2} a subset of set_a?", subset_result)

## is superset
superset_result = set_a.issuperset({1, 2})
print("Is set_a a superset of {1, 2}?", superset_result)
## clear method to remove all elements from the set
my_set.clear()
print("Set after clear():", my_set)


# Note: Sets are mutable, but the elements within a set must be immutable (e.g., numbers, strings, tuples).
# Sets do not support indexing or slicing since they are unordered collections.
# Attempting to access elements by index will raise an error
# Example of error when trying to access by index
# print(my_set[0])  # Uncommenting this line will raise a TypeError
# Sets can be created using the set() constructor as well

another_set = set([1, 2, 3, 4, 5])
print("Another set created using set() constructor:", another_set)
# Demonstrating that sets automatically remove duplicates
duplicate_set = {1, 2, 2, 3, 4, 4, 5}
print("Set with duplicates removed:", duplicate_set)# Output: Set with duplicates removed: {1, 2, 3, 4, 5}
# Output: Initial set: {1, 2, 3, 4, 5}
# Set after adding 6: {1, 2, 3, 4, 5, 6}
# Set after removing 3: {1, 2, 4, 5, 6}
# Set after discarding 10 (not present): {1, 2, 4, 5, 6}
# Removed element using pop(): 1
# Set after pop(): {2, 4, 5, 6}
# Is 4 in the set? True
# Union of set_a and set_b: {1, 2, 3, 4, 5}
# Intersection of set_a and set_b: {3}
# Difference of set_a and set_b (set_a - set_b): {1, 2}
# convert list and remove duplicates using set

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))    
print("List with duplicates removed using set:", unique_list)
# Output: List with duplicates removed using set: [1, 2, 3, 4, 5]
# convert list and remove duplicates using set
my_list = [1, 2, 2, 3, 4, 4, 5]
# find unique elemnets using set
unique_list = list(set(my_list))
print("List with duplicates removed using set:", unique_list)
# Output: List with duplicates removed using set: [1, 2, 3, 4, 5]
# convert list and remove duplicates using set
my_list = [1, 2, 2, 3, 4, 4, 5]
# find unique elemnets using set
unique_list = list(set(my_list))
print("List with duplicates removed using set:", unique_list)
# Output: List with duplicates removed using set: [1, 2, 3, 4, 5]

