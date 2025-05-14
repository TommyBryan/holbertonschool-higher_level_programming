#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of the sentence and its first character.
    If the sentence is empty, the first character is None.
    """
    if sentence == "":  # Check if the sentence is empty
        return (0, None)  # Return length 0 and None as the first character
    return (len(sentence), sentence[0])  # Return length and first character
