#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:  # iterate through the list
        if i == search:  # if element equals search, append replace
            new_list.append(replace)
        else:
            new_list.append(i)
    return new_list
