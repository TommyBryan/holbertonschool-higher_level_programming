#!/usr/bin/python3
"""Reads a text file (utf-8) and prints it to stdout."""


def read_file(filename=""):
    """ Opens a file in read mode in utf-8 encoding and prints its content."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
