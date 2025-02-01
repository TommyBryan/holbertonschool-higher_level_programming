#!/usr/bin/python3

# Import the Square class from the 1-square module
Square = __import__('1-square').Square

# Create an instance of the Square class with size 3
my_square = Square(3)

# Print the type of the my_square instance
print(type(my_square))

# Print the dictionary representation of the my_square instance
print(my_square.__dict__)

# Attempt to print the public attribute 'size' (which does not exist)
try:
    print(my_square.size)
except Exception as e:
    print(e)  # Print the exception message

# Attempt to print the private attribute '__size' (which is name-mangled)
try:
    print(my_square.__size)
except Exception as e:
    print(e)  # Print the exception message
