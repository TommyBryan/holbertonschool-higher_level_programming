#!/usr/bin/python3
"""Function to write a string to a text file"""

def write_file(filename="", text=""):
    """ Opens a file in write mode in utf-8 and writes the given text to it."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
