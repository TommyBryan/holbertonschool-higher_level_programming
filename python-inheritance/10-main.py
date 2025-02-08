#!/usr/bin/python3

"""
Write a class Square that inherits from Rectangle (9-rectangle.py):

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
"""

Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())

""" Output:
[Rectangle] 13/13
169
"""
