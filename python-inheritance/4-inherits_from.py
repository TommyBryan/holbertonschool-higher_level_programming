#!/usr/bin/python3
""" Defines a class named inherits_from """


def inherits_from(obj, a_class):
    """ Checks if object is instance of a class
      inherited dircetly or indirectly. """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
