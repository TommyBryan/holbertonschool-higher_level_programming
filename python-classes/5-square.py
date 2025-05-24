#!/usr/bin/python3
""" Creates a class Square. """


class Square:
    """ Defines a square by its size. """

    def __init__(self, size=0):
        """ Initializes the square with a private size attribute. """
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """ Retrieves the size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size of the square with validation. """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the area of the square. """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()  # Print an empty line if size is 0
        else:
            for i in range(self.__size):  # Loop each row
                for j in range(self.__size):  # Loop each column in row
                    print("#", end="")  # Print '#' without newline
                print()  # Move to the next line after each row
