#!/usr/bin/python3
"""Reads a text file (utf-8) and prints it to stdout."""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
