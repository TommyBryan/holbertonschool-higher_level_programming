#!/usr/bin/python3

def no_c(my_string):

    # Replace all occurrences of 'c' and 'C' in the string
    return ''.join([char for char in my_string if char != 'C' and char != 'c'])
