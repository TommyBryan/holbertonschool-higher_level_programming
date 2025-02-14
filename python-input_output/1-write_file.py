#!/usr/bin/python3
""" Module for writing a string to a file. """


def write_file(filename="", text=""):
    """ Appends a string at the end of a text file. """
    
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
