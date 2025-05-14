#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    
    new_list = []
    
    for i in range(len(my_list)):  # Iterate through the list
        if my_list[i] % 2 == 0:  # Check if the element is divisible by 2
            new_list.append(True)  # Append True if divisible by 2
        else:
            new_list.append(False)  # Append False if not divisible by 2
    return new_list  # Return the new list
