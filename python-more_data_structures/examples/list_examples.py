"""
List - []
 Ordered: ELements keep their order you add them
 Mutable: You can change them, add, remove elements
 Allows duplicates: You can add the same element multiple times
 Uses: When you want to keep the order of elements, and you want to allow duplicates
"""
# Example:

my_list = [1, 2, 3, 2]
print(my_list)  # Output: [1, 2, 3, 2]
my_list[0] = 10  # Change the first element
print(my_list)  # Output: [10, 2, 3, 2]
my_list.append(4)  # Add an element at the end
print(my_list)  # Output: [10, 2, 3, 2, 4]
