#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r") as file:
        print(file.read())


read_file("my_file_0.txt")
