#!/usr/bin/python3
"""creates class Square with
private instance attribute size and public instance method"""


class Square:
    """defines class with instantiated and validated private instance attribute
    and public instance method."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates and returns current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints square using '#' character"""
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for y in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for x in range(self.__size):
                    print("#", end="")
                print()
