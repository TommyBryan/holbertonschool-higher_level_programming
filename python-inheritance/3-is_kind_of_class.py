#!/usr/bin/python3
""" Defines a class. """


def is_kind_of_class(obj, a_class):
    """ Checks if object is an instanc or inherited instance of a class. """
    if isinstance(obj, a_class):
        return True
    else:
        return False
