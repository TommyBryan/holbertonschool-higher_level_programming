#!/usr/bin/python3
""" Creates a class Square. """


class Square:
    """ Defines a square by its size. """

    def __init__(self, size=0):
        """ Initializes the square with a private size attribute."""
        self.__size = size

        """ Checks if size is an integer. """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        """ Checks if size is negative. """
        if size < 0:
            raise ValueError("size must be >= 0")
