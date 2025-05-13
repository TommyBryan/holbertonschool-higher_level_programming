#!/usr/bin/python3

def no_c(my_string):

    # Iterates through the string and removes 'c' and 'C'
    for char in my_string:
        if char == 'c' or char == 'C':
            # Replaces 'c' and 'C' with an empty string
            my_string = my_string.replace(char, "")
    return my_string
