#!/usr/bin/python3
""" Creates a class name MyList. """


class MyList(list):
    """ Class inherits from list(). """

    def print_sorted(self):
        """ Prints sorted list. """
        print(sorted(self))
