#!/usr/bin/pyhton3
""" Module for writing a string to a file. """


def write_file(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
