#!/usr/bin/python3

def add_tuple(tuple_a=(), yuple_b=()):

    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
