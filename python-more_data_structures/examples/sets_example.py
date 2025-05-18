"""
Set - {} or set()
 Unordered collection of unique elements
    Mutable
    No duplicates
    Uses: When you want to store unique elements, and you don't care about the order
"""
# Important: {} is a dictionary, not a set. Use set() to create an empty set.
# Example:

my_set = {1, 2, 3, 2}
print(my_set)  # Output: {1, 2, 3} - Duplicates are removed
my_set.add(4)  # Add an element
print(my_set)  # Output: {1, 2, 3, 4}
