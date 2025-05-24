#!/usr/bin/python3
""" Creates an empty class Rectangle """


class Rectangle:
    
    def __init__(self, width=0, height=0):
        """ Initializes the rectangle with width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle """
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("heighty must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
