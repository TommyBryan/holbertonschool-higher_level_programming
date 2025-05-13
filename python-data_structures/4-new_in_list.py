#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # If index is out of range, return the original list
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Create a copy of my_list
    new_list = my_list.copy()
    # Replace the element at the specified index
    # with the new element
    new_list[idx] = element
    return new_list
