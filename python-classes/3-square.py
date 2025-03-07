#!/usr/bin/python3
""" creates a class Square """


class Square:
    """ defines a class Square """

    def __init__(self, size=0):
        """ initializes the square with a private size attribute """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns the current square area """
        return self.__size ** 2
