#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    """
    Adds two tuples.
    If the tuples are less than 2 elements, they are padded with zeros.
    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.
        Returns:
        tuple: A new tuple with the sum 
    """

    # Ensure both tuples have at least 2 elements
    # If a tuple has less than 2 elements, pad it with zeros
    # to make it 2 elements long
    # If a tuple has more than 2 elements, truncate it to 2 elements
    # This is done by concatenating the tuple with (0, 0) and then slicing
    # the first 2 elements
    
    tuple_a = (tuple_a + (0, 0))[:2]
    tuple_b = (tuple_b + (0, 0))[:2]

    return (tuple_a[0] + tuple_b[0],  tuple_a[1] + tuple_b[1])
