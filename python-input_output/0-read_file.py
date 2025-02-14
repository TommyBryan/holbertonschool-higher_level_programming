#!/usr/bin/python3
""" Module for reading a file. """


def read_file(filename=""):
    """ Fucntion that reads a text file and prints it to stdout. """
    with open(filename, "r") as file:
        print(file.read())
