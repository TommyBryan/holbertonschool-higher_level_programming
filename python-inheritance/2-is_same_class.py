#!/usr/bin/python3
""" Create class """


def is_same_class(obj, a_class):
    """ Returns true if object is instance of the specified class. """
    if type(obj) is a_class:
        return True
    else:
        return False
