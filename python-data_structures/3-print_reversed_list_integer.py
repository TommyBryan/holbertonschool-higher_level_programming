#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    for i in my_list[::-1]:  # reverse the list
        print("{:d}".format(i))  # print each element in the list
